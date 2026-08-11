import csv

O="data/research_batches/detailed_verified_3001_batch_386.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D=[
("3293","001","Epistulae","Legrand 1892 pp. 1–192","18740","The Philelphus Greek letter collection is the exact item."),
("3293","002","Poema ad Georgium Gemistum","Legrand 1892 p. 49","49","The single-page poem to George Gemistus remains distinct from the broader poem collection."),
("3293","003","Poemata","Legrand 1892 pp. 195–221","4735","The poem collection remains separate from the individually catalogued Gemistus poem."),
("3293","004","De psychagogia","Maltese 1997 pp. 29–143","13651","The De psychagogia poem and exact edition locus define this item."),
("3294","001","Historiae dogmaticae liber I","Cozza-Luzi 1871 pp. 1–178","41818","Dogmatic History book I shares a duplicated canonical key with unrelated Fragmenta; both records are retained explicitly."),
]
C=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for aid,wid,title,locus,wc,note in D:
  s=next(r for r in C if r['tlg_author_id']==aid and r['tlg_work_id']==wid and r['work_title']==title);r={f:'' for f in F};r.update(tlg_author_id=aid,tlg_work_id=wid,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {title} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {title} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
