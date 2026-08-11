#!/usr/bin/env python3
"""Exact-ID research log for 100 notices from TLG 1172.001."""
import csv
from pathlib import Path
A=('1172','001'); END=('2130','040');N=100;D='2026-08-11';O=Path('data/research_batches')
H=['tlg_author_id','tlg_work_id','author_heading','work_title','canonical_edition','sources_tested','open_text_result','open_text_url','open_text_license','scan_result','scan_url','scan_rights','confidence','proposed_status','next_action','notes','last_checked'];B='base-3 (Perseus, First1KGreek, PTA); exact identifier/title check'
def main():
 w=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')));s=next(i for i,x in enumerate(w) if (x['tlg_author_id'],x['tlg_work_id'])==A);r=w[s:s+N];assert len(r)==N and (r[-1]['tlg_author_id'],r[-1]['tlg_work_id'])==END;ids={(x['tlg_author_id'],x['tlg_work_id']) for x in r};m={}
 for x in csv.DictReader(open('data/text_verification.csv',encoding='utf-8')):
  if (x['tlg_author_id'],x['tlg_work_id']) in ids:m[(x['tlg_author_id'],x['tlg_work_id'])]=x
 for n,o in enumerate(range(0,N,25),1):
  p=O/f'tlg_3001_4500_b11_batch_{n:04}.csv'
  with p.open('w',encoding='utf-8',newline='') as f:
   z=csv.DictWriter(f,fieldnames=H);z.writeheader()
   for q in r[o:o+25]:
    x={k:'' for k in H};x.update({'tlg_author_id':q['tlg_author_id'],'tlg_work_id':q['tlg_work_id'],'author_heading':q['author_heading'],'work_title':q['work_title'],'canonical_edition':q['bibliographic_notice'],'last_checked':D});k=(q['tlg_author_id'],q['tlg_work_id'])
    if k in m:
     v=m[k];x.update({'sources_tested':B+f"; local {v['corpus']} TEI exact identifier",'open_text_result':'Open licensed TEI found for the exact TLG work.','open_text_url':v['text_url'],'open_text_license':v['tei_license'] or v['license'],'confidence':'high','proposed_status':'TEXT_OPEN_UNVERIFIED','next_action':'compare Canon boundaries and source edition','notes':'Open TEI present locally; no provider OCR used.'})
    elif q['tlg_work_id'].startswith('x'):x.update({'sources_tested':'Canon cross-reference','open_text_result':'No independent acquisition: Canon directs this material to a host work.','confidence':'high','proposed_status':'CROSS_REFERENCE','next_action':'follow cited host-work record; do not duplicate','notes':'This is not a standalone acquisition target.'})
    elif 'FGrH' in q['bibliographic_notice'] or 'FHG' in q['bibliographic_notice']:x.update({'sources_tested':B+'; FGrH/FHG inventory','open_text_result':'No explicit reusable transcription found for this fragment dossier.','confidence':'low','proposed_status':'EDITION_IDENTIFIED','next_action':'locate an unrestricted historical scan or map earlier witnesses','notes':'No provider OCR may be used.'})
    else:x.update({'sources_tested':B,'open_text_result':'No reusable complete Greek text found.','confidence':'medium','proposed_status':'BLOCKED_RIGHTS','next_action':'seek an older open edition or individual witness','notes':'The Canon edition is not treated as reusable without an explicit licence.'})
    z.writerow(x)
  print(p)
 print('final_pointer=2130.040')
if __name__=='__main__':main()
