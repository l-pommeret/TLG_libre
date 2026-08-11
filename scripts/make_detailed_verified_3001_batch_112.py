"""Verified register for 2017.037--041; no page image or OCR is downloaded."""
import csv

IDS = ("037", "038", "039", "040", "041")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_112.csv"
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
        work = next(r for r in works if (r["tlg_author_id"],r["tlg_work_id"]) == ("2017",work_id))
        row={field:"" for field in FIELDS}
        row.update(tlg_author_id="2017",tlg_work_id=work_id,author_heading=work["author_heading"],work_title=work["work_title"],canonical_edition=work["bibliographic_notice"],open_text_result="No exact licensed TEI match in local corpus.",last_checked="2026-08-11")
        if work_id in {"037","038","039"}:
            row.update(sources_tested=f"GNOO exclusion status {GNOO}; cited Hörner 1972 supplement catalogue",
                       scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",
                       next_action="Locate a rights-cleared scan of the cited Hörner edition or a verified historical Greek witness; no OCR.",notes="Spurious recension retained; no scan claimed without an item-level match.")
        else:
            detail="PG 46, cols. 701--721" if work_id=="040" else "PG 46, cols. 960--1000"
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; alternative Migne PG 46 {PG46}",
                       scan_result=f"ALTERNATIVE_SCAN_CANDIDATE: {detail}; not the canonical critical edition.",scan_url=PG46,
                       scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",confidence="medium",proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                       next_action="Collate PG 46 against the cited edition; use original images only, never supplied OCR.",notes="No images downloaded.")
        out.writerow(row)
