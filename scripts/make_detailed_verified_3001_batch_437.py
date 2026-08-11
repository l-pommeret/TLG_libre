import csv
O="data/research_batches/detailed_verified_3001_batch_437.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","029"):("Lexicon (Α—Δ)","Theodoridis 1982, vol. 1 pp. 3–4 and 7–440","55589","Both discontinuous loci and the cross-reference to 4040.030 are preserved."),
("4040","030"):("Lexicon (Ε—Ω)","Porson 1822, pt. 1 pp. 10–367; pt. 2 pp. 367–659","81980","Both parts, their shared page 367 and the cross-reference to 4040.029 are preserved; this older broad segment is not merged with later Theodoridis segments."),
("4040","031"):("Epistula ad Arsenium de Manichaeis","Conus-Wolska 1970, pp. 181–183","388","The short letter to Arsenius is checked independently from Contra Manichaeos 4040.003."),
("4040","032"):("Lexicon (Ε—Μ)","Theodoridis 1998, vol. 2 pp. 3–592","52185","This modern Ε—Μ segment remains distinct from Porson's Ε—Ω and retains cross-references to 4040.029 and 4040.030."),
("4040","033"):("Lexicon (Ν—Φ)","Theodoridis 2013, vol. 3 pp. 3–594","50192","The Ν—Φ segment remains a separate modern-edition record."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
