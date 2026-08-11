import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_595.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["028", "029", "030", "031", "032"]
COMMIT = "bfea9acd07ee1b7cea70cdd927c8f092d5637695"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in WORKS:
        source = canon[("0018", work)]; row = {field: "" for field in FIELDS}
        if work != "032":
            urn = f"urn:cts:greekLit:tlg0018.tlg{work}.1st1K-grc1"; raw = f"https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/{COMMIT}/data/tlg0018/tlg{work}/tlg0018.tlg{work}.1st1K-grc1.xml"
            row.update(open_text_result="Complete licensed Greek TEI in the exact canonical Cohn–Reiter edition.", open_text_url=raw, open_text_license="CC BY-SA 4.0", scan_result="No scan needed because the exact canonical Greek text is openly available.", confidence="high", proposed_status="OPEN_TEXT_AVAILABLE", next_action="Ingest the immutable First1K TEI and retain canonical pagination.", notes="Exact XML fetched; CTS URN, editor and Greek body sampled. Not provider OCR; no image used.")
        else:
            row.update(open_text_result="No standalone licensed TEI matching the Cohn–Reiter Hypothetica excerpt arrangement was verified; the work survives through indirect excerpts and was not substituted by an uncollated host text.", scan_result="No exact reusable item-level scan was verified.", confidence="medium", proposed_status="EDITION_IDENTIFIED", next_action="Map the Cohn–Reiter pages to their exact ancient excerpt hosts before reusing any open text.", notes="No provider OCR or image used; no completeness inferred from neighbouring Philo TEIs.")
        row.update(tlg_author_id="0018", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact Canon item, First1KGreek Philo directory and immutable XML where present, local corpus and scan registry checked.", last_checked="2026-08-11"); writer.writerow(row)
