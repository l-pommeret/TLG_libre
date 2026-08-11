import csv
O="data/research_batches/detailed_verified_3001_batch_439.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4041","001"):("Epigramma AG 5.284","Anthologia Graeca 5.284","14","The single fourteen-word epigram locus is the complete exact item."),
("4042","001"):("Epistula synodica","MPG 87.3, cols. 3148–3200","","The canon's explicit duplicate link to 5000.009 is preserved; no absent word count is inferred."),
("4042","002"):("Orationes","MPG 87.3, cols. 3217–3364","","The homiletic collection remains separate from the following theological and fragmentary items; no word count is inferred."),
("4042","003"):("De peccatorum confessione","MPG 87.3, cols. 3365–3372","1089","The confession treatise remains separate from the baptism fragment sharing boundary column 3372."),
("4042","004"):("Fragmentum de baptismate apostolorum","MPG 87.3, col. 3372","","The single-column baptism fragment remains separate from 4042.003; no word count is inferred."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG/Anthologia Graeca citation, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
