import csv
O="data/research_batches/detailed_verified_3001_batch_422.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4028","004"):("Ethnica (Libri Δ–Ι)","Billerbeck–Zubler, CFHB 43/2 (2011), pp. 4–304","16960","Books Δ–Ι remain an autonomous edition segment."),
("4028","005"):("Ethnica (Libri Κ–Ο)","Billerbeck–Lentini–Neumann-Hartmann, CFHB 43/3 (2014), pp. 4–446","19903","Books Κ–Ο remain an autonomous edition segment."),
("4028","006"):("Ethnica (Libri Π–Υ)","Billerbeck–Neumann-Hartmann, CFHB 43/4 (2016), pp. 6–386","20803","Books Π–Υ remain an autonomous edition segment."),
("4028","007"):("Ethnica (Libri Φ–Ω)","Billerbeck–Neumann-Hartmann, CFHB 43/5 (2017), even pp. 4–152","8751","The canon's volume-title/series-number mismatch (Volumen IV versus 43/5) and even-page restriction are preserved verbatim, not normalized."),
("4029","001"):("De bellis","Wirth post Haury, Opera omnia 1–2 (1962–1963), all explicit discontinuous loci","224601","All printed discontinuities and the Persian/Vandal/Gothic book mapping are retained. A Perseus candidate is not treated as exact Wirth edition/license verification."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
