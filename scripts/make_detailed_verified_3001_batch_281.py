import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_281.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3064","002"):("Continuatio Scylitzae","Tsolakes 1968 pp. 103–186","21242","This Tsolakes edition record remains distinct from the Bekker edition at 3064.001.","NO_EXACT_OPEN_TEXT"),
("3070","001"):("Chronicon, redactions A+B","Bekker 1842 pp. 3–331","59369","Both manuscript-defined sections, Paris gr. 854 pp. 3–207 and Paris gr. 1711 pp. 207–331, are explicit; shared p. 207 requires visual separation.","NO_EXACT_OPEN_TEXT"),
("3070","002"):("Epistulae","Darrouzès 1960 pp. 99–115 and 130–163","11999","Both discontinuous page spans are explicit and the intervening pages are excluded.","NO_EXACT_OPEN_TEXT"),
("3070","003"):("Chronicon","Wahlgren 2006 pp. 5–343","61170","Canon duplicate link to 3070.001 is preserved, while the Wahlgren edition remains a distinct acquisition target.","DUPLICATE_DISTINCT_EDITION_NO_TEXT"),
("3076","001"):("Canones","Valentini 1957 pp. 18–88 even pages","3105","Only the even-page Greek text is canonical; odd facing pages are excluded.","NO_EXACT_OPEN_TEXT")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note,status) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status=status,next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
