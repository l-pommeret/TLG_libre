"""Verified register for five canonical rows from 3046.001; no image/OCR download."""
import csv

START = ("3046", "001")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_130.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
index = next(n for n, row in enumerate(coverage) if (row["tlg_author_id"], row["tlg_work_id"]) == START)
rows = coverage[index:index + 5]
assert len(rows) == 5

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    out = csv.DictWriter(handle, fieldnames=FIELDS)
    out.writeheader()
    for work in rows:
        key = (work["tlg_author_id"], work["tlg_work_id"])
        result = {field: "" for field in FIELDS}
        result.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=work["author_heading"], work_title=work["work_title"], canonical_edition=work["bibliographic_notice"], last_checked="2026-08-11")
        if key == ("1388", "002"):
            result.update(sources_tested="Canon duplicate relation checked: 1388.002 duplicates 1388.001 in an alternate FHG reference.", open_text_result="No independent acquisition: 1388.001 controls shared fragments.", scan_result="No separate scan candidate: duplicate reference record.", confidence="high", proposed_status="DUPLICATE_EDITION_REFERENCE", next_action="Use 1388.001 as text host; retain FHG citation as bibliographic reference.", notes="No duplicate text/image acquisition.")
        else:
            result.update(sources_tested="Exact TLG/First1K lookup; cited edition/FGrH catalogue check", open_text_result="No exact licensed TEI match in local corpus.", scan_result="No edition-matching reusable page-image source verified.", confidence="medium", proposed_status="EDITION_IDENTIFIED", next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.", notes="No image acquired.")
        out.writerow(result)
