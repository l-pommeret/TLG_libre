import csv
O="data/research_batches/detailed_verified_3001_batch_472.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4146","024"):("Boethii de philosophiae consolatione in linguam Graecam translati","Megas 1996, pp. 65–355","32160","The Greek Consolation translation remains separate from Vita Boethii and the scholia in the same volume."),
("4146","025"):("Encomium ad sanctum Diomedem","Westerink, Analecta Bollandiana 84 (1966), pp. 180–227","12966","Both cross-references, to Nicetas David 2705.006 and Vitae sancti Diomedis 5136.001, are preserved."),
("4146","026"):("Translatio Augustini De Trinitate","Papathomopoulos–Tsavare–Rigotti 1995, vol. 1 pp. 2–463; vol. 2 odd pp. 465–995","146327","All fifteen books, both volume loci and the odd-page restriction for volume 2 are preserved."),
("4146","027"):("Ψηφοφορία κατ’ Ἰνδούς ἡ λεγομένη μεγάλη","Allard 1981, even pp. 25–199","17641","The even-page restriction and cross-reference to Nicolaus Rhabdas 4371.001 are preserved."),
("4146","028"):("Macrobii commentariorum in Somnium Scipionis in linguam graecam translati","Megas 1995, pp. 11–174","47255","Both Macrobius books and Greek translation status are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
