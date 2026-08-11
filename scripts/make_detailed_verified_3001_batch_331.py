import csv

O="data/research_batches/detailed_verified_3001_batch_331.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3130","001"):("Epistulae","Zanetto 1985 pp. 1–44","7534","The Simocatta letter collection is distinct from Theophylactus of Ochrid's letters."),
("3130","002"):("Historiae (Bekker edition)","Bekker, CSHB (1834), pp. 23–346","word count not supplied","This is the Bekker edition record; duplicate-title record 3130.003 for de Boor is preserved separately."),
("3130","003"):("Historiae (de Boor edition)","de Boor 1887, corrected reprint 1972, pp. 20–314","63739","This is the de Boor edition record; duplicate-title record 3130.002 for Bekker is preserved separately."),
("3130","007"):("Quaestiones physicae","Massa Positano 1965 pp. 7–38","4137","The exact natural-history dialogue and second-edition locus were checked."),
("3130","008"):("Ὅροι ζωῆς","Garton and Westerink 1978 pp. 2–30","word count not supplied","The work on predestined terms of life is distinct from Quaestiones physicae."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
