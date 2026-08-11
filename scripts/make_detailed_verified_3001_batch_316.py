import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_316.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","077"):("Vita Pauli confessoris, BHG 1473","MPG 116 cols. 884–896","2295","Shared col. 896 with 3115.066 requires visual separation."),
("3115","078"):("Passio Hieronis et sociorum, BHG 750","Acta Sanctorum Nov. III 1910 pp. 335–338","2071","Reference to Vitae 5283 is contextual and does not merge holdings."),
("3115","079"):("Vita Matronae Pergensis, BHG 1222","Acta Sanctorum Nov. III 1910 pp. 813–822","6887","Matrona's Pergensis qualifier defines the item."),
("3115","080"):("Vita altera Theoctistae Lesbiae, BHG 1725","Acta Sanctorum Nov. IV 1925 pp. 224–225","206","The alternate-life and Lesbian qualifiers define this short item; embedded heading artefact is excluded and reference 3201.002 remains contextual."),
("3115","081"):("Passio Menae, BHG 1250","Van Hoof 1884 pp. 258–270","2196","Reference to Miracula 5152 is contextual and does not merge holdings.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
