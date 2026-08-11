import csv
O="data/research_batches/detailed_verified_3001_batch_469.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4146","008"):("Prolegomena in Hermogenis librum περὶ ἰδεῶν","Walz 1833, pp. 437–439","","The prolegomena and partial-duplicate link to Anonymi in Hermogenem 5024.013 are preserved; page 439 is shared with the main commentary."),
("4146","009"):("Commentarium in Hermogenis librum περὶ ἰδεῶν","Walz 1833, pp. 439–561","","The main commentary remains separate from its prolegomena despite shared page 439; no word count is supplied."),
("4146","010"):("Commentarium in Hermogenis librum περὶ μεθόδου δεινότητος","Walz 1833, pp. 562–576","","The method-of-force commentary remains a separate exact item; no word count is supplied."),
("4146","011"):("Epistulae","Leone 1991, pp. 1–215","54609","The Planudes letter collection is checked as the exact Leone item."),
("4146","012"):("Somnium Scipionis in Graecum translatum","Pavano 1992, pp. 3–19","2730","The Greek translation of Cicero's Somnium Scipionis remains explicitly a translation item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
