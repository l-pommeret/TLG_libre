import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_521.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA = {
    ("4386", "001"): ("Bassi–Martini, CCAG 4 (1903), pp. 156–158", "936", "Neapolitanus II C 33 fol. 443v and both astrological and epistolary genres are preserved."),
    ("4386", "002"): ("Caudano, Byzantion 81 (2011), even pp. 52–72", "3,536", "The even-page restriction and Oxon. Selden supra 17 fols. 170–177 are preserved."),
    ("4387", "001"): ("Cumont, CCAG 2 (1900), pp. 181–186", "1,640", "Marcianus 335 fol. 25 and both astrological and astronomical classifications are preserved."),
    ("4389", "001"): ("Olivieri, CCAG 2 (1900), p. 213", "245", "The Greek title and Marcianus 335 fol. 193v are preserved."),
    ("4393", "001"): ("Müller, FHG 4 (1851), pp. 178–180", "1,208", "The Malalas fragment on pp. 178–179 and Photius fragment on pp. 179–180 remain separately bounded within the canonical aggregate."),
}

canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for key, (locus, count, note) in DATA.items():
        source = canon[key]
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Exact local TLG, historical/astrological corpus, First1KGreek, Perseus, OPP, PTA and scan-register lookup; {locus} and the printed {count}-word count checked.", open_text_result=f"No exact licensed TEI matching {locus} was verified.", scan_result=f"No reusable page-image source matching {locus} is registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT", next_action=f"Locate page images for {locus}, sample the Greek in the exact item, then transfer only its pages without provider OCR.", notes=note + " No image or OCR used.", last_checked="2026-08-11")
        writer.writerow(row)
