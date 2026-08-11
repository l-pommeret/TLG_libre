import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_596.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["033", "034", "035", "036", "038"]
WENDLAND = "https://archive.org/details/11537522bsb"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in WORKS:
        source = canon[("0018", work)]; wendland = work == "036"; row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="0018", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact Canon item, First1KGreek Philo directory, Perseus/OPP identifiers, Internet Archive title search and local scan registry checked.", open_text_result="No complete licensed Greek transcription matching this exact fragment or excerpt edition was verified.", scan_result=("Exact Wendland 1891 volume identified at Internet Archive/BSB, but image-reuse terms and printed-page Greek sampling are not verified for transfer." if wendland else "No exact rights-cleared, Greek-sampled item-level scan was verified."), scan_url=(WENDLAND if wendland else ""), scan_rights=("Rights not verified for public redistribution" if wendland else ""), confidence=("high" if wendland else "medium"), proposed_status=("CANDIDATE_SCAN_RIGHTS_AND_GREEK_UNVERIFIED" if wendland else "NO_EXACT_OPEN_TEXT"), next_action=("Verify image rights and visually sample Wendland pp.22–25 before any HF transfer." if wendland else "Map the fragments to primary witnesses or ancient hosts before acquisition."), notes="No completeness inferred from neighbouring Philo TEIs. No provider OCR or image used.", last_checked="2026-08-11"); writer.writerow(row)
