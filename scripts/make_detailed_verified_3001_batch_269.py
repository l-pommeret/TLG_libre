import csv
START=("3002","006");OUTPUT="data/research_batches/detailed_verified_3001_batch_269.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3002","006"):("Comoediae veterae nomina poetarum et dramata","Koster 1975 p. 18","29","Page 18 is shared with 3002.005; visual separation is required."),
("3002","007"):("De Hellenismo et Atticismo","Koster 1975 p. 19","151","Page 19 is shared with 3002.008; visual separation is required."),
("3002","008"):("De choro","Koster 1975 pp. 19–20","89","This De choro is distinct from 3002.005 by locus and word count."),
("3002","009"):("De scoliis","Koster 1975 pp. 20–21","111","Pages 20–21 overlap adjacent items; exact start and end must be checked visually."),
("3002","010"):("De histrionibus","Koster 1975 p. 21","23","Page 21 contains multiple short items; the 23-word boundary is mandatory.")}
c=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")));i=next(i for i,r in enumerate(c)if(r["tlg_author_id"],r["tlg_work_id"])==START);rows=c[i:i+5];assert [(r["tlg_author_id"],r["tlg_work_id"])for r in rows]==list(ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for s in rows:
  k=(s["tlg_author_id"],s["tlg_work_id"]);title,locus,wc,boundary=ITEMS[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item boundary checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title}, {locus}, was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the {wc}-word item boundary before transcription or OCR.",notes=boundary+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
