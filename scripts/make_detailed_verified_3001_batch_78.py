import csv
w=list(csv.DictReader(open('data/canon_works.csv')));v=list(csv.DictReader(open('data/text_verification.csv')));m={(x['tlg_author_id'],x['tlg_work_id']):x for x in v};ids={('2707','x01'),('3277','001'),('0964','x01'),('2833','001'),('2833','002')};h='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
with open('data/research_batches/detailed_verified_3001_batch_78.csv','w',newline='') as f:
 z=csv.DictWriter(f,fieldnames=h);z.writeheader()
 for q in w:
  k=(q['tlg_author_id'],q['tlg_work_id'])
  if k not in ids:continue
  x={a:'' for a in h};x.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=q['author_heading'],work_title=q['work_title'],canonical_edition=q['bibliographic_notice'],last_checked='2026-08-11')
  if k[1].startswith('x'):x.update(sources_tested='Canon cross-reference checked',open_text_result='No independent acquisition.',confidence='high',proposed_status='CROSS_REFERENCE',next_action='Resolve cited host work; do not duplicate.',notes='No provider OCR used.')
  elif k in m:
   y=m[k];x.update(sources_tested='First1KGreek/Perseus exact TLG ID; external catalogue check',open_text_result='Exact open TEI match.',open_text_url=y['text_url'],open_text_license=y['tei_license'] or y['license'],scan_result='No edition-matching reusable scan verified.',confidence='high',proposed_status='TEXT_OPEN_UNVERIFIED',next_action='Compare against cited edition; no OCR.',notes='No provider OCR used.')
  else:x.update(sources_tested='First1KGreek/Perseus exact TLG ID; external catalogue check',open_text_result='No exact licensed TEI match in local corpus.',scan_result='No edition-matching reusable scan verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate historical edition scan; no OCR.',notes='No provider OCR used.')
  z.writerow(x)
