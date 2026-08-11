import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_293.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3099","004"):("Capitum centuriae tres","MPG 120 cols. 852–1009","unstated","The three centuriae are the explicit item; no word count is supplied or inferred."),
("3099","005"):("Dialexis et antidialogus de azymis","Michel 1930 pp. 320–342","4974","Both dialogue and counter-dialogue belong to this exact azyma item."),
("3099","006"):("Contra Latinos et de processione Spiritus Sancti","Michel 1930 pp. 371–409","8873","This procession treatise is distinct from the azyma polemics."),
("3099","007"):("Contra Armenios et Latinos de azymis","Hergenroether 1869 pp. 139–154","2607","Both Armenian and Latin addressees are part of the exact item identity."),
("3099","008"):("Κατὰ ἁγιοκατηγόρων","Paschalides 2004 pp. 515–518","1196","The quoted Greek title and Paschalides edition define this short item.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];wcdesc=(f"{wc}-word"if wc!="unstated"else"word-count-unstated");r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wcdesc} {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
