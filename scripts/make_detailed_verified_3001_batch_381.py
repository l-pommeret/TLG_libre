import csv

O="data/research_batches/detailed_verified_3001_batch_381.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3271","002"):("Oratio adversus Becci blasphemias","Samara 2018 pp. 71–95","word count not supplied","The anti-Beccus oration remains distinct and no missing word count was invented."),
("3271","003"):("Oratio ad sanctum Nicetam iuniorem (BHG 2302)","Samara 2018 pp. 129–156","word count not supplied","The catalogue explicitly marks this as duplicate of the Nicetas oration at duplicated key 3271.001; both edition records remain separate."),
("3271","004"):("Epistulae","Samara 2018 pp. 215–224","word count not supplied","The letter collection remains separate; trailing MYIA catalogue text is not part of this item."),
("3272","001"):("Sermo in sanctissimam Deiparam","Jugie 1935 pp. 2–210","22893","The Marian sermon is the exact Theophanes III homiletic item."),
("3272","002"):("De lumine Thaborio orationes i–v","Soteropoulos 1990 pp. 79–206","42179","The explicit five-oration scope on the Tabor light is preserved exactly."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
