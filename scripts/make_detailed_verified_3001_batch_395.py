import csv

O="data/research_batches/detailed_verified_3001_batch_395.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3322","005"):("Sententia data Florentiae","Jugie 1937 pp. 176–178","766","The Florentine council profession of faith is a distinct short theological item."),
("3322","006"):("Epistula ad Demetrium de synodo Florentina [Sp.]","Jugie, Byzantion 22 (1939), pp. 81–93","3929","The spurious marker and possible authorship by George Korressios are preserved as uncertainty, not resolved."),
("3330","001"):("Encomium in Petrum episcopum Argi","Kyriakopoulos 1976 pp. 232–254","3999","Saint Peter, bishop of Argos, defines the exact encomium."),
("3330","002"):("Epistulae","Darrouzès 1960 pp. 262–316","13129","The Theodore of Nicaea letter collection is the exact item."),
("3333","001"):("De vita sua","Grégoire, Byzantion 29–30 (1959–60), pp. 447–474","5121","The autobiographical text of Michael VIII is the exact ecclesiastical-typikon item; the truncated author heading is retained from canon."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
