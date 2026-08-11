import csv

O="data/research_batches/detailed_verified_3001_batch_385.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3280","001"):("Laudatio in martyrem Caesareae","Halkin, CCSG 21 (1989), pp. 65–76","2860","The unnamed Caesarean martyr defines this distinct hagiographic laudation."),
("3280","002"):("Laudatio in Bartholomaeum","Makris, Byzantina 22 (2001), pp. 86–93","2927","The Bartholomew laudation remains separate from the Mark and Caesarean-martyr items."),
("3280","003"):("Laudatio in Marcum (BHG 1037)","MPG 100 cols. 1188–1200","1993","The BHG 1037 identifier defines this exact Mark laudation."),
("3281","001"):("Narratio de sancto Onuphrio","Halkin, CCSG 21 (1989), pp. 79–88","2740","The Onuphrius narrative is the exact Paphnutius hagiographic item."),
("3284","001"):("Vitae breviores duae Theodori Syceotae","Paris 1534 and Patmos 736; Festugière 1970 pp. 288–301","5504","Both short lives are retained: first pp. 288–300 and second p. 301; the printed BHG markers are preserved without silent correction."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
