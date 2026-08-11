"""Verified register for 2022.057--061; records scans, never downloads them."""
import csv

IDS = ("057", "058", "059", "060", "061")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_102.csv"
PG37 = "https://archive.org/details/patrologiaecursu37mignuoft"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
verified = list(csv.DictReader(open("data/text_verification.csv", encoding="utf-8")))
by_id = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in verified}

with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == ("2022", work_id))
        text = by_id.get(("2022", work_id))
        result = {field: "" for field in FIELDS}
        result.update(
            tlg_author_id="2022", tlg_work_id=work_id,
            author_heading=work["author_heading"], work_title=work["work_title"],
            canonical_edition=work["bibliographic_notice"],
            sources_tested=f"Internet Archive PG 37 item {PG37}; exact TLG/First1K lookup",
            scan_result="EXACT_SCAN_CANDIDATE: PG 37 (Migne, 1857) covers the cited columns.",
            scan_url=PG37,
            scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.",
            confidence="high", proposed_status="SCAN_CANDIDATE",
            next_action="Use original page images and match cited PG columns; do not use supplied OCR.",
            notes="No images downloaded; IA OCR derivatives expressly excluded.", last_checked="2026-08-11",
        )
        if text:
            result.update(open_text_result="Exact open TEI match.", open_text_url=text["text_url"],
                          open_text_license=text["tei_license"] or text["license"],
                          proposed_status="TEXT_OPEN_UNVERIFIED; SCAN_CANDIDATE")
        else:
            result["open_text_result"] = "No exact licensed TEI match in local corpus."
        out.writerow(result)
