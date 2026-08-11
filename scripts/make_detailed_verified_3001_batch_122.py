"""Verified register for 2017.x01/x02, 4499.001, 4498.001, 2063.001."""
import csv
TARGETS=[('2017','x01'),('2017','x02'),('4499','001'),('4498','001'),('2063','001')]
OUTPUT='data/research_batches/detailed_verified_3001_batch_122.csv'
PG10='https://archive.org/details/patrologiaecursu10mignuoft'
FIELDS=('tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked').split()
XREF={('2017','x01'):'2040.004 (Basilius Caesariensis, Epist. 38)',('2017','x02'):'0743.001 (Nemesius, De natura hominis, cap. 2--3)'}
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for key in TARGETS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==key);r={f:'' for f in FIELDS};r.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],last_checked='2026-08-11')
  if key in XREF:
   host=XREF[key];r.update(sources_tested=f'Canon cross-reference resolved to {host}',open_text_result='No independent acquisition: host work controls text.',scan_result='No separate scan candidate: cross-reference only.',confidence='high',proposed_status='CROSS_REFERENCE',next_action=f'Process host {host}; do not duplicate this referring record.',notes=f'Resolved canon reference: {host}.')
  elif key==('2063','001'):
   r.update(sources_tested=f'SC 148 citation; alternative historical PG 10 source {PG10}',open_text_result='No exact licensed TEI match in local corpus.',scan_result='ALTERNATIVE_SCAN_CANDIDATE: PG 10 historical text; column match required, not SC 148.',scan_url=PG10,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify concordance before transfer.',confidence='medium',proposed_status='ALTERNATIVE_SCAN_CANDIDATE',next_action='Collate PG 10 against SC 148; use original images only, never supplied OCR.',notes='No images downloaded.')
  else:
   r.update(sources_tested='Exact TLG/First1K lookup; cited-edition catalogue check',open_text_result='No exact licensed TEI match in local corpus.',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the cited edition; do not substitute OCR.',notes='No image acquired.')
  out.writerow(r)
