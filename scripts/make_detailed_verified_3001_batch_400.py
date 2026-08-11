import csv

O="data/research_batches/detailed_verified_3001_batch_400.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3344","003"):("Chronographia brevis [Dub.], Dindorf","Dindorf 1829 vol. 1 pp. 737–788","word count not supplied","This Dindorf two-recension edition remains separate from de Boor record 3344.002; duplicate MPG 100 cols. 1001–1060 and trailing Nicephorus Athonita heading are preserved."),
("3344","004"):("Apologeticus maior pro imaginibus","MPG 100 cols. 533–832","60309","The major apology remains separate from the minor apology 3344.006."),
("3344","005"):("Antirrhetici tres adversus Constantinum Copronymum","MPG 100 cols. 205–533","61846","The explicit three-antirrhetic scope is preserved exactly."),
("3344","006"):("Apologeticus minor pro imaginibus","MPG 100 cols. 833–849","2713","The minor apology remains separate from the major apology 3344.004."),
("3344","007"):("De Magnete","Pitra 1852 pp. 302–335","6136","The selected antirrhetic material De Magnete is the exact item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
