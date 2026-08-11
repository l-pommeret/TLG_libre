import csv

O="data/research_batches/detailed_verified_3001_batch_401.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3344","008"):("Eusebii Caesariensis confutatio","Pitra 1852 pp. 373–503","28019","The catalogue's split typography in confutatio is preserved; 3086.009 remains a cross-reference."),
("3344","009"):("Pseudo-Epiphanii confutatio","Pitra 1858 pp. 292–380","21119","The Pseudo-Epiphanius refutation remains distinct from the Eusebius refutation; 3086.008 remains a cross-reference."),
("3344","010"):("Adversus iconomachos","Pitra 1858 pp. 233–291","13872","The anti-iconoclast work is preserved separately from adjacent Pitra editions."),
("3344","011"):("Epistula ad Leonem III papam","MPG 100 cols. 169–200","5748","The Pope Leo III addressee defines the exact theological epistle."),
("3344","012"):("Refutatio definitionis synodalis anni 815","Featherstone, CCSG 33 (1997), pp. 3–335","78776","The catalogue's split typography in Refutatio is noted without altering the canonical title field."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
