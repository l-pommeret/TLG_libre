"""Build the verified research register for canon rows 2022.052--056.

The two scan candidates are original page-image sources; this script downloads
neither their images nor any OCR derivative.
"""
import csv

IDS = ("052", "053", "054", "055", "056")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_101.csv"
PG36 = "https://archive.org/details/patrologiaecursu36mignuoft"
IDELER = "https://archive.org/details/physicietmedicig01ideluoft"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
verified = list(csv.DictReader(open("data/text_verification.csv", encoding="utf-8")))
by_id = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in verified}

with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS)
    out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == ("2022", work_id))
        text = by_id.get(("2022", work_id))
        pg = work_id != "056"
        scan_url = PG36 if pg else IDELER
        tested = (
            f"Internet Archive PG 36 {PG36}; BiblIndex PG 36, Orationes 42--45"
            if pg else
            f"Internet Archive Ideler 1841 {IDELER}; Wikimedia Commons public-domain record"
        )
        rights = (
            "Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer."
            if pg else
            "Wikimedia Commons marks the 1841 edition public domain; verify source image before transfer."
        )
        result = {field: "" for field in FIELDS}
        result.update(
            tlg_author_id="2022", tlg_work_id=work_id,
            author_heading=work["author_heading"], work_title=work["work_title"],
            canonical_edition=work["bibliographic_notice"], sources_tested=tested,
            open_text_result="No exact licensed TEI match in local corpus.",
            scan_result=(
                "EXACT_SCAN_CANDIDATE: PG 36 (Migne, 1857) covers the cited columns."
                if pg else
                "EXACT_SCAN_CANDIDATE: Ideler, Physici et medici Graeci minores 1 (1841), pp. 297--298."
            ),
            scan_url=scan_url, scan_rights=rights, confidence="high",
            proposed_status="SCAN_CANDIDATE",
            next_action="Use original page images and match cited pages; do not use supplied OCR.",
            notes="No images downloaded; OCR/PDF text derivatives excluded.",
            last_checked="2026-08-11",
        )
        if text:
            result.update(
                open_text_result="Exact open TEI match.", open_text_url=text["text_url"],
                open_text_license=text["tei_license"] or text["license"],
                proposed_status="TEXT_OPEN_UNVERIFIED; SCAN_CANDIDATE",
            )
        out.writerow(result)
