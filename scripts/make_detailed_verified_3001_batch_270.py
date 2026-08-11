import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_270.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3002","011"):("De partibus comoediae","Koster 1975 p. 21","47","Page 21 contains several short prolegomena; exact boundaries are mandatory."),
("3002","012"):("De metro comico","Koster 1975 p. 22","75","This item begins after the cluster on p. 21 and must remain distinct from the Tzetzes cross-reference spanning pp. 22–38."),
("3002","013"):("De comoedia (Anonymus Crameri i)","Koster 1975 pp. 39–42","862","The Anonymus Crameri i label is part of the exact item identity."),
("3002","014"):("De comoedia (Anonymus Crameri ii)","Koster 1975 pp. 43–48","1360","The trailing PROMATHIDAS heading in the extracted notice is not part of this item."),
("3002","015"):("De poeticae generibus (fort. auctore Joanne Tzetza)","Koster 1975 p. 50","89","The uncertain Tzetzes attribution is preserved; p. 50 is shared with 3002.016.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(title,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item boundary checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title}, {locus}, was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
