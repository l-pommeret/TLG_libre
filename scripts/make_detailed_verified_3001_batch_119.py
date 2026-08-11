"""Verified register for 2017.073--077; no page image or OCR is downloaded."""
import csv
IDS=("073","074","075","076","077")
OUTPUT="data/research_batches/detailed_verified_3001_batch_119.csv"
PG46='https://archive.org/details/patrologiaecursu46mignuoft'
PG45='https://archive.org/details/patrologiaecursu45mignuoft'
DIEKAMP='https://seminario.atcult.it/semarc/download?format=pdf&id=61106'
FIELDS=("tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked").split()
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for wid in IDS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==('2017',wid));r={f:'' for f in FIELDS}
  r.update(tlg_author_id='2017',tlg_work_id=wid,author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],open_text_result='No exact licensed TEI match in local corpus.',last_checked='2026-08-11')
  if wid=='073':
   r.update(sources_tested=f'Exact canonical PG citation; Internet Archive source {PG46}',scan_result='EXACT_SCAN_CANDIDATE: PG 46 covers cols. 1152--1181.',scan_url=PG46,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.',confidence='high',proposed_status='SCAN_CANDIDATE',next_action='Use original page images matching cited PG columns; do not use supplied OCR.',notes='No images downloaded.')
  elif wid=='076':
   r.update(sources_tested=f'Exact canonical PG citation; Internet Archive source {PG45}',scan_result='EXACT_SCAN_CANDIDATE: PG 45 covers cols. 221--236.',scan_url=PG45,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.',confidence='high',proposed_status='SCAN_CANDIDATE',next_action='Use original page images matching cited PG columns; do not use supplied OCR.',notes='No images downloaded.')
  elif wid=='074':
   r.update(sources_tested=f'Exact TLG lookup; cited Diekamp 1938 catalogue/PDF {DIEKAMP}',scan_result='No rights-cleared edition-matching page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Confirm reuse rights and page images for Diekamp 1938 before any transfer; no OCR.',notes='No image acquired.')
  else:
   r.update(sources_tested='Exact canonical PG citation; Internet Archive and catalogue search tested',scan_result='No concrete reusable page-image item verified for the cited PG volume.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate an item-level scan for the cited PG volume; do not substitute third-party OCR.',notes='No image acquired.')
  out.writerow(r)
