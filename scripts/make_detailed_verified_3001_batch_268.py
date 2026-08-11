import csv
START=("3002","001");OUTPUT="data/research_batches/detailed_verified_3001_batch_268.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3002","001"):("De comoedia","Koster 1975 pp. 7–10","596"),
("3002","002"):("De comoedia","Koster 1975 pp. 11–12","231"),
("3002","003"):("De comoedia","Koster 1975 pp. 13–15","241"),
("3002","004"):("De comoedia","Koster 1975 pp. 15–16","146"),
("3002","005"):("De choro","Koster 1975 pp. 17–18","92")}
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(i for i,r in enumerate(c)if(r["tlg_author_id"],r["tlg_work_id"])==START);rows=c[i:i+5];assert [(r["tlg_author_id"],r["tlg_work_id"])for r in rows]==list(ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for s in rows:
  k=(s["tlg_author_id"],s["tlg_work_id"]);title,locus,wc=ITEMS[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item boundary checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title}, {locus}, was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and distinguish this {wc}-word item from adjacent same-titled prolegomena before transcription or OCR.",notes="Repeated titles are distinct Canon items identified by exact page span and word count; no image or OCR used.",last_checked="2026-08-11");w.writerow(r)
