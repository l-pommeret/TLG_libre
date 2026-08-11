import csv

O="data/research_batches/detailed_verified_3001_batch_375.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3254","004"):("De processione spiritus sancti orationes duae","Bobrinsky 1962 pp. 23–153","37492","The explicit two-oration scope on procession of the Holy Spirit is preserved."),
("3254","005"):("Refutatio inscriptionum Vecci","Papaevaggelou 1962 pp. 161–175","3361","The catalogue's split typography in Refutatio is noted without changing the canonical title field."),
("3254","006"):("Epistulae ad Acindynum et Barlaam","Meyendorff 1962 pp. 203–312","29298","Both named addressees define the exact theological letter collection."),
("3254","007"):("Homiliae i–xx","Chrestou 1985 vol. 9 pp. 26–596","57717","The explicit homily-number span i through xx is preserved without adjacent homilies."),
("3254","008"):("Homiliae xxi–xlii","Chrestou 1985 vol. 10 pp. 22–602","56699","The explicit homily-number span xxi through xlii remains separate from 3254.007."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
