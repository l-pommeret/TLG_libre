import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_294.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3099","009"):("Practicorum capitum centuriae tres","MPG 120 cols. 852–1009","33081","This explicitly word-counted practical-centuriae item shares the printed MPG span with 3099.004; the apparent overlap is preserved and not silently collapsed."),
("3100","001"):("Epistulae","Jenkins–Westerink 1973 pp. 2–520","84437","The complete letters edition and its exact CFHB volume define the item."),
("3100","002"):("Opuscula diversa","Westerink 1981 pp. 2–138","12998","The embedded NICOLAUS V Papa heading artefact is excluded from author, title, and edition."),
("3100","003"):("Parergon liturgicum de oblatione","Mai–Cozza-Luzi 1905 vol. 10.2 pp. 111–112","209","This 209-word priestly-oblation instruction is a distinct short item."),
("3101","001"):("Versus de abdicatione","Doanidou 1934 pp. 110–141","5714","The abdication from the archbishopric of Cyprus defines the poem's identity.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
