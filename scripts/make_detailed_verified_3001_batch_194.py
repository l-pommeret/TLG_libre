"""Verified register for five canonical rows beginning at 0559.010."""
import csv

START=("0559","010")
OUTPUT="data/research_batches/detailed_verified_3001_batch_194.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));ver={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/text_verification.csv",encoding="utf-8"))}
start=next(n for n,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START);works=coverage[start:start+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for w in works:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key in ver:
   tei=ver[key];r.update(sources_tested=f"Exact First1KGreek TLG identifier {tei['cts_urn']}; local TEI metadata and CC BY-SA 4.0 declaration checked.",open_text_result="Exact TEI candidate found; source metadata remains marked REVIEW_REQUIRED in the local verification register.",open_text_url=tei["text_url"],open_text_license="CC BY-SA 4.0 (First1KGreek TEI metadata)",scan_result="No edition-matching reusable page-image source verified.",confidence="high",proposed_status="TEXT_OPEN_UNVERIFIED",next_action="Compare Canon boundaries and cited Heron edition before ingest; no OCR.",notes="Exact identifier, provenance, and TEI licence recorded; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited Prou bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(r)
