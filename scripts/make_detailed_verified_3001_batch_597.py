import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_597.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = [("0018", "039"), ("0018", "041"), ("0018", "042"), ("0021", "001"), ("0021", "002")]
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for key in WORKS:
        source = canon[key]; row = {field: "" for field in FIELDS}
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact Canon item, First1KGreek and Perseus identifiers, papyrus/edition-title search and local scan registry checked.", open_text_result="No complete licensed Greek transcription matching this exact canonical fragment, papyrus or modern arrangement was verified.", scan_result="No exact rights-cleared, Greek-sampled item-level scan was verified.", confidence="medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action=("Resolve each fragment to its host or primary papyrus before acquisition." if key[0] == "0018" else "Map the Lasserre testimonia/doctrina items to their ancient sources before reusing open host texts."), notes="Modern editorial aggregations were not substituted with neighbouring works. No provider OCR or image used.", last_checked="2026-08-11"); writer.writerow(row)
