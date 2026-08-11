import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_519.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA = {
    ("4381", "003"): ("Boll–Cumont, CCAG 5.1 (1904), pp. 227–228", "", "Angelicanus 29 fol. 226 and the exact two-page boundary are retained."),
    ("4381", "004"): ("Olivieri, CCAG 2 (1900), pp. 132–136", "1,703", "The fragment embedded in Achmet's introduction, Marc. 324 fol. 267v, and the cross-reference to 4384.002 are preserved without merging."),
    ("4384", "001"): ("Drexl, Achmetis Oneirocriticon (1925), pp. 1–241", "57,884", "The complete Oneirocriticon is kept distinct from the astrological introduction notices."),
    ("4384", "002"): ("Kroll–Olivieri, CCAG 2 (1900), pp. 122–132 and 136–138", "4,299", "Both discontinuous spans, Marc. 324 fol. 202, and the Eleutherius cross-reference are preserved."),
    ("4384", "003"): ("Kroll–Olivieri, CCAG 2 (1900), pp. 153–157", "1,228", "Chapter IX and Marc. 334 fol. 116 remain an item distinct from the selected prooemium and chapters in 4384.002."),
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
