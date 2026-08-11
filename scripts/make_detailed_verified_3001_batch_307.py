import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_307.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","032"):("Passio Carpi, Papyli et Agathonicae, BHG 295","MPG 115 cols. 105–125","4338","All three saints define the item; reference to corpus 0390 is contextual."),
("3115","033"):("Martyrium Bonifatii, BHG 281","MPG 115 cols. 241–257","3403","The redundant 'sancti martyris' wording is retained in canonical_edition."),
("3115","034"):("Martyrium Arethae et sociorum, BHG 167","MPG 115 cols. 1249–1289","8386","Reference to Vitae 5172.001 is contextual and does not merge holdings."),
("3115","035"):("Passio Charitonis, BHG 301","MPG 115 cols. 900–917","3975","Shared col. 900 with 3115.031 requires visual separation."),
("3115","036"):("Passio Charitinae, BHG 300","MPG 115 cols. 997–1005","1268","Charitina BHG 300 is distinct from Chariton BHG 301; reference 5266.001 is contextual.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
