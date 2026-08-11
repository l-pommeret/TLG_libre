import csv
O="data/research_batches/detailed_verified_3001_batch_441.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4042","012"):("Commentarius liturgicus [Sp.]","MPG 87.3, cols. 3981–4001","4374","Spurious status, possible Theodore of Andida authorship and boundary column 3981 shared with 4042.011 are preserved."),
("4042","017"):("Homilia in nativitatem Christi","Usener, RhM N.F. 41 (1886), pp. 501–516","4151","The Christmas homily is checked as the exact journal item."),
("4042","018"):("Homilia in Hypapanten","Usener 1889, pp. 8–18","4912","The Presentation homily is checked separately from the Christmas and Theophany homilies."),
("4042","019"):("Homilia in theophania","Papadopoulos-Kerameus 1898 (repr. 1963), pp. 151–168","4754","The Athos Dionysiou manuscript 228 witness and 1963 reprint are preserved."),
("4042","020"):("Sermo in annuntiationem deiparae","MPG 87.3, cols. 3217–3288","10391","The sermon remains an explicit item even though its locus falls within the broad Orationes span of 4042.002; no duplicate relation beyond the canon is asserted."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
