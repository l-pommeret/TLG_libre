import csv
FIELDS='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
def build(output,works):
 canon={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
 with open(output,'w',newline='',encoding='utf-8') as h:
  w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
  for work in works:
   s=canon[('0096',work)];row={f:'' for f in FIELDS};row.update(tlg_author_id='0096',tlg_work_id=work,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact Canon Aesop subset; local open fable collection and AG registries; subset boundaries checked.',scan_result='No exact rights-cleared and Greek-sampled subset scan promoted.',confidence='medium',last_checked='2026-08-11')
   if work=='014': row.update(open_text_result='AG 10.123 is a concrete open-text lead requiring attribution-level verification.',proposed_status='PARTIAL_OPEN_TEXT_REQUIRES_AG_CONCORDANCE',next_action='Verify AG 10.123 individually.',notes='No collection-wide completeness inferred.')
   else: row.update(open_text_result='No exact licensed Greek transcription of this separately edited fable or sententia subset was verified.',proposed_status='NO_EXACT_OPEN_TEXT',next_action='Map the subset item by item against open Aesop collections or its direct witness.',notes='No inclusion in 0096.002 inferred from genre or proximity; no OCR/images used.')
   w.writerow(row)
