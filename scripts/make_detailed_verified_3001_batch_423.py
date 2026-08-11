import csv
O="data/research_batches/detailed_verified_3001_batch_423.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4029","002"):("Historia arcana (= Anecdota)","Wirth post Haury, Opera omnia 3 (1963), pp. 1 and 4–186","32253","Both canonical titles and the discontinuous preliminary page are preserved. A Perseus candidate is not exact Wirth edition/license verification."),
("4029","003"):("De aedificiis (lib. 1–6)","Wirth post Haury, Opera omnia 4 (1964), pp. 1 and 5–186","35694","Books 1–6 and both discontinuous loci are preserved."),
("4030","001"):("In Aristotelis libros de anima paraphrasis","Hayduck, CAG 23.1 (1883), pp. 1–152","69492","A First1KGreek candidate exists, but exact Hayduck edition and license verification is not established locally."),
("4034","001"):("In ethica Nicomachea ix–x commentaria","Heylbut, CAG 20 (1892), pp. 461–620","64421","Only books IX–X and Michael's explicit page span are checked within the composite CAG volume."),
("4034","002"):("In parva naturalia commentaria","Wendland, CAG 22.1 (1903), pp. 1–149","50831","A First1KGreek candidate exists, but exact Wendland edition and license verification is not established locally."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
