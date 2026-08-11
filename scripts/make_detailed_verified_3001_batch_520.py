import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_520.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA = {
    ("4384", "004"): ("Weinstock, CCAG 5.4 (1940), pp. 169–170", "", "Chapter X and Pal. Vat. 312 fol. 90v are preserved as an item separate from chapter IX."),
    ("4384", "005"): ("Mavroudi 2002, pp. 432–435", "", "All six fragments and their distinct Paris/Vatican folios and page allocations are preserved; no global count is invented."),
    ("4385", "001"): ("Olivieri, CCAG 4 (1903), pp. 118–119", "91", "The astronomical excerpt and Mutinensis 85 fol. 94 are preserved."),
    ("4385", "002"): ("Bassi–Martini, CCAG 4 (1903), pp. 139–142", "", "The supplied Persian-philosopher title and Neapolitanus II C 33 fol. 393 are preserved."),
    ("4385", "003"): ("Bassi–Martini, CCAG 4 (1903), pp. 145–146", "357", "The exact title and Neapolitanus II C 33 fol. 398 are preserved."),
}

canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for key, (locus, count, note) in DATA.items():
        source = canon[key]
        row = {field: "" for field in FIELDS}
        count_note = f" and the printed {count}-word count" if count else ""
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Exact local TLG, astrological corpus, First1KGreek, Perseus, OPP, PTA and scan-register lookup; {locus}{count_note} checked.", open_text_result=f"No exact licensed TEI matching {locus} was verified.", scan_result=f"No reusable page-image source matching {locus} is registered locally.", confidence="high" if count else "medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action=f"Locate page images for {locus}, sample the Greek in the exact item, then transfer only its pages without provider OCR.", notes=note + " No image or OCR used.", last_checked="2026-08-11")
        writer.writerow(row)
