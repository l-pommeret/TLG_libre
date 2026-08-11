import csv

START = ("0012", "x01")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_263.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()

DETAILS = {
    ("0012", "x01"): dict(sources_tested="Canon item and explicit host reference 7052.001 inspected; local identifier paths and scan register checked.", open_text_result="No independent Homer holding applies: the notice assigns the uncertain App. Anth. 1.2 attribution to canonical host 7052.001.", scan_result="No separate scan object applies to this cross-reference.", confidence="high", proposed_status="CROSS_REFERENCE_HOST_7052.001", next_action="Resolve and verify App. Anth. 1.2 within 7052.001; retain the question mark on attribution.", notes="Cross-reference preserved; no separate acquisition, image, or OCR used."),
    ("0253", "001"): dict(sources_tested="Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; West 1972 pp. 72–73 and 75–76 item requirement checked; local scan register checked.", open_text_result="No exact licensed TEI of the Margites fragments in West 1972 was found.", scan_result="No reusable page images of West 1972 pp. 72–73 and 75–76 are registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Locate rights-cleared images of the four exact West pages and transcribe or OCR only after page verification.", notes="The following biographical Homerus Byzantius text is not part of this item; no image or OCR used."),
    ("1440", "001"): dict(sources_tested="Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; all ten stated AG loci checked as the item boundary; local scan register checked.", open_text_result="No licensed TEI was verified as containing exactly the ten Honestus epigrams AG 5.20; 7.66, 274; 9.216, 225, 230, 250, 292; 11.32, 45.", scan_result="No item-verified reusable page images for all ten AG loci are registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Resolve all ten loci in a licensed Anthologia Graeca TEI or rights-cleared edition and retain locus-level provenance.", notes="Item boundary is the explicit locus list; no image acquisition or OCR used."),
    ("1440", "x01"): dict(sources_tested="Canon item and explicit host reference 7052.001 inspected; App. Anth. 1.134–137 locus range retained; local identifier paths and scan register checked.", open_text_result="No independent Honestus holding applies: the four dedicatory epigrams belong under canonical host 7052.001.", scan_result="No separate scan object applies to this cross-reference.", confidence="high", proposed_status="CROSS_REFERENCE_HOST_7052.001", next_action="Verify App. Anth. 1.134–137 within 7052.001 and link the locus-level result back to Honestus.", notes="Cross-reference preserved as four explicit loci, not a range-inferred review; no image or OCR used."),
    ("2052", "001"): dict(sources_tested="Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; Sbordone 1940 pp. 1–216 edition requirement checked; local scan register checked.", open_text_result="No exact licensed TEI of Sbordone's 1940 Greek text of Philippus' translation was found.", scan_result="No reusable page-image source for Sbordone 1940 pp. 1–216 is registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Locate a rights-cleared scan of Sbordone 1940 and verify the Greek Philippus recension before transcription or OCR.", notes="Do not substitute another Horapollo recension or translation; no image or OCR used."),
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
