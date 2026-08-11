import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_304.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","017"):("Passio Sebastiani et sociorum, BHG 1620","Lequeux 2005 pp. 255–287","3946","The target is the BHG 1620 abridgement, not the BHG 1619z full passion discussed in the same article; reference 5219.001 is contextual."),
("3115","018"):("Vita Abramii confessoris, BHG 8","MPG 115 cols. 44–77","7457","BHG 8 and the exact MPG span define this life."),
("3115","019"):("Passio Acepsimae, Iosephi et Aeithalae, BHG 19","Delehaye 1905 pp. 546–557 / MPG 116 cols. 832–860","5965","The stated MPG textual equivalence is preserved as an alternate printing, not a separate work."),
("3115","020"):("Vita Acindyni, Pegasii, Anempodisti, Aphthonii et Elpidephori, BHG 23","MPG 116 cols. 9–36","5347","All five saints are mandatory item identifiers."),
("3115","021"):("Passio Aecaterinae, BHG 32","MPG 116 cols. 276–301","5352","Shared col. 301 with the following Barbara passion requires visual separation.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
