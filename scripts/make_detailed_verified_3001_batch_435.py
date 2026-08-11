import csv
O="data/research_batches/detailed_verified_3001_batch_435.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","019"):("Philippians catena fragments","Staab 1933, pp. 621–630","2883","The Philippians excerpts remain separate despite the shared boundary with Ephesians."),
("4040","020"):("Colossians catena fragments","Staab 1933, pp. 631–633","562","The Colossians excerpts are checked only at their explicit short locus."),
("4040","021"):("1 Thessalonians catena fragments","Staab 1933, pp. 633–636","873","The 1 Thessalonians excerpts remain separate despite the shared page boundary with Colossians."),
("4040","022"):("2 Thessalonians catena fragments","Staab 1933, p. 636","128","The single-page 2 Thessalonians excerpts remain a separate exact item."),
("4040","023"):("1 Timothy catena fragments","Staab 1933, pp. 636–637","141","The 1 Timothy excerpts remain separate despite sharing page 636 with 2 Thessalonians."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena-corpus, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of the {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact catena item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
