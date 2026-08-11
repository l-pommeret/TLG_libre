import csv
from make_detailed_verified_3001_ag_batch import FIELDS
OUTPUT='data/research_batches/detailed_verified_3001_batch_638.csv';canon={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))};matches=list(csv.DictReader(open('data/corpus_matches.csv',encoding='utf-8')));checks=list(csv.DictReader(open('data/text_verification.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for key in [('0099','003'),('0099','004'),('0101','001'),('0102','001'),('0103','001')]:
  s=canon[key];row={f:'' for f in FIELDS};row.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact Canon notice; local TEI/AG registry and edition boundaries.',scan_result='No separate scan promoted.',last_checked='2026-08-11')
  if key==('0099','004'):
   c=[r for r in matches if r['tlg_author_id']=='0099' and r['tlg_work_id']=='004'][0];v=[r for r in checks if r['tlg_author_id']=='0099' and r['tlg_work_id']=='004' and r['automated_check']=='AUTOMATED_TEI_CHECK_PASSED'][0];row.update(open_text_result='Complete licensed Greek Chrestomathy verified in an open historical edition alternative to Radt 2010.',open_text_url=c['text_url'],open_text_license='CC BY-SA 4.0',confidence='high',proposed_status='OPEN_TEXT_COMPLETE_ALTERNATE_EDITION',next_action='Prepare licensed TEI while preserving source edition.',notes=f"{v['greek_characters']} Greek characters; no OCR/images used.")
  elif key==('0099','003'): row.update(open_text_result='No complete licensed Greek transcription matching the separate FGrH fragment aggregate was verified.',confidence='medium',proposed_status='NO_COMPLETE_OPEN_TEXT',next_action='Map fragments to ancient hosts.',notes='Full Strabo text is not substituted.')
  else: row.update(open_text_result='Printed AG loci are concrete open-text leads requiring full attribution concordance.',confidence='medium',proposed_status='PARTIAL_OPEN_TEXT_REQUIRES_AG_CONCORDANCE',next_action='Verify every AG locus individually.',notes='No homonym or anonymous cross-reference merged; no OCR/images used.')
  w.writerow(row)
