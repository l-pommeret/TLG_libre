import csv
from make_detailed_verified_3001_ag_batch import FIELDS
OUTPUT='data/research_batches/detailed_verified_3001_batch_640.csv';TARGETS=[('0109','001'),('0110','001'),('0116','001'),('0116','002'),('0123','001')];canon={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for key in TARGETS:
  s=canon[key];row={f:'' for f in FIELDS};row.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact Canon notice; local AG/FGrH/FHG/open-corpus registries; duplicate and language boundaries preserved.',scan_result='No exact rights-cleared and Greek-sampled item-level scan promoted.',last_checked='2026-08-11')
  if key[0] in {'0109','0110'}: row.update(open_text_result='Printed AG loci are concrete open-text leads requiring complete attribution concordance.',confidence='medium',proposed_status='PARTIAL_OPEN_TEXT_REQUIRES_AG_CONCORDANCE',next_action='Verify every AG locus individually.',notes='Cross-references and homonyms are not merged; no OCR/images used.')
  elif key[0]=='0116': row.update(open_text_result='No complete licensed Greek transcription matching this exact FGrH/FHG fragment aggregate was verified.',confidence='medium',proposed_status='NO_COMPLETE_OPEN_TEXT',next_action='Map Greek fragments to ancient hosts and keep Latin-only fragments distinct.',notes='Partial duplicate relation preserved; Latin witnesses are not mislabeled as Greek.')
  else: row.update(open_text_result='No complete licensed Greek transcription of the exact testimonia collection was verified.',confidence='medium',proposed_status='NO_COMPLETE_OPEN_TEXT',next_action='Identify every ancient testimony host.',notes='No doctrine or neighbouring philosophical corpus substituted; no OCR/images used.')
  w.writerow(row)
