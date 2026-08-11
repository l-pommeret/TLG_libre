"""Verified register for 2017.012--016; no page image or OCR is downloaded."""
import csv

IDS = ("012", "013", "014", "015", "016")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_107.csv"
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
                   sources_tested=f"GNOO TLG concordance {GNOO}; Pinakes GNO IX record {PINAKES}",
                   open_text_result="No exact licensed TEI match in local corpus.", last_checked="2026-08-11")
        if work_id == "013":
            row.update(scan_result="No reusable page-image candidate verified for the cited GNO IX edition.",
                       confidence="medium", proposed_status="EDITION_IDENTIFIED",
                       next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",
                       notes="Pinakes identifies a historical PG 64 printing but no concrete reusable scan was verified.")
        else:
            item_detail = "PG 46 contains Contra usurarios at cols. 433--452." if work_id == "012" else "PG 46 historical text identified; column verification required."
            row.update(scan_result=f"ALTERNATIVE_SCAN_CANDIDATE: {item_detail} Not the canonical GNO 9.1 edition.",
                       scan_url=PG46,
                       scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",
                       confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                       next_action="Collate Migne text against GNO 9.1; use original images only, never supplied OCR.",
                       notes="No images downloaded; the 1967 critical edition remains the canonical reference.")
        out.writerow(row)
