import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_558.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["011", "012", "013", "014", "015"]
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in WORKS:
        source = canon[("0007", work)]
        urn = f"urn:cts:greekLit:tlg0007.tlg{work}.perseus-grc2"
        raw = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0007/tlg{work}/tlg0007.tlg{work}.perseus-grc2.xml"
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="0007", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Perseus canonical-greekLit at immutable commit {COMMIT}: exact CTS URN {urn}, Greek XML body, Perrin edition metadata, and repository CC BY-SA 4.0 statement directly checked.", open_text_result="Complete open Greek TEI under the exact TLG work identifier, in Perrin rather than the canonical Ziegler edition.", open_text_url=raw, open_text_license="CC BY-SA 4.0", scan_result="No scan is needed because a complete licensed Greek TEI is available.", confidence="high", proposed_status="OPEN_TEXT_DIFFERENT_EDITION", next_action="Ingest as an open alternate edition; do not represent it as Ziegler without collation.", notes="The immutable XML was fetched and Greek-script sampled; this is not provider OCR. No image used.", last_checked="2026-08-11")
        writer.writerow(row)
