import csv
O="data/research_batches/detailed_verified_3001_batch_476.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4154","007"):("Commentaria in Joannis epistulas catholicas","MPG 119, cols. 617–704","","The Johannine Catholic-epistles commentary remains separate despite shared boundary columns with Peter and Jude; no count is supplied."),
("4154","008"):("Commentaria in Judae epistulam catholicam","MPG 119, cols. 704–721","","The Jude commentary remains separate despite sharing column 704 with John; no count is supplied."),
("4155","001"):("Nauticus lapidarius liber","Halleux–Schamp 1985, pp. 188–189","","The two-page nautical lapidary is checked as the exact item; no word count is supplied."),
("4158","001"):("Vita Aristophanis 1","Koster 1975, pp. 133–136","648","This first generic Vita title remains distinct by its exact locus and count."),
("4158","002"):("Vita Aristophanis 2","Koster 1975, pp. 136–140","433","This second generic Vita remains distinct despite sharing page 136 with 4158.001."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
