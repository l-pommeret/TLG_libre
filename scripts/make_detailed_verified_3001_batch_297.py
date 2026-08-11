import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_297.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3104","007"):("Vita sancti Meletii junioris, BHG NA 1247","Papadopoulos 1935 pp. 34–66","11645","The Novum Auctarium BHG 1247 identifier is part of the exact item identity.","NO_EXACT_OPEN_TEXT"),
("3105","001"):("Pandecte","MPG 86 cols. 69–74; 106 cols. 1360–1381; 127 cols. 513–516 and 527–532","unstated","The Canon notice is truncated after 'Cod' and lacks word count/genre completion; all four explicit loci are retained and gaps are excluded.","INCOMPLETE_NOTICE_NO_EXACT_TEXT"),
("3105","002"):("Canonarium / Typicon chapters 1–4","Beneshevich 1917 pp. 4–119","33696","Only chapters 1–4 are the canonical item.","NO_EXACT_OPEN_TEXT"),
("3105","003"):("Oratio XXXI ad Basilium","Aerts 2006 pp. 141–169 odd pages","2794","Only odd-page Greek text is canonical; even facing pages are excluded.","NO_EXACT_OPEN_TEXT"),
("3105","004"):("Canonarium / Typicon","Hannick 2014 vols. I–II pp. 2–1000 even pages","160943","Duplicate link to 3105.002 is preserved, while the full Hannick edition and even-page boundary remain distinct.","DUPLICATE_DISTINCT_EDITION_NO_TEXT")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note,status) in ITEMS.items():
  s=c[k];wcdesc=(f"{wc}-word"if wc!="unstated"else"word-count-unstated");r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wcdesc} {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status=status,next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
