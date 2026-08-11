import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_271.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3002","016"):("De comoedia","Koster 1975 p. 50","55","Page 50 is shared with 3002.015; the same generic title used elsewhere cannot establish identity."),
("3002","018"):("Ἐκ τοῦ Ἡφαιστίωνος ἐπιτομὴ τῶν ἐννέα μέτρων","Koster 1975 pp. 51–55","642","The missing 3002.017 number is not filled or inferred."),
("3002","019"):("Tractatus Coislinianus","Janko 1984 pp. 22–40","416","The possible status as an epitome of Aristotle Poetics II is preserved as uncertainty, not asserted authorship."),
("3024","007"):("Διδασκαλία τρίτη (excerptum)","Criscuolo 1980–1981 pp. 83–85","625","Only the stated excerpt of the third didascalia is the canonical item."),
("3024","008"):("Epistulae II","Criscuolo 1983 pp. 14–18","597","The item comprises exactly the two letters of Criscuolo's edition; no neighbouring Stilbes text is included.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(title,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item boundary checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title}, {locus}, was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
