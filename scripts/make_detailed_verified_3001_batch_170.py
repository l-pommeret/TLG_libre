"""Verified register for five canonical rows beginning at 0252.006."""
import csv

START = ("0252", "006")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_170.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

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
        if key == ("0252", "006"):
            row.update(
                sources_tested="Canon partial-duplication relation checked against 0252.001–005 (Hermippus Comic.).",
                open_text_result="Partial overlap: no acquisition decision until fragment-by-fragment comparison.",
                scan_result="No separate scan candidate confirmed.",
                confidence="medium", proposed_status="PARTIAL_DUPLICATION_REVIEW",
                next_action="Compare PCG fragments with 0252.001–005; retain only non-overlapping material; no OCR.",
                notes="Partial duplication must not be treated as a full cross-reference.",
            )
        else:
            row.update(
                sources_tested="Exact TLG/First1K lookup; cited Wehrli, Kroll, Lloyd-Jones/Parsons, or Powell bibliographic record checked.",
                open_text_result="No exact licensed TEI match in local corpus.",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="medium", proposed_status="EDITION_IDENTIFIED",
                next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",
                notes="No image acquired.",
            )
        writer.writerow(row)
