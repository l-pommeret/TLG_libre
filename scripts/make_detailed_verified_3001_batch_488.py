import csv
O="data/research_batches/detailed_verified_3001_batch_488.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4270","001"):("Testimonium","Döring 1972, pp. 52 and 61, testimonium 164a","The explicit equivalence to Stilpo 4262.001 is preserved."),
("4271","001"):("Testimonia","Döring 1972, pp. 52 and 61, testimonia 164a–b","The explicit equivalence of both testimonia to Stilpo 4262.001 is preserved."),
("4272","001"):("Testimonium","Döring 1972, pp. 52 and 61, testimonium 164a","The explicit equivalence to Stilpo 4262.001 is preserved."),
("4274","001"):("Testimonium","Döring 1972, pp. 52 and 61, testimonium 165","The explicit equivalence to Stilpo 4262.001 is preserved."),
("4275","001"):("Testimonium","Döring 1972, pp. 52 and 61, testimonium 164a","The explicit equivalence to Stilpo 4262.001 is preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, Megaric testimonia corpus, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact testimony before transcription or OCR.',notes=note+' The NQ notice supplies no word count. No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
