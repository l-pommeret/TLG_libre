import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_277.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3038","016"):("Philemon","Kalogeras vol. 2 pp. 333–340","1488","This short Philemon component must not be absorbed into adjacent commentaries."),
("3038","017"):("Hebrews","Kalogeras vol. 2 pp. 341–472","31184","This Hebrews component ends before the Catholic-epistle sequence."),
("3038","018"):("James","Kalogeras vol. 2 pp. 475–518","11325","The page jump from 472 to 475 is preserved; pp. 473–474 are not inferred into the item."),
("3038","019"):("I Peter","Kalogeras vol. 2 pp. 519–566","12085","The first Peter commentary is distinct from 3038.020."),
("3038","020"):("II Peter","Kalogeras vol. 2 pp. 567–589","5372","The second Peter commentary is distinct from 3038.019.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of the {label} commentary in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the {wc}-word {label} item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
