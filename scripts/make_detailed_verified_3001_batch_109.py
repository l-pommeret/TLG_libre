"""Verified register for 2017.022--026; no page image or OCR is downloaded."""
import csv

IDS = ("022", "023", "024", "025", "026")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_109.csv"
PG46 = "https://archive.org/details/patrologiaecursu46mignuoft"
GNOO = "https://scholarlyeditions.brill.com/gnoo/"
PINAKES = "https://pinakes.irht.cnrs.fr/notices/bibliographie/4SHEQ8Q5/"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == ("2017", work_id))
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="2017", tlg_work_id=work_id, author_heading=work["author_heading"],
                   work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                   open_text_result="No exact licensed TEI match in local corpus.", last_checked="2026-08-11")
        if work_id in {"022", "023"}:
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; Pinakes GNO IX record {PINAKES}; PG 46 {PG46}",
                       scan_result="ALTERNATIVE_SCAN_CANDIDATE: historical PG 46 text identified; column match required. Not GNO 9.1.",
                       scan_url=PG46,
                       scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",
                       confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                       next_action="Collate PG 46 against GNO 9.1; use original images only, never supplied OCR.",
                       notes="No images downloaded; GNO 9.1 is canonical.")
        else:
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; cited GNO 8.1 bibliographic record",
                       scan_result="No edition-matching reusable page-image source verified.",
                       confidence="medium", proposed_status="EDITION_IDENTIFIED",
                       next_action="Locate a rights-cleared scan of cited GNO 8.1; do not substitute OCR.",
                       notes="No historical scan was claimed without an item-level match; no images acquired.")
        out.writerow(row)
