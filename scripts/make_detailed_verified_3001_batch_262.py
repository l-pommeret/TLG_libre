import csv

START = ("1802", "002")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_262.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()

DETAILS = {
    ("1802", "002"): dict(
        sources_tested="Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; Bernabé 1987 item and p. 64 requirement checked; local scan register checked.",
        open_text_result="No exact licensed TEI for Bernabé 1987 p. 64 was found. The local First1KGreek tlg1802 holding is tlg001, not this tlg002 item.",
        scan_result="No reusable page image of Bernabé 1987 p. 64 is registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT",
        next_action="Locate a rights-cleared image of Bernabé 1987 p. 64, then transcribe or OCR only that verified item.",
        notes="Item-level negative result; no identifier-neighbour substitution, image acquisition, or OCR used."),
    ("0012", "001"): dict(
        sources_tested="Exact local TLG/Perseus identifier and TEI metadata inspection; Allen 1931 canonical edition compared with Perseus grc2 (Monro–Allen 1908–1920); local scan register checked.",
        open_text_result="Perseus grc2 is the same work but not the canonical Allen 1931 edition; it is rejected as an exact item-level match.",
        scan_result="No reusable page-image source for Allen 1931 vols. 2–3 is registered locally.", confidence="high", proposed_status="TEXT_FOUND_EDITION_MISMATCH",
        next_action="Locate an exact licensed Allen 1931 TEI or rights-cleared scans of vols. 2–3; retain Perseus only as a noncanonical witness.",
        notes="TEI file exists locally and passes structural checks, but its edition statement prevents canonical promotion; no image or OCR used."),
    ("0012", "002"): dict(
        sources_tested="Exact local TLG/Perseus identifier and TEI metadata inspection; von der Mühll 1962 canonical edition compared with Perseus grc2 (Murray 1919); local scan register checked.",
        open_text_result="Perseus grc2 is the same work but not the canonical von der Mühll 1962 edition; it is rejected as an exact item-level match.",
        scan_result="No reusable page-image source for von der Mühll 1962 pp. 1–456 is registered locally.", confidence="high", proposed_status="TEXT_FOUND_EDITION_MISMATCH",
        next_action="Locate an exact licensed von der Mühll 1962 TEI or rights-cleared scan; retain Perseus only as a noncanonical witness.",
        notes="TEI file exists locally and passes structural checks, but its edition statement prevents canonical promotion; no image or OCR used."),
    ("0012", "003"): dict(
        sources_tested="Exact local TLG/Perseus identifier and TEI metadata inspection; Canon loci AG 7.153 and 14.147 compared with Perseus grc1 (Evelyn-White 1914 Homeric epigrams); cross-reference to 2123.001 retained; local scan register checked.",
        open_text_result="Perseus grc1 shares the TLG work identifier but its edition/content description does not establish the two canonical AG items; it is rejected as an exact item-level match.",
        scan_result="No separately verified reusable images for the two stated AG loci are registered locally.", confidence="high", proposed_status="TEXT_FOUND_ITEM_MISMATCH",
        next_action="Verify AG 7.153 and 14.147 in a licensed Anthologia Graeca TEI or rights-cleared edition; keep AG 10.32 attached to host 2123.001.",
        notes="The Palladas sentence is a cross-reference, not a third Homeric acquisition item; no image or OCR used."),
    ("0012", "004"): dict(
        sources_tested="Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; West 1998/2000 edition statement checked; Canon duplicate marker Dup. 0012.001 preserved; local scan register checked.",
        open_text_result="No exact licensed TEI of West's 1998/2000 Ilias was found. The available Perseus tlg0012.tlg001 file is Monro–Allen 1908–1920 and cannot satisfy this duplicate edition record.",
        scan_result="No reusable page-image source for West 1998/2000 vols. 1–2 is registered locally.", confidence="high", proposed_status="DUPLICATE_DISTINCT_EDITION_NO_TEXT",
        next_action="Preserve the duplicate link to 0012.001 while seeking the exact West 1998/2000 edition; do not collapse the two edition records.",
        notes="Duplicate work, distinct canonical edition; no image acquisition or OCR used."),
}

coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
start = next(i for i, row in enumerate(coverage) if (row["tlg_author_id"], row["tlg_work_id"]) == START)
items = coverage[start:start + 5]
assert [(r["tlg_author_id"], r["tlg_work_id"]) for r in items] == list(DETAILS)
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for item in items:
        key = (item["tlg_author_id"], item["tlg_work_id"])
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=item["author_heading"],
                   work_title=item["work_title"], canonical_edition=item["bibliographic_notice"],
                   open_text_url="", open_text_license="", scan_url="", scan_rights="", last_checked="2026-08-11")
        row.update(DETAILS[key])
        writer.writerow(row)
