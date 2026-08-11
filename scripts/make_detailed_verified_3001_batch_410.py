import csv

O="data/research_batches/detailed_verified_3001_batch_410.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3415","001"):("Epistula ad Hierosolymitanos","MPG 86.2 cols. 3228–3233","word count not supplied","The Jerusalem addressees and CPG 7825 identifier define the exact letter."),
("3416","001"):("Homilia in exaltationem crucis","MPG 98 cols. 1265–1269","word count not supplied","CPG 7915 and BHG 430 identify the exact Cross-exaltation homily; truncated author heading is retained."),
("4001","001"):("Theophrastus dialogus","Colonna 1958 pp. 1–68","14888","The dialogue on immortality of souls and resurrection of bodies is the exact item."),
("4001","002"):("Epistulae","Massa Positano 1962 pp. 39–53","2901","Equivalence to Epistulae Graecae pp. 24–32 is preserved."),
("4013","001"):("In quattuor libros De caelo","Heiberg, CAG 7 (1894), pp. 1–361 and 365–731","262880","Both discontinuous loci are preserved; pages 361–364 belong to 4013.002, and embedded SIMUS is a catalogue heading artefact."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
