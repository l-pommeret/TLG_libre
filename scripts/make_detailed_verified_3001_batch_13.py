import csv
w=list(csv.DictReader(open('data/canon_works.csv')));v=list(csv.DictReader(open('data/text_verification.csv')));m={(x['tlg_author_id'],x['tlg_work_id']):x for x in v};ids={('0530','046'),('3238','001'),('2452','001'),('0189','001'),('0797','x01')};h='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
with open('data/research_batches/detailed_verified_3001_batch_13.csv','w',newline='') as f:
 z=csv.DictWriter(f,fieldnames=h);z.writeheader()
 for q in w:
  k=(q['tlg_author_id'],q['tlg_work_id'])
  if k not in ids:continue
  x={a:'' for a in h};x.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=q['author_heading'],work_title=q['work_title'],canonical_edition=q['bibliographic_notice'],sources_tested='First1KGreek/Perseus exact TLG ID; external catalogue check',scan_result='No edition-matching reusable scan verified.',next_action='Compare against cited edition; no OCR.',notes='No provider OCR used.',last_checked='2026-08-11');y=m.get(k)
  if y:x.update(open_text_result='Exact open TEI match.',open_text_url=y['text_url'],open_text_license=y['tei_license'] or y['license'],confidence='high',proposed_status='TEXT_OPEN_UNVERIFIED')
  else:x.update(open_text_result='No exact licensed TEI match in local corpus.',confidence='medium',proposed_status='EDITION_IDENTIFIED')
  z.writerow(x)
