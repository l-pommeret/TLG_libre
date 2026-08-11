"""Verified register for 2017.017--021; no page image or OCR is downloaded."""
import csv

IDS = ("017", "018", "019", "020", "021")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_108.csv"
PG46 = "https://archive.org/details/patrologiaecursu46mignuoft"
GNOO = "https://scholarlyeditions.brill.com/gnoo/"
PINAKES = "https://pinakes.irht.cnrs.fr/notices/bibliographie/4SHEQ8Q5/"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
DETAIL = {
    "017": "PG 46 covers the fourth Paschal sermon at cols. 681--684.",
    "018": "PG 46 covers the fifth Paschal sermon at cols. 684--689.",
    "019": "PG 46 historical text is attested; column match remains to be checked.",
    "020": "PG 46 historical text is attested; column match remains to be checked.",
    "021": "PG 46 historical text is attested; column match remains to be checked.",
}

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for work_id in IDS:
        work = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == ("2017", work_id))
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="2017", tlg_work_id=work_id, author_heading=work["author_heading"],
                   work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                   sources_tested=f"GNOO TLG concordance {GNOO}; Pinakes GNO IX record {PINAKES}; PG 46 {PG46}",
                   open_text_result="No exact licensed TEI match in local corpus.",
                   scan_result=f"ALTERNATIVE_SCAN_CANDIDATE: {DETAIL[work_id]} Not the canonical GNO 9.1 edition.",
                   scan_url=PG46,
                   scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",
                   confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                   next_action="Collate PG 46 against GNO 9.1; use original images only, never supplied OCR.",
                   notes="No images downloaded; GNO 9.1 (1967) remains the canonical reference.", last_checked="2026-08-11")
        out.writerow(row)
