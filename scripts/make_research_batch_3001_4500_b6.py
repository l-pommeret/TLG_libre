#!/usr/bin/env python3
"""Research records for the 100 Canon notices following TLG 1779.001."""
from __future__ import annotations
import csv
from pathlib import Path

AFTER=("1779","001"); LIMIT=100; DATE="2026-08-11"; OUT=Path("data/research_batches")
HEADER=["tlg_author_id","tlg_work_id","author_heading","work_title","canonical_edition","sources_tested","open_text_result","open_text_url","open_text_license","scan_result","scan_url","scan_rights","confidence","proposed_status","next_action","notes","last_checked"]
BASE="base-3 (Perseus, First1KGreek, PTA); exact identifier/title check"; F1K="CC BY-SA 4.0 (licence declared in the local First1KGreek TEI)."; PER="CC BY-SA 4.0 (Perseus repository licence; TEI licence recorded locally)."
def tei(urn,text,note,per=False): return {"sources_tested":BASE+("; local Perseus TEI" if per else "; local First1KGreek TEI"),"open_text_result":text,"open_text_url":f"https://scaife.perseus.org/reader/urn:cts:greekLit:{urn}","open_text_license":PER if per else F1K,"confidence":"high","proposed_status":"TEXT_OPEN_UNVERIFIED","next_action":"compare Canon boundaries and source edition","notes":note+" No provider OCR used."}
def lead(i,f,size,sha,note,exact=True): return {"sources_tested":BASE+"; Internet Archive metadata API","open_text_result":"No reusable complete Greek text found in base-3.","scan_result":("Exact historical image-package candidate" if exact else "Historical series-volume image candidate (edition/part must be checked)")+f": {f} ({size}).","scan_url":f"https://archive.org/details/{i}","scan_rights":"Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.","confidence":"high" if exact else "medium","proposed_status":"SCAN_CANDIDATE","next_action":"inspect cited pages and image quality; then remote-stage only if approved","notes":note+f" IA source ZIP SHA-1: {sha}. Do not retain or rely on IA OCR."}

O={
 ("1134","001"):tei("tlg1134.tlg001.1st1K-grc1","Open First1KGreek TEI found for the anonymous Iamblichus fragments.","Compare it with the Canon's Diels–Kranz selection."),
 ("0643","001"):tei("tlg0643.tlg001.1st1K-grc1","Open First1KGreek TEI found for Anonymus Londinensis Iatrica.","The text edition and sigla are separately represented in the local corpus."),
 ("0643","002"):tei("tlg0643.tlg002.1st1K-grc1","Open First1KGreek TEI found for the Anonymus Londinensis fragments.","Compare the short Canon selection."),
 ("0618","001"):tei("tlg0618.tlg001.1st1K-grc1","Open First1KGreek TEI found for Antigoni epistula.","Compare with Hercher's cited edition."),
 ("0044","001"):tei("tlg0044.tlg001.1st1K-grc1","Open First1KGreek TEI found for Antiochi regis epistulae.","Compare with Hercher's cited edition."),
 ("7000","001"):tei("tlg7000.tlg001.perseus-grc6:1.1","Open Perseus TEI volumes cover the Greek Anthology.","The Canon's Beckby edition differs; compare all sixteen books.",True),
 ("0215","002"):tei("tlg7000.tlg001.perseus-grc7:7.103/","The cited Anthologia Graeca loci 7.103 and 9.147 are in open Paton TEI volumes.","Content-level locus match, not an author-URN match.",True),
 ("0239","003"):tei("tlg7000.tlg001.perseus-grc8:9.321/","The cited Anthologia Graeca locus 9.321 is in open Paton TEI.","Content-level locus match, not an author-URN match.",True),
 ("0112","001"):tei("tlg7000.tlg001.perseus-grc9:11.412/","The cited Anthologia Graeca loci 11.412 and 11.422 are in open Paton TEI.","Content-level locus match, not an author-URN match.",True),
}
# Explicit aliases never become standalone acquisition targets.
for key,target in {("1779","x01"):"1629.002",("0799","x01"):"0057.076",("1119","x01"):"0057.076–077",("0800","x01"):"0057.076",("0705","x01"):"0718.011",("1086","x01"):"0057.076–077",("0215","x01"):"7052.003",("0775","x01"):"0057.076",("0759","x01"):"0718.012",("0139","x01"):"0199.009",("0776","x01"):"0057.076",("0568","x01"):"0582.001",("0778","x01"):"0715.001",("0778","x02"):"0718.003",("0777","x01"):"0057.078"}.items():
 O[key]={"sources_tested":"Canon cross-reference; host-work record checked","open_text_result":"No independent acquisition: Canon directs this material to a host work.","confidence":"high","proposed_status":"CROSS_REFERENCE","next_action":f"follow {target}; do not duplicate","notes":"This is not a standalone acquisition target."}
