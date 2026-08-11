"""Verified register for 2017.032--036; no page image or OCR is downloaded."""
import csv

IDS = ("032", "033", "034", "035", "036")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_111.csv"
PG44 = "https://archive.org/details/patrologiaecursu44mignuoft"
PG46 = "https://archive.org/details/patrologiaecursu46mignuoft"
GNOO = "https://scholarlyeditions.brill.com/gnoo/"
BNF = "https://catalogue.bnf.fr/ark:/12148/cb16672365c"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"],r["tlg_work_id"]) == ("2017", work_id))
        row = {field:"" for field in FIELDS}
        row.update(tlg_author_id="2017", tlg_work_id=work_id, author_heading=work["author_heading"],
                   work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                   open_text_result="No exact licensed TEI match in local corpus.", last_checked="2026-08-11")
        if work_id == "032":
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; BiblIndex PG 44; Migne scan {PG44}",
                       scan_result="ALTERNATIVE_SCAN_CANDIDATE: PG 44, cols. 756--1120; not GNO 6 (1960).",
                       scan_url=PG44,
                       scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify concordance before transfer.",
                       confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                       next_action="Collate PG 44 against GNO 6; use original images only, never supplied OCR.",
                       notes="No images downloaded.")
        elif work_id == "033":
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; alternative Migne volume {PG46}",
                       scan_result="ALTERNATIVE_SCAN_CANDIDATE: PG 46 historical correspondence; item-level column match required.",
                       scan_url=PG46,
                       scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify letter coverage before transfer.",
                       confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                       next_action="Map individual letters to PG 46 before any image transfer; exclude OCR.",
                       notes="No images downloaded; cited GNO 8.2 remains canonical.")
        else:
            row.update(sources_tested=f"GNOO excludes this spurious work; BnF attribution/PG survey {BNF}",
                       scan_result="No edition-matching reusable page-image source verified.", confidence="medium",
                       proposed_status="EDITION_IDENTIFIED",
                       next_action="Locate a rights-cleared scan matching Hörner 1972 or a verified historical Greek witness; no OCR.",
                       notes="The work is [Sp.]; historical PG attributions require item-level identification before use.")
        out.writerow(row)
