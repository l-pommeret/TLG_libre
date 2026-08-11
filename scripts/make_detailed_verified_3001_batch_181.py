"""Verified register for five canonical rows beginning at 0087.017."""
import csv

START = ("0087", "017")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_181.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()

coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
verification = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/text_verification.csv", encoding="utf-8"))}
start = next(n for n, row in enumerate(coverage) if (row["tlg_author_id"], row["tlg_work_id"]) == START)
works = coverage[start:start + 5]
assert len(works) == 5 and all((w["tlg_author_id"], w["tlg_work_id"]) in verification for w in works)

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS); writer.writeheader()
    for work in works:
        key = (work["tlg_author_id"], work["tlg_work_id"]); tei = verification[key]
        row = {field: "" for field in FIELDS}
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=work["author_heading"], work_title=work["work_title"], canonical_edition=work["bibliographic_notice"], sources_tested=f"Exact First1KGreek TLG identifier {tei['cts_urn']}; local TEI metadata and CC BY-SA 4.0 declaration checked.", open_text_result="Exact TEI candidate found; source metadata remains marked REVIEW_REQUIRED in the local verification register.", open_text_url=tei["text_url"], open_text_license="CC BY-SA 4.0 (First1KGreek TEI metadata)", scan_result="No edition-matching reusable page-image source verified.", confidence="high", proposed_status="TEXT_OPEN_UNVERIFIED", next_action="Compare Canon boundaries and Lentz edition before ingest; no OCR.", notes="Exact identifier, provenance, and TEI licence recorded; no image acquired.", last_checked="2026-08-11")
        writer.writerow(row)
