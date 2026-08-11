import csv
w=list(csv.DictReader(open('data/canon_works.csv',encoding='utf8')));v=list(csv.DictReader(open('data/text_verification.csv',encoding='utf8')));m={(x['tlg_author_id'],x['tlg_work_id']):x for x in v}
h='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split();ids=[('0057',f'0{x}') for x in range(82,87)]
with open('data/research_batches/detailed_verified_3001_batch_02.csv','w',encoding='utf8',newline='') as f:
 z=csv.DictWriter(f,fieldnames=h);z.writeheader()
 for q in w:
  k=(q['tlg_author_id'],q['tlg_work_id'])
  if k not in ids:continue
  y=m[k];x={a:'' for a in h};x.update({a:q.get(a,'') for a in ['tlg_author_id','tlg_work_id','author_heading','work_title']});x.update(canonical_edition=q['bibliographic_notice'],sources_tested='First1KGreek exact TLG ID; Google Books catalogue checked',open_text_result='Exact open TEI match.',open_text_url=y['text_url'],open_text_license=y['tei_license'] or y['license'],scan_result='No edition-matching scan retained.',scan_url='',scan_rights='',confidence='high',proposed_status='TEXT_OPEN_UNVERIFIED',next_action='Compare TEI boundaries; do not use provider OCR.',notes='Google Books confirms Kühn vol.14 and De praenotione 599–673 only for 083; no claimed scan for other editions.',last_checked='2026-08-11');z.writerow(x)