# Reusable DFHG EpiDoc transcriptions with licence CC BY-SA 4.0 confirmed in the volume README.
for key,file,pages in [(("2322","003"),"ANTENOR.xml","FHG 4, p.305"),(("2547","003"),"ANTIGONUS.xml","FHG 4, pp.305–306")]:
 O[key]={"sources_tested":BASE+"; DFHG volume_4 EpiDoc page-break check","open_text_result":f"DFHG reusable EpiDoc transcription covers {pages} ({file}).","open_text_url":f"https://github.com/DFHG-project/volume_4/blob/master/data/epidoc_xml/{file}","open_text_license":"CC BY-SA 4.0 (DFHG volume README).","confidence":"high","proposed_status":"TEXT_OPEN_UNVERIFIED","next_action":"compare FHG page range and fragment boundaries","notes":"DFHG is a new digital representation of FHG, not provider OCR."}
O[("0643","001")].update({"scan_result":"Exact historical image-package candidate: p1anonymilondine03diel_jp2.zip (57 MB).","scan_url":"https://archive.org/details/p1anonymilondine03diel","scan_rights":"Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.","notes":O[("0643","001")]["notes"]+" IA source ZIP SHA-1: 7be51a255220797c804453b6daac9fc3c4201f84; do not use IA OCR."})
for key in [("1144","004")]: O[key]=lead("CatalogusCodicumAstrologorumGraec8p3","Catalogus_codicum_astrologorum_graec_8p3_jp2.zip","51 MB","8f1514a2a5c21cf5c1d55e6ff4308a2f3ea49862","Exact CCAG 8.3 source-image lead already logged in b2; do not duplicate staging. ")
for key in [("3007",w) for w in ("001","002","003")]: O[key]=lead("patrologicursus105migngoog","patrologicursus105migngoog_jp2.zip","527 MB","6b3879991d64975f83090d69746512c9e9c3a972","MPG 89 source-image lead already logged in b2; do not duplicate staging. ")
def default(r):
 if "FGrH" in r["bibliographic_notice"]: return {"sources_tested":BASE+"; FGrH inventory","open_text_result":"No explicit reusable transcription found for this FGrH dossier.","confidence":"low","proposed_status":"EDITION_IDENTIFIED","next_action":"locate an unrestricted FGrH scan or map earlier witnesses","notes":"Do not infer content from a non-concordant FHG overlap."}
 if "FHG" in r["bibliographic_notice"]: return {"sources_tested":BASE+"; DFHG/FHG inventory","open_text_result":"No author-specific reusable transcription confirmed for this FHG dossier.","confidence":"medium","proposed_status":"EDITION_IDENTIFIED","next_action":"locate an unrestricted complete FHG volume and inspect cited pages","notes":"No provider OCR may be used."}
 return {"sources_tested":BASE,"open_text_result":"No reusable complete Greek text found.","confidence":"medium","proposed_status":"BLOCKED_RIGHTS","next_action":"seek an older open edition or an individual witness","notes":"The Canon edition is not treated as reusable without an explicit licence."}
def main():
 w=list(csv.DictReader(Path("data/canon_works.csv").open(encoding="utf-8",newline=""))); s=next(i for i,r in enumerate(w) if (r["tlg_author_id"],r["tlg_work_id"])==AFTER)+1; rows=w[s:s+LIMIT]
 assert len(rows)==100 and (rows[0]["tlg_author_id"],rows[0]["tlg_work_id"])==("1779","002") and (rows[-1]["tlg_author_id"],rows[-1]["tlg_work_id"])==("3007","003")
 for n,off in enumerate(range(0,LIMIT,25),1):
  p=OUT/f"tlg_3001_4500_b6_batch_{n:04}.csv"
  with p.open("w",encoding="utf-8",newline="") as f:
   out=csv.DictWriter(f,fieldnames=HEADER);out.writeheader()
   for r in rows[off:off+25]:
    x={k:"" for k in HEADER};x.update({"tlg_author_id":r["tlg_author_id"],"tlg_work_id":r["tlg_work_id"],"author_heading":r["author_heading"],"work_title":r["work_title"],"canonical_edition":r["bibliographic_notice"],"last_checked":DATE});x.update(default(r));x.update(O.get((r["tlg_author_id"],r["tlg_work_id"]),{}));out.writerow(x)
  print(p)
 print(f"final_pointer={rows[-1]['tlg_author_id']}.{rows[-1]['tlg_work_id']}")
if __name__=="__main__":main()
