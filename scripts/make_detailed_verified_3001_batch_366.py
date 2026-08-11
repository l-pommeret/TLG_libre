import csv

O="data/research_batches/detailed_verified_3001_batch_366.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3228","001"):("Epistulae ad Georgium Lacapenum","Lindstam 1924 pp. 88–93, 99–103, 108–112, 119–120, 124–125, 139–144, 150–154 and 164–168","7169","All eight explicit discontinuous loci are preserved without filling gaps."),
("3231","001"):("De fructibus, redaction A","Winterwerb 1992 pp. 139–145","795","Redaction A remains separate from redactions B and C."),
("3231","002"):("De fructibus et lentibus, redaction B","Winterwerb 1992 pp. 147–149","432","Redaction B remains separate from redactions A and C."),
("3231","003"):("Liber brevis de fructibus, redaction C","Winterwerb 1992 pp. 151–154","447","Redaction C remains separate; trailing Porphyrius/cross-reference text is a new catalogue heading, not part of Poricologos."),
("3232","001"):("Dialogus adversus omnes haereses","MPG 155 cols. 33–696","word count not supplied","The full MPG locus defines the exact ecclesiastical dialogue; no word count was invented."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
