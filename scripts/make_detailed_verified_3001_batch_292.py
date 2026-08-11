import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_292.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3098","004"):("De controversiis, recensio PG","Gahbauer 1975 pp. 1–21","1431","Recension PG is distinct from recension A at 3098.001 and recension I at 3098.005."),
("3098","005"):("De controversiis, recensio I","Gahbauer 1975 pp. 52–75","2151","Recension I is distinct from recension A and recension PG despite the shared work title."),
("3099","001"):("Vita Simeonis Novi Theologici","Hausherr 1928 pp. 1–230","34763","The life of Symeon the New Theologian is the exact hagiographic item."),
("3099","002"):("Epistulae","Darrouzès 1961 pp. 228, 234–244 and 246–290","6488","All three discontinuous loci are explicit; intervening pages are excluded."),
("3099","003"):("Orationes","Darrouzès 1961 pp. 56–226 and 292–514","41594","Both discontinuous speech spans are explicit; the intervening letter section is excluded.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
