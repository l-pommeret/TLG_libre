import csv

O="data/research_batches/detailed_verified_3001_batch_392.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3312","001"):("Argyrobulla","Lampros 1930 pp. 231–240","1464","The Thomas Palaeologus silver-seal documents are the exact legal-historical item."),
("3313","001"):("Epistula ad Amadaeum Sabaudicum","Lampros 1930 p. 3","195","The single-page letter and alternative Italian form Amedeo di Savoia identify the addressee exactly."),
("3314","001"):("Argyrobulla","Lampros 1930 pp. 104–109","1033","The Theodore II silver-seal documents remain distinct from other Palaeologan argyrobulls."),
("3314","002"):("Epistula ad Angelum Acciaiolum","Lampros 1930 pp. 110–111","254","The cardinal Angelus Acciaiolus defines the exact epistle; trailing Thomas Palaeologus is a catalogue heading."),
("3317","001"):("Argyrobulla","Lampros 1930 pp. 187–195","1961","The Demetrius Palaeologus silver-seal documents remain separate from his letters."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
