import csv
O="data/research_batches/detailed_verified_3001_batch_513.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4354","005"):("Canones Januarii","Analecta hymnica graeca, vol. 5 (1971), pp. 1–522","49,628","January scope, editors Schirò–Proiou, volume 5, and complete page bounds are preserved."),
("4354","006"):("Canones Februarii","Analecta hymnica graeca, vol. 6 (1974), pp. 1–418","38,010","February scope, editors Schirò–Tomadakis, volume 6, and complete page bounds are preserved."),
("4354","007"):("Canones Martii","Analecta hymnica graeca, vol. 7 (1971), pp. 1–350","34,062","March scope, editors Schirò–Tomadakis, volume 7, and complete page bounds are preserved."),
("4354","008"):("Canones Aprilis","Analecta hymnica graeca, vol. 8 (1970), pp. 2–374","35,554","April scope, editors Schirò–Nicas, volume 8, and the page start at 2 are preserved."),
("4354","009"):("Canones Maii","Analecta hymnica graeca, vol. 9 (1973), pp. 2–347","32,955","May scope, editors Schirò–Nicas, volume 9, and the page start at 2 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, liturgical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
