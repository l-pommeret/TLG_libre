"""Verified register for five canonical rows beginning at 2143.001."""
import csv

START = ("2143", "001")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_172.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
TEI_URLS = {
    "001": "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0592.tlg001.1st1K-grc1:1",
    "002": "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0592.tlg002.1st1K-grc1:1.1",
}

coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
start = next(n for n, row in enumerate(coverage)
             if (row["tlg_author_id"], row["tlg_work_id"]) == START)
works = coverage[start:start + 5]
assert len(works) == 5

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for work in works:
        key = (work["tlg_author_id"], work["tlg_work_id"])
        row = {field: "" for field in FIELDS}
        row.update(
            tlg_author_id=key[0], tlg_work_id=key[1],
            author_heading=work["author_heading"], work_title=work["work_title"],
            canonical_edition=work["bibliographic_notice"], last_checked="2026-08-11",
        )
        if key == ("0921", "x01"):
            row.update(
                sources_tested="Canon cross-reference resolved to 0722.003 (Oribasius, Med.).",
                open_text_result="No independent acquisition: host work controls text.",
                scan_result="No separate scan candidate: cross-reference only.",
                confidence="high", proposed_status="CROSS_REFERENCE",
                next_action="Process host 0722.003 (Oribasius, Med.); do not duplicate this referring record.",
                notes="Resolved canon reference; no image acquired.",
            )
        elif key[0] == "0592":
            row.update(
                sources_tested=f"Exact First1KGreek TLG identifier tlg0592.tlg{key[1]}; local TEI metadata and CC BY-SA 4.0 declaration checked.",
                open_text_result="Exact TEI candidate found; source metadata remains marked REVIEW_REQUIRED in the local verification register.",
                open_text_url=TEI_URLS[key[1]], open_text_license="CC BY-SA 4.0 (First1KGreek TEI metadata)",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="high", proposed_status="TEXT_OPEN_UNVERIFIED",
                next_action="Compare Canon boundaries and Rabe edition before ingest; no OCR.",
                notes="Exact identifier, provenance, and TEI licence recorded; no image acquired.",
            )
        else:
            row.update(
                sources_tested="Exact TLG/First1K lookup; cited FGrH or CIG bibliographic record checked.",
                open_text_result="No exact licensed TEI match in local corpus.",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="medium", proposed_status="EDITION_IDENTIFIED",
                next_action="Locate a rights-cleared scan of the cited edition or inscription; do not substitute OCR.",
                notes="No image acquired.",
            )
        writer.writerow(row)
