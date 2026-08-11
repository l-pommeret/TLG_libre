#!/usr/bin/env python3
from __future__ import annotations
import csv
from pathlib import Path
A=("2074","030");N=100;D="2026-08-11";O=Path("data/research_batches")
H=["tlg_author_id","tlg_work_id","author_heading","work_title","canonical_edition","sources_tested","open_text_result","open_text_url","open_text_license","scan_result","scan_url","scan_rights","confidence","proposed_status","next_action","notes","last_checked"]
B="base-3 (Perseus, First1KGreek, PTA); exact identifier/title check";L="CC BY-SA 4.0 (licence declared in the local corpus TEI)."
def t(urn,c):return {"sources_tested":B+f"; local {c} TEI","open_text_result":"Open licensed TEI found for the exact TLG work.","open_text_url":f"https://scaife.perseus.org/reader/urn:cts:greekLit:{urn}","open_text_license":L,"confidence":"high","proposed_status":"TEXT_OPEN_UNVERIFIED","next_action":"compare Canon boundaries and source edition","notes":"Open TEI present locally; no provider OCR used."}
X={}
for w in ('001','002','003','004'):X[("0082",w)]=t(f"tlg0082.tlg{w}.1st1K-grc1","First1KGreek")
for w in ('001','002'):X[("0548",w)]=t(f"tlg0548.tlg{w}.perseus-grc2","Perseus")
X[("0550","001")]=t("tlg0550.tlg001.1st1K-grc1","First1KGreek")
for key in [("2074","x01"),("2074","x02"),("2074","x03"),("1221","x01"),("1221","x02"),("0785","x01"),("0549","x01"),("0786","x01"),("0786","x02"),("0680","x01"),("0739","x01"),("0741","x01"),("0782","x01"),("0792","x01"),("0747","x01"),("0789","x01"),("0791","x01"),("0817","x01"),("0619","x02"),("0619","x03"),("0810","x01")]:X[key]={"sources_tested":"Canon cross-reference; host-work record checked","open_text_result":"No independent acquisition: Canon directs this material to a host work.","confidence":"high","proposed_status":"CROSS_REFERENCE","next_action":"follow the cited host-work record; do not duplicate","notes":"This is not a standalone acquisition target."}
def d(r):
 if 'FGrH' in r['bibliographic_notice'] or 'FHG' in r['bibliographic_notice']:return {"sources_tested":B+"; FGrH/FHG inventory","open_text_result":"No explicit reusable transcription found for this fragment dossier.","confidence":"low","proposed_status":"EDITION_IDENTIFIED","next_action":"locate an unrestricted historical scan or map earlier witnesses","notes":"No provider OCR may be used."}
 return {"sources_tested":B,"open_text_result":"No reusable complete Greek text found.","confidence":"medium","proposed_status":"BLOCKED_RIGHTS","next_action":"seek an older open edition or an individual witness","notes":"The Canon edition is not treated as reusable without an explicit licence."}
def main():
 w=list(csv.DictReader(Path('data/canon_works.csv').open(encoding='utf-8',newline='')));s=next(i for i,r in enumerate(w) if (r['tlg_author_id'],r['tlg_work_id'])==A);r=w[s:s+N];assert len(r)==100 and (r[-1]['tlg_author_id'],r[-1]['tlg_work_id'])==('2491','001')
 for n,o in enumerate(range(0,N,25),1):
  p=O/f'tlg_3001_4500_b9_batch_{n:04}.csv'
  with p.open('w',encoding='utf-8',newline='') as f:
   z=csv.DictWriter(f,fieldnames=H);z.writeheader()
   for q in r[o:o+25]:
    x={k:'' for k in H};x.update({'tlg_author_id':q['tlg_author_id'],'tlg_work_id':q['tlg_work_id'],'author_heading':q['author_heading'],'work_title':q['work_title'],'canonical_edition':q['bibliographic_notice'],'last_checked':D});x.update(d(q));x.update(X.get((q['tlg_author_id'],q['tlg_work_id']),{}));z.writerow(x)
  print(p)
 print(f"final_pointer={r[-1]['tlg_author_id']}.{r[-1]['tlg_work_id']}")
if __name__=='__main__':main()
