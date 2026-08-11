import csv
O="data/research_batches/detailed_verified_3001_batch_465.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","049"):("2 Timothy catena fragments","Staab 1933, pp. 342–344","571","The item remains separate despite sharing page 344 with Titus."),
("4139","050"):("Titus catena fragments","Staab 1933, pp. 344–345","158","The item remains separate despite shared pages with 2 Timothy, Philemon and Hebrews."),
("4139","051"):("Philemon catena fragment","Staab 1933, p. 345","31","The single thirty-one-word fragment remains separate from Titus and Hebrews sharing page 345."),
("4139","052"):("Hebrews catena fragments","Staab 1933, pp. 345–351","1602","The Hebrews item remains separate despite sharing page 345 with Titus and Philemon."),
("4139","053"):("In centurionem et contra Manichaeos et Apollinaristas","Aubineau 1983, pp. 108–140","5480","The Christological treatise and its later use by Severus of Antioch and Lateran 649 are preserved. Trailing SEVERUS Iatrosophista is recorded as a heading artefact; the PTA candidate remains unverified."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
