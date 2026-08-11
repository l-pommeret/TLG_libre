import csv
O="data/research_batches/detailed_verified_3001_batch_460.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","008"):("In psalmum 95 [Sp.] (CPG 488e)","MPG 55, cols. 619–630","4995","Spurious status is preserved; the PTA candidate is not exact licensed MPG verification."),
("4139","009"):("De serpente homilia [Sp.] (BHG 451h)","MPG 56, cols. 499–516","7957","Spurious status and BHG identifier are preserved; the PTA candidate is not exact licensed MPG verification."),
("4139","010"):("De spiritu sancto [Sp.] (CPG 4188)","MPG 52, cols. 813–816","7431","Spurious status and former attribution to John Chrysostom are preserved; the PTA candidate does not resolve exact edition/license."),
("4139","011"):("In mundi creationem (homiliae 1–6)","MPG 56, cols. 429–500","32310","All six homilies remain one canon item; six PTA work candidates do not establish exact licensed MPG verification."),
("4139","012"):("In illud: Quomodo scit litteras [Sp.] (CPG 4201)","MPG 59, cols. 643–652","5559","Spurious status is preserved; the PTA candidate is not exact licensed MPG verification."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
