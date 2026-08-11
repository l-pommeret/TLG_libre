import csv
O="data/research_batches/detailed_verified_3001_batch_434.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","014"):("Romans catena fragments","Staab 1933, pp. 470–544","25253","The Romans excerpts are treated as one exact catena-fragment item."),
("4040","015"):("1 Corinthians catena fragments","Staab 1933, pp. 544–583","12636","The 1 Corinthians excerpts remain separate despite the shared page boundary with Romans."),
("4040","016"):("2 Corinthians catena fragments","Staab 1933, pp. 583–604","6907","The 2 Corinthians excerpts remain separate despite the shared page boundary with 1 Corinthians."),
("4040","017"):("Galatians catena fragments","Staab 1933, pp. 604–610","1791","The Galatians excerpts are checked only at their explicit locus."),
("4040","018"):("Ephesians catena fragments","Staab 1933, pp. 611–621","3422","The gap between pages 610 and 611 is preserved; no continuous collective range is substituted."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena-corpus, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of the {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact catena item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
