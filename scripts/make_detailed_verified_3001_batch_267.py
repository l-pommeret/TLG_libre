import csv

START=("0742","008"); OUTPUT="data/research_batches/detailed_verified_3001_batch_267.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("0742","008"):("Heitsch 1963 2nd edn., p. 168","Hymnus in Apollinem","the 46-word Apollo hymn","Page 168 is shared with the preceding 0742.007 item; visual separation is required."),
("0742","009"):("Heitsch 1963 2nd edn., pp. 169–170","Paean in Apollinem, P. Berol. 6870v","the P. Berol. 6870 verso paean","The verso designation is part of the exact papyrus item identity."),
("0742","010"):("Heitsch 1963 2nd edn., p. 171","Hymnus in Asclepium","the 65-word Asclepius hymn","Page 171 is shared with 0742.011; visual item separation is required."),
("0742","011"):("Heitsch 1963 2nd edn., p. 171","Hymnus in Hecatam","the 49-word Hecate hymn","Page 171 is shared with 0742.010; visual item separation is required."),
("0742","012"):("Heitsch 1963 2nd edn., p. 172","Hymnus in Fortunam, P. Berol. Mus. 9734v","the P. Berol. Mus. 9734 verso hymn","The partial duplicate link to 0230.001 fragment 34 must be preserved, not collapsed.")}
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))); i=next(i for i,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START); rows=coverage[i:i+5]
assert [(r["tlg_author_id"],r["tlg_work_id"]) for r in rows]==list(ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8") as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for s in rows:
  k=(s["tlg_author_id"],s["tlg_work_id"]); ed,title,target,boundary=ITEMS[k]; r={f:"" for f in FIELDS}; status="PARTIAL_DUPLICATE_NO_EXACT_TEXT" if k==("0742","012") else "NO_EXACT_OPEN_TEXT"; action=("Locate rights-cleared images of p. 172, verify the hymn, and compare only the stated overlap with 0230.001 fragment 34." if k==("0742","012") else f"Locate rights-cleared images of {ed.split(', ',1)[1]} and verify {title} before transcription or OCR.");r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {ed} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {target} in the specified Heitsch edition was found.",scan_result=f"No reusable page image verified for {ed} is registered locally.",confidence="high",proposed_status=status,next_action=action,notes=boundary+" No image acquisition or OCR used.",last_checked="2026-08-11");w.writerow(r)
