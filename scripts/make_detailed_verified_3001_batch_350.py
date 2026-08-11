import csv

O="data/research_batches/detailed_verified_3001_batch_350.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3191","004"):("Epitaphius in Theodoram Palaeologinam","Sideras 1990 pp. 249–267","5346","The addressee Theodora Palaeologina defines this exact epitaph."),
("3191","005"):("Monodia in abbatem Lucam","Ševčenko 1975 pp. 58–82","6588","The monody for Abbot Lucas remains distinct from the following Methodius epistle."),
("3191","006"):("Epistula ad Methodium Senacherim","Ševčenko 1975 pp. 86–88","862","The named monk Methodius Senacherim defines this short epistle."),
("3191","007"):("Carmina iii–iv","Ševčenko and Featherstone 1981 pp. 14–44","4624","The explicit poem numbers iii–iv are preserved; embedded Georgius Metochites text is a catalogue heading artefact."),
("3191","008"):("Πρεσβευτικός","Mavromatis 1978 pp. 89–119","11260","The Presbeutikos and its exact historical locus define the item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
