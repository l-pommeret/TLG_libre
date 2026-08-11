import csv

O="data/research_batches/detailed_verified_3001_batch_406.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3373","002"):("Oratio ad Isaacium Angelum","Regel and Novosadskij 1917 pp. 254–280","6544","The Isaac Angelus oration is exact; trailing Tractatus Coislinianus/Comoedia text is catalogue heading material."),
("3375","001"):("Oratio ad impios Chionas","Phanourgakes 1988 pp. 148–165","4038","The Chionas addressees define the exact theological oration."),
("3376","001"):("Dialogus Palamae et Gregorae","Phanourgakes 1988 pp. 191–230","9027","The two named interlocutors define the exact dialogue; Phaedimus heading and Palamas 3254.018 cross-reference remain contextual."),
("3377","001"):("Euchologium","Johnson 1995 pp. 46–80","4337","The Euchologia 5332 cross-reference remains separate; appended Contra Manichaeos bibliographic text belongs to a following catalogue item and is not merged."),
("3378","001"):("Contra Manichaeos","Poirier et al., CCSG 82 (2013), pp. 7–293, 393 and 400–404","29796","All three explicit discontinuous loci are preserved without filling gaps."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
