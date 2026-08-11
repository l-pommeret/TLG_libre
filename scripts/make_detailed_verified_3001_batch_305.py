import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_305.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","022"):("Passio sanctae Barbarae, BHG 216","MPG 116 cols. 301–316","2838","Shared col. 301 with 3115.021 requires visual item separation."),
("3115","023"):("Vita sancti Alexii, BHG 54","Massmann 1843 pp. 192–200","3920","The Greek BHG 54 life within the multilingual historical volume is the target."),
("3115","024"):("Passio Marciani et Martyrii, BHG 1029","MPG 115 cols. 1289–1293","775","Both notaries and the short exact column span define this item."),
("3115","025"):("Vita Amphilochii Iconiensis, BHG 72","MPG 116 cols. 956–969","3216","The Canon explicitly prints 3,216 after Cod, but extraction misplaced it in genres; it is retained as the explicit word count."),
("3115","026"):("Vita Ananiae apostoli, BHG 76","MPG 114 cols. 1001–1009","1459","Ananias the apostle, BHG 76, and the exact MPG span define the item.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and explicit {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
