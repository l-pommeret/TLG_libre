"""Verified register for 2017.007--011; no page image or OCR is downloaded."""
import csv

IDS = ("007", "008", "009", "010", "011")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_106.csv"
PG45 = "https://archive.org/details/patrologiaecursu45mignuoft"
PG46 = "https://archive.org/details/patrologiaecursu46mignuoft"
GNOO = "https://scholarlyeditions.brill.com/gnoo/"
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
        pg = PG45 if work_id in {"007", "008"} else PG46
        detail = {
            "007": "PG 45 contains Ad Theophilum at cols. 1269--1278.",
            "008": "PG 45 historical text identified; column verification still required.",
            "009": "PG 46 contains De mortuis non esse dolendum at cols. 497--537.",
            "010": "PG 46 historical text identified; column verification still required.",
            "011": "PG 46 historical text identified; column verification still required.",
        }[work_id]
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="2017", tlg_work_id=work_id, author_heading=work["author_heading"],
                   work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                   sources_tested=f"GNOO TLG concordance {GNOO}; alternative Migne source {pg}",
                   open_text_result="No exact licensed TEI match in local corpus.",
                   scan_result=f"ALTERNATIVE_SCAN_CANDIDATE: {detail} Not the canonical GNO edition.",
                   scan_url=pg,
                   scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",
                   confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                   next_action="Collate Migne text against cited GNO edition; use original images only, never supplied OCR.",
                   notes="No images downloaded; canonical editions are GNO 3.1 (1958) or GNO 9.1 (1967).",
                   last_checked="2026-08-11")
        out.writerow(row)
