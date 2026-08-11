"""Verified register for five canonical rows beginning at 0926.x03."""
import csv

START=("0926","x03")
OUTPUT="data/research_batches/detailed_verified_3001_batch_191.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
HOSTS={"x03":"0718.004 (Aëtius, Med.)","x04":"0718.005 (Aëtius, Med.)","x05":"0718.009 (Aëtius, Med.)","x06":"0718.015 (Aëtius, Med.)"}
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));start=next(n for n,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START);works=coverage[start:start+5];assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for w in works:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key[1] in HOSTS:
   host=HOSTS[key[1]];r.update(sources_tested=f"Canon cross-reference resolved to {host}.",open_text_result="No independent acquisition: host work controls text.",scan_result="No separate scan candidate: cross-reference only.",confidence="high",proposed_status="CROSS_REFERENCE",next_action=f"Process host {host}; do not duplicate this referring record.",notes="Resolved canon reference; no image acquired.")
  else:
   r.update(sources_tested="Canon doubtful-attribution relation checked against 0721.026 (Anonymi Medici) and Fuchs bibliographic record.",open_text_result="Doubtful attribution requires comparison before any acquisition.",scan_result="No separate scan candidate confirmed.",confidence="medium",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Compare text and attribution with 0721.026; retain only non-overlapping material; no OCR.",notes="A doubtful ‘Cf.’ relation is not converted to a full cross-reference; no image acquired.")
  writer.writerow(r)
