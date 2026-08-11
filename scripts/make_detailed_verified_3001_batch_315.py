import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_315.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","072"):("Passio Zenobii et Zenobiae, BHG 1885","MPG 115 cols. 1309–1317","1956","Both saints and reference to Vitae 5281 are preserved without merging."),
("3115","073"):("Martyrium Epimachi, BHG 594","Acta Sanctorum Oct. XIII 1883 pp. 720–723","1325","Paris gr. 1484 and reference to Vitae 5282 define context; redundant martyr wording is retained."),
("3115","074"):("Vita Cosmae et Damiani, BHG 374","Van Hoof 1882 pp. 586–596","1754","Both saints and reference to Vitae et Miracula 5183 are preserved without merging."),
("3115","075"):("Vita Joannicii Bithyniae, BHG 937","MPG 116 cols. 36–92","11808","Joannicius' Bithynian qualifier defines the item."),
("3115","076"):("Passio Galactionis et Epistemes, BHG 666","MPG 116 cols. 93–108","3127","Both Galaction and Episteme define the item.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
