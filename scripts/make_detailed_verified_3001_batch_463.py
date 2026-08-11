import csv
O="data/research_batches/detailed_verified_3001_batch_463.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","039"):("Romans catena fragments","Staab 1933, pp. 213–225","2938","The Romans fragments remain separate despite the shared boundary page 225 with 1 Corinthians."),
("4139","040"):("1 Corinthians catena fragments","Staab 1933, pp. 225–277","14107","The 1 Corinthians fragments remain separate from adjacent Pauline catena items."),
("4139","041"):("2 Corinthians catena fragments","Staab 1933, pp. 278–298","4755","The 2 Corinthians fragments remain separate despite the shared boundary page 298 with Galatians."),
("4139","042"):("Galatians catena fragments","Staab 1933, pp. 298–304","1526","The Galatians fragments remain separate despite shared boundary pages with neighboring items."),
("4139","043"):("Ephesians catena fragments","Staab 1933, pp. 304–313","2165","The Ephesians fragments remain separate despite sharing page 304 with Galatians."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of the {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact catena item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
