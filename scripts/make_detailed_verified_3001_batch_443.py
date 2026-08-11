import csv
O="data/research_batches/detailed_verified_3001_batch_443.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4044","001"):("Epigrammata","AG 6.27; 9.659; 10.16; 16.32b, 221, 233","252","All six loci, uncertain grammarian attribution and cross-reference to Lexicon de Atticis nominibus 4292.001 are preserved."),
("4045","001"):("Epigramma AG 7.556","Anthologia Graeca 7.556","16","The single sixteen-word epigram locus is the complete exact item."),
("4046","001"):("Chronographia","de Boor 1883 (repr. 1963), pp. 3–503","131942","The reprint is preserved; the author_heading ending 'Chro-' is retained as a canon heading truncation rather than silently expanded."),
("4046","002"):("Epigrammata","Anthologia Graeca 15.14 and 15.35","57","Both explicitly listed epigram loci are preserved as one collection item."),
("4047","001"):("Epigramma AG 7.559","Anthologia Graeca 7.559","27","The single twenty-seven-word epigram locus is the complete exact item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, Anthologia Graeca, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
