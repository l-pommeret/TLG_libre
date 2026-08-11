"""Verified register for five canonical rows beginning at 1418.001."""
import csv

START = ("1418", "001")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_163.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
HOST = ("0974", "x01")
HOST_WORK = "0671.001 (Philumenus, Med.)"

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
        if key == HOST:
            row.update(
                sources_tested=f"Canon cross-reference resolved to {HOST_WORK}.",
                open_text_result="No independent acquisition: host work controls text.",
                scan_result="No separate scan candidate: cross-reference only.",
                confidence="high", proposed_status="CROSS_REFERENCE",
                next_action=f"Process host {HOST_WORK}; do not duplicate this referring record.",
                notes="Resolved canon reference; no image acquired.",
            )
        else:
            row.update(
                sources_tested="Exact TLG/First1K lookup; cited FGrH, Krohn, or Longo Auricchio bibliographic record checked.",
                open_text_result="No exact licensed TEI match in local corpus.",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="medium", proposed_status="EDITION_IDENTIFIED",
                next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",
                notes="No image acquired.",
            )
        writer.writerow(row)
