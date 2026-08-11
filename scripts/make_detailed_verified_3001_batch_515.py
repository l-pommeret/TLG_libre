import csv
O="data/research_batches/detailed_verified_3001_batch_515.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4360","002"):("Fragmentum apotelesmaticum","Cumont, CCAG 4 (1903), pp. 122–123","256","Fragment status and Mutinensis 215 fol.44v are preserved."),
("4360","007"):("De rebus praesertim bellicis","Zuretti, CCAG 11.1 (1932), pp. 204–266, 270–271","14,270","Both discontinuous page spans, Scorialensis I R 14 fol.183, and additional unspecified witnesses are preserved."),
("4360","008"):("Fragmentum apotelesmaticum (= Σχόλιον περὶ ζωῆς)","Olivieri, CCAG 2 (1900), p. 195","56","Fragment status, equivalent Greek title, and Venetian Marcianus 335 fol.127v are preserved."),
("4360","009"):("Περὶ προβολῆς ἄρχοντος","Cumont, CCAG 4 (1903), pp. 93–94","287","Taurinensis C VII 10 fol.71 is preserved."),
("4364","001"):("De ruta","Sangin, CCAG 12 (1936), pp. 119–121","718","Tentative attribution to Theophilus Corydaleus, excerpt status, Petropolitanus witness, magical genre, and trailing THEOPHILUS cross-reference token are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, astrological manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
