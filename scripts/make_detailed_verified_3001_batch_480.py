import csv
O="data/research_batches/detailed_verified_3001_batch_480.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4161","008"):("De zodiaco","Martin 1974, pp. 529–532","512","Former attribution to Leontius Mechanicus is preserved."),
("4161","009"):("Epistula ad Julianum quendam data","Martin 1974, pp. 533–534","148","Former attribution to Theon Alexandrinus mathematicus and the otherwise unspecified Julian recipient are preserved."),
("4161","010"):("Excerpta varia de phaenomenis Arati","Martin 1974, pp. 535–544","1063","The varied Aratean excerpts remain a separate exact item."),
("4161","011"):("Astronomica","Martin 1974, pp. 556–557","220","The appendix context in Escorialensis Σ III 3 is preserved."),
("4161","012"):("Ἐξ ἑτέρων σχολίων εἰσαγωγή (= Anonymus I)","Maass 1898 (repr. 1958), pp. 89–98","2672","The Anonymus I equivalence, Vaticanus graecus 191 witness and reprint are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
