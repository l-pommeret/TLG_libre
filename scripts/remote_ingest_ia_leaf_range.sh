#!/usr/bin/env bash
set -euo pipefail

for name in IA_IDENTIFIER START_LEAF END_LEAF TARGET_PATH EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done

case "$TARGET_PATH" in
  scans/*) ;;
  *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;;
esac
case "$TARGET_PATH" in
  *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;;
esac
[[ "$START_LEAF" =~ ^[0-9]+$ && "$END_LEAF" =~ ^[0-9]+$ ]] || {
  echo "leaf bounds must be integers" >&2; exit 2;
}
test "$START_LEAF" -le "$END_LEAF" || { echo "invalid leaf range" >&2; exit 2; }
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }

mkdir -p "$TARGET_PATH/images"
for ((leaf=START_LEAF; leaf<=END_LEAF; leaf++)); do
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
echo "verified $actual_count page images from $IA_IDENTIFIER leaves $START_LEAF-$END_LEAF"
