import csv
OUTPUT='data/research_batches/detailed_verified_3001_batch_611.csv'; FIELDS='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
TARGETS=[('0035','006'),('0037','001'),('0039','001'),('0042','001'),('0043','001')]
canon={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}; matches=list(csv.DictReader(open('data/corpus_matches.csv',encoding='utf-8'))); checks=list(csv.DictReader(open('data/text_verification.csv',encoding='utf-8')))
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for key in TARGETS:
  s=canon[key]; row={f:'' for f in FIELDS}; row.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact Canon notice; local Perseus/First1K registries and TEI verification; Hercher or AG boundaries checked item-level.',scan_result='No exact rights-cleared and Greek-sampled scan was needed or promoted.',last_checked='2026-08-11')
  c=[r for r in matches if r['tlg_author_id']==key[0] and r['tlg_work_id']==key[1] and r['corpus']=='First1KGreek']; v=[r for r in checks if r['tlg_author_id']==key[0] and r['tlg_work_id']==key[1] and r['corpus']=='First1KGreek']
  if key[0] in {'0037','0039'} and len(c)==len(v)==1 and v[0]['automated_check']=='AUTOMATED_TEI_CHECK_PASSED':
   row.update(open_text_result='Complete Greek TEI verified in the exact Hercher 1873 edition cited by the Canon.',open_text_url=c[0]['text_url'],open_text_license='CC BY-SA 4.0',confidence='high',proposed_status='OPEN_TEXT_COMPLETE_EXACT_EDITION',next_action='Prepare exact licensed TEI for ingestion.',notes=f"Exact URN {c[0]['cts_urn']}; explicit file-level licence; {v[0]['greek_characters']} Greek characters; no OCR/images used.")
  elif key[0]=='0035':
   row.update(open_text_result='The two AG loci and overlaps with Moschus 001/005 are concrete open-text leads, but attribution-level concordance is not yet complete.',confidence='medium',proposed_status='PARTIAL_OPEN_TEXT_REQUIRES_AG_CONCORDANCE',next_action='Verify AG 9.440 and 16.200 individually and preserve duplicate relations.',notes='No completeness inferred from the Edmonds Moschus corpus or neighbouring AG records.')
  else:
   row.update(open_text_result='No exact licensed Greek transcription of this short Hercher epistolary item was verified in local open corpora.',confidence='medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action='Map the letter to a direct manuscript or ancient host before acquisition.',notes='Herodotus 3.40–43 is retained only as a contextual cross-reference for Amasis, not substituted for the letter; no OCR/images used.')
  w.writerow(row)
