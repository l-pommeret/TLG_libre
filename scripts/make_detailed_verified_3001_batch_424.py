import csv
O="data/research_batches/detailed_verified_3001_batch_424.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4034","003"):("In libros de partibus animalium commentaria","Hayduck, CAG 22.2 (1904), pp. 1–99","40557","This first item in the composite CAG volume remains separate; the First1KGreek candidate is not exact licensed verification."),
("4034","004"):("In libros de animalium motione commentarium","Hayduck, CAG 22.2 (1904), pp. 103–131","9886","The explicit page gap after 4034.003 is retained; the First1KGreek candidate is not exact licensed verification."),
("4034","005"):("In librum de animalium incessu commentarium","Hayduck, CAG 22.2 (1904), pp. 135–170","13684","The embedded MICHAEL Rhetor heading artefact between edition and pages is recorded without changing the exact item; the First1KGreek candidate remains unverified."),
("4034","006"):("In librum quintum ethicorum Nicomacheorum commentarium","Hayduck, CAG 22.3 (1901), pp. 1–72","28743","Only Nicomachean Ethics book V is included; the First1KGreek candidate is not exact licensed verification."),
("4034","008"):("In Aristotelis sophisticos elenchos commentarius (= Pseudo-Alexander 1)","Wallies, CAG 2.3 (1898), pp. 1–198","72149","Former attribution to Alexander of Aphrodisias, Pseudo-Alexander 1 designation, and cross-reference to 4034.011 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
