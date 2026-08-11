"""Verified register for five canonical rows beginning at 1414.001."""
import csv

START = ("1414", "001")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_158.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
HOSTS = {
    ("2671", "x01"): "7052.001 (Anthologiae Graecae Appendix)",
    ("0917", "x01"): "0057.076, 0057.077, and 0057.078 (Galenus, Med.)",
    ("0917", "x02"): "0715.001 (Paulus, Med.)",
    ("0917", "x03"): "0718.012 (Aëtius, Med.)",
}
TEI_URL = "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg1414.tlg001.1st1K-grc1:1"

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
        if key == ("1414", "001"):
            row.update(
                sources_tested="Exact First1KGreek TLG identifier tlg1414.tlg001; local TEI metadata and CC BY-SA 4.0 declaration checked.",
                open_text_result="Exact TEI candidate found; source metadata remains marked REVIEW_REQUIRED in the local verification register.",
                open_text_url=TEI_URL, open_text_license="CC BY-SA 4.0 (First1KGreek TEI metadata)",
                scan_result="No edition-matching reusable page-image source verified.",
                confidence="high", proposed_status="TEXT_OPEN_UNVERIFIED",
                next_action="Compare Canon boundaries and source edition before ingest; no OCR.",
                notes="Exact identifier, provenance, and TEI licence recorded; no image acquired.",
            )
        else:
            host = HOSTS[key]
            row.update(
                sources_tested=f"Canon cross-reference resolved to {host}.",
                open_text_result="No independent acquisition: host work controls text.",
                scan_result="No separate scan candidate: cross-reference only.",
                confidence="high", proposed_status="CROSS_REFERENCE",
                next_action=f"Process host {host}; do not duplicate this referring record.",
                notes="Resolved canon reference; no image acquired.",
            )
        writer.writerow(row)
