#!/usr/bin/env python3
"""Propagate verified TEI evidence into the Canon coverage table."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


PASSED = "AUTOMATED_TEI_CHECK_PASSED"
EXACT_STATUS = "TEXT_OPEN_VERIFIED_IDENTIFIER_MATCH"
ALTERNATE_STATUS = "TEXT_OPEN_VERIFIED_ALTERNATE_EDITION"


def verified_text_url(row: dict[str, str]) -> str:
    """Return a stable URL even for repaired catalog rows lacking text_url."""
    if row["text_url"]:
        return row["text_url"]
    if row["corpus"] == "First1KGreek" and row["source_revision"] and row["local_path"]:
        relative = row["local_path"].removeprefix("sources/upstream/first1kgreek/")
        return (
            "https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/"
            f"{row['source_revision']}/{relative}"
        )
    return ""


def main() -> None:
    verification = list(csv.DictReader(Path("data/text_verification.csv").open(encoding="utf-8")))
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in verification:
        by_key[(row["tlg_author_id"], row["tlg_work_id"])].append(row)

    aliases: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    alias_path = Path("data/open_text_aliases.csv")
    if alias_path.exists():
        for row in csv.DictReader(alias_path.open(encoding="utf-8")):
            aliases[(row["tlg_author_id"], row["tlg_work_id"])].append(row)

    coverage_path = Path("data/canon_coverage.csv")
    with coverage_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        coverage = list(reader)
    promoted_exact = 0
    promoted_alternate = 0
    for row in coverage:
        key = (row["tlg_author_id"], row["tlg_work_id"])
        candidates = by_key.get(key, [])
        passed = [candidate for candidate in candidates if candidate["automated_check"] == PASSED]
        if passed:
            row["pipeline_status"] = EXACT_STATUS
            row["open_text_url"] = verified_text_url(passed[0])
            licenses = []
            for candidate in passed:
                license_value = candidate["tei_license"] or candidate["license"]
                if license_value and license_value not in licenses:
                    licenses.append(license_value.replace("\n", " ").strip())
            row["open_text_license"] = "; ".join(licenses)
            row["next_action"] = "compare_verified_open_edition_with_canon_edition"
            promoted_exact += 1
            continue

        alternate = aliases.get(key, [])
        if alternate:
            row["pipeline_status"] = ALTERNATE_STATUS
            row["open_text_url"] = alternate[0]["source_url"]
            licenses = []
            for candidate in alternate:
                value = candidate["source_license"].replace("\n", " ").strip()
                if value and value not in licenses:
                    licenses.append(value)
            row["open_text_license"] = "; ".join(licenses)
            row["next_action"] = "compare_verified_open_edition_with_canon_edition"
            promoted_alternate += 1

    with coverage_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(coverage)
    print(
        f"coverage_rows={len(coverage)} promoted_exact={promoted_exact} "
        f"promoted_alternate={promoted_alternate}"
    )


if __name__ == "__main__":
    main()
