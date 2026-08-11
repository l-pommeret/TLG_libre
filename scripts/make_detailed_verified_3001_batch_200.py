import csv
START=("0225","002");OUTPUT="data/research_batches/detailed_verified_3001_batch_200.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split();c=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')));i=next(i for i,x in enumerate(c) if (x['tlg_author_id'],x['tlg_work_id'])==START);w=c[i:i+5];assert len(w)==5
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 o=csv.DictWriter(h,fieldnames=F);o.writeheader()
 for x in w:
  r={f:'' for f in F};r.update(tlg_author_id=x['tlg_author_id'],tlg_work_id=x['tlg_work_id'],author_heading=x['author_heading'],work_title=x['work_title'],canonical_edition=x['bibliographic_notice'],sources_tested='Exact TLG/First1K lookup; cited Lasserre, Flach, or Dindorf bibliographic record checked.',open_text_result='No exact licensed TEI match in local corpus.',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the cited edition; do not substitute OCR.',notes='No image acquired.',last_checked='2026-08-11')
  if (x['tlg_author_id'],x['tlg_work_id'])==('2274','001'):
   r.update(sources_tested='Canon partial-duplication relation checked against 2274.005 and 2274.007.',open_text_result='Partial overlap: no acquisition decision until comparison.',scan_result='No separate scan candidate confirmed.',proposed_status='PARTIAL_DUPLICATION_REVIEW',next_action='Compare overlaps with 2274.005/.007; retain only non-overlapping material; no OCR.',notes='No image acquired.')
  o.writerow(r)
