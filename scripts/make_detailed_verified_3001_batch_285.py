import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_285.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3085","001"):("Oratio in nativitatem Deiparae","Jugie 1922 pp. 528–532","1208","This Nativity homily is distinct from the following Entrance homily."),
("3085","002"):("Oratio in ingressum Mariae","Jugie 1922 pp. 533–538","1629","This short Entrance homily is distinct from 3085.001."),
("3085","003"):("Testamentum / Τυπικὴ Διαθήκη","Tsiknopoullos 1969 pp. 71–104","9474","The link to Typica 5330 is contextual. The printed self-duplicate 'Dup. 3085 003' is retained as an unresolved Canon anomaly, not converted to another host.","DUPLICATE_SELF_REFERENCE_UNRESOLVED"),
("3085","004"):("Decem homiliae","Stephanes 1996 vol. 1 pp. 35–212","42503","The embedded NEOPHYTUS INCLUSUS heading artefact is not part of the title or edition.","NO_EXACT_OPEN_TEXT"),
("3085","005"):("Liber quinquaginta capitulorum","Sotiroudis 1996 vol. 1 pp. 241–374","34655","The fifty-chapter work must remain distinct from the ten homilies in the same volume.","NO_EXACT_OPEN_TEXT")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,val in ITEMS.items():
  label,locus,wc,note=val[:4];status=val[4]if len(val)==5 else"NO_EXACT_OPEN_TEXT";s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status=status,next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
