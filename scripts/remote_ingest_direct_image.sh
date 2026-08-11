#!/usr/bin/env bash
set -euo pipefail

for name in SOURCE_URL TARGET_PATH OUTPUT_NAME; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done

case "$SOURCE_URL" in https://*) ;; *) echo "SOURCE_URL must use HTTPS" >&2; exit 2 ;; esac
case "$TARGET_PATH" in scans/*) ;; *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;; esac
case "$TARGET_PATH" in *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;; esac
case "$OUTPUT_NAME" in *..*|*/*|'') echo "unsafe OUTPUT_NAME" >&2; exit 2 ;; esac
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }

stage="$(mktemp -d)"
trap 'find "$stage" -depth -delete' EXIT
curl --fail --location --retry 5 --retry-all-errors --output "$stage/$OUTPUT_NAME" "$SOURCE_URL"
test -s "$stage/$OUTPUT_NAME" || { echo "empty source image" >&2; exit 1; }
if test "$(stat -c %s "$stage/$OUTPUT_NAME")" -gt 99000000; then
  echo "source image approaches GitHub's 100 MB file limit" >&2
  exit 1
fi

mkdir -p "$TARGET_PATH/images"
mv "$stage/$OUTPUT_NAME" "$TARGET_PATH/images/$OUTPUT_NAME"
(
  cd "$TARGET_PATH"
  sha1sum "images/$OUTPUT_NAME" > SHA1SUMS
)
echo "stored one direct source image from $SOURCE_URL"
