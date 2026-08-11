#!/usr/bin/env python3
"""Promote manually verified external Greek texts into Canon coverage."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


REGISTRY = Path("data/external_open_text_verification.csv")
COVERAGE = Path("data/canon_coverage.csv")
ALLOWED_MATCHES = {
    "EXACT_IDENTIFIER_MATCH": "TEXT_OPEN_VERIFIED_IDENTIFIER_MATCH",
    "ALTERNATE_EDITION_MATCH": "TEXT_OPEN_VERIFIED_ALTERNATE_EDITION",
}


def main() -> None:
    evidence_rows = list(csv.DictReader(REGISTRY.open(encoding="utf-8")))
    evidence: dict[tuple[str, str], dict[str, str]] = {}
    for row in evidence_rows:
        key = (row["tlg_author_id"], row["tlg_work_id"])
        if key in evidence:
            raise SystemExit(f"duplicate external verification key: {key}")
        if row["match_type"] not in ALLOWED_MATCHES:
            raise SystemExit(f"invalid match_type for {key}: {row['match_type']}")
        for field in ("source", "source_url", "source_license", "evidence", "verified_date"):
            if not row[field].strip():
                raise SystemExit(f"missing {field} for {key}")
        evidence[key] = row

    with COVERAGE.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)

    work_key_counts = Counter(
        (row["tlg_author_id"], row["tlg_work_id"])
        for row in rows
        if row["record_type"] == "work"
    )
    external_urls = {row["source_url"] for row in evidence_rows}
    for row in rows:
        if (
            row["pipeline_status"] in ALLOWED_MATCHES.values()
            and row["open_text_url"] in external_urls
        ):
            row["pipeline_status"] = "NOT_CHECKED"
            row["open_text_url"] = ""
            row["open_text_license"] = ""
            row["next_action"] = ""

    seen: set[tuple[str, str]] = set()
    promoted_by_key: Counter[tuple[str, str]] = Counter()
    promoted = 0
    for row in rows:
        key = (row["tlg_author_id"], row["tlg_work_id"])
        item = evidence.get(key)
        if item is None:
            continue
        if row["record_type"] != "work":
            raise SystemExit(f"external verification targets non-work row: {key}")
        selector = (item.get("work_title_selector") or "").strip()
        if work_key_counts[key] > 1:
            if not selector:
                raise SystemExit(
                    f"ambiguous duplicate Canon key requires work_title_selector: {key}"
                )
            if selector not in row["work_title"]:
                continue
        row["pipeline_status"] = ALLOWED_MATCHES[item["match_type"]]
        row["open_text_url"] = item["source_url"]
        row["open_text_license"] = item["source_license"]
        row["next_action"] = "compare_verified_open_edition_with_canon_edition"
        seen.add(key)
        promoted_by_key[key] += 1
        promoted += 1

    missing = set(evidence) - seen
    if missing:
        raise SystemExit(f"external verification keys absent from Canon works: {sorted(missing)}")
    non_unique = {key: count for key, count in promoted_by_key.items() if count != 1}
    if non_unique:
        raise SystemExit(f"external verification did not select one Canon work: {non_unique}")

    with COVERAGE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"registry_rows={len(evidence)} promoted_rows={promoted}")


if __name__ == "__main__":
    main()
