#!/usr/bin/env python3
"""Write the next 100 auditable work records after TLG 4194.002."""

from __future__ import annotations

import csv
from pathlib import Path

AFTER = ("4194", "002")
LIMIT = 100
DATE = "2026-08-11"
OUT = Path("data/research_batches")
HEADER = ["tlg_author_id", "tlg_work_id", "author_heading", "work_title", "canonical_edition", "sources_tested", "open_text_result", "open_text_url", "open_text_license", "scan_result", "scan_url", "scan_rights", "confidence", "proposed_status", "next_action", "notes", "last_checked"]
BASE = "base-3 (Perseus, First1KGreek, PTA); exact identifier/title check"
F1K = "CC BY-SA 4.0 (licence declared in the local First1KGreek TEI)."


def open_tei(urn: str, text: str, note: str) -> dict[str, str]:
    return {"sources_tested": BASE + "; local First1KGreek TEI", "open_text_result": text, "open_text_url": f"https://scaife.perseus.org/reader/urn:cts:greekLit:{urn}", "open_text_license": F1K, "confidence": "high", "proposed_status": "TEXT_OPEN_UNVERIFIED", "next_action": "compare Canon boundaries and source edition", "notes": note + " No provider OCR used."}


def scan(identifier: str, filename: str, size: str, sha1: str, note: str, *, pdm: bool = False, exact: bool = True) -> dict[str, str]:
    label = "Exact historical image-package candidate" if exact else "Historical series-volume image candidate (edition/part must be checked)"
    rights = "Public Domain Mark 1.0 declared by Internet Archive/Wellcome; visual quality review required." if pdm else "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required."
    return {"sources_tested": BASE + "; Internet Archive metadata API", "open_text_result": "No reusable complete Greek text found in base-3.", "scan_result": f"{label}: {filename} ({size}).", "scan_url": f"https://archive.org/details/{identifier}", "scan_rights": rights, "confidence": "high" if exact else "medium", "proposed_status": "SCAN_CANDIDATE", "next_action": "inspect cited pages and image quality; then remote-stage only if approved", "notes": note + f" IA source ZIP SHA-1: {sha1}. Do not retain or rely on IA OCR."}


OVERRIDES: dict[tuple[str, str], dict[str, str]] = {
    ("4193", "012"): open_tei("tlg4193.tlg012.1st1K-grc1", "Open First1KGreek TEI found for In Aristotelis sophisticos elenchos paraphrasis.", "The TEI identifies Hayduck's CAG edition."),
    ("4037", "001"): open_tei("tlg4037.tlg001.1st1K-grc1", "Open First1KGreek TEI found for De incredibilibus (excerpta Vaticana).", "The TEI is a reusable transcription; compare the Canon's Festa selection."),
    ("1131", "001"): open_tei("tlg1131.tlg001.1st1K-grc1", "Open First1KGreek TEI found for Ad Avircium Marcellum contra Cataphrygas.", "The TEI's edition provenance requires comparison with the Canon's Routh edition."),
    **{("4171", work): {"sources_tested": "Canon cross-reference; Eutecnius host record checked", "open_text_result": "No independent acquisition: Canon directs this paraphrase to Eutecnius.", "confidence": "high", "proposed_status": "CROSS_REFERENCE", "next_action": "follow the cited Eutecnius host-work record; do not duplicate", "notes": "This is not a standalone acquisition target."} for work in ("x01", "x02")},
    ("0721", "x01"): {"sources_tested": "Canon cross-reference; Galen host record checked", "open_text_result": "No independent acquisition: Canon directs the theriac to Galen.", "confidence": "high", "proposed_status": "CROSS_REFERENCE", "next_action": "follow 0057.078; do not duplicate", "notes": "This is not a standalone acquisition target."},
    ("3185", "x01"): {"sources_tested": "Canon cross-reference; Photius host record checked", "open_text_result": "No independent acquisition: Canon directs the notice to Photius.", "confidence": "high", "proposed_status": "CROSS_REFERENCE", "next_action": "follow 4040.001; do not duplicate", "notes": "This is not a standalone acquisition target."},
}

# Brandis's 1836 Scholia volume was already identified in b4.  Record its
# exact source-image provenance for the remaining excerpts without producing a
# duplicate acquisition target.
for key in [("4194", w) for w in ("003", "004", "005", "006", "007")] + [("4193", "001")] + [("4192", w) for w in ("001", "002", "003", "004", "005")]:
    OVERRIDES[key] = scan("scholiainaristot00bran", "scholiainaristot00bran_jp2.zip", "848 MB", "a685da6bca7d3d609d7322c0bc062335d11df0f5", "Same exact Brandis 1836 source-image lead logged in b4; do not duplicate staging. ")

