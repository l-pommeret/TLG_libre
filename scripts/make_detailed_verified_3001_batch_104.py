"""Verified register for four 2022 cross-references and 2017.001.

Cross-references deliberately contain no copied host text or scan: the host is
named so downstream acquisition can de-duplicate it.
"""
import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_104.csv"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
XREFS = {
    ("2022", "x01"): "7052.003 (Anthologiae Graecae Appendix)",
    ("2022", "x02"): "2063.006 (Gregorius Thaumaturgus, Scr. Eccl.)",
    ("2022", "x03"): "0541.047 (Menander, Comic.)",
    ("2022", "x04"): "2042.019 and 2042.020 (Origenes, Theol.)",
}
TARGETS = [("2022", "x01"), ("2022", "x02"), ("2022", "x03"), ("2022", "x04"), ("2017", "001")]
PG45 = "https://archive.org/details/patrologiaecursu45mignuoft"
ERARA = "https://www.e-rara.ch/bau_1/content/structure/1127567"

works = list(csv.DictReader(open("data/canon_works.csv", encoding="utf-8")))
with open(OUTPUT, "w", newline="", encoding="utf-8") as fh:
    out = csv.DictWriter(fh, fieldnames=FIELDS); out.writeheader()
    for key in TARGETS:
        work = next(r for r in works if (r["tlg_author_id"], r["tlg_work_id"]) == key)
        result = {field: "" for field in FIELDS}
        result.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=work["author_heading"],
                      work_title=work["work_title"], canonical_edition=work["bibliographic_notice"],
                      last_checked="2026-08-11")
        if key in XREFS:
            host = XREFS[key]
            result.update(sources_tested=f"Canon cross-reference resolved to {host}",
                          open_text_result="No independent acquisition: host work controls text.",
                          scan_result="No separate scan candidate: cross-reference only.", confidence="high",
                          proposed_status="CROSS_REFERENCE",
                          next_action=f"Process host {host}; do not duplicate this referring record.",
                          notes=f"Resolved canon reference: {host}.")
        else:
            result.update(sources_tested=f"GNOO TLG concordance; alternative PG 45 {PG45}; 1571 Basel record {ERARA}",
                          open_text_result="No exact licensed TEI match in local corpus.",
                          scan_result="ALTERNATIVE_SCAN_CANDIDATE: historical editions identified, not the canonical GNO 3.1 (1958).",
                          scan_url=ERARA,
                          scan_rights="Public-domain 1571 source; verify Greek-text content and image reuse before transfer.",
                          confidence="medium", proposed_status="ALTERNATIVE_SCAN_CANDIDATE",
                          next_action="Verify the 1571/PG text against GNO 3.1; acquire original images only if concordant.",
                          notes="GNOO identifies tlg2017.tlg001; no OCR used or downloaded.")
        out.writerow(result)
