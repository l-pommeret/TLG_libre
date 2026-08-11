import csv
O="data/research_batches/detailed_verified_3001_batch_436.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","024"):("2 Timothy catena fragment","Staab 1933, p. 637","19","The nineteen-word fragment remains separate from the other items sharing page 637."),
("4040","025"):("Philemon catena fragment","Staab 1933, p. 637","13","The thirteen-word fragment remains separate from 2 Timothy and Hebrews on the same page."),
("4040","026"):("Hebrews catena fragments","Staab 1933, pp. 637–652","4539","The Hebrews excerpts remain separate despite beginning on the shared page 637."),
("4040","027"):("Commentarii in Joannem (in catenis)","Reuss, TU 89 (1966), pp. 359–412","15065","The Johannine catena commentary is checked independently from the Matthaean item."),
("4040","028"):("Commentarii in Matthaeum (in catenis)","Reuss, TU 61 (1957), pp. 270–337","17348","The Matthaean catena commentary is checked independently from the Johannine item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena-corpus, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of the {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact catena item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
