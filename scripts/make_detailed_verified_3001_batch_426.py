import csv
O="data/research_batches/detailed_verified_3001_batch_426.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4036","005"):("Institutio theologica","Dodds, 2nd ed. (1963, repr. 1977), pp. 2–184","27968","The second Dodds edition and reprint are preserved as the exact item."),
("4036","006"):("Institutio physica","Ritzenfeld 1912, pp. 2–58","7500","The physical Institutio remains separate from Institutio theologica."),
("4036","007"):("In Platonis Alcibiadem I","Westerink 1954, pp. 1–158","68092","The first-Alcibiades commentary is checked as the exact Westerink item."),
("4036","008"):("In Platonis Parmenidem","Cousin, Opera inedita pt. 3 (1864, repr. 1961), pp. 617–1244","170634","The high continuous locus within part 3 and the reprint are preserved."),
("4036","009"):("In Platonis Cratylum commentaria","Pasquali 1908, pp. 1–113","27813","The Cratylus commentary is checked independently from the other Platonic commentaries."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
