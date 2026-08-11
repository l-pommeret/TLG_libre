import csv

O="data/research_batches/detailed_verified_3001_batch_376.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3254","009"):("Homiliae xliii–lxiii","Chrestou 1986 vol. 11 pp. 22–608","60353","The explicit homily-number span xliii through lxiii remains separate from earlier homily volumes."),
("3254","010"):("Orationes antirrheticae contra Acindynum","Kontogiannes and Phanourgakes 1970 pp. 39–506","117776","The anti-Akindynos refutational orations are the exact large theological item."),
("3254","011"):("Orationes dogmaticae","Mantzarides 1966 pp. 69–277","51649","The dogmatic discourse collection is preserved separately from apologetic and ascetic collections."),
("3254","012"):("Epistulae","Matsoukas 1966 pp. 315–547","60652","The Palamas letter collection and exact edition locus define this item."),
("3254","013"):("Orationes apologeticae","Pseftonkas 1966 pp. 567–670","24427","Five explicit components and their loci—568–578, 579–586, 587–623, 625–647 and 649–670—are preserved without filling gaps."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
