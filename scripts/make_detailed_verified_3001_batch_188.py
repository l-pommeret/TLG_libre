"""Verified register for five canonical rows beginning at 0087.054."""
import csv

START=("0087","054")
OUTPUT="data/research_batches/detailed_verified_3001_batch_188.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")))
start=next(n for n,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START);works=coverage[start:start+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for w in works:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS}
  r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key==("0087","x01"):
   r.update(sources_tested="Canon attribution/related-text relation checked against 0708.002 (<Ammonius> Gramm.).",open_text_result="Potentially overlapping material: no acquisition decision until attribution comparison.",scan_result="No separate scan candidate confirmed.",confidence="medium",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Compare attribution and text with 0708.002; retain only non-overlapping material; no OCR.",notes="A ‘Cf.’ relation is not converted to a full cross-reference; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited Cramer, Lentz, or Hajdú bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(r)
