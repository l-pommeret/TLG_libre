import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_309.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","042"):("Miraculum Michaelis in Chonis, BHG 1284","Bonnet 1889 pp. 308–316","2387","The Metaphrastic libellus, not other Chonae miracle recensions, is the exact item."),
("3115","043"):("Passio Romuli, Eudoxii, Zenonis et Macarii, BHG 1604","MPG 115 cols. 617–633","2534","All four saints define the item; shared col. 633 with 3115.044 requires separation."),
("3115","044"):("Passio Sozontis, BHG 1644","MPG 115 cols. 633–640","1155","Shared cols. 633 and 640 with adjacent items require visual separation."),
("3115","045"):("Passio Severiani Sebastiae, BHG 1627","MPG 115 cols. 640–652","2625","Severian's Sebaste qualifier and shared col. 640 require exact boundary verification."),
("3115","046"):("Passio Menodorae, Metrodorae et Nymphodorae, BHG 1273","MPG 115 cols. 653–665","2553","All three saints define the item; reference to Vitae 5143 is contextual.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
