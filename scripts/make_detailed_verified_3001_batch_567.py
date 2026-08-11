import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_567.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["056", "057", "058", "059", "060"]
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
matches = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/corpus_matches.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in WORKS:
        source, match = canon[("0007", work)], matches[("0007", work)]; urn = match["cts_urn"]; filename = urn.rsplit(":", 1)[1] + ".xml"
        raw = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0007/tlg{work}/{filename}"
        row = {field: "" for field in FIELDS}; row.update(tlg_author_id="0007", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Perseus canonical-greekLit at immutable commit {COMMIT}: exact CTS URN {urn}, Greek XML, Perrin metadata and CC BY-SA 4.0 statement checked.", open_text_result="Complete open Greek TEI under the exact TLG identifier, in Perrin rather than the canonical Ziegler edition.", open_text_url=raw, open_text_license="CC BY-SA 4.0", scan_result="No scan needed: complete licensed Greek TEI available.", confidence="high", proposed_status="OPEN_TEXT_DIFFERENT_EDITION", next_action="Ingest as alternate edition; do not label it Ziegler without collation.", notes="Immutable XML fetched and Greek-script sampled; not provider OCR. No image used.", last_checked="2026-08-11"); writer.writerow(row)
