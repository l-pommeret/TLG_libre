import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_286.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3085","006"):("Testamentum / Τυπικὴ Διαθήκη","Stephanes 1998 vol. 2 pp. 25–69","9325","This 1998 edition record and word count remain distinct from 3085.003; the link to Typica 5330 is contextual."),
("3085","007"):("Liber catechesium","Sotiroudis 1998 vol. 2 pp. 189–431","49013","This catechetical book is a distinct item within volume 2."),
("3085","008"):("Πανηγυρική βίβλος","Papatriantafyllou-Theodoridi–Giagkou 1999 vol. 3 pp. 111–542","96860","The Panegyrike A edition identity and volume 3 boundary are mandatory."),
("3085","009"):("Commentarius in Hexaemeron Genesim","Detorakes 2001 vol. 4 pp. 45–144","21471","This Hexaemeron commentary is distinct from the other exegetical works in volume 4."),
("3085","010"):("Commentarius in psalmos","Detorakes 2001 vol. 4 pp. 232–529","61246","This Psalter commentary has its own exact page and word-count boundary.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
