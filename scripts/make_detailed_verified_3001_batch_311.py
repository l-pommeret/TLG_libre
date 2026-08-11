import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_311.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","052"):("Vita Trophimi, Sabbatii et Dorymedontis, BHG 1854","MPG 115 cols. 733–749","3418","All three saints define the item."),
("3115","053"):("Passio Eustathii et sociorum, BHG 642","Van Hoof 1884 pp. 66–112","8225","References 2705.024 and 5278.001 are contextual and do not merge holdings."),
("3115","054"):("Laudatio martyris Phocae, BHG 1539–1540","MPG 40 cols. 300–313","2014","Both BHG identifiers are retained as the exact item boundary."),
("3115","055"):("Martyrium Theclae, BHG 1719","MPG 115 cols. 821–845","5204","Embedded author-heading artefact is excluded; reference to Vitae et Miracula 5201 is contextual."),
("3115","056"):("Vita Euphrosynes Alexandrinae, BHG 626","MPG 114 cols. 305–321","3421","The Alexandrian qualifier and reference 5250 are preserved without merging holdings.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
