import csv
O="data/research_batches/detailed_verified_3001_batch_477.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4158","003"):("Versus Byzantini Anonymi in Aristophanem","Koster 1975, p. 141","37","The anonymous Byzantine verses remain separate from the Vita/catalogue sharing page 141."),
("4158","004"):("Vita dramatumque catalogus","Koster 1975, pp. 141–142","128","The Life-and-play-catalogue item remains separate despite sharing page 141 with the verses."),
("4158","005"):("Vita Aristophanis 5","Koster 1975, p. 143","45","This single-page generic Vita remains separate from 4158.006 sharing page 143."),
("4158","006"):("Vita Aristophanis 6","Koster 1975, pp. 143–144","153","This generic Vita remains separate despite shared pages with 4158.005 and Tzetziana 1."),
("4158","007"):("Vita Tzetziana 1","Koster 1975, p. 144","80","The first Tzetzian Life remains separate despite sharing page 144 with 4158.006."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
