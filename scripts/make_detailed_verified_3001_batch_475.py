import csv
O="data/research_batches/detailed_verified_3001_batch_475.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4154","002"):("Fragmenta in epistulas apostoli Pauli","Staab 1933 (repr. 1967), pp. 423–469 and all listed epistle loci","Former attribution to Oecumenius Philosophus, cross-reference to TLG 2866 and every Pauline subdivision are preserved. The embedded OEDIPODEA heading before Ephesians is recorded as an artefact."),
("4154","003"):("Commentaria in acta apostolorum","MPG 118, cols. 36–308","The Acts commentary remains separate from the Pauline commentary sharing boundary column 308."),
("4154","004"):("Commentaria in epistulas apostoli Pauli","MPG 118 cols. 308–1325 and MPG 119 cols. 9–452","Both MPG volumes and loci are preserved; no word count is supplied."),
("4154","005"):("Commentaria in Jacobi epistulam catholicam","MPG 119, cols. 452–509","The James commentary remains separate despite shared boundary columns 452 and 509."),
("4154","006"):("Commentaria in Petri epistulas catholicas","MPG 119, cols. 509–617","The Petrine commentary remains separate despite sharing column 509 with James."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG/catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No word count is supplied by the canon. No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
