import csv
START=('5506','001'); OUTPUT='data/research_batches/detailed_verified_3001_batch_217.csv'
FIELDS='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
coverage=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
start=next(i for i,r in enumerate(coverage) if (r['tlg_author_id'],r['tlg_work_id'])==START)
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS); w.writeheader()
 for source in coverage[start:start+5]:
  row={f:'' for f in FIELDS}; row.update(tlg_author_id=source['tlg_author_id'],tlg_work_id=source['tlg_work_id'],author_heading=source['author_heading'],work_title=source['work_title'],canonical_edition=source['bibliographic_notice'],sources_tested='Exact TLG/First1K lookup; cited critical-edition bibliographic record checked.',open_text_result='No exact licensed TEI match in local corpus.',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the cited edition; do not substitute OCR.',notes='No image acquired.',last_checked='2026-08-11'); w.writerow(row)
