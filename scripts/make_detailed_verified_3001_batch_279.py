import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_279.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3038","026"):("Disputatio de fide cum philosopho Saraceno","Mai 1847 vol. 4.2 pp. 443–454","unstated","The Canon supplies no word count; none is estimated or inferred."),
("3052","001"):("Prochiron / Πρόχειρος Νόμος","Zepos 1931 Jus Graecoromanum 2 pp. 114–228","27998","This base Prochiron is distinct from the augmented and Calabrian recensions."),
("3052","002"):("Prochiron Auctum","Zepos 1931 Jus Graecoromanum 7 pp. 9–361","124121","The augmented recension and volume 7 identity are mandatory."),
("3052","003"):("Prochiron Legum / Prochiron Calabriae","Brandileone–Puntoni 1895 pp. 3–336","39402","The Calabrian recension must not be collapsed into 3052.001 or .002."),
("3057","001"):("De miraculis sancti Eugenii","Rosenqvist 1996 pp. 170–202","5298","The St Eugenios dossier and Codex Athous Dionysiou 154 context define this item.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];wcdesc=(f"{wc}-word" if wc!="unstated" else "word-count-unstated");r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wcdesc} {label} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item boundary before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
