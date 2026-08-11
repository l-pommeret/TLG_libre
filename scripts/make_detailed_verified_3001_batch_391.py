import csv

O="data/research_batches/detailed_verified_3001_batch_391.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3304","001"):("Epistula ad Janum Lascarim","Legrand 1892 pp. 363–366","938","The alternative forename Janus/John and Lascaris addressee define the exact epistle."),
("3305","001"):("Epistulae","Lampros 1912–1924 pp. 182–185, 189, 193–197 and 198–199","2086","All four discontinuous loci are preserved; trailing Notitiae Episcopatuum text is a catalogue heading."),
("3309","001"):("Argyrobulla","Lampros 1930 pp. 14–18","628","The silver-seal documents remain distinct from the following chrysobulls."),
("3309","002"):("Chrysobulla","Lampros 1930 pp. 19–25","1558","The gold-seal documents remain distinct from the preceding argyrobulls."),
("3310","001"):("Epistula ad Constantinum imperatorem","Lampros 1930 pp. 49–63","2039","The Greek translation by Theodore Gaza and cross-reference to Gaza 3194 are preserved without merging records."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
