"""Verified register for five canonical rows beginning at 0020.008."""
import csv

START=("0020","008");OUTPUT="data/research_batches/detailed_verified_3001_batch_199.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(n for n,r in enumerate(c) if (r["tlg_author_id"],r["tlg_work_id"])==START);works=c[i:i+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as h:
 out=csv.DictWriter(h,fieldnames=FIELDS);out.writeheader()
 for w in works:
  k=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if k==("0020","008"):
   r.update(sources_tested="Canon partial-duplication relation checked against 0020.004 fr. 1 v. 16 and Renehan bibliographic record.",open_text_result="Partial overlap: no acquisition decision until fragment comparison.",scan_result="No separate scan candidate confirmed.",confidence="medium",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Compare fragment with 0020.004; retain only non-overlapping material; no OCR.",notes="No image acquired.")
  elif k==("0020","x01"):
   r.update(sources_tested="Canon App. Anth. relation checked against 7052.007 and partial-duplication relation against 0020.004 fr. 278.",open_text_result="Host witness and fragment record require comparison before acquisition.",scan_result="No separate scan candidate confirmed.",confidence="high",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Process host 7052.007 and compare with 0020.004 fr. 278; retain only non-overlapping material; no OCR.",notes="No image acquired.")
  elif k==("1428","002"):
   r.update(sources_tested="Canon exact-duplication statement checked against 1428.001.",open_text_result="No independent acquisition pending duplicate comparison.",scan_result="No separate scan candidate confirmed.",confidence="high",proposed_status="DUPLICATE_REVIEW",next_action="Compare FHG with 1428.001; do not duplicate text; no OCR.",notes="Canon marks this record as duplicate; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited FGrH or Lasserre bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  out.writerow(r)
