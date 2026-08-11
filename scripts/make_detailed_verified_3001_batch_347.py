import csv

O="data/research_batches/detailed_verified_3001_batch_347.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3186","009"):("Adversus Hagarenos, Bogomilos et Judaeos","De Groote, HTR 97.3 (2004), pp. 337–351","2805","The catalogue's terminus ante quem 1223 and all three addressed groups are preserved."),
("3188","001"):("De spiritu animali","Ideler 1841 vol. 1 pp. 312–386","22488","The physiological treatise remains distinct from De urinis and De diagnosi."),
("3188","002"):("De urinis","Ideler 1842 vol. 2 pp. 3–192","54415","The urine treatise and its exact second-volume locus define the item."),
("3188","003"):("De diagnosi","Ideler 1842 vol. 2 pp. 353–463","32319","The diagnostic treatise remains distinct from the other Actuarius medical works."),
("3190","001"):("Epitaphius in Joannem Mesaritem","Heisenberg, repr. 1973, pp. 16–72","16109","The addressee, Nicholas Mesarites' brother John, defines the exact epitaph."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
