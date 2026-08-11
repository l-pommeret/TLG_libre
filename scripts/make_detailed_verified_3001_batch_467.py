import csv
O="data/research_batches/detailed_verified_3001_batch_467.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","089"):("In ascensionem et in principium Actorum","Bishop–Rambault, Sacris erudiri 56 (2017), pp. 184–227","10026","Former attribution to John Chrysostom, CPG 4187 and equivalence to MPG 52, cols. 773–792 are preserved; the PTA candidate remains unverified."),
("4139","090"):("Oratio de Nativitate Christi [Dub.]","Datema–Allen, JÖB 39 (1989), even pp. 70–78","1293","Doubtful attribution, Pseudo-Chrysostom framing and the even-page restriction are preserved."),
("4141","001"):("Vita Aeschyli","Page 1972, pp. 331–335","897","The short Life of Aeschylus is checked as the exact Page item."),
("4146","001"):("Commentarium in arithmetica Diophanti","Tannery 1895, vol. 2 pp. 125–255","30151","The Marcianus 308 witness and cross-reference to Diophantus 2039.001 are preserved."),
("4146","002"):("Prolegomena in artem rhetoricam","Rabe, Rhetores Graeci 14 (1931), pp. 64–73","1962","The rhetorical prolegomena are checked independently from Planudes's mathematical commentary."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
