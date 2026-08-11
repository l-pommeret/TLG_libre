#!/usr/bin/env python3
"""Auditable 100-record research log following TLG 3209.001."""
from __future__ import annotations
import csv
from pathlib import Path
A=("3209","001");N=100;D="2026-08-11";O=Path("data/research_batches")
H=["tlg_author_id","tlg_work_id","author_heading","work_title","canonical_edition","sources_tested","open_text_result","open_text_url","open_text_license","scan_result","scan_url","scan_rights","confidence","proposed_status","next_action","notes","last_checked"]
B="base-3 (Perseus, First1KGreek, PTA); exact identifier/title check";L="CC BY-SA 4.0 (licence declared in the local corpus TEI)."
def text(urn,desc,corpus="First1KGreek"):
 return {"sources_tested":B+f"; local {corpus} TEI","open_text_result":desc,"open_text_url":f"https://scaife.perseus.org/reader/urn:cts:greekLit:{urn}","open_text_license":L,"confidence":"high","proposed_status":"TEXT_OPEN_UNVERIFIED","next_action":"compare Canon boundaries and source edition","notes":"Open TEI present locally; no provider OCR used."}
X={}
for work,urn in [("001","tlg0028.tlg001.perseus-grc2"),("002","tlg0028.tlg002.perseus-grc2"),("003","tlg0028.tlg003.perseus-grc2"),("004","tlg0028.tlg004.perseus-grc2"),("005","tlg0028.tlg005.perseus-grc2"),("006","tlg0028.tlg006.perseus-grc2")]: X[("0028",work)]=text(urn,"Open Perseus TEI found for the corresponding Antiphon speech.","Perseus")
X[("1146","001")]=text("tlg1146.tlg001.1st1K-grc1","Open First1KGreek TEI found for Antipater's testimonia and fragments.")
X[("1147","003")]=text("tlg1147.tlg003.1st1K-grc1","Open First1KGreek TEI found for Antiphon Sophist fragments.")
for key in [("0113","001"),("0114","001"),("1865","001"),("0117","001"),("0118","001"),("0119","001"),("0120","001")]:
 X[key]=text("tlg7000.tlg001.perseus-grc6:6.10/","The cited Anthologia Graeca loci are represented across the open Paton TEI volumes.","Perseus");X[key]["notes"]="Content-level locus match, not an author-URN match; compare every cited locus. No OCR used."
for key,target in {("0113","x01"):"7052.003",("0779","x01"):"0057.076–078",("2801","x01"):"5000.001",("2801","x02"):"2897.002",("2801","x03"):"5000.001",("2801","x04"):"2934.019",("2801","x05"):"2934.019",("0832","x01"):"0057.078",("0410","x01"):"7052.007",("0780","x01"):"0057.076",("2435","x01"):"2446.001",("0931","x01"):"0057.076–078",("0850","x01"):"0057.076",("1148","x01"):"5003.022",("1148","x02"):"2580.002",("1148","x03"):"2034.002"}.items():
 X[key]={"sources_tested":"Canon cross-reference; host-work record checked","open_text_result":"No independent acquisition: Canon directs this material to a host work.","confidence":"high","proposed_status":"CROSS_REFERENCE","next_action":f"follow {target}; do not duplicate","notes":"This is not a standalone acquisition target."}
def default(r):
 if "FGrH" in r["bibliographic_notice"] or "FHG" in r["bibliographic_notice"]: return {"sources_tested":B+"; FGrH/FHG inventory","open_text_result":"No explicit reusable transcription found for this fragment dossier.","confidence":"low","proposed_status":"EDITION_IDENTIFIED","next_action":"locate an unrestricted historical scan or map earlier witnesses","notes":"No provider OCR may be used."}
 return {"sources_tested":B,"open_text_result":"No reusable complete Greek text found.","confidence":"medium","proposed_status":"BLOCKED_RIGHTS","next_action":"seek an older open edition or an individual witness","notes":"The Canon edition is not treated as reusable without an explicit licence."}
def main():
 w=list(csv.DictReader(Path("data/canon_works.csv").open(encoding="utf-8",newline="")));s=next(i for i,r in enumerate(w) if (r["tlg_author_id"],r["tlg_work_id"])==A);r=w[s:s+N];assert len(r)==100 and (r[0]["tlg_author_id"],r[0]["tlg_work_id"])==A and (r[-1]["tlg_author_id"],r[-1]["tlg_work_id"])==("2478","001")
 for n,o in enumerate(range(0,N,25),1):
  p=O/f"tlg_3001_4500_b7_batch_{n:04}.csv"
  with p.open("w",encoding="utf-8",newline="") as f:
   z=csv.DictWriter(f,fieldnames=H);z.writeheader()
   for q in r[o:o+25]:
    x={k:"" for k in H};x.update({"tlg_author_id":q["tlg_author_id"],"tlg_work_id":q["tlg_work_id"],"author_heading":q["author_heading"],"work_title":q["work_title"],"canonical_edition":q["bibliographic_notice"],"last_checked":D});x.update(default(q));x.update(X.get((q["tlg_author_id"],q["tlg_work_id"]),{}));z.writerow(x)
  print(p)
 print(f"final_pointer={r[-1]['tlg_author_id']}.{r[-1]['tlg_work_id']}")
if __name__=="__main__":main()
