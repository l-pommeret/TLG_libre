"""Verified register for five canonical rows beginning at 0087.032."""
import csv

START = ("0087", "032")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_184.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
verification = {(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/text_verification.csv",encoding="utf-8"))}
start = next(n for n,row in enumerate(coverage) if (row["tlg_author_id"],row["tlg_work_id"]) == START)
works = coverage[start:start+5]; assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS); writer.writeheader()
 for work in works:
  key=(work["tlg_author_id"],work["tlg_work_id"]); row={field:"" for field in FIELDS}
  row.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=work["author_heading"],work_title=work["work_title"],canonical_edition=work["bibliographic_notice"],last_checked="2026-08-11")
  if key in verification:
   tei=verification[key]; row.update(sources_tested=f"Exact First1KGreek TLG identifier {tei['cts_urn']}; local TEI metadata and CC BY-SA 4.0 declaration checked.",open_text_result="Exact TEI candidate found; source metadata remains marked REVIEW_REQUIRED in the local verification register.",open_text_url=tei["text_url"],open_text_license="CC BY-SA 4.0 (First1KGreek TEI metadata)",scan_result="No edition-matching reusable page-image source verified.",confidence="high",proposed_status="TEXT_OPEN_UNVERIFIED",next_action="Compare Canon boundaries and Lentz edition before ingest; no OCR.",notes="Exact identifier, provenance, and TEI licence recorded; no image acquired.")
  elif key==("0087","034"):
   row.update(sources_tested="Canon related-text relation checked against 0087.009 (Περὶ παθῶν).",open_text_result="Supplementary material requires comparison before any acquisition.",scan_result="No separate scan candidate confirmed.",confidence="medium",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Compare supplement with 0087.009; retain only non-overlapping material; no OCR.",notes="‘Cf.’ relation is not converted to a full cross-reference; no image acquired.")
  else:
   row.update(sources_tested="Exact TLG/First1K lookup; cited Spengel or Boissonade bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(row)
