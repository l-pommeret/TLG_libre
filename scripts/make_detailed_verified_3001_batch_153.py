"""Verified register for the five canonical cross-references beginning at 0694.x01."""
import csv

START = ("0694", "x01")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_153.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
HOSTS = {
    ("0694", "x01"): "0057.076, 0057.077, and 0057.078 (Galenus, Med.)",
    ("0694", "x02"): "0718.006 (Aëtius, Med.)",
    ("0694", "x03"): "0008.001 (Athenaeus, Soph.)",
    ("0694", "x04"): "0738.006 (Hippiatrica)",
    ("0915", "x01"): "0722.003 (Oribasius, Med.)",
}

coverage = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
start = next(
    n for n, row in enumerate(coverage)
    if (row["tlg_author_id"], row["tlg_work_id"]) == START
)
works = coverage[start:start + 5]
assert len(works) == 5
assert {(w["tlg_author_id"], w["tlg_work_id"]) for w in works} == set(HOSTS)

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for work in works:
        key = (work["tlg_author_id"], work["tlg_work_id"])
        host = HOSTS[key]
        row = {field: "" for field in FIELDS}
        row.update(
            tlg_author_id=key[0],
            tlg_work_id=key[1],
            author_heading=work["author_heading"],
            work_title=work["work_title"],
            canonical_edition=work["bibliographic_notice"],
            sources_tested=f"Canon cross-reference resolved to {host}.",
            open_text_result="No independent acquisition: host work controls text.",
            scan_result="No separate scan candidate: cross-reference only.",
            confidence="high",
            proposed_status="CROSS_REFERENCE",
            next_action=f"Process host {host}; do not duplicate this referring record.",
            notes="Resolved canon reference; no image acquired.",
            last_checked="2026-08-11",
        )
        writer.writerow(row)
