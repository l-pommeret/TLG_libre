import csv
O="data/research_batches/detailed_verified_3001_batch_431.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4039","004"):("Epigrammata","all explicitly listed Anthologia Graeca loci in books 5–7, 9–11 and 16","3434","The full discontinuous AG locus list and cross-references to 4024.002, 4050.001 and 4063.001 remain in canonical_edition."),
("4039","005"):("Descriptio Sanctae Sophiae","De Stefani 2011, pp. 1–71","","The canon explicitly marks this modern edition as a duplicate of 4039.001; no absent word count is inferred."),
("4039","006"):("Descriptio ambonis","De Stefani 2011, pp. 72–88","","The canon explicitly marks this modern edition as a duplicate of 4039.002; no absent word count is inferred."),
("4040","001"):("Bibliotheca","Henry 1959–1977, all explicit loci in vols. 1–8","344703","All eight dates and volume-specific page spans are preserved, including vol. 1 beginning at page 1 and vols. 2–8 at page 8."),
("4040","002"):("Quaestiones ad Amphilochium","MPG 101, cols. 45–1172","","The MPG column span and theological classification are the full supplied item; the canon gives no word count."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, Anthologia Graeca/MPG citation, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
