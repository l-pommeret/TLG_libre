import csv
O="data/research_batches/detailed_verified_3001_batch_414.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4015","007"):("In libros de generatione animalium commentaria","Hayduck, CAG 14.3 (1903), pp. 1–249","95158","The edition's parenthetical attribution to Michael of Ephesus is preserved; a First1KGreek candidate is not treated as exact licensed verification."),
("4015","008"):("In Aristotelis libros de anima commentaria","Hayduck, CAG 15 (1897), pp. 1–607","236925","A First1KGreek candidate exists, but exact Hayduck edition and license verification is not established locally."),
("4015","009"):("In Aristotelis physicorum libros commentaria","Vitelli, CAG 16–17 (1887–1888), pp. 1–495 and 496–908","302242","Both volumes and the canon's division of books 1–3 versus 4–8 are preserved; the First1KGreek candidate remains unverified at edition/license level."),
("4015","010"):("De aeternitate mundi","Rabe 1899, pp. 1–646","141961","The Contra Proclum work is checked as the exact Rabe item."),
("4015","011"):("De opificio mundi","Reichardt 1897, pp. 1–308","62818","The seven-book De opificio mundi is checked as the exact Reichardt item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
