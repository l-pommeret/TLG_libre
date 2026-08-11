import csv

OUTPUT="data/research_batches/detailed_verified_3001_batch_523.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA={
("4398","004"):("Bakker–van Gemert 2002, pp. 123–141","3,573","The Passion/Crucifixion lament remains distinct from the secular dream poems."),
("4398","005"):("Bakker–van Gemert 1972, pp. 103–117","2,890","The consolatory rime and its narrative-fiction classification are preserved."),
("4401","001"):("Gassisi 1906, pp. 55–62","1,122","The allocations to St Nilus on pp. 55–56 and 60–62 and St Martin on pp. 56–59 remain explicit and discontinuous."),
("4402","001"):("Papadopoulos-Kerameus 1905, pp. 1–51","14,061","The Vita and both Athanasius/Calothetus cross-references are preserved without merger."),
("4402","002"):("Talbot 1983, pp. 44–123","10,340","The translation-of-relics oration remains distinct from the Vita and carries both hagiographic and homiletic classifications."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for k,(locus,count,note) in DATA.items():
  s=C[k];r={f:'' for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, hagiographic/poetic corpus, First1KGreek, Perseus, OPP, PTA and scan-register lookup; {locus} and the printed {count}-word count checked.',open_text_result=f'No exact licensed TEI matching {locus} was verified.',scan_result=f'No reusable page-image source matching {locus} is registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate page images for {locus}, sample Greek in the exact item, then transfer only its pages without provider OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
