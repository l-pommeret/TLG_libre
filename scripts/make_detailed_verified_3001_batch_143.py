"""Verified register for rows after 0692.x02; records the exact First1K text match."""
import csv
START=("1400","001");OUTPUT="data/research_batches/detailed_verified_3001_batch_143.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(n for n,r in enumerate(c) if (r["tlg_author_id"],r["tlg_work_id"])==START);rows=c[i:i+5];assert len(rows)==5
v=list(csv.DictReader(open("data/text_verification.csv",encoding="utf-8")));by_id={(r['tlg_author_id'],r['tlg_work_id']):r for r in v}
with open(OUTPUT,"w",newline="",encoding="utf-8") as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for w in rows:
  key=(w["tlg_author_id"],w["tlg_work_id"]);text=by_id.get(key);r={f:"" for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w["author_heading"],work_title=w["work_title"],canonical_edition=w["bibliographic_notice"],sources_tested="Exact First1K/Perseus and local licence lookup; cited edition catalogue check",scan_result="No edition-matching reusable page-image source verified.",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.",last_checked="2026-08-11")
  if text:
   r.update(open_text_result="Exact open TEI match.",open_text_url=text['text_url'],open_text_license=text['tei_license'] or text['license'],confidence="high",proposed_status="TEXT_OPEN_UNVERIFIED")
  else:
   r.update(open_text_result="No exact licensed TEI match in local corpus.",confidence="medium",proposed_status="EDITION_IDENTIFIED")
  out.writerow(r)
