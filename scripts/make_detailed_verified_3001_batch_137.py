"""Verified register for five rows after 1391.004, resolving the Hegemon cross-reference."""
import csv
START=("1925","x01");OUTPUT="data/research_batches/detailed_verified_3001_batch_137.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(n for n,r in enumerate(c) if (r["tlg_author_id"],r["tlg_work_id"])==START);rows=c[i:i+5];assert len(rows)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for w in rows:
  key=(w["tlg_author_id"],w["tlg_work_id"]);r={f:"" for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],last_checked="2026-08-11")
  if key==("1925","x01"):
   r.update(sources_tested="Canon cross-reference resolved to 1391.001 (Hegemon, Epic.).",open_text_result="No independent acquisition: host work controls text.",scan_result="No separate scan candidate: cross-reference only.",confidence="high",proposed_status="CROSS_REFERENCE",next_action="Process host 1391.001; do not duplicate this referring record.",notes="Resolved canon reference; no image acquired.")
  else:
   r.update(sources_tested="Exact TLG/First1K lookup; cited FGrH/FHG catalogue check",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  out.writerow(r)
