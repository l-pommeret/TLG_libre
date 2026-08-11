import csv
O="data/research_batches/detailed_verified_3001_batch_421.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4024","002"):("Epigrammata","all explicitly listed Anthologia Graeca loci in books 1, 4–7, 9–11 and 16","6159","The complete discontinuous locus list is retained in canonical_edition. Cross-references to 0533.004, 0138.001, 1457.001, 4039.004, 4063.001 and 4073.001 are preserved; a First1KGreek candidate is not exact licensed verification."),
("4024","003"):("Historiae","Niebuhr, CSHB (1828), pp. 4–335","","The canon explicitly marks the Niebuhr edition as a duplicate of 4024.001; both edition records remain separate."),
("4028","001"):("Ethnica (epitome)","Meineke 1849, pp. 1–713","98196","The epitome is kept distinct from the separately edited full-book segments."),
("4028","002"):("Epigramma AG 9.385","Anthologia Graeca 9.385","178","The single AG epigram locus is checked independently from the Ethnica records."),
("4028","003"):("Ethnica (Libri Α–Γ)","Billerbeck, CFHB 43/1 (2006), pp. 8–438","30670","Books Α–Γ are preserved as an explicit modern edition segment, separate from the Meineke epitome."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
