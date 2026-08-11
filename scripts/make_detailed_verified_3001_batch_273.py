import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_273.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3024","014"):("Oratio in honorem Georgii Xiphilini","Loukaki 2005 pp. 169–177","1905","The George Xiphilinos honorand is part of the exact item identity."),
("3024","015"):("Contra Latinos","Darrouzès 1963 pp. 61–91","4534","No other anti-Latin work may be substituted on title similarity."),
("3024","016"):("Didascalia de mandylio et ceramo (BHG 796m)","Flusin 1997 pp. 66–78","2407","BHG 796m and both mandylion and ceramos subjects are part of the item identity."),
("3037","001"):("Orationes","Darrouzès 1968 pp. 56–72, 76–89 and 94–117","13433","The item explicitly comprises three discontinuous speeches; gaps and neighbouring journal matter are excluded."),
("3037","003"):("Epistula ad Michaelem Choniatam","Kolovou 1995 pp. 66–73","1974","The Michael Choniates reference is contextual and does not create or merge a 3080 holding.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(title,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
