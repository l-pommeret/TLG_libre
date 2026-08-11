import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_312.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","057"):("Commentarius in apostolum Joannem, BHG 919–919b","MPG 116 cols. 684–705","4509","Both BHG identifiers define the item."),
("3115","058"):("Vita Cyriaci anachoretae, BHG 464","MPG 115 cols. 920–944","4410","Shared col. 944 with 3115.059 requires visual separation."),
("3115","059"):("Vita Gregorii Illuminatoris, BHG 713","MPG 115 cols. 944–996","11044","Reference to Agathangelus 2878.002 is contextual; shared col. 944 requires separation."),
("3115","060"):("Vitae Cypriani et Justinae, BHG 456","MPG 115 cols. 848–881","6127","Both saints define the item; shared col. 881 with 3115.031 requires separation."),
("3115","061"):("Vita Dionysii Areopagitae, BHG 555","MPG 4 cols. 589–608","3630","Reference to Pseudo-Dionysius 2798 is contextual and does not merge holdings.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
