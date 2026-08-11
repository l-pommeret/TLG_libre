import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_300.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3114","001"):("Apocalypsis recension 1","Lolos 1976 pp. 46–140","6733","Recension 1 remains distinct from recensions 2–4 despite overlapping pagination."),
("3114","002"):("Apocalypsis recension 2","Lolos 1976 pp. 47–141","4239","Recension 2 remains distinct from recension 1 despite nearly identical page span."),
("3114","003"):("Apocalypsis recension 3","Lolos 1978 pp. 22, 25–38 and 40–75","4568","The Canon explicitly prints 4,568 after Cod, but extraction misplaced it in genres; the discontinuous loci are retained and gaps excluded."),
("3114","004"):("Apocalypsis recension 4","Lolos 1978 pp. 23, 39–69 and 76–78","2859","All discontinuous loci are explicit and gaps are excluded; recension 4 remains distinct from recension 3."),
("3115","001"):("Chronicon breve books 7–8, recent recension","MPG 110 cols. 1261–1285","4814","The recent recension and books 7–8 limitation are explicit; reference to 3043.002 is contextual.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and explicit {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact recension/item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
