import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_313.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","062"):("Passio Sergii et Bacchi, BHG 1625","MPG 115 cols. 1005–1032","5184","Reference to Vitae 5279 is contextual; shared col. 1005 with 3115.036 requires separation."),
("3115","063"):("Vita Pelagiae, BHG 1479","MPG 116 cols. 908–920","2313","Reference to Vitae 5124 is contextual; shared col. 908 with 3115.066 requires separation."),
("3115","064"):("Passio Eulampii et Eulampiae, BHG 617","MPG 115 cols. 1053–1065","2453","Both Eulampius and Eulampia define the item."),
("3115","065"):("Passio Probi, Tarachi et Andronici, BHG 1575","MPG 115 cols. 1068–1080","2667","All three martyrs define the item."),
("3115","066"):("Vita et certamen Nazarii, Gervasii, Protasii et Celsi, BHG 1324","MPG 116 cols. 896–908","2434","All four saints define the item; shared col. 908 with 3115.063 requires separation.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
