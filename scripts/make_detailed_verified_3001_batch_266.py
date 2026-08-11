import csv

START=("0742","003"); OUTPUT="data/research_batches/detailed_verified_3001_batch_266.csv"
FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("0742","003"):("Heitsch 1963 2nd edn., pp. 164–165","Carminis de mundi creatione exordium","the 47-word creation-poem opening","The shared p. 164 boundary with 0742.002 requires visual item separation."),
("0742","004"):("Heitsch 1963 2nd edn., p. 165","Hymnus in Jovem","the 28-word Hymnus in Jovem","Page 165 also contains neighbouring items; title and word-count boundaries must be checked."),
("0742","005"):("Heitsch 1963 2nd edn., pp. 165–166","Hymnus in Isim, PSI 7.844","the PSI 7.844 Isis hymn","The papyrus identifier PSI 7.844 is part of the exact item identity."),
("0742","006"):("Heitsch 1963 2nd edn., p. 166","Hymnus in Sarapidem, P. Schubart 12","the P. Schubart 12 Sarapis hymn","The papyrus identifier P. Schubart 12 is part of the exact item identity."),
("0742","007"):("Heitsch 1963 2nd edn., pp. 167–168","Aretalogia Sarapidis, P. Berol. 10525","the P. Berol. 10525 Sarapis aretalogy","The papyrus identifier P. Berol. 10525 is part of the exact item identity.")}
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))); i=next(i for i,r in enumerate(coverage) if (r["tlg_author_id"],r["tlg_work_id"])==START); rows=coverage[i:i+5]
assert [(r["tlg_author_id"],r["tlg_work_id"]) for r in rows]==list(ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8") as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for s in rows:
  k=(s["tlg_author_id"],s["tlg_work_id"]); ed,title,target,boundary=ITEMS[k]; r={f:"" for f in FIELDS}; r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {ed} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {target} in the specified Heitsch edition was found.",scan_result=f"No reusable page image verified for {ed} is registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {ed.split(', ',1)[1]} and verify {title} before transcription or OCR.",notes=boundary+" No image acquisition or OCR used.",last_checked="2026-08-11");w.writerow(r)
