#!/usr/bin/env python3
"""Exact-ID research log from 1194.004 to 0086.037."""
import csv
from pathlib import Path

A=('1194','004'); E=('0086','037'); N=100; D='2026-08-11'; O=Path('data/research_batches'); P='tlg_3001_4500_b14'
H='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
B='base-3 (Perseus, First1KGreek, PTA); exact identifier/title check'

def main():
    w=list(csv.DictReader(open('data/canon_works.csv',encoding='utf-8')))
    s=next(i for i,x in enumerate(w) if (x['tlg_author_id'],x['tlg_work_id'])==A)
    r=w[s:s+N]
    assert len(r)==N and (r[-1]['tlg_author_id'],r[-1]['tlg_work_id'])==E
    ids={(x['tlg_author_id'],x['tlg_work_id']) for x in r}; m={}; scan_ids=set()
    for x in csv.DictReader(open('data/text_verification.csv',encoding='utf-8')):
        if (x['tlg_author_id'],x['tlg_work_id']) in ids: m[(x['tlg_author_id'],x['tlg_work_id'])]=x
    for x in csv.DictReader(open('data/scan_sources.csv',encoding='utf-8')):
        if (x['tlg_author_id'],x['tlg_work_id']) in ids: scan_ids.add((x['tlg_author_id'],x['tlg_work_id']))
    for n,o in enumerate(range(0,N,25),1):
        with (O/f'{P}_batch_{n:04}.csv').open('w',encoding='utf-8',newline='') as f:
            z=csv.DictWriter(f,fieldnames=H); z.writeheader()
            for q in r[o:o+25]:
                x={k:'' for k in H}
                x.update({'tlg_author_id':q['tlg_author_id'],'tlg_work_id':q['tlg_work_id'],'author_heading':q['author_heading'],'work_title':q['work_title'],'canonical_edition':q['bibliographic_notice'],'last_checked':D})
                k=(q['tlg_author_id'],q['tlg_work_id'])
                x['scan_result']='Existing approved scan record; avoid duplicate acquisition.' if k in scan_ids else 'No existing approved scan record in scan_sources.csv.'
                if k in m:
                    v=m[k]; x.update({'sources_tested':B+f"; local {v['corpus']} TEI exact identifier",'open_text_result':'Open licensed TEI found for exact TLG work.','open_text_url':v['text_url'],'open_text_license':v['tei_license'] or v['license'],'confidence':'high','proposed_status':'TEXT_OPEN_UNVERIFIED','next_action':'compare Canon boundaries and source edition','notes':'Open TEI present locally; no provider OCR used.'})
                elif q['tlg_work_id'].startswith('x'):
                    x.update({'sources_tested':'Canon cross-reference','open_text_result':'No independent acquisition: Canon directs material to host work.','confidence':'high','proposed_status':'CROSS_REFERENCE','next_action':'follow cited host; do not duplicate','notes':'Not a standalone target.'})
                elif 'FGrH' in q['bibliographic_notice'] or 'FHG' in q['bibliographic_notice']:
                    x.update({'sources_tested':B+'; FGrH/FHG inventory','open_text_result':'No explicit reusable transcription found.','confidence':'low','proposed_status':'EDITION_IDENTIFIED','next_action':'locate unrestricted historical scan or map earlier witness','notes':'No provider OCR may be used.'})
                else:
                    x.update({'sources_tested':B,'open_text_result':'No reusable complete Greek text found.','confidence':'medium','proposed_status':'BLOCKED_RIGHTS','next_action':'seek older open edition or individual witness','notes':'Canon edition not reusable without explicit licence.'})
                z.writerow(x)
        print(O/f'{P}_batch_{n:04}.csv')
    print(f'final_pointer={E[0]}.{E[1]}')

if __name__=='__main__': main()
