import csv
O="data/research_batches/detailed_verified_3001_batch_510.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4351","002"):("Palchi capitula selecta","Cumont–Olivieri, CCAG 1 (1898), pp. 94–97, 102–108, 113–117","2,541","The three discontinuous page spans, both manuscript witnesses at fol.210v, excerpt status, and tentative Eleutherius compilation are preserved."),
("4351","003"):("Dodecaeteris chaldaica","Cumont, CCAG 5.1 (1904), pp. 172–193","5,931","Angelicus 29 fol.92v, the explicit doubtful marker, and tentative Eleutherius compilation are preserved."),
("4351","004"):("Fragmenta astrologica","Heeg, CCAG 5.3 (1910), pp. 125–127","741","Vaticanus gr.216 fol.163, fragment status, and tentative Eleutherius compilation are preserved."),
("4351","005"):("Exempla geniturarum ex Palcho","Kroll, CCAG 6 (1903), pp. 63–67","1,001","Vindobonensis phil. gr.108 fol.299 and tentative Eleutherius compilation are preserved."),
("4351","006"):("De interrogationibus","Weinstock, CCAG 9.1 (1951), pp. 162–172","2,350","Cromwellianus 12 p.427, excerpt status, and tentative Eleutherius compilation are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, astrological manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
