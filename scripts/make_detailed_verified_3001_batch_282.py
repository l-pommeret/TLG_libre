import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_282.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3076","002"):("Commentarius in I Peter 1.1–23","van Deun 2017 pp. 394–415","5725","The canonical item is limited to chapter 1 verses 1–23, not the complete First Peter commentary."),
("3076","003"):("Laudatio Michaelis et Gabrielis, BHG 1292","Gielen–van Deun 2015 pp. 657–663","2161","The reference to the collective miracles corpus 5208 is contextual and does not merge holdings."),
("3078","001"):("Oratio aditialis","Browning 1961 pp. 187–203","6096","The inaugural lecture and hypatos-philosophon context define the exact item."),
("3078","002"):("Epistula ad Alexandrum III papam","Hofmann 1953 pp. 77–80","983","The recipient Alexander III is part of the exact letter identity."),
("3078","003"):("Praxis synodalis de matrimoniis","Schminck 1977 pp. 237–240","910","References to 3331.002 and 3355.001 are parallels; this 3078.003 holding remains distinct.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
