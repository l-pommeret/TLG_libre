import csv
O="data/research_batches/detailed_verified_3001_batch_479.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4161","003"):("Vita Arati (= Vita 2)","Martin 1974, pp. 11–13","391","Both Madrid manuscript witnesses 4691 and 4629 are preserved."),
("4161","004"):("Arati genus (= Vita 3)","Martin 1974, pp. 14–18","372","Both possible Theon attributions and the Edinburgh plus Ambrosianus C263 witnesses are preserved without resolution."),
("4161","005"):("Vita Arati (= Vita 4)","Martin 1974, pp. 19–21","235","All eight listed manuscript sigla/witnesses are retained in canonical_edition."),
("4161","006"):("Prolegomena in Aratum","Martin 1974, pp. 23–31","1482","The Parisinus supplementum graecum 607A witness distinguishes this prolegomenon item."),
("4161","007"):("Prolegomena in Aratum (= Περὶ ἐξηγήσεως)","Martin 1974, pp. 32–34","514","The Greek equivalent title, former Achilles Tatius attribution and Vaticanus graecus 191 witness are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
