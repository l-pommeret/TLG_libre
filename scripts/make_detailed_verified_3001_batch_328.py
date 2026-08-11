import csv

O="data/research_batches/detailed_verified_3001_batch_328.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3128","002"):("Theognosti canones","Schneider 1887 pp. 4–20","word count not supplied","This Schneider additamentum remains distinct from the Cramer Canones catalogued as 3128.001."),
("3129","001"):("Πρὸς τοὺς αὐτοῦ μαθητὰς ἀτακτήσαντας i","Gautier 1980 pp. 131–143","1708","The first discourse to the disorderly pupils is distinct from the second."),
("3129","002"):("Πρὸς τοὺς αὐτοῦ μαθητὰς ἀτακτήσαντας ii","Gautier 1980 pp. 147–165","2492","The second discourse to the disorderly pupils is distinct from the first."),
("3129","003"):("Πρὸς τὸν μέγαν οἰκονόμον τοῦ πατριάρχου ἀδελφόν","Gautier 1980 pp. 169–175","932","The addressee and exact six-page locus define this short epistle."),
("3129","004"):("Λόγος εἰς τὸν πορφυρογέννητον κῦρ Κωνσταντῖνον","Gautier 1980 pp. 179–211","4486","The oration to Constantine Porphyrogenitus was checked separately from the following Alexius oration."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
