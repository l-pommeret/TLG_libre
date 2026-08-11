#!/usr/bin/env python3
"""100 work-level records from TLG 0669.x01 through 2074.028."""
from __future__ import annotations
import csv
from pathlib import Path
A=("0669","x01");N=100;D="2026-08-11";O=Path("data/research_batches")
H=["tlg_author_id","tlg_work_id","author_heading","work_title","canonical_edition","sources_tested","open_text_result","open_text_url","open_text_license","scan_result","scan_url","scan_rights","confidence","proposed_status","next_action","notes","last_checked"]
B="base-3 (Perseus, First1KGreek, PTA); exact identifier/title check"
def cross(t):return {"sources_tested":"Canon cross-reference; host-work record checked","open_text_result":"No independent acquisition: Canon directs this material to a host work.","confidence":"high","proposed_status":"CROSS_REFERENCE","next_action":f"follow {t}; do not duplicate","notes":"This is not a standalone acquisition target."}
X={("1126","003"):{"sources_tested":B+"; local First1KGreek TEI","open_text_result":"Open First1KGreek TEI found for Anubion fragmenta (cod. Paris. 2417).","open_text_url":"https://scaife.perseus.org/reader/urn:cts:greekLit:tlg1126.tlg003.1st1K-grc1","open_text_license":"CC BY-SA 4.0 (licence declared in the local First1KGreek TEI).","confidence":"high","proposed_status":"TEXT_OPEN_UNVERIFIED","next_action":"compare Canon boundaries and source edition","notes":"Open TEI present locally; no provider OCR used."}}
for k,t in {("0669","x01"):"0057.076",("0669","x02"):"0718.008",("0749","x01"):"0722.001",("0749","x02"):"0715.001",("0749","x03"):"0718.003",("0749","x04"):"0718.007",("0749","x05"):"0718.009",("0852","x01"):"0722.001",("0853","x01"):"0718.003",("1046","x01"):"2042.022",("0858","x01"):"0057.078",("0783","x01"):"0057.076–078",("0866","x01"):"0057.076",("0760","x01"):"0057.077",("4100","x01"):"0096.006",("4100","x02"):"1765.004",("0784","x01"):"0722.003",("0769","x01"):"0057.077",("1153","x01"):"0619.002"}.items():X[k]=cross(t)
for w in [f'{i:03}' for i in range(1,29)]:
 k=("2074",w);X[k]={"sources_tested":B+"; Internet Archive metadata API","open_text_result":"No reusable complete Greek text found in base-3.","scan_result":"Exact historical image-package candidate: apollinarisvonl00apolgoog_jp2.zip (72 MB).","scan_url":"https://archive.org/details/apollinarisvonl00apolgoog","scan_rights":"Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.","confidence":"high","proposed_status":"SCAN_CANDIDATE","next_action":"inspect cited pages and image quality; then remote-stage only if approved","notes":"Exact Lietzmann 1904 source volume. IA source ZIP SHA-1: 542dd33254faeb3a52d73333097ca737f933e206. Do not retain or rely on IA OCR."}
def default(r):
 if "FGrH" in r["bibliographic_notice"] or "FHG" in r["bibliographic_notice"]:return {"sources_tested":B+"; FGrH/FHG inventory","open_text_result":"No explicit reusable transcription found for this fragment dossier.","confidence":"low","proposed_status":"EDITION_IDENTIFIED","next_action":"locate an unrestricted historical scan or map earlier witnesses","notes":"No provider OCR may be used."}
 return {"sources_tested":B,"open_text_result":"No reusable complete Greek text found.","confidence":"medium","proposed_status":"BLOCKED_RIGHTS","next_action":"seek an older open edition or an individual witness","notes":"The Canon edition is not treated as reusable without an explicit licence."}
def main():
 w=list(csv.DictReader(Path("data/canon_works.csv").open(encoding="utf-8",newline="")));s=next(i for i,r in enumerate(w) if (r["tlg_author_id"],r["tlg_work_id"])==A);r=w[s:s+N];assert len(r)==100 and (r[-1]["tlg_author_id"],r[-1]["tlg_work_id"])==("2074","028")
 for n,o in enumerate(range(0,N,25),1):
  p=O/f"tlg_3001_4500_b8_batch_{n:04}.csv"
  with p.open("w",encoding="utf-8",newline="") as f:
   z=csv.DictWriter(f,fieldnames=H);z.writeheader()
   for q in r[o:o+25]:
    x={a:"" for a in H};x.update({"tlg_author_id":q["tlg_author_id"],"tlg_work_id":q["tlg_work_id"],"author_heading":q["author_heading"],"work_title":q["work_title"],"canonical_edition":q["bibliographic_notice"],"last_checked":D});x.update(default(q));x.update(X.get((q["tlg_author_id"],q["tlg_work_id"]),{}));z.writerow(x)
  print(p)
 print(f"final_pointer={r[-1]['tlg_author_id']}.{r[-1]['tlg_work_id']}")
if __name__=="__main__":main()
