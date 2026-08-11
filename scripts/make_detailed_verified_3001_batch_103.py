"""Verified register for 2022.062--066; records scans, never downloads them."""
import csv

IDS = ("062", "063", "064", "065", "066")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_103.csv"
PG37 = "https://archive.org/details/patrologiaecursu37mignuoft"
PG38 = "https://archive.org/details/patrologiaecursu38mignuoft"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == ("2022", work_id))
        result = {field: "" for field in FIELDS}
        result.update(tlg_author_id="2022", tlg_work_id=work_id,
                      author_heading=work["author_heading"], work_title=work["work_title"],
                      canonical_edition=work["bibliographic_notice"],
                      open_text_result="No exact licensed TEI match in local corpus.",
                      last_checked="2026-08-11")
        if work_id == "062":
            result.update(sources_tested=f"Internet Archive PG 37 item {PG37}; exact TLG/First1K lookup",
                          scan_result="EXACT_SCAN_CANDIDATE: PG 37 covers cols. 1451--1577.", scan_url=PG37,
                          scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.",
                          confidence="high", proposed_status="SCAN_CANDIDATE",
                          next_action="Use original images for cited columns; do not use supplied OCR.",
                          notes="No images downloaded; IA OCR derivatives excluded.")
        elif work_id in {"063", "064"}:
            result.update(sources_tested=f"Internet Archive PG 38 item {PG38}; exact TLG/First1K lookup",
                          scan_result="EXACT_SCAN_CANDIDATE: PG 38 covers the cited columns.", scan_url=PG38,
                          scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.",
                          confidence="high", proposed_status="SCAN_CANDIDATE",
                          next_action="Use original images for cited columns; do not use supplied OCR.",
                          notes="No images downloaded; IA OCR derivatives excluded.")
        else:
            result.update(sources_tested="Exact TLG/First1K lookup; cited modern-edition catalogue check",
                          scan_result="No edition-matching reusable page-image source verified.",
                          confidence="medium", proposed_status="EDITION_IDENTIFIED",
                          next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",
                          notes="1894/1976 cited editions retained; no image acquired.")
        out.writerow(result)
