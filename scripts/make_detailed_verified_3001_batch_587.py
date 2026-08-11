import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_587.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["005", "006", "007", "008", "009"]
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}; matches = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/corpus_matches.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in WORKS:
        key = ("0011", work); source = canon[key]; row = {field: "" for field in FIELDS}
        if work in {"005", "006", "007", "008"}:
            match = matches[key]; urn = match["cts_urn"]; filename = urn.rsplit(":", 1)[1] + ".xml"; raw = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0011/tlg{work}/{filename}"; fragment = work == "008"
            row.update(open_text_result=("Open Greek TEI covers the Oxyrhynchus fragment edition only; it is not the complete Radt fragment corpus." if fragment else "Complete open Greek TEI under the exact TLG work identifier, in Storr rather than the canonical Dain–Mazon edition."), open_text_url=raw, open_text_license="CC BY-SA 4.0", scan_result="No scan needed for the available licensed Greek TEI.", confidence="high", proposed_status=("PARTIAL_OPEN_TEXT_AVAILABLE" if fragment else "OPEN_TEXT_DIFFERENT_EDITION"), next_action=("Map the Oxyrhynchus text to exact Radt fragment numbers; retain the remainder as missing." if fragment else "Ingest as the open Storr edition and preserve the edition distinction."), notes="Immutable XML fetched; exact CTS URN and Greek text sampled. Not provider OCR; no image used.")
        else:
            row.update(open_text_result="No complete licensed Greek transcription matching West's three elegiac/epigrammatic fragments was verified.", scan_result="No exact reusable page-image source for the canonical West edition was verified.", confidence="medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Map frr. 1, 4–5 to their ancient witnesses before acquisition.", notes="No provider OCR or image used.")
        row.update(tlg_author_id="0011", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact TLG identifier, Perseus canonical-greekLit immutable revision, edition metadata, repository licence, local corpus and scan registry checked.", last_checked="2026-08-11"); writer.writerow(row)
