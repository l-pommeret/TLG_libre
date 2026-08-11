import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_284.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3083","005"):("Vita Cosmae Melodi et Joannis Damasceni","Papadopoulos-Kerameus 1897 pp. 271–302","9100","The [Dub.] attribution marker is preserved; the 1963 reprint does not define a different text item.","NO_EXACT_OPEN_TEXT"),
("3083","006"):("Laudatio sancti Mocii","Delehaye 1912 pp. 176–187","3666","The reference to Vitae 5083 is contextual and does not merge this holding.","NO_EXACT_OPEN_TEXT"),
("3083","007"):("Encomium martyrum XLII Amoriensum, Versio Γ","Vasilievskij–Nikitin 1906 pp. 22–36","5552","Version Gamma is part of the exact item identity.","NO_EXACT_OPEN_TEXT"),
("3083","008"):("Encomium Isacii et Dalmati, BHG 956d","Hatlie 2003 pp. 277–293","5648","Both saints and BHG 956d define the exact encomium.","NO_EXACT_OPEN_TEXT"),
("3083","009"):("Laudatio Dionysii Areopagitae, BHG 556","Podolak 2015 pp. 223–258","10669","The duplicate link to 3083.002 is preserved, but the Podolak edition is a distinct acquisition target.","DUPLICATE_DISTINCT_EDITION_NO_TEXT")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note,status) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status=status,next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