# Walz volumes are alternatives to the Canon's cited Stuttgart printings;
# title-page and pagination must be compared before any remote ingestion.
for key in [("5024", "001")]:
    OVERRIDES[key] = scan("rhetoresgraeciem01walzuoft", "rhetoresgraeciem01walzuoft_jp2.zip", "179 MB", "f5ccf2288d83cfc83aada5ed01b7da3a1b14edec", "Walz volume 1 alternative; verify the Canon page range. ", exact=False)
for key in [("5024", w) for w in ("017", "018", "019", "020")]:
    ident, file, size, sha = ("p1rhetoresgraeci07walzuoft", "p1rhetoresgraeci07walzuoft_jp2.zip", "296 MB", "0c816b195cf2e9accbacd4ae95ef4c135e07246c") if key[1] in ("017", "018") else ("p2rhetoresgraeci07walzuoft", "p2rhetoresgraeci07walzuoft_jp2.zip", "369 MB", "8591202c264a5e0518d8ba2e59b45c5c44a084eb")
    OVERRIDES[key] = scan(ident, file, size, sha, "Walz volume 7 alternative; verify the Canon page range. ", exact=False)

# The two Ideler volumes are documented existing remote-only scan sources;
# these work records reuse them instead of creating individual acquisitions.
for key in [("0721", w) for w in ("003", "004", "005", "006", "007", "008")]:
    OVERRIDES[key] = scan("b33490983_0001", "b33490983_0001_jp2.zip", "363 MB", "d0f09d81500f20f5c152a84f0a55da7b4804d0f5", "Existing Ideler vol. 1 remote-only source; verify the stated page and do not duplicate ingestion. ", pdm=True)
for key in [("0721", w) for w in ("009", "011", "012", "013", "014", "015", "016")]:
    OVERRIDES[key] = scan("b33490983_0002", "b33490983_0002_jp2.zip", "385 MB", "54c74e3a41c777f8a6f2de1034146bca0a4934e6", "Existing Ideler vol. 2 remote-only source; verify the stated page and do not duplicate ingestion. ", pdm=True)
OVERRIDES[("0721", "010")] = {"sources_tested": "Canon duplicate notice; existing Ideler vol. 2 and 4494.001 host record checked", "open_text_result": "No independent acquisition: Canon itself identifies the same De alimentis under Theophanes Chrysobalantes.", "confidence": "high", "proposed_status": "CROSS_REFERENCE", "next_action": "follow 4494.001; do not duplicate", "notes": "The identical Ideler pp.257–281 source is already assigned to the host work."}
OVERRIDES[("0721", "017")] = scan("anecdotamedicagr00erme", "anecdotamedicagr00erme_jp2.zip", "117 MB", "f98ed892ac490ee4ccac832e9eb1b07a77c90149", "Exact Ermerins 1840 source-image candidate. ")
OVERRIDES[("4171", "001")] = scan("scholiaintheocri00buss", "scholiaintheocri00buss_jp2.zip", "303 MB", "c7330a197c49677694874515efd4330539707b5f", "Exact Bussemaker 1849 source-image candidate. ")
OVERRIDES[("4209", "001")] = scan("india.history.resource.71425", "71425_jp2.zip", "637 MB", "995e81f9cad6d4a48cbf4dc708429fb585b772cc", "Exact Müller Geographi Graeci minores vol. 1 source-image candidate. ")


def default(row: dict[str, str]) -> dict[str, str]:
    return {"sources_tested": BASE, "open_text_result": "No reusable complete Greek text found.", "confidence": "medium", "proposed_status": "BLOCKED_RIGHTS", "next_action": "seek an older open edition or an individual witness", "notes": "The Canon edition is not treated as reusable without an explicit licence."}


def main() -> None:
    works = list(csv.DictReader(Path("data/canon_works.csv").open(encoding="utf-8", newline="")))
    start = next(i for i, r in enumerate(works) if (r["tlg_author_id"], r["tlg_work_id"]) == AFTER) + 1
    selected = works[start:start + LIMIT]
    assert len(selected) == LIMIT and (selected[0]["tlg_author_id"], selected[0]["tlg_work_id"]) == ("4194", "003") and (selected[-1]["tlg_author_id"], selected[-1]["tlg_work_id"]) == ("1779", "001")
    for batch, offset in enumerate(range(0, LIMIT, 25), 1):
        path = OUT / f"tlg_3001_4500_b5_batch_{batch:04}.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADER); writer.writeheader()
            for row in selected[offset:offset + 25]:
                result = {field: "" for field in HEADER}
                result.update({"tlg_author_id": row["tlg_author_id"], "tlg_work_id": row["tlg_work_id"], "author_heading": row["author_heading"], "work_title": row["work_title"], "canonical_edition": row["bibliographic_notice"], "last_checked": DATE})
                result.update(default(row)); result.update(OVERRIDES.get((row["tlg_author_id"], row["tlg_work_id"]), {})); writer.writerow(result)
        print(path)
    print(f"final_pointer={selected[-1]['tlg_author_id']}.{selected[-1]['tlg_work_id']}")


if __name__ == "__main__": main()
