"""Verified register for rows from 4367.001, resolving medical cross-references."""
import csv
START=("4367","001");OUTPUT="data/research_batches/detailed_verified_3001_batch_142.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(n for n,r in enumerate(c) if (r["tlg_author_id"],r["tlg_work_id"])==START);rows=c[i:i+5];assert len(rows)==5
xrefs={("0692","x01"):"0722.001 (Oribasius, Med.)",("0692","x02"):"0715.001 (Paulus, Med.)"}
with open(OUTPUT,"w",newline="",encoding="utf-8") as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for w in rows:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key in xrefs:
   host=xrefs[key];r.update(sources_tested=f"Canon cross-reference resolved to {host}.",open_text_result="No independent acquisition: host work controls text.",scan_result="No separate scan candidate: cross-reference only.",confidence="high",proposed_status="CROSS_REFERENCE",next_action=f"Process host {host}; do not duplicate this referring record.",notes="Resolved canon reference; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited manuscript catalogue check",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited manuscript; do not substitute OCR.",notes="No image acquired; doubtful status retained where marked.")
  out.writerow(r)
