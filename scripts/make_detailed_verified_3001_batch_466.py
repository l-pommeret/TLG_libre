import csv
O="data/research_batches/detailed_verified_3001_batch_466.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","067"):("De tribus pueris","MPG 56, cols. 593–600","2917","Former attribution to John Chrysostom is preserved; the PTA candidate does not establish exact licensed MPG verification."),
("4139","072"):("De caeco nato","MPG 59, cols. 543–554","6277","Former attribution to John Chrysostom is preserved; the PTA candidate does not establish exact licensed MPG verification."),
("4139","081"):("De caeco et Zacchaeo","MPG 59, cols. 599–610","5323","Former attribution to John Chrysostom is preserved; the PTA candidate does not establish exact licensed MPG verification."),
("4139","087"):("In illud: Quando ipsi subiciet omnia","Haidacher, ZKT 31 (1907), pp. 150–167","4133","Former attribution to John Chrysostom and the Basel manuscript context are preserved; the PTA candidate remains unverified at edition/license level."),
("4139","088"):("In tentationem domini nostri Jesu Christi","Carter, Traditio 52 (1997), pp. 56–70","1792","Former attribution to John Chrysostom and CPG 4906 are preserved; two PTA text variants are candidates only."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
