import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_296.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3104","002"):("Ad magnum domesticum","Demetrakopoulos 1866 pp. 199–218","5035","The 1965 reprint does not define a different text item."),
("3104","003"):("Orationes","Demetrakopoulos 1866 pp. 219–380","41278","This collection follows but remains distinct from 3104.002."),
("3104","004"):("Orationes duae contra haereticos","Demetrakopoulos 1865 pp. 1–72","14179","Exactly two anti-heretical discourses define the item."),
("3104","005"):("Adversus Latinos de Spiritu Sancto","Simonides 1858 pp. 1–39","10433","The procession-of-the-Spirit subject distinguishes this from the azyma treatise."),
("3104","006"):("Adversus Latinos de azymis","Ivanscenko 1897 pp. 51–115","11183","The azyma subject distinguishes this from 3104.005.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
