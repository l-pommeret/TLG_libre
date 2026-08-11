import csv
O="data/research_batches/detailed_verified_3001_batch_462.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","018"):("De pace (CPG 4214)","Papadopoulos-Kerameus 1891, pp. 15–26","2369","The Sabbaiticus 32 fols.130r–135v witness is preserved; the PTA candidate is not exact licensed edition verification."),
("4139","020"):("In incarnationem domini (CPG 4204)","Regtuit 1992, pp. 232–286","7794","The modern Regtuit edition is the exact target; the PTA candidate is not treated as verified edition/license equivalence."),
("4139","032"):("Homilia de lotione pedum","Wenger, REB 25 (1967), pp. 225–229","1605","The previously unpublished foot-washing homily is checked as its exact journal item."),
("4139","034"):("In Genesim (sermo 1)","MPG 56, cols. 519–522","1743","Former attribution to John Chrysostom is preserved; the PTA candidate does not resolve exact MPG edition/license."),
("4139","038"):("In Job (sermones 1–4)","MPG 56, cols. 563–582","11941","All four sermons and former Chrysostom attribution are preserved; four PTA item candidates are not exact licensed MPG verification."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
