import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_517.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA = {
    ("4373", "004"): ("Halkin, Le corpus athénien de saint Pachome (1982), pp. 73–93", "9,460", "This Athenian Paralipomena/Ascetica recension remains separate from 4373.003."),
    ("4373", "005"): ("Halkin, Subsidia hagiographica 19 (1932), pp. 166–271", "23,621", "All Vatican, Parisian, and additional witnesses stated by the Canon are retained."),
    ("4373", "006"): ("Halkin, Subsidia hagiographica 19 (1932), pp. 272–406", "27,984", "The Patmos monastery witness is retained at item level."),
    ("4373", "007"): ("Halkin, Subsidia hagiographica 19 (1932), pp. 407–456", "14,595", "The Munich and Athos Lavra witnesses are retained at item level."),
    ("4373", "009"): ("Halkin, Analecta Bollandiana 97 (1979), pp. 6–55 and 241–287", "16,736", "Both discontinuous article spans, Ath. BN 2560, and BHG 1401a are preserved without filling the gap."),
}

canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for key, (locus, count, note) in DATA.items():
        source = canon[key]
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Exact local TLG, First1KGreek, Perseus, OPP, PTA and scan-register identifier lookup; {locus} and the printed {count}-word count checked.", open_text_result=f"No exact licensed TEI matching {locus} was verified.", scan_result=f"No reusable page-image source matching {locus} is registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT", next_action=f"Locate page images for {locus}, sample the Greek in the exact item, then transfer only its pages without provider OCR.", notes=note + " No image or OCR used.", last_checked="2026-08-11")
        writer.writerow(row)
