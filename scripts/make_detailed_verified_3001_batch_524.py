import csv

OUTPUT="data/research_batches/detailed_verified_3001_batch_524.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA={
("4402","003"):("Papadopoulos-Kerameus 1905, pp. iv–vi","640","The short Synaxarium remains separate from the Vita and Encomium."),
("4402","004"):("Fusco 1997, pp. 112–127","4,898","BHG 194a–b and the Athanasius cross-reference are retained."),
("4402","005"):("Afentoulidou-Leitgeb 2008, pp. 165–227","8,942","The canons retain their ecclesiastical and liturgical classifications."),
("4406","001"):("Lampsides 1982, pp. 251–256","1,932","The Testamentum retains its ecclesiastical, legal, and typikon classifications."),
("4407","001"):("Walz, Rhetores Graeci 4 (1833), pp. 39–846","183,311","The very large Hermogenic scholia item is preserved as the first of two duplicate canonical occurrences."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(OUTPUT,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
 for k,(locus,count,note) in DATA.items():
  s=C[k];r={f:'' for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, ecclesiastical/rhetorical corpus, First1KGreek, Perseus, OPP, PTA and scan-register lookup; {locus} and the printed {count}-word count checked.',open_text_result=f'No exact licensed TEI matching {locus} was verified.',scan_result=f'No reusable page-image source matching {locus} is registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate page images for {locus}, sample Greek in the exact item, then transfer only its pages without provider OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
