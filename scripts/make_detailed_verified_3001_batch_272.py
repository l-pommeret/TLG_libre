import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_272.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3024","009"):("Professio religionis Christianorum","van Deun 1989 pp. 260–263","1180","The embedded STILPO/TIN line-break artefact in the notice does not alter the author or item."),
("3024","010"):("Praelocutio","Cresci 1987 pp. 42–67","4294","The exact Cresci edition is required."),
("3024","011"):("Monodiae","Criscuolo 1980–1981 pp. 90–92 and 96–97","510","Both discontinuous printed loci belong to this item and must be verified; intervening pages are not inferred."),
("3024","012"):("Versus sepulcrales","Hörandner–Diethart 2005 pp. 1–8","714","This epitaphic collection must remain distinct from the following poem in the same edition."),
("3024","013"):("Carmen de incendio","Hörandner–Diethart 2005 pp. 8–51","6639","Shared p. 8 with 3024.012 requires exact visual item separation.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(title,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {title} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
