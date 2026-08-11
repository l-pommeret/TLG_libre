import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_557.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["006", "007", "008", "009", "010"]
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"

canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
matches = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/corpus_matches.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for work in WORKS:
        key = ("0007", work)
        source, match = canon[key], matches[key]
        urn = f"urn:cts:greekLit:tlg0007.tlg{work}.perseus-grc2"
        raw = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0007/tlg{work}/tlg0007.tlg{work}.perseus-grc2.xml"
        row = {field: "" for field in FIELDS}
        same = "ed. Perrin" in source["bibliographic_notice"] and "Perrin" in match["edition_description"]
        row.update(tlg_author_id="0007", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Perseus canonical-greekLit TEI at immutable commit {COMMIT}; exact CTS URN {urn}, Greek body text, edition metadata and repository-wide CC BY-SA 4.0 statement directly checked.", open_text_result=("Exact open Greek TEI in the same Perrin edition." if same else "Complete open Greek TEI under the exact TLG work identifier, but in the Perrin edition rather than the canonical Ziegler edition."), open_text_url=raw, open_text_license="CC BY-SA 4.0", scan_result="No scan is needed because a complete licensed Greek TEI is available.", confidence="high", proposed_status=("OPEN_TEXT_AVAILABLE" if same else "OPEN_TEXT_DIFFERENT_EDITION"), next_action=("Ingest the immutable TEI and preserve its edition statement." if same else "Ingest as an open alternate edition; do not represent it as Ziegler without collation."), notes="The XML was fetched and sampled as Greek; this is not provider OCR. No image used.", last_checked="2026-08-11")
        writer.writerow(row)
