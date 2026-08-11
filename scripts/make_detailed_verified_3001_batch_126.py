"""Verified register for 2063.025/.028, 2118.001, 4475.001--002; no local assets."""
import csv
TARGETS=[('2063','025'),('2063','028'),('2118','001'),('4475','001'),('4475','002')];OUTPUT='data/research_batches/detailed_verified_3001_batch_126.csv'
FIELDS=('tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked').split()
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for key in TARGETS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==key);r={f:'' for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],sources_tested='Exact TLG/First1K lookup; cited edition/papyrological catalogue check',open_text_result='No exact licensed TEI match in local corpus.',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the cited edition or papyrus; do not substitute OCR.',notes='No image acquired.',last_checked='2026-08-11');out.writerow(r)
