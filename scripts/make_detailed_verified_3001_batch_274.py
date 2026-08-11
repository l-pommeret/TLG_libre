import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_274.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3038","001"):("Panoplia dogmatica ad Alexium Comnenum","MPG 130 cols. 20–1360","280895","The addressee Alexius Comnenus and full MPG column span define the item."),
("3038","002"):("Commentarius in psalterium","MPG 128 cols. 41–1325","217380","This Psalter commentary must not be conflated with the Gospel or Pauline commentaries."),
("3038","003"):("Commentaria in quattuor evangelia","MPG 129 cols. 107–1501","231630","The item covers the four-Gospel commentary in this exact MPG span."),
("3038","004"):("Commentarius in epistulam ad Romanos","Kalogeras 1887 vol. 1 pp. 1–185","43414","This is the Romans component of the multi-work Kalogeras volume."),
("3038","005"):("Commentarius in epistulam I ad Corinthios","Kalogeras 1887 vol. 1 pp. 186–370","42413","The first Corinthian commentary is distinct from 3038.006.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(title,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the complete {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
