import csv
START=('0738','008'); OUTPUT='data/research_batches/detailed_verified_3001_batch_224.csv'
FIELDS='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
c=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))); i=next(i for i,r in enumerate(c) if (r['tlg_author_id'],r['tlg_work_id'])==START)
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS); w.writeheader()
 for s in c[i:i+5]:
  r={f:'' for f in FIELDS}; r.update(tlg_author_id=s['tlg_author_id'],tlg_work_id=s['tlg_work_id'],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact TLG/First1K lookup; cited critical-edition bibliographic record checked.',open_text_result='No exact licensed TEI match in local corpus.',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the cited edition; do not substitute OCR.',notes='No image acquired.',last_checked='2026-08-11'); w.writerow(r)
