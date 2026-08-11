#!/usr/bin/env bash
set -euo pipefail

for name in SOURCE_URL PAGE_RANGES TARGET_PATH EXPECTED_COUNT; do
  test -n "${!name:-}" || { echo "$name is required" >&2; exit 2; }
done
case "$TARGET_PATH" in scans/*) ;; *) echo "TARGET_PATH must be below scans/" >&2; exit 2 ;; esac
case "$TARGET_PATH" in *..*|*//*|/*) echo "unsafe TARGET_PATH" >&2; exit 2 ;; esac
[[ "$EXPECTED_COUNT" =~ ^[0-9]+$ ]] || { echo "EXPECTED_COUNT must be an integer" >&2; exit 2; }
[[ "$PAGE_RANGES" =~ ^[0-9]+-[0-9]+(,[0-9]+-[0-9]+)*$ ]] || { echo "invalid PAGE_RANGES" >&2; exit 2; }
test -d "$TARGET_PATH" || { echo "metadata directory does not exist" >&2; exit 2; }
test ! -e "$TARGET_PATH/images" || { echo "images already exist" >&2; exit 2; }

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT
curl --fail --location --retry 5 --retry-all-errors --output "$tmp_dir/source.pdf" "$SOURCE_URL"
file "$tmp_dir/source.pdf" | grep -q 'PDF document' || { echo "source is not a PDF" >&2; exit 1; }
mkdir -p "$TARGET_PATH/images"

IFS=',' read -r -a ranges <<< "$PAGE_RANGES"
for range in "${ranges[@]}"; do
  start="${range%-*}"
  end="${range#*-}"
  test "$start" -le "$end" || { echo "invalid range: $range" >&2; exit 2; }
  range_dir="$tmp_dir/range-$start-$end"
  mkdir -p "$range_dir"
  pdftoppm -f "$start" -l "$end" -jpeg -jpegopt quality=95 "$tmp_dir/source.pdf" "$range_dir/page"
  page="$start"
  while IFS= read -r source_image; do
    mv "$source_image" "$TARGET_PATH/images/commons_p$(printf '%04d' "$page").jpg"
    page=$((page + 1))
  done < <(find "$range_dir" -maxdepth 1 -type f -name 'page-*.jpg' | sort -V)
  test "$page" = "$((end + 1))" || { echo "render count mismatch for $range" >&2; exit 1; }
done

actual_count="$(find "$TARGET_PATH/images" -type f -name '*.jpg' | wc -l | tr -d ' ')"
test "$actual_count" = "$EXPECTED_COUNT" || { echo "image-count mismatch: expected $EXPECTED_COUNT, got $actual_count" >&2; exit 1; }
(cd "$TARGET_PATH" && find images -type f -print0 | sort -z | xargs -0 sha1sum > SHA1SUMS)
echo "verified $actual_count page images from Commons PDF ranges $PAGE_RANGES"
