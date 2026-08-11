import csv

OUTPUT="data/research_batches/detailed_verified_3001_batch_525.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA=[
(("4407","001"),"Walz, Rhetores Graeci 4 (1833), pp. 39–846","183,311","This is the second duplicate canonical occurrence; it is recorded explicitly rather than silently collapsed."),
(("4407","002"),"Duffy–Parker, pp. 149–196","11,886","The alternate recension of the Synodicon remains distinct."),
(("4407","003"),"Duffy–Parker, pp. 147–148","327","Sinaiticus gr. 482, the scholia status, and all trailing author cross-references are preserved."),
(("4408","001"),"Gouillard 1967, pp. 45–107","9,608","The Synodicon orthodoxiae retains conciliar, ecclesiastical, and theological classifications."),
(("4408","002"),"Gouillard 1967, pp. 108–118","2,411","The episcopal encomia preserved within recensions remain a separate canonical item."),
]
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for k,locus,count,note in DATA:
  s=C[k];r={f:'' for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, ecclesiastical/rhetorical corpus, First1KGreek, Perseus, OPP, PTA and scan-register lookup; {locus} and the printed {count}-word count checked.',open_text_result=f'No exact licensed TEI matching {locus} was verified.',scan_result=f'No reusable page-image source matching {locus} is registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate page images for {locus}, sample Greek in the exact item, then transfer only its pages without provider OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
