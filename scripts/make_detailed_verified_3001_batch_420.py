import csv
O="data/research_batches/detailed_verified_3001_batch_420.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4019","005"):("In Platonis Gorgiam commentaria","Westerink 1970, pp. 1–268","62307","The Gorgias commentary is checked independently from the other Platonic commentaries."),
("4019","006"):("In Platonis Phaedonem commentaria","Westerink, Greek commentaries on Plato's Phaedo 1 (1976), pp. 39–181","18929","The bracketed Olympiodorus attribution in the edition statement is preserved without reinterpretation."),
("4019","008"):("Scholia in Aristotelis librum de interpretatione (e cod. Vat. Urbin. gr. 35)","Tarán 1978, pp. xxvi–xli","2492","The Vaticanus Urbinas graecus 35 scholia are kept distinct from the anonymous commentary named in the edition title."),
("4023","001"):("Epigramma AG 9.762","Anthologia Graeca 9.762","26","The single AG epigram locus is the complete canon item; no broader author range is inferred."),
("4024","001"):("Historiae","Keydell, CFHB 2 (1967), pp. 3–197","59466","A First1KGreek candidate exists, but exact Keydell edition and license verification is not established locally."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
