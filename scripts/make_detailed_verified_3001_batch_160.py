"""Verified register for five canonical rows beginning at 2336.001 (passim)."""
import csv

START = ("2336", "001", "passim")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_160.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
start = next(n for n, row in enumerate(coverage) if (
    row["tlg_author_id"], row["tlg_work_id"], row["work_title"]
) == START)
works = coverage[start:start + 5]
assert len(works) == 5

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for work in works:
        row = {field: "" for field in FIELDS}
        row.update(
            tlg_author_id=work["tlg_author_id"], tlg_work_id=work["tlg_work_id"],
            author_heading=work["author_heading"], work_title=work["work_title"],
            canonical_edition=work["bibliographic_notice"], last_checked="2026-08-11",
        )
        if work["work_title"] == "passim":
            row.update(
                sources_tested="Canon row checked: bibliographic notice is only ‘passim’; identifier collides with preceding records.",
                open_text_result="No acquisition decision: the referent and edition are not specified.",
                scan_result="No scan search is actionable without a specified referent or edition.",
                confidence="low", proposed_status="RECORD_REVIEW_REQUIRED",
                next_action="Resolve the intended referent from the Canon source before text or scan work; no OCR.",
                notes="Preserved as a separate canonical occurrence; no image acquired.",
            )
        else:
            row.update(
                sources_tested="Exact TLG/First1K lookup; cited Palmieri or FGrH bibliographic record checked.",
                open_text_result="No exact licensed TEI match in local corpus.",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="medium", proposed_status="EDITION_IDENTIFIED",
                next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",
                notes="Identifier/author-heading collision retained from Canon; no image acquired.",
            )
        writer.writerow(row)
