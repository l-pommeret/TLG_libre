import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_280.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3057","002"):("Martyrium sancti Eugenii","Lampsides 1984 pp. 19–43","6656","This martyrdom is distinct from the miracle collection 3057.001."),
("3057","003"):("Oratio in tertiam jejuniorum hebdomadem","MPG 120 cols. 1260–1288","6206","BHG 428 and the cross-adoration subject are part of the exact item identity."),
("3057","004"):("Prologus ad homiliam XXXII","Halkin 1971 pp. 286–288","513","Only the prologue, not homily XXXII as a whole, is the canonical item."),
("3063","001"):("Synopsis historiarum","Thurn 1973 pp. 3–500","123789","The trailing Georgius Scylitzes heading in the extracted notice is not part of this item."),
("3064","001"):("Continuatio Scylitzae","Bekker 1839 vol. 2 pp. 641–744","unstated","The Canon supplies no word count; this Bekker edition record remains distinct from 3064.002.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];wcdesc=(f"{wc}-word"if wc!="unstated"else"word-count-unstated");r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wcdesc} {label} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
