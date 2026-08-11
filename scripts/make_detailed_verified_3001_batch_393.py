import csv

O="data/research_batches/detailed_verified_3001_batch_393.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3317","002"):("Epistulae","Lampros 1930 pp. 198–199 and 201–202","429","The two letters to Borso, lord of Ferrara, and their discontinuous loci are preserved."),
("3320","001"):("Epistula ad Borsonum Ferrarae","Lampros 1930 p. 265","186","The single-page letter to Marquis Borso of Ferrara is distinct from Demetrius' two letters."),
("3321","001"):("Epistula ad Gemistum","Lampros 1926 p. 330","195","The single-page letter to philosopher Gemistus remains separate from the following grant."),
("3321","002"):("Chrysobullum ad Gemistum","Lampros 1926 pp. 331–333","873","The grant of a lantern and fountain to Gemistus remains distinct from his letter and Florentine chrysobulls."),
("3321","003"):("Chrysobulla pro Florentinis","Lampros 1926 pp. 334–344","3194","The Florentine chrysobulls remain separate from the individual Gemistus grant."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
