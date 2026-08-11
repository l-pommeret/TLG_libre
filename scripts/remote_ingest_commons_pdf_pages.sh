#!/usr/bin/env bash
set -euo pipefail

for name in SOURCE_URL START_PAGE END_PAGE TARGET_PATH EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done
case "$TARGET_PATH" in scans/*) ;; *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;; esac
case "$TARGET_PATH" in *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;; esac
[[ "$START_PAGE" =~ ^[0-9]+$ && "$END_PAGE" =~ ^[0-9]+$ ]] || { echo "page bounds must be integers" >&2; exit 2; }
test "$START_PAGE" -le "$END_PAGE" || { echo "invalid page range" >&2; exit 2; }
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
curl --fail --location --retry 5 --retry-all-errors --output "$tmp_dir/source.pdf" "$SOURCE_URL"
file "$tmp_dir/source.pdf" | grep -q 'PDF document' || { echo "source is not a PDF" >&2; exit 1; }
mkdir -p "$TARGET_PATH/images"
pdftoppm -f "$START_PAGE" -l "$END_PAGE" -jpeg -jpegopt quality=95 "$tmp_dir/source.pdf" "$tmp_dir/page"
page="$START_PAGE"
while IFS= read -r source_image; do
  mv "$source_image" "$TARGET_PATH/images/commons_p$(printf '%04d' "$page").jpg"
  page=$((page + 1))
done < <(find "$tmp_dir" -maxdepth 1 -type f -name 'page-*.jpg' | sort -V)
actual_count="$(find "$TARGET_PATH/images" -type f -name '*.jpg' | wc -l | tr -d ' ')"
test "$actual_count" = "$EXPECTED_COUNT" || { echo "image-count mismatch: expected $EXPECTED_COUNT, got $actual_count" >&2; exit 1; }
(cd "$TARGET_PATH" && find images -type f -print0 | sort -z | xargs -0 sha1sum > SHA1SUMS)
echo "verified $actual_count page images from Commons PDF pages $START_PAGE-$END_PAGE"
