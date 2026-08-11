import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_317.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","082"):("Vita Joannis Eleemosynarii, BHG 888","MPG 114 cols. 896–965","13793","Reference to author/corpus 2925 is contextual and does not merge holdings."),
("3115","083"):("Commentarius Philippi apostoli, BHG 1527","MPG 115 cols. 188–197","1952","Philip the apostle and BHG 1527 define the item."),
("3115","084"):("Commentarius Matthaei apostoli, BHG 1226","MPG 115 cols. 813–820","1155","Matthew the apostle and BHG 1226 define the item."),
("3115","085"):("Vita Nicolai Myrensis, BHG 1349","MPG 116 cols. 317–356","8450","Reference to Vitae et Miracula 5067 is contextual; Nicholas' Myra qualifier defines the item."),
("3115","086"):("Vita Patapii, BHG 1424","MPG 116 cols. 357–368","2153","Patapius and BHG 1424 define the item.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
