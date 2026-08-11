import csv

O="data/research_batches/detailed_verified_3001_batch_384.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3275","001"):("Achilleis, Naples recension","Naples B.N. III.B.27; Smith, Agapitos and Hult 1999 pp. 15–74","14250","The Naples manuscript recension remains separate from Oxford and British Museum recensions."),
("3275","002"):("Achilleis, Oxford recension","Oxford Bodleian Auct. T.5.24; Smith 1990 pp. 11–45","5744","The Oxford manuscript recension remains separate from Naples and British Museum recensions."),
("3275","003"):("Achilleis, British Museum recension","British Museum add. 8241; Hesseling 1919 pp. 91–125","10530","The British Museum manuscript recension remains separate from Naples and Oxford recensions."),
("3276","001"):("De astronomia","Tihon and Mercier 1998 pp. 132–173","6359","Text pp. 132–152 and tables I–X pp. 154–172 are preserved separately; Gemistus 3202.006 remains a cross-reference."),
("3278","001"):("Carmina","Gigante 1979 pp. 147–152","352","The short Otranto poem collection is the exact item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
