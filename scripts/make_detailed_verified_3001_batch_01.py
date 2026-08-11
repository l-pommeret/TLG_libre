import csv
from pathlib import Path
w=list(csv.DictReader(open('data/canon_works.csv',encoding='utf8'))); v=list(csv.DictReader(open('data/text_verification.csv',encoding='utf8')))
ids=[('0057',f'{n:03d}') for n in range(57,82)]; m={(x['tlg_author_id'],x['tlg_work_id']):x for x in v}
h='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
with open('data/research_batches/detailed_verified_3001_batch_01.csv','w',encoding='utf8',newline='') as f:
 z=csv.DictWriter(f,fieldnames=h);z.writeheader()
 for q in w:
  k=(q['tlg_author_id'],q['tlg_work_id'])
  if k not in ids:continue
  x={a:'' for a in h};x.update({a:q.get(a,'') for a in ['tlg_author_id','tlg_work_id','author_heading','work_title']});x['canonical_edition']=q['bibliographic_notice'];x['last_checked']='2026-08-11'
  if k in m:
   y=m[k];x.update(sources_tested='First1KGreek local catalog; exact TLG ID',open_text_result='Exact open TEI match.',open_text_url=y['text_url'],open_text_license=y['tei_license'] or y['license'],scan_result='No scan acquired.',confidence='high',proposed_status='TEXT_OPEN_UNVERIFIED',next_action='Compare textual boundaries.',notes='No third-party OCR.')
  else:x.update(sources_tested='First1KGreek local catalog exact-ID check',open_text_result='No exact open TEI match found.',scan_result='No scan candidate verified.',confidence='medium',proposed_status='BLOCKED_RIGHTS',next_action='Research historical edition catalogues.',notes='No third-party OCR.')
  z.writerow(x)
