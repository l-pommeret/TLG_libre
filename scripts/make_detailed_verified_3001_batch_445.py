import csv
O="data/research_batches/detailed_verified_3001_batch_445.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4079","001"):("Epigrammata","Anthologia Graeca 1.33 and 16.247","49","Both epigram loci are preserved as one collection item."),
("4082","001"):("Hero et Leander","Farber 1961, pp. 6–26","2176","The epic is checked as the exact Farber item."),
("4084","001"):("Historia nova","Paschoud 1971–1989, all explicit loci in vols. 1–3.2","62320","Every volume, date and discontinuous locus is retained; the First1KGreek candidate is not exact Paschoud edition/license verification."),
("4086","001"):("Fragmentum alchemicum (sine titulo)","Berthelot–Ruelle 1888, vol. 2 p. 115","16","The untitled sixteen-word fragment and Venice Marcianus 299 fol.95v witness are preserved; the First1KGreek candidate remains unverified."),
("4086","002"):("Ἀγαθοδαίμων εἰς τὸν χρησμόν","Berthelot–Ruelle 1888, pp. 268–271","856","The full Greek title and Paris BnF gr.2327 fol.262r witness are preserved; the First1KGreek candidate remains unverified."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
