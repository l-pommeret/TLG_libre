import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_516.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
DATA = {
    ("4371", "001"): ("Tannery, Mémoires scientifiques 4 (1920), pp. 86–116", "4,283", "The mathematical treatise and its cross-reference from Planudes 4146.027 are preserved without merging the two canonical records."),
    ("4371", "002"): ("Tannery, Mémoires scientifiques 4 (1920), pp. 118–186", "11,043", "The epistle is kept separate from 4371.001 despite the shared editor and volume."),
    ("4373", "001"): ("Halkin, Sancti Pachomii vitae graecae (1932), pp. 1–96", "", "The Laurentian and Ambrosian witnesses and the partial duplicate relation to 4373.002 are preserved; no absent word count is invented."),
    ("4373", "002"): ("Halkin, Le corpus athénien de saint Pachome (1982), pp. 11–72", "25,411", "The Atheniensis 1015 recension collated with Ambrosianus D 69 Sup. remains distinct from the 1932 Vita prima."),
    ("4373", "003"): ("Halkin, Subsidia hagiographica 19 (1932), pp. 122–165", "", "The Paralipomena and both named manuscript witnesses are preserved; no absent word count is invented."),
}

canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for key, (locus, count, note) in DATA.items():
        source = canon[key]
        row = {field: "" for field in FIELDS}
        count_note = f" and the printed {count}-word count" if count else ""
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Exact local TLG, First1KGreek, Perseus, OPP, PTA and scan-register identifier lookup; {locus}{count_note} checked.", open_text_result=f"No exact licensed TEI matching {locus} was verified.", scan_result=f"No reusable page-image source matching {locus} is registered locally.", confidence="high" if count else "medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action=f"Locate page images for {locus}, sample the Greek in the exact item, then transfer only its pages without provider OCR.", notes=note + " No image or OCR used.", last_checked="2026-08-11")
        writer.writerow(row)
