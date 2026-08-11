"""Verified register for 2017.002--006; no scan or OCR is downloaded."""
import csv

IDS = ("002", "003", "004", "005", "006")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_105.csv"
PG45 = "https://archive.org/details/patrologiaecursu45mignuoft"
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
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="2017", tlg_work_id=work_id, author_heading=work["author_heading"],
                   work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                   sources_tested=f"GNOO TLG concordance {GNOO}; alternative historical PG 45 {PG45}",
                   open_text_result="No exact licensed TEI match in local corpus.",
                   scan_result="ALTERNATIVE_SCAN_CANDIDATE: PG 45 historical text, not canonical GNO 3.1 (1958).",
                   scan_url=PG45,
                   scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",
                   confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                   next_action="Collate PG 45 against cited GNO 3.1 pages; use original images only, never supplied OCR.",
                   notes="GNOO maps these TLG identifiers to its authoritative work records; no images downloaded.",
                   last_checked="2026-08-11")
        out.writerow(row)
