"""Verified register for five canonical rows beginning at 2625.001."""
import csv

START=("2625","001")
OUTPUT="data/research_batches/detailed_verified_3001_batch_189.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")))
start=next(n for n,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START);works=coverage[start:start+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for w in works:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS}
  r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key==("2625","x01"):
   r.update(sources_tested="Canon App. Anth. reference resolved to 7052.005 and partial-duplication relation checked against 2625.001 fr. 494.",open_text_result="Partial overlap: host witness and fragment record require comparison before acquisition.",scan_result="No separate scan candidate confirmed.",confidence="high",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Process host 7052.005 and compare with 2625.001 fr. 494; retain only non-overlapping material; no OCR.",notes="Full cross-reference is not assumed because Canon also marks a partial duplicate; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited Supplementum Hellenisticum or FGrH bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(r)
