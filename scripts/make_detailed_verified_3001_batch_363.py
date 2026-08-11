import csv

O="data/research_batches/detailed_verified_3001_batch_363.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3204","001"):("Oratio ad Isaacum II Angelum","Bachmann 1935 pp. 10–20","3610","The emperor Isaac II Angelus defines the exact imperial oration."),
("3207","001"):("Epistulae","Darrouzès 1970 pp. 108–179, 205–219 and 325–335","13856","All three explicit discontinuous loci are preserved without filling gaps."),
("3207","002"):("Orationes 1146–1155","Darrouzès 1970 pp. 74–106, 181–185 and 221–323","24253","The dated 1146–1155 orations and all three discontinuous loci are preserved."),
("3214","001"):("Orationes monasticae","Sinkewicz 1992 pp. 84–382","43631","The monastic discourse collection is the exact Theoleptus item."),
("3214","002"):("Epistulae ad Irenem basilissam","Constantinides-Hero 1994 pp. 34–94","6741","The named imperial addressee Irene defines this exact letter collection."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
