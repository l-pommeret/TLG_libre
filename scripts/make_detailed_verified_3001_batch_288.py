import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_288.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3085","016"):("Περὶ τῆς Ἱεραρχίας Χριστοῦ","Papatriantafyllou-Theodoridi 2005 vol. 5 pp. 305–312","1404","This short hierarchy homily has its own exact boundary."),
("3085","017"):("Oratio in Spiritum Sanctum et Pentecosten","Katsaros 2005 vol. 5 pp. 321–335","3214","The edition title includes a responsory-letter excerpt with the Pentecost discourse; that printed item boundary is retained."),
("3085","018"):("Τὸ Βιβλίον τῆς Θεοσημείας","Sophianos 2005 vol. 5 pp. 355–387","6748","The embedded NEOPTOLEMUS heading artefact is excluded from author, title, and edition."),
("3085","019"):("Epistulae","Karpozilos 2005 vol. 5 pp. 405–470","6375","The collection boundary is the exact Karpozilos page span."),
("3091","001"):("Tactica chapters 63–74","de Foucault 1973 pp. 287–311","5015","Only the twelve explicit chapters 63–74 are included; the rest of the Tactica is excluded.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
