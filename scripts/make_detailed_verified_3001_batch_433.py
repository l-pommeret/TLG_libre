import csv
O="data/research_batches/detailed_verified_3001_batch_433.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","009"):("Epistulae et Amphilochia","Laourdas–Westerink 1983–1988, explicit loci in vols. 1–6.1","349135","All published volumes through 6.2 and dates are retained, while the supplied text loci stop at 6.1; no locus for 6.2 is invented."),
("4040","010"):("Syntagma canonum","MPG 104, cols. 441–976","","The bibliographic notice terminates at 'Cod' and supplies no word count or genre; these are not inferred."),
("4040","011"):("Epigramma AG 9.203","Anthologia Graeca 9.203","64","The single epigram locus is preserved; the trailing PHOTIUS text is recorded as a heading artefact rather than part of the item."),
("4040","012"):("Interrogationes decem","MPG 104, cols. 1220–1232","","The ten questions' MPG column span and ecclesiastical classification are preserved; no word count is inferred."),
("4040","013"):("Nomocanon [Sp.]","Rhalles–Potles 1852, vol. 1 pp. 5–335","34324","Spurious status and the stated equivalence to MPG 104, cols. 980–1217 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG/Anthologia Graeca citation, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
