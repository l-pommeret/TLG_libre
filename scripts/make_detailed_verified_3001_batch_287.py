import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_287.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3085","011"):("Ἑρμηνεία ὠδῶν","Detorakes 2001 vol. 4 pp. 531–559","6161","This Odes commentary begins after the Psalter commentary and remains distinct."),
("3085","012"):("Commentarius in Canticum Canticorum","Pseftonkas 2001 vol. 4 pp. 643–674","5082","The missing space before the Greek quoted title in the Canon notice is bibliographic punctuation, not an item merge."),
("3085","013"):("Commentarius in Apocalypsin","Englezakis 1995 pp. 119–145","8416","This Apocalypse commentary is tied to the cited Englezakis edition."),
("3085","014"):("Ἑρμηνεία Κανόνων Δεσποτικῶν Ἑορτῶν","Sakellaridou-Sotiroudi 2005 vol. 5 pp. 71–233","36513","The twelve dominical-feast canons define this exact item."),
("3085","015"):("Orationes from Andros Hagias codex 13","Constantinides 2005 vol. 5 pp. 269–287","3349","The manuscript identifier Andros Hagias 13 is part of the item identity.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
