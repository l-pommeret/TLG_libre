"""Verified register for five canonical rows beginning at split record 0087.047."""
import csv

START = ("0087", "047")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_187.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")))
start=next(n for n,row in enumerate(coverage) if (row["tlg_author_id"],row["tlg_work_id"])==START)
works=coverage[start:start+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for work in works:
  key=(work["tlg_author_id"],work["tlg_work_id"]);row={f:"" for f in FIELDS}
  row.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=work["author_heading"],work_title=work["work_title"],canonical_edition=work["bibliographic_notice"],last_checked="2026-08-11")
  if key in {("0087","047"),("0087","529")}:
   row.update(sources_tested="Canonical split-record relation checked: 0087.047 title/notice continues in 0087.529.",open_text_result="No independent acquisition until the two Canon rows are reconstituted as one bibliographic record.",scan_result="No separate scan candidate confirmed.",confidence="high",proposed_status="SPLIT_RECORD_REVIEW",next_action="Reconstitute 0087.047 + 0087.529 before any text/scan work; then compare cited 0087.038; no OCR.",notes="Both canonical occurrences retained; no image acquired.")
  else:
   row.update(sources_tested="Exact TLG/First1K lookup; cited Cramer, Del Furia, or La Roche bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(row)
