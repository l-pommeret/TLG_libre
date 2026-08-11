import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_290.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3091","007"):("Tactica chapters 56–65","McGeer 1995 pp. 88–163","12636","Chapters 63–65 overlap the chapter range in 3091.001; this explicit overlap is preserved without collapsing the distinct edition/item record."),
("3093","001"):("Confutatio falsi libri Mohamedis","Förstel 2000 pp. 2–198","35934","The split form 'Conf utatio' is retained in canonical_edition but treated as a spacing artefact for matching."),
("3093","002"):("Capita syllogistica XXIV","Hergenroether 1869 pp. 84–138","11912","All twenty-four chapters on the procession of the Holy Spirit define the item."),
("3093","003"):("Refutatio epistulae principis Armeniae","MPG 105 cols. 588–665","18219","The split form 'Ref utatio' is retained in canonical_edition but treated as a spacing artefact for matching."),
("3096","001"):("Scholia in Lucam from Athos Iviron 371","Krikones 1973 pp. 67–519","unstated","The catena manuscript identifier is mandatory; no word count is supplied or inferred.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];wcdesc=(f"{wc}-word"if wc!="unstated"else"word-count-unstated");r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wcdesc} {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
