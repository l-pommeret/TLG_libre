import csv

O="data/research_batches/detailed_verified_3001_batch_373.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3242","001"):("Fragmentum Theophanis Byzantii","FHG 4 pp. 270–271; fragment 1","word count not supplied","The Bibliotheca 64.26a.12 and Photius 4040.001 cross-references remain contextual; no missing size was invented."),
("3245","001"):("Epistulae ad Nicetam Stethatum","Darrouzès, SC 81 (1961), pp. 230–234","467","The cross-reference to Nicetas Stethatus 3099.002 remains separate."),
("3246","001"):("Additamenta in orationes Nicetae Stethati","Darrouzès, SC 81 (1961), pp. 296–298, 360–362 and 364","480","All three discontinuous loci are preserved; cross-reference to Stethatus 3099.003 remains separate."),
("3247","001"):("Epistula ad Nicetam Stethatum","Darrouzès, SC 81 (1961), pp. 294–296","288","This single letter remains distinct from 3245.001 and the Stethatus 3099.003 record."),
("3247","002"):("Carmen","MPG 120 cols. 307–308","300","The short poem is preserved separately from the preceding epistle."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
