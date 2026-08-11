import csv
O="data/research_batches/detailed_verified_3001_batch_464.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","044"):("Philippians catena fragments","Staab 1933, pp. 313–314","393","The item remains separate despite sharing page 314 with Colossians."),
("4139","045"):("Colossians catena fragments","Staab 1933, pp. 314–328","3635","The item remains separate despite sharing boundary pages with Philippians and 1 Thessalonians."),
("4139","046"):("1 Thessalonians catena fragments","Staab 1933, pp. 328–331","730","The item preserves the gap before 2 Thessalonians beginning on page 332."),
("4139","047"):("2 Thessalonians catena fragments","Staab 1933, pp. 332–336","1129","The item remains separate despite sharing page 336 with 1 Timothy."),
("4139","048"):("1 Timothy catena fragments","Staab 1933, pp. 336–341","1655","The item preserves the gap before 2 Timothy beginning on page 342."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of the {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact catena item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
