"""Verified register for 2017.068--072; records PG page images, never downloads them."""
import csv
IDS=("068","069","070","071","072")
OUTPUT="data/research_batches/detailed_verified_3001_batch_118.csv"
PG46="https://archive.org/details/patrologiaecursu46mignuoft"
FIELDS=("tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked").split()
works=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for wid in IDS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==('2017',wid));r={f:'' for f in FIELDS}
  r.update(tlg_author_id='2017',tlg_work_id=wid,author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],sources_tested=f'Exact canonical PG citation; Internet Archive source {PG46}',open_text_result='No exact licensed TEI match in local corpus.',scan_result='EXACT_SCAN_CANDIDATE: PG 46 covers the cited canonical columns.',scan_url=PG46,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.',confidence='high',proposed_status='SCAN_CANDIDATE',next_action='Use original page images matching cited PG columns; do not use supplied OCR.',notes='No images downloaded; attribution note retained where [Sp.].',last_checked='2026-08-11');out.writerow(r)
