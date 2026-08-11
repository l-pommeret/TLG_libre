import csv
O="data/research_batches/detailed_verified_3001_batch_514.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4354","010"):("Canones Junii","Analecta hymnica graeca, vol. 10 (1972), pp. 1–309","28,126","high","June scope, editors Schirò–Acconcia Longo, volume 10, and complete page bounds are preserved."),
("4354","011"):("Canones Julii","Analecta hymnica graeca, vol. 11 (1978), pp. 2–516","44,725","high","July scope, editors Schirò–Acconcia Longo, volume 11, and the page start at 2 are preserved."),
("4354","012"):("Canones Augusti","Analecta hymnica graeca, vol. 12 (1980), pp. 1–403","37,596","high","August scope, editors Schirò–Proiou, volume 12, and complete page bounds are preserved."),
("4358","001"):("Καταρχαί","Olivieri, CCAG 1 (1898), pp. 128–129","word count not supplied","medium","Laurentianus plut.28.34 fol.22v is preserved; no word count is invented."),
("4359","001"):("Περὶ κατακλίσεως","Olivieri, CCAG 1 (1898), pp. 118–122","word count not supplied","medium","Pancharius epitome status and Laurentianus plut.28.34 fol.16 are preserved; no word count is invented."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,conf,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, relevant liturgical and astrological corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc} item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence=conf,proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
