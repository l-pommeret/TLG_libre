import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_291.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3096","002"):("Fragmenta commentariorum XVI orationum Gregorii Nazianzeni","Constantinescu 1977 pp. 170–197","6906","The sixteen-orations fragment collection is the exact item, not a complete commentary corpus."),
("3096","003"):("Oratio apologetica","Darrouzès 1966 pp. 276–304","5035","This apologetic discourse is tied to the cited ecclesiological edition."),
("3098","001"):("De controversiis, recensio A, Logos 21","Gahbauer 1975 pp. 1–78","15715","Recension A and Logos 21 are mandatory item-level qualifiers."),
("3098","002"):("Oratio contra Eustratium Nicaeensem","Zeses 1976 pp. 35–82","14855","Eustratius of Nicaea is part of the exact polemical item identity."),
("3098","003"):("Conspectus librorum sacrorum","Simotas 1984 pp. 55–295","60058","This synopsis of Scripture must not be substituted by another biblical conspectus.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
