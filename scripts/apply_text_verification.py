#!/usr/bin/env python3
"""Propagate verified TEI evidence into the Canon coverage table."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


PASSED = "AUTOMATED_TEI_CHECK_PASSED"


def main() -> None:
    verification = list(csv.DictReader(Path("data/text_verification.csv").open(encoding="utf-8")))
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in verification:
        by_key[(row["tlg_author_id"], row["tlg_work_id"])].append(row)

    coverage_path = Path("data/canon_coverage.csv")
    with coverage_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        coverage = list(reader)
    promoted = 0
    for row in coverage:
        candidates = by_key.get((row["tlg_author_id"], row["tlg_work_id"]), [])
        passed = [candidate for candidate in candidates if candidate["automated_check"] == PASSED]
        if not passed:
            continue
        row["pipeline_status"] = "TEXT_OPEN_VERIFIED_IDENTIFIER_MATCH"
        row["open_text_url"] = passed[0]["text_url"]
        licenses = []
        for candidate in passed:
            license_value = candidate["tei_license"] or candidate["license"]
            if license_value and license_value not in licenses:
                licenses.append(license_value.replace("\n", " ").strip())
        row["open_text_license"] = "; ".join(licenses)
        row["next_action"] = "compare_verified_open_edition_with_canon_edition"
        promoted += 1

    with coverage_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(coverage)
    print(f"coverage_rows={len(coverage)} promoted_verified_text={promoted}")


if __name__ == "__main__":
    main()
