import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_295.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3101","002"):("Oratio ad Alexium I de processione Spiritus Sancti","Zeses 1978 pp. 307–329","8269","Alexios I and the procession subject are mandatory item qualifiers."),
("3101","003"):("Sermo ad Nicolaum III","Darrouzès 1988 pp. 17–53","7150","The patriarch Nicholas III is the exact addressee/honorand."),
("3102","001"):("Vita Sabae Junioris","Cozza-Luzi 1893 pp. 5–70","12903","This Sabas life is distinct from the following Christopher and Macarius life in the same edition."),
("3102","002"):("Vita Christophori et Macarii","Cozza-Luzi 1893 pp. 71–96","4724","Both Christopher and Macarius define the exact item."),
("3104","001"):("Refutatio institutionis theologicae Procli","Angelou 1984 pp. 1–174","55475","The split form 'Ref utatio' is retained in canonical_edition but treated as a spacing artefact for matching.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
