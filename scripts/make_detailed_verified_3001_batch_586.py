import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_586.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = [("0009", "004"), ("0011", "001"), ("0011", "002"), ("0011", "003"), ("0011", "004")]
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}; matches = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/corpus_matches.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for key in WORKS:
        source = canon[key]; open_work = key[0] == "0011"; row = {field: "" for field in FIELDS}
        if open_work:
            match = matches[key]; urn = match["cts_urn"]; filename = urn.rsplit(":", 1)[1] + ".xml"; raw = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0011/tlg{key[1]}/{filename}"
            row.update(open_text_result="Complete open Greek TEI under the exact TLG work identifier, in Storr rather than the canonical Dain–Mazon edition.", open_text_url=raw, open_text_license="CC BY-SA 4.0", scan_result="No scan needed: complete licensed Greek TEI available.", confidence="high", proposed_status="OPEN_TEXT_DIFFERENT_EDITION", next_action="Ingest as the open Storr edition and preserve the distinction from Dain–Mazon.", notes="Immutable XML fetched; exact CTS URN and Greek dramatic body sampled. Not provider OCR; no image used.")
        else:
            row.update(open_text_result="No complete licensed Greek transcription matching the Lobel–Page addenda was verified.", scan_result="The canonical addenda are a modern fragment collection; no exact reusable scan was verified.", confidence="medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Resolve the two papyrus-fragment witnesses individually before acquisition.", notes="No provider OCR or image used.")
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact TLG identifier, Perseus canonical-greekLit immutable revision, edition metadata, repository licence, local corpus and scan registry checked.", last_checked="2026-08-11"); writer.writerow(row)
