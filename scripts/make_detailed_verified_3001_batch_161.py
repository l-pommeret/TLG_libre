"""Verified register for five canonical rows beginning at 2336.007."""
import csv

START = ("2336", "007")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_161.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
OVERLAPS = {
    ("2336", "007"): "0708.001 (<Ammonius> Gramm.)",
    ("2336", "x01"): "0708.001 (<Ammonius> Gramm.)",
    ("2336", "x02"): "0708.002 (<Ammonius> Gramm.)",
}

coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
start = next(n for n, row in enumerate(coverage)
             if (row["tlg_author_id"], row["tlg_work_id"]) == START)
works = coverage[start:start + 5]
assert len(works) == 5

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for work in works:
        key = (work["tlg_author_id"], work["tlg_work_id"])
        row = {field: "" for field in FIELDS}
        row.update(
            tlg_author_id=key[0], tlg_work_id=key[1],
            author_heading=work["author_heading"], work_title=work["work_title"],
            canonical_edition=work["bibliographic_notice"], last_checked="2026-08-11",
        )
        if key in OVERLAPS:
            host = OVERLAPS[key]
            row.update(
                sources_tested=f"Canon overlap/attribution relation checked against {host} and the cited Nickau or Palmieri record.",
                open_text_result="Potentially overlapping material: no acquisition decision until comparison and attribution review.",
                scan_result="No separate scan candidate confirmed.",
                confidence="medium", proposed_status="PARTIAL_DUPLICATION_REVIEW",
                next_action=f"Compare material and attribution with {host}; retain only non-overlapping text; no OCR.",
                notes="A ‘Cf.’ relation is retained as a review requirement, not converted to a full cross-reference.",
            )
        else:
            row.update(
                sources_tested="Exact TLG/First1K lookup; cited FHG or SVF bibliographic record checked.",
                open_text_result="No exact licensed TEI match in local corpus.",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="medium", proposed_status="EDITION_IDENTIFIED",
                next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",
                notes="No image acquired.",
            )
        writer.writerow(row)
