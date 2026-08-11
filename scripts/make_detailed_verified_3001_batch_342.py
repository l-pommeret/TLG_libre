import csv

O="data/research_batches/detailed_verified_3001_batch_342.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3157","002"):("Chronica","Tocci, CFHB 46 (2015), pp. 5–182","24746","The Scutariotes chronicle remains distinct from his additions to Acropolites in 3157.001."),
("3158","001"):("Epistulae (Darrouzès)","Darrouzès 1960 pp. 317–341","6359","This Darrouzès letter collection is retained separately from the Vienna-manuscript collection 3158.002."),
("3158","002"):("Epistulae e cod. Vindob. phil. gr. 342","Lampros 1925–1926: vol. 19 pp. 269–296; vol. 20 pp. 144–150 and 152–157","10100","All discontinuous journal loci are preserved; this manuscript dossier is not merged with 3158.001."),
("3161","001"):("Relatio motionis inter Maximum et principes (BHG 1231)","MPG 90 cols. 109–129","4101","The BHG 1231 identifier defines this exact biographical relation."),
("3161","002"):("Vita sancti Maximi confessoris (BHG 1233m)","Epifanovic 1907 pp. 1–10","3107","The BHG 1233m life is distinct from the epitome BHG 1236."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
