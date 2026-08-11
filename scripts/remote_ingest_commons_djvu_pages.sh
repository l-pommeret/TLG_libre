#!/usr/bin/env bash
set -euo pipefail
for name in SOURCE_URL START_PAGE END_PAGE TARGET_PATH EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done
case "$TARGET_PATH" in scans/*) ;; *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;; esac
[[ "$START_PAGE" =~ ^[0-9]+$ && "$END_PAGE" =~ ^[0-9]+$ ]] || exit 2
test "$START_PAGE" -le "$END_PAGE" || exit 2
test -d "$TARGET_PATH" && test ! -e "$TARGET_PATH/images"
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
curl --fail --location --retry 5 --retry-all-errors --output "$tmp_dir/source.djvu" "$SOURCE_URL"
file "$tmp_dir/source.djvu" | grep -qi 'DjVu' || { echo "source is not DjVu" >&2; exit 1; }
mkdir -p "$TARGET_PATH/images"
for ((page=START_PAGE; page<=END_PAGE; page++)); do
  ddjvu -format=ppm -page="$page" "$tmp_dir/source.djvu" "$tmp_dir/page.ppm"
  cjpeg -quality 95 -outfile "$TARGET_PATH/images/commons_p$(printf '%04d' "$page").jpg" "$tmp_dir/page.ppm"
  rm "$tmp_dir/page.ppm"
done
actual_count="$(find "$TARGET_PATH/images" -type f -name '*.jpg' | wc -l | tr -d ' ')"
test "$actual_count" = "$EXPECTED_COUNT" || { echo "image-count mismatch" >&2; exit 1; }
(cd "$TARGET_PATH" && find images -type f -print0 | sort -z | xargs -0 sha1sum > SHA1SUMS)
echo "verified $actual_count Commons DjVu pages $START_PAGE-$END_PAGE"
