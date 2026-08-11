import csv

O="data/research_batches/detailed_verified_3001_batch_334.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3135","007"):("Hypomnema in s. Sophronium (BHG 1641)","Kaltsogianni 2013 pp. 560–570","3490","The BHG 1641 identifier defines the exact Sophronius item."),
("3135","008"):("Hypomnema in s. Cyrillum (BHG 2099)","Kaltsogianni 2013 pp. 572–584","4477","The BHG 2099 identifier defines the exact Cyril item."),
("3135","009"):("Homilia in Hypapanten (BHG 1962c)","Kaltsogianni 2013 pp. 586–598","4832","The BHG 1962c identifier and Hypapante subject define the exact homily."),
("3135","010"):("Homilia de festo s. Crucis (BHG 419m)","Kaltsogianni 2013 pp. 600–610","3669","The BHG 419m identifier defines the exact Holy Cross homily."),
("3135","011"):("De matrimonio sobrinorum","MPG 135 cols. 429–437","1597","The exact theological tract on cousins' marriage was checked separately from the hagiographic works."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
