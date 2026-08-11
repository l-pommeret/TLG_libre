import csv

O="data/research_batches/detailed_verified_3001_batch_332.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3130","009"):("De vitae termino","Zanetto 1979 pp. 37–52","3361","This work remains distinct from the related Ὅροι ζωῆς catalogued as 3130.008."),
("3131","001"):("Disputatio cum Armeniorum Catholico","MPG 133 cols. 120–212","18954","The first Armenian disputation was checked separately from the second."),
("3131","002"):("Disputatio secunda cum Nersete","MPG 133 cols. 212–293","16986","The second disputation with Nerses was checked separately from the first."),
("3132","001"):("Timarion","Romano 1974 pp. 49–92","9800","The Pseudo-Lucianic dialogue and satire is the exact item."),
("3135","001"):("Epitome historiarum, books 1–12 (Dindorf)","Dindorf 1868–1870: vol. 1 pp. 1–402; vol. 2 pp. 1–457; vol. 3 pp. 1–169","230015","This Dindorf edition record remains separate from the Pinder duplicate-title edition 3135.004 and linked parts .002–.003."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
