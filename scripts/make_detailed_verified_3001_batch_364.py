import csv

O="data/research_batches/detailed_verified_3001_batch_364.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3214","003"):("Carmina","Gregoropoulos 1996 vol. 2 pp. 371–430","4411","The attributed hymn collection remains separate from the doubtful poems 3214.004."),
("3214","004"):("Carmina dubia","Gregoropoulos 1996 vol. 2 pp. 431–438","545","The catalogue's doubtful status is preserved; these poems are not merged with 3214.003."),
("3214","005"):("Orationes anti-Arsenitae","Sinkewicz, Mediaeval Studies 50 (1988), pp. 52–95","7746","The anti-Arsenite discourse collection is the exact theological item."),
("3215","001"):("Epistulae","Dennis 1982 pp. 5–19","4410","The Theodore Potamius letter collection and exact edition locus define this item."),
("3215","002"):("Monodia in Joannem Palaeologum","Lampros 1885 pp. 49–56","2271","The named subject John Palaeologus defines this exact monody."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
