"""Verified register for 2017.078--082; no page image or OCR is downloaded."""
import csv
IDS=('078','079','080','081','082');OUTPUT='data/research_batches/detailed_verified_3001_batch_120.csv'
PG44='https://archive.org/details/patrologiaecursu44mignuoft';PG46='https://archive.org/details/patrologiaecursu46mignuoft'
FIELDS=('tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked').split()
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
detail={'078':(PG44,'EXACT_SCAN_CANDIDATE: PG 44, cols. 61--124.'),'079':(PG44,'EXACT_SCAN_CANDIDATE: PG 44, cols. 124--256.'),'080':(PG46,'EXACT_SCAN_CANDIDATE: PG 46, col. 1112.'),'081':(PG44,'ALTERNATIVE_SCAN_CANDIDATE: PG 44 historical text; not GNO 3.2 (1986).')}
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for wid in IDS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==('2017',wid));r={f:'' for f in FIELDS};r.update(tlg_author_id='2017',tlg_work_id=wid,author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],open_text_result='No exact licensed TEI match in local corpus.',last_checked='2026-08-11')
  if wid in detail:
   scan,result=detail[wid];r.update(sources_tested=f'Exact canonical/alternative PG citation; Internet Archive source {scan}',scan_result=result,scan_url=scan,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.',confidence='high' if result.startswith('EXACT') else 'medium',proposed_status='SCAN_CANDIDATE' if result.startswith('EXACT') else 'ALTERNATIVE_SCAN_CANDIDATE',next_action='Use original page images matching cited PG columns; do not use supplied OCR.' if result.startswith('EXACT') else 'Collate PG text against GNO 3.2 before transfer; do not use OCR.',notes='No images downloaded.')
  else:
   r.update(sources_tested='GNO 3.2 bibliographic record; exact TLG/First1K lookup',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the GNO 3.2 edition or verified historical witness; no OCR.',notes='No image acquired.')
  out.writerow(r)
