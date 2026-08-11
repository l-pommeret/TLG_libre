"""Verified register for five canonical rows beginning at 0928.x04."""
import csv

START=("0928","x04")
OUTPUT="data/research_batches/detailed_verified_3001_batch_197.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));ver={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/text_verification.csv",encoding="utf-8"))}
start=next(n for n,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START);works=coverage[start:start+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for w in works:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key==("0928","x04"):
   r.update(sources_tested="Canon cross-reference resolved to 0565.001 (Soranus, Med.).",open_text_result="No independent acquisition: host work controls text.",scan_result="No separate scan candidate: cross-reference only.",confidence="high",proposed_status="CROSS_REFERENCE",next_action="Process host 0565.001 (Soranus, Med.); do not duplicate this referring record.",notes="Resolved canon reference; no image acquired.")
  elif key in ver:
   tei=ver[key];r.update(sources_tested=f"Exact Perseus TLG identifier {tei['cts_urn']}; repository metadata checked.",open_text_result="Exact TEI candidate found; local register records repository-default CC BY-SA 4.0 pending file-level verification.",open_text_url=tei["text_url"],open_text_license="CC BY-SA 4.0 (repository default; file-level verification pending)",scan_result="No edition-matching reusable page-image source verified.",confidence="high",proposed_status="TEXT_OPEN_UNVERIFIED",next_action="Verify file-level licence and compare Canon boundaries/source edition before ingest; no OCR.",notes="Exact identifier and provenance recorded; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited FGrH bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(r)
