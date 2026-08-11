import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_518.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA = {
    ("4373", "010"): ("Halkin, Analecta Bollandiana 96 (1978), pp. 368–381", "3,746", "The abbreviated imperial-menologion Vita, Patm. 736, and BHG 1401b are kept separate from the longer Pachomian vitae."),
    ("4377", "001"): ("Cumont, CCAG 8.4 (1921), pp. 108–114", "", "Fragment status, Paris gr. 2219 fol. 20, and the combined astrological/natural-history classification are preserved; no absent count is invented."),
    ("4380", "001"): ("Boll, CCAG 7 (1908), pp. 188–191", "", "The address to Philip and Berlin phil. 1577 fol. 117 are preserved; no absent count is invented."),
    ("4381", "001"): ("Boll–Cumont, CCAG 5.1 (1904), p. 227", "", "Angelicanus 29 fol. 176v and the short item boundary are preserved."),
    ("4381", "002"): ("Boll–Cumont, CCAG 5.1 (1904), p. 227", "", "This second item on the same printed page and manuscript folio remains a distinct canonical notice."),
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
