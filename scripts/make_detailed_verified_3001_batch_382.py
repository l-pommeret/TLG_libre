import csv

O="data/research_batches/detailed_verified_3001_batch_382.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3272","003"):("Epistulae","MPG 150 cols. 288–350","10174","The Theophanes III letter collection and exact MPG locus define this item."),
("3272","004"):("Oratio eucharistica ad Jesum Christum","MPG 150 cols. 352–356","553","The thanksgiving for deliverance from plague and death defines this short oration."),
("3272","005"):("Ἀπόδειξις καὶ ἀνατροπή","Polemis, Philosophi Byzantini 10 (2000), pp. 1–49","10228","The proof and its refutation are preserved as the exact combined philosophical-theological item."),
("3273","001"):("Epistulae i–ii ad Eutychium","Schwartz and Straub 1971 pp. 236–238 and 245–247","2101","The explicit two-letter scope and discontinuous loci are preserved; Eutychius 2822.001 remains a cross-reference."),
("3274","001"):("Deputatorium Latinorum cedula de igne purgatorio","Petit, PO 15.1 (1920), pp. 25–38","2750","Cross-references to Bessarion 3229 and Marcus Eugenicus are preserved; the latter reference is split into malformed continuation 3274.012."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
