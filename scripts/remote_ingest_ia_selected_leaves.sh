#!/usr/bin/env bash
set -euo pipefail

for name in IA_IDENTIFIER LEAVES TARGET_PATH EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done

case "$TARGET_PATH" in
  scans/*) ;;
  *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;;
esac
case "$TARGET_PATH" in
  *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;;
esac
[[ "$EXPECTED_COUNT" =~ ^[0-9]+$ ]] || { echo "EXPECTED_COUNT must be an integer" >&2; exit 2; }
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }

IFS=',' read -r -a leaves <<< "$LEAVES"
test "${#leaves[@]}" = "$EXPECTED_COUNT" || {
  echo "leaf-count mismatch in input" >&2; exit 2;
}
mkdir -p "$TARGET_PATH/images"
declare -A seen=()
for leaf in "${leaves[@]}"; do
  [[ "$leaf" =~ ^[0-9]+$ ]] || { echo "invalid leaf: $leaf" >&2; exit 2; }
  test -z "${seen[$leaf]:-}" || { echo "duplicate leaf: $leaf" >&2; exit 2; }
  seen[$leaf]=1
  name="${IA_IDENTIFIER}_n$(printf '%04d' "$leaf").jpg"
  url="https://archive.org/download/${IA_IDENTIFIER}/page/n${leaf}_w3000.jpg"
  curl --fail --location --retry 5 --retry-all-errors \
    --output "$TARGET_PATH/images/$name" "$url"
  file "$TARGET_PATH/images/$name" | grep -q 'JPEG image data' || {
    echo "non-JPEG response for leaf $leaf" >&2; exit 1;
  }
done

actual_count="$(find "$TARGET_PATH/images" -type f -name '*.jpg' | wc -l | tr -d ' ')"
test "$actual_count" = "$EXPECTED_COUNT" || {
  echo "image-count mismatch: expected $EXPECTED_COUNT, got $actual_count" >&2
  exit 1
}
(
  cd "$TARGET_PATH"
  find images -type f -print0 | sort -z | xargs -0 sha1sum > SHA1SUMS
)
echo "verified $actual_count selected page images from $IA_IDENTIFIER leaves $LEAVES"
