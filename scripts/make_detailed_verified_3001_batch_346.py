import csv

O="data/research_batches/detailed_verified_3001_batch_346.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3186","002"):("Dialogus Timothei et Aquilae","Robertson dissertation 1986 pp. i–cxxix","22870","The catalogue's Roman-numeral dissertation locus is preserved exactly."),
("3186","004"):("Papisci et Philonis cum monacho colloquium","McGiffert 1889 pp. 51–83","6709","Both explicit witnesses, Venice gr. 505 and Paris gr. 1111, define this exact dialogue."),
("3186","005"):("Trophaea Damasci","Bardy, PO 15.2 (1920), pp. 189–275 [19–105]","15273","Both outer and bracketed pagination are preserved; the embedded Scripta Anonyma in Joannem Chrysostomum text is a heading artefact."),
("3186","006"):("Adversus haereses","Bardy, PO 15.2 (1920), pp. 277–284 [107–114]","1433","The Coislin 299 witness and dual pagination define this exact short item."),
("3186","008"):("Dissertatio contra Judaeos","Hostens, CCSG 14 (1986), pp. 3–285","81985","The exact anonymous Theognosia anti-Jewish dissertation was checked."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
