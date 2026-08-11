#!/usr/bin/env bash
set -euo pipefail

for name in IA_IDENTIFIER IMAGE_FILE TARGET_PATH EXPECTED_SHA1 EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done

case "$TARGET_PATH" in
  scans/*) ;;
  *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;;
esac
case "$TARGET_PATH" in
  *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;;
esac
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }
[[ "$EXPECTED_SHA1" =~ ^[0-9a-f]{40}$ ]] || { echo "invalid SHA-1" >&2; exit 2; }
[[ "$EXPECTED_COUNT" =~ ^[0-9]+$ ]] || { echo "invalid image count" >&2; exit 2; }

stage="$(mktemp -d)"
trap 'find "$stage" -depth -delete' EXIT
encoded_file="$(python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$IMAGE_FILE")"
url="https://archive.org/download/${IA_IDENTIFIER}/${encoded_file}"
curl --fail --location --retry 5 --retry-all-errors --output "$stage/images.zip" "$url"

actual_sha1="$(sha1sum "$stage/images.zip" | awk '{print $1}')"
test "$actual_sha1" = "$EXPECTED_SHA1" || {
  echo "SHA-1 mismatch: expected $EXPECTED_SHA1, got $actual_sha1" >&2
  exit 1
}

mkdir -p "$stage/extracted" "$TARGET_PATH/images"
unzip -q "$stage/images.zip" -d "$stage/extracted"
find "$stage/extracted" -type f \( -iname '*.jp2' -o -iname '*.tif' -o -iname '*.tiff' \) \
  -exec mv -t "$TARGET_PATH/images" -- {} +

actual_count="$(find "$TARGET_PATH/images" -type f | wc -l | tr -d ' ')"
test "$actual_count" = "$EXPECTED_COUNT" || {
  echo "image-count mismatch: expected $EXPECTED_COUNT, got $actual_count" >&2
  exit 1
}

if find "$TARGET_PATH/images" -type f -size +95M -print -quit | grep -q .; then
  echo "an extracted image approaches GitHub's 100 MB file limit" >&2
  exit 1
fi

(
  cd "$TARGET_PATH"
  find images -type f -print0 | sort -z | xargs -0 sha1sum > SHA1SUMS
)
echo "verified $actual_count images from $IA_IDENTIFIER ($actual_sha1)"
