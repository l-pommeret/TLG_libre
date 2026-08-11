import csv

O="data/research_batches/detailed_verified_3001_batch_413.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4015","002"):("In Aristotelis analytica priora commentaria","Wallies, CAG 13.2 (1905), pp. 1–485","162401","A First1KGreek identifier candidate exists, but exact Wallies item-level edition and license verification is not established locally."),
("4015","003"):("In Aristotelis analytica posteriora commentaria (prooemium e codd. BRL)","Wallies, CAG 13.3 (1909), pp. xxvii–xxx","1584","The proem from manuscripts BRL is preserved as a separate item from the main commentary 4015.004."),
("4015","004"):("In Aristotelis analytica posteriora commentaria","Wallies, CAG 13.3 (1909), pp. 1–440","144910","A First1KGreek identifier candidate exists; it does not collapse the separate BRL proem 4015.003, and exact license verification is absent."),
("4015","005"):("In Aristotelis meteorologicorum librum primum commentarium","Hayduck, CAG 14.1 (1901), pp. 1–131","52939","A First1KGreek identifier candidate exists, but exact Hayduck item-level edition and license verification is not established locally."),
("4015","006"):("In Aristotelis libros de generatione et corruptione commentaria","Vitelli, CAG 14.2 (1897), pp. 1–314","106550","A First1KGreek identifier candidate exists, but exact Vitelli item-level edition and license verification is not established locally."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
