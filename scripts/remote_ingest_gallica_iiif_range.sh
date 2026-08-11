#!/usr/bin/env bash
set -euo pipefail

for name in GALLICA_ARK START_PAGE END_PAGE TARGET_PATH EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done
case "$GALLICA_ARK" in bpt[0-9a-z]*) ;; *) echo "unsafe Gallica ARK" >&2; exit 2 ;; esac
case "$TARGET_PATH" in scans/*) ;; *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;; esac
case "$TARGET_PATH" in *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;; esac
[[ "$START_PAGE" =~ ^[0-9]+$ && "$END_PAGE" =~ ^[0-9]+$ ]] || {
  echo "IIIF page bounds must be integers" >&2; exit 2;
}
test "$START_PAGE" -le "$END_PAGE" || { echo "invalid IIIF range" >&2; exit 2; }
test $((END_PAGE - START_PAGE + 1)) = "$EXPECTED_COUNT" || {
  echo "range does not match EXPECTED_COUNT" >&2; exit 2;
}
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }

mkdir -p "$TARGET_PATH/images"
for ((page=START_PAGE; page<=END_PAGE; page++)); do
  name="${GALLICA_ARK}_f$(printf '%04d' "$page").jpg"
  url="https://gallica.bnf.fr/iiif/ark:/12148/${GALLICA_ARK}/f${page}/full/full/0/default.jpg"
  curl --user-agent 'TLG_libre image research' --fail --location \
    --retry 5 --retry-all-errors --output "$TARGET_PATH/images/$name" "$url"
  file "$TARGET_PATH/images/$name" | grep -q 'JPEG image data' || {
    echo "non-JPEG response for Gallica f$page" >&2; exit 1;
  }
done
actual_count="$(find "$TARGET_PATH/images" -type f -name '*.jpg' | wc -l | tr -d ' ')"
test "$actual_count" = "$EXPECTED_COUNT" || {
  echo "image-count mismatch: expected $EXPECTED_COUNT, got $actual_count" >&2; exit 1;
}
(
  cd "$TARGET_PATH"
  find images -type f -print0 | sort -z | xargs -0 sha1sum > SHA1SUMS
)
echo "verified $actual_count full-resolution Gallica IIIF images f$START_PAGE-f$END_PAGE"
