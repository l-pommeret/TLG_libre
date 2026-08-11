import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_275.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3038","006"):("Commentarius in epistulam II ad Corinthios","Kalogeras 1887 vol. 1 pp. 371–495","28064","The second Corinthian commentary is distinct from 3038.005."),
("3038","007"):("Commentarius in epistulam ad Galatas","Kalogeras 1887 vol. 1 pp. 496–560","15185","This is the Galatians component, not a generic Pauline commentary."),
("3038","008"):("Commentarius in epistulam ad Ephesios","Kalogeras 1887 vol. 2 pp. 1–68","15383","The volume changes from vol. 1 to vol. 2 at this item and must be preserved."),
("3038","009"):("Commentarius in epistulam ad Philippenses","Kalogeras 1887 vol. 2 pp. 69–112","9587","This Philippians component has its own exact page and word-count boundary."),
("3038","010"):("Commentarius in epistulam ad Colossenses","Kalogeras 1887 vol. 2 pp. 113–156","10102","This Colossians component has its own exact page and word-count boundary.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(title,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the complete {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
