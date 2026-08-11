import csv
O="data/research_batches/detailed_verified_3001_batch_440.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4042","005"):("Laudes in sanctos Cyrum et Joannem","Bringel, PO 51.1 (2008), pp. 16–72","8450","The modern edition and stated equivalence to MPG 87.3, cols. 3380–3424 are both preserved."),
("4042","006"):("Narratio miraculorum sanctorum Cyri et Joannis","Fernández Marcos 1975, pp. 243–400","50172","The thaumata edition and equivalence to MPG 87.3, cols. 3424–3676 are preserved, including the boundary shared with 4042.005."),
("4042","009"):("Vita Mariae Aegyptiacae [Sp.]","MPG 87.3, cols. 3697–3726","7676","The spurious attribution is preserved without assigning another author."),
("4042","010"):("Anacreontica","Gigante 1957, pp. 25–144","8565","The modern edition and stated equivalence to MPG 87.3, cols. 3733–3838 are both preserved."),
("4042","011"):("Triodium [Sp.]","MPG 87.3, cols. 3840–3981","23518","The spurious status and terminal column shared with the next item are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
