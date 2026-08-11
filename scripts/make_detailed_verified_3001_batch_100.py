"""Build the verified research register for canon rows 2022.047--051.

No asset is downloaded here: the Internet Archive link is retained solely as an
item-level, page-image candidate for the 1857 PG 36 volume.
"""
import csv

IDS = ("047", "048", "049", "050", "051")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_100.csv"
IA_PG36 = "https://archive.org/details/patrologiaecursu36mignuoft"
CATALOGUES = {
    "047": "https://www.biblindex.org/fr/work-editions/discours-38-41",
    "048": "https://www.biblindex.org/fr/work-editions/discours-38-41",
    "049": "https://www.biblindex.org/fr/work-editions/discours-38-41",
    "050": "https://pinakes.irht.cnrs.fr/notices/oeuvre/12675/",
    "051": "https://www.biblindex.org/en/work-editions/orationes-42-45/patrologia-graeca-36",
}
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
        row = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == ("2022", work_id))
        text = by_id.get(("2022", work_id))
        result = {field: "" for field in FIELDS}
        result.update(
            tlg_author_id="2022",
            tlg_work_id=work_id,
            author_heading=row["author_heading"],
            work_title=row["work_title"],
            canonical_edition=row["bibliographic_notice"],
            sources_tested=(
                f"Internet Archive PG 36 item {IA_PG36}; edition catalogue {CATALOGUES[work_id]}"
            ),
            scan_result="EXACT_SCAN_CANDIDATE: PG 36 (Migne, 1857) covers the cited columns.",
            scan_url=IA_PG36,
            scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify image reuse before transfer.",
            confidence="high",
            proposed_status="SCAN_CANDIDATE",
            next_action="Use IA original page images only; match cited PG columns; do not use supplied OCR.",
            notes="No images downloaded. IA exposes OCR derivatives, which are explicitly excluded.",
            last_checked="2026-08-11",
        )
        if text:
            result.update(
                open_text_result="Exact open TEI match.",
                open_text_url=text["text_url"],
                open_text_license=text["tei_license"] or text["license"],
                proposed_status="TEXT_OPEN_UNVERIFIED; SCAN_CANDIDATE",
            )
        else:
            result["open_text_result"] = "No exact licensed TEI match in local corpus."
        out.writerow(result)
