"""Verified register for five canonical rows after 1395.001; no image/OCR download."""
import csv
START=("1395","002");OUTPUT="data/research_batches/detailed_verified_3001_batch_139.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(n for n,r in enumerate(c) if (r["tlg_author_id"],r["tlg_work_id"])==START);rows=c[i:i+5];assert len(rows)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for w in rows:
  r={f:"" for f in FIELDS};r.update(tlg_author_id=w["tlg_author_id"],tlg_work_id=w["tlg_work_id"],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],sources_tested="Exact TLG/First1K lookup; cited FGrH/FHG catalogue check",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="Spurious attribution retained where marked; no image acquired.",last_checked="2026-08-11");out.writerow(r)
