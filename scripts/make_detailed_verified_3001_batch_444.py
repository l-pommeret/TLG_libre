import csv
O="data/research_batches/detailed_verified_3001_batch_444.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D=[
("4048","001","Epigramma, AG: 16.379. Q: 25: Epigr.","Epigramma AG 16.379","Anthologia Graeca 16.379","25","The single epigram locus is the complete item."),
("4049","001","Epigramma, AG: 16.315. Q: 23: Epigr.","Epigramma AG 16.315","Anthologia Graeca 16.315","23","The single epigram locus is the complete item."),
("4077","001","Epigrammata, AG: 9.360, 712. Q: 93: Epigr.","Epigrammata AG 9.360 and 9.712","Anthologia Graeca 9.360 and 9.712","93","Both epigram loci are preserved as one exact collection item."),
("4078","001","Epigramma, AG: 16.316. Q: 39: Epigr. 1509 <MILON> <Phil.> Incertum: Crotoniensis","Epigramma AG 16.316","Anthologia Graeca 16.316","39","This first duplicate-key notice retains the trailing Milon uncertain-attribution heading artefact and remains separate from the philosophical fragment."),
("4078","001","Fragmentum, ed. H. Thesleff, The Pythagorean texts of the Hellenistic period, Åbo: Åbo Akademi, 1965: 122–123. Q: 62: Phil.","Fragmentum","Thesleff 1965, pp. 122–123","62","This second duplicate-key notice is the philosophical fragment and remains separate from the epigram."),
]
C=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for a,b,title,label,locus,wc,note in D:
  s=next(r for r in C if r['tlg_author_id']==a and r['tlg_work_id']==b and r['bibliographic_notice']==title)
  r={f:'' for f in F};r.update(tlg_author_id=a,tlg_work_id=b,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, Anthologia Graeca, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' Duplicate canon key intentionally preserved. No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
