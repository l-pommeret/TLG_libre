import csv
O="data/research_batches/detailed_verified_3001_batch_512.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4351","012"):("Περὶ τοῦ γνῶναι ἀπὸ τοῦ κλήρου τῆς τύχης τὸν πυνθανόμενον περὶ τίνος θέλει ἐρωτᾶν","Zuretti, CCAG 11.1 (1932), pp. 202–203","461","Scorialensis I Φ 5 fol.322 and the interrogational lot-of-fortune scope are preserved."),
("4354","001"):("Canones Septembris","Analecta hymnica graeca, vol. 1 (1966), pp. 1–396","37,840","September scope, editors Schirò–Debiasi Gonzato, volume 1, and complete page bounds are preserved."),
("4354","002"):("Canones Octobris","Analecta hymnica graeca, vol. 2 (1979), pp. 1–365","35,509","October scope, editors Schirò–Debiasi Gonzato, volume 2, and complete page bounds are preserved."),
("4354","003"):("Canones Novembris","Analecta hymnica graeca, vol. 3 (1972), pp. 1–553","52,485","November scope, editors Schirò–Kominis, volume 3, and complete page bounds are preserved."),
("4354","004"):("Canones Decembris","Analecta hymnica graeca, vol. 4 (1976), pp. 1–775","69,209","December scope, editors Schirò–Kominis, volume 4, and complete page bounds are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, relevant manuscript and liturgical corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
