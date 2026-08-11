import csv
w=list(csv.DictReader(open('data/canon_works.csv',encoding='utf8')));v=list(csv.DictReader(open('data/text_verification.csv',encoding='utf8')));m={(x['tlg_author_id'],x['tlg_work_id']):x for x in v};ids=[('0057',f'0{x}') for x in range(87,92)]
h='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
urls={'087':'https://cmg.bbaw.de/epubl/online/cmg_05_09_01.php','088':'https://cmg.bbaw.de/epubl/online/cmg_05_09_02.php','089':'https://cmg.bbaw.de/epubl/online/cmg_05_10_01.php','090':'https://pinakes.irht.cnrs.fr/notices/oeuvre/7933/','091':'https://cmg.bbaw.de/'}
with open('data/research_batches/detailed_verified_3001_batch_03.csv','w',encoding='utf8',newline='') as f:
 z=csv.DictWriter(f,fieldnames=h);z.writeheader()
 for q in w:
  k=(q['tlg_author_id'],q['tlg_work_id'])
  if k not in ids:continue
  y=m.get(k);x={a:'' for a in h};x.update({a:q.get(a,'') for a in ['tlg_author_id','tlg_work_id','author_heading','work_title']});x.update(canonical_edition=q['bibliographic_notice'],sources_tested='First1KGreek exact TLG ID; CMG/Pinakes external edition catalogue',scan_result='Edition catalogue confirmed; no downloadable scan retained.',scan_url=urls[k[1]],scan_rights='No explicit reusable image licence verified; not a scan candidate.',next_action='Compare text against cited CMG edition; do not use provider OCR.',notes='External catalogue agrees with editor/year/pages stated in Canon where applicable.',last_checked='2026-08-11')
  if y:x.update(open_text_result='Exact open TEI match.',open_text_url=y['text_url'],open_text_license=y['tei_license'] or y['license'],confidence='high',proposed_status='TEXT_OPEN_UNVERIFIED')
  else:x.update(open_text_result='No exact licensed TEI found in First1KGreek.',confidence='medium',proposed_status='EDITION_IDENTIFIED')
  z.writerow(x)
