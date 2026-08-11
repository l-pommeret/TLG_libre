import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_609.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
canon={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
matches=list(csv.DictReader(open('data/corpus_matches.csv',encoding='utf-8')))
checks=list(csv.DictReader(open('data/text_verification.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for work in ['001','002','003','004','005']:
  s=canon[('0033',work)]; row={f:'' for f in FIELDS}; c=[r for r in matches if r['tlg_author_id']=='0033' and r['tlg_work_id']==work and r['corpus']=='Perseus']; v=[r for r in checks if r['tlg_author_id']=='0033' and r['tlg_work_id']==work and r['corpus']=='Perseus']
  row.update(tlg_author_id='0033',tlg_work_id=work,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact Canon item; local Perseus registry and Greek TEI; Sandys edition metadata; repository-level CC BY-SA 4.0 and Greek-content check.',scan_result='No separate scan acquisition was promoted.',last_checked='2026-08-11')
  if work!='005' and len(c)==len(v)==1 and v[0]['automated_check']=='AUTOMATED_TEI_CHECK_PASSED':
   row.update(open_text_result='Complete Greek text verified in the Sandys 1937 reprint, an open alternative to the Canon Maehler/Snell 1971 edition.',open_text_url=c[0]['text_url'],open_text_license='CC BY-SA 4.0 (Perseus repository)',confidence='high',proposed_status='OPEN_TEXT_COMPLETE_ALTERNATE_EDITION',next_action='Prepare the licensed TEI while preserving Sandys edition provenance.',notes=f"Exact CTS URN {c[0]['cts_urn']}; {v[0]['greek_characters']} Greek characters. File-level TEI omits a licence element, so provenance relies on the explicit Perseus repository licence; no OCR/images used.")
  else:
   row.update(open_text_result='No complete licensed Greek transcription matching the large Maehler fragment corpus was verified.',confidence='medium',proposed_status='NO_COMPLETE_OPEN_TEXT',next_action='Map fragment groups to individual ancient or papyrus witnesses.',notes='The four complete epinician collections are not extended to the separate fragment corpus. No OCR/images used.')
  w.writerow(row)
