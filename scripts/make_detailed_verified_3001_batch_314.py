import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_314.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","067"):("Vita et martyrium Luciani, BHG 997","MPG 114 cols. 397–416","3492","Both life and martyrdom components define the item."),
("3115","068"):("Martyrium Longini centurionis, BHG 989","MPG 115 cols. 32–44","2507","The centurion qualifier and Hesychius reference 2797.051 are preserved without merging."),
("3115","069"):("Commentarius in Lucam apostolum, BHG 991","MPG 115 cols. 1129–1140","2241","Reference to Vitae 5280 is contextual and does not merge holdings."),
("3115","070"):("Commentarius in Jacobum apostolum, BHG 764","MPG 115 cols. 200–217","3284","Reference to Andreas Cretensis 3005.025 is contextual and does not merge holdings."),
("3115","071"):("Passio Demetrii, BHG 498","MPG 116 cols. 1185–1201","3166","Reference to Vitae et Miracula 5057 is contextual and does not merge holdings.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
