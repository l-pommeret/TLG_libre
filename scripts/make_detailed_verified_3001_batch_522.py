import csv

OUTPUT="data/research_batches/detailed_verified_3001_batch_522.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA={
("4396","001"):("Müller, FHG 4, pp. 519–520","288","Fragments 1a, 1b and 2–6 and the title περὶ λιμένων are preserved."),
("4397","001"):("Müller, FHG 4, pp. 454–455","213","The six editorial fragments remain one canonical aggregate."),
("4398","001"):("Bakker–van Gemert 1977, pp. 65–75","2,809","The didactic poem is kept separate from the author's other poetic works."),
("4398","002"):("van Gemert 1980, pp. 99–130","6,845","Both fictional-narrative and poetic classifications are preserved."),
("4398","003"):("van Gemert 1980, pp. 131–135","1,154","The trailing PHANIAS heading artefact is excluded from the work while the canonical edition is preserved verbatim."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for k,(locus,count,note) in DATA.items():
  s=C[k];r={f:'' for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, historical-text, First1KGreek, Perseus, OPP, PTA and scan-register lookup; {locus} and the printed {count}-word count checked.',open_text_result=f'No exact licensed TEI matching {locus} was verified.',scan_result=f'No reusable page-image source matching {locus} is registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate page images for {locus}, sample Greek in the exact item, then transfer only its pages without provider OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
