"""Verified register for 2063.008/.009/.010/.013/.016; no image/OCR download."""
import csv
IDS=('008','009','010','013','016');OUTPUT='data/research_batches/detailed_verified_3001_batch_124.csv';PG10='https://archive.org/details/patrologiaecursu10mignuoft'
FIELDS=('tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked').split()
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for wid in IDS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==('2063',wid));r={f:'' for f in FIELDS};r.update(tlg_author_id='2063',tlg_work_id=wid,author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],open_text_result='No exact licensed TEI match in local corpus.',last_checked='2026-08-11')
  if wid!='016':
   r.update(sources_tested=f'Exact canonical PG citation; Internet Archive source {PG10}',scan_result='EXACT_SCAN_CANDIDATE: PG 10 covers the cited canonical columns.',scan_url=PG10,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.',confidence='high',proposed_status='SCAN_CANDIDATE',next_action='Use original page images matching cited PG columns; do not use supplied OCR.',notes='No images downloaded; partial duplicate relation retained where noted.')
  else:
   r.update(sources_tested='Exact TLG/First1K lookup; cited Pitra 1883 edition catalogue check',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of Pitra 1883; do not substitute OCR.',notes='No image acquired.')
  out.writerow(r)
