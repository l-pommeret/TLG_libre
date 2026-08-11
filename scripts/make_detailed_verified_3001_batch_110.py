"""Verified register for 2017.027--031; no page image or OCR is downloaded."""
import csv

IDS = ("027", "028", "029", "030", "031")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_110.csv"
PG44 = "https://archive.org/details/patrologiaecursu44mignuoft"
PG45 = "https://archive.org/details/patrologiaecursu45mignuoft"
GNOO = "https://scholarlyeditions.brill.com/gnoo/"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
DETAIL = {
    "027": "PG 44, cols. 432--608.", "028": "PG 44, cols. 608--616.",
    "029": "PG 44, cols. 616--753.", "030": "PG 45 historical text; GNO 1.1/2.2 remains canonical.",
    "031": "PG 45 historical text; GNO 2.2 remains canonical.",
}

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"],r["tlg_work_id"]) == ("2017", work_id))
        scan = PG44 if work_id in {"027", "028", "029"} else PG45
        row = {field:"" for field in FIELDS}
        row.update(tlg_author_id="2017", tlg_work_id=work_id, author_heading=work["author_heading"],
                   work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                   sources_tested=f"GNOO TLG concordance {GNOO}; alternative Migne source {scan}",
                   open_text_result="No exact licensed TEI match in local corpus.",
                   scan_result=f"ALTERNATIVE_SCAN_CANDIDATE: {DETAIL[work_id]} Not the cited GNO critical edition.",
                   scan_url=scan,
                   scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",
                   confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                   next_action="Collate the historical printing against GNO; use original images only, never supplied OCR.",
                   notes="No images downloaded.", last_checked="2026-08-11")
        out.writerow(row)
