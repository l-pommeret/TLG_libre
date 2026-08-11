"""Verified register for 2017.083, .084, .088--.090; no page image or OCR is downloaded."""
import csv
IDS=('083','084','088','089','090');OUTPUT='data/research_batches/detailed_verified_3001_batch_121.csv'
PG45='https://archive.org/details/patrologiaecursu45mignuoft';PG46='https://archive.org/details/patrologiaecursu46mignuoft'
FIELDS=('tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked').split()
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for wid in IDS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==('2017',wid));r={f:'' for f in FIELDS};r.update(tlg_author_id='2017',tlg_work_id=wid,author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],open_text_result='No exact licensed TEI match in local corpus.',last_checked='2026-08-11')
  if wid=='083':
   r.update(sources_tested=f'GNO 3.2 citation; alternative PG 46 {PG46}',scan_result='ALTERNATIVE_SCAN_CANDIDATE: PG 46, cols. 161--192; not GNO 3.2.',scan_url=PG46,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify concordance before transfer.',confidence='medium',proposed_status='ALTERNATIVE_SCAN_CANDIDATE',next_action='Collate PG 46 against GNO 3.2; original images only, no OCR.',notes='No images downloaded.')
  elif wid=='088':
   r.update(sources_tested=f'SC 453 citation; alternative PG 45 {PG45}',scan_result='ALTERNATIVE_SCAN_CANDIDATE: PG 45, cols. 11--105; not SC 453.',scan_url=PG45,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify concordance before transfer.',confidence='medium',proposed_status='ALTERNATIVE_SCAN_CANDIDATE',next_action='Collate PG 45 against SC 453; original images only, no OCR.',notes='No images downloaded.')
  elif wid=='089':
   r.update(sources_tested='Canon duplicate relation checked: 2017.089 duplicates 2017.082 (different Bandini edition).',open_text_result='No independent acquisition: duplicate work host controls text.',scan_result='No separate scan candidate: duplicate edition record.',confidence='high',proposed_status='DUPLICATE_EDITION_REFERENCE',next_action='Use 2017.082 as text host; retain Bandini 2003 solely as bibliographic reference.',notes='No duplicate text/image acquisition.')
  elif wid=='090':
   r.update(sources_tested='Canon duplicate relation checked: 2017.090 duplicates 2017.047 (different SC edition).',open_text_result='No independent acquisition: duplicate work host controls text.',scan_result='No separate scan candidate: duplicate edition record.',confidence='high',proposed_status='DUPLICATE_EDITION_REFERENCE',next_action='Use 2017.047 as text host; retain SC 596 solely as bibliographic reference.',notes='No duplicate text/image acquisition.')
  else:
   r.update(sources_tested='GNO 3.2 bibliographic record; exact TLG/First1K lookup',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of GNO 3.2 or verified historical witness; no OCR.',notes='No image acquired.')
  out.writerow(r)
