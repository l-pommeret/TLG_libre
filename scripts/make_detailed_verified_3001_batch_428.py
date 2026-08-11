import csv
O="data/research_batches/detailed_verified_3001_batch_428.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4036","015"):("Hymni 1–7","Vogt 1957, pp. 27–33","1144","The seven hymns form the exact item, separate from the following fragments."),
("4036","016"):("Hymnorum fragmenta","Vogt 1957, p. 33, fragments 1–2","14","The two fourteen-word fragments remain separate from Hymni 1–7."),
("4036","017"):("Epigrammata","Vogt 1957, p. 34","69","Epigram 1's explicit duplicate link to 4036.003 is preserved without collapsing the collection."),
("4036","018"):("De sacrificio et magia","Bidez, Catalogue des manuscrits alchimiques grecs 6 (1928), pp. 148–151","1029","The short sacrifice-and-magic treatise is checked as its exact item."),
("4036","020"):("Excerpta e Platonica Procli theologia","Cousin, pp. 1243–1258","3440","The canon's partial-duplicate link to Theologia Platonica 4036.004 is preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
