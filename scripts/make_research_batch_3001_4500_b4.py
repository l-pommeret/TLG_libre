#!/usr/bin/env python3
"""Research log for the 100 Canon records immediately after TLG 0072.010.

This only records verifiable open texts and source-image leads.  It neither
downloads images nor accepts an OCR derivative as a text source.
"""

from __future__ import annotations

import csv
from pathlib import Path


AFTER = ("0072", "010")
LIMIT = 100
DATE = "2026-08-11"
OUT = Path("data/research_batches")
HEADER = [
    "tlg_author_id", "tlg_work_id", "author_heading", "work_title",
    "canonical_edition", "sources_tested", "open_text_result",
    "open_text_url", "open_text_license", "scan_result", "scan_url",
    "scan_rights", "confidence", "proposed_status", "next_action",
    "notes", "last_checked",
]
BASE = "base-3 (Perseus, First1KGreek, PTA); exact identifier/title check"
F1K_LICENSE = "CC BY-SA 4.0 (licence declared in the local First1KGreek TEI)."


def tei(work: str, urn: str, description: str, note: str) -> dict[str, str]:
    return {
        "sources_tested": BASE + "; local First1KGreek TEI",
        "open_text_result": description,
        "open_text_url": f"https://scaife.perseus.org/reader/urn:cts:greekLit:{urn}",
        "open_text_license": F1K_LICENSE,
        "confidence": "high", "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare Canon boundaries and source edition",
        "notes": note + " No provider OCR used.",
    }


def image_lead(identifier: str, filename: str, size: str, sha1: str, *, exact: bool = True) -> dict[str, str]:
    label = "Exact historical image-package candidate" if exact else "Historical series-volume image candidate (edition/part must be checked)"
    return {
        "sources_tested": BASE + "; Internet Archive metadata API",
        "open_text_result": "No reusable complete Greek text found in base-3.",
        "scan_result": f"{label}: {filename} ({size}).",
        "scan_url": f"https://archive.org/details/{identifier}",
        "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
        "confidence": "high" if exact else "medium", "proposed_status": "SCAN_CANDIDATE",
        "next_action": "inspect cited pages and image quality; then remote-stage only if approved",
        "notes": f"IA source ZIP SHA-1: {sha1}. Do not retain or rely on IA OCR.",
    }


OVERRIDES: dict[tuple[str, str], dict[str, str]] = {
    # Explicit Canon aliases: do not create a duplicate source target.
    **{("0072", work): {
        "sources_tested": "Canon cross-reference; stated host-work record checked",
        "open_text_result": "No independent acquisition: Canon directs this text to a host record.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow the cited host-work record; do not duplicate",
        "notes": "This entry has no separate acquisition target.",
    } for work in ("x01", "x02")},
    **{("1139", work): {
        "sources_tested": "Canon cross-reference; 1139.007 host record checked",
        "open_text_result": "No independent acquisition: Canon groups this papyrus fragment under 1139.007.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow 1139.007; do not duplicate",
        "notes": "The entry is a constituent fragment, not a separate edition target.",
    } for work in ("x01", "x02", "x03", "x04")},
    ("5045", "x01"): {
        "sources_tested": "Canon cross-reference; 5024.022 host-work record checked",
        "open_text_result": "No independent acquisition: Canon directs the synopsis to the Hermogenes commentary.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow 5024.022; do not duplicate",
        "notes": "The Walz page reference is a cross-reference, not a distinct work target.",
    },

    # Exact, locally present open TEI editions.
    ("4026", "001"): tei("4026.001", "tlg4026.tlg001.1st1K-grc1", "Open First1KGreek TEI found for In Aristotelis artem rhetoricam commentarium.", "The TEI identifies Rabe's CAG 21.2 edition."),
    ("4026", "002"): tei("4026.002", "tlg4026.tlg002.1st1K-grc1", "Open First1KGreek TEI found for the fragmentary commentary in Aristotle's Rhetoric.", "The TEI identifies Rabe's CAG 21.2 edition."),
    ("4026", "003"): tei("4026.003", "tlg4026.tlg003.1st1K-grc1", "Open First1KGreek TEI found for the fragmentary Rhetoric paraphrase.", "The TEI identifies Rabe's CAG 21.2 edition."),
    ("4027", "001"): tei("4027.001", "tlg4027.tlg001.1st1K-grc1", "Open First1KGreek TEI found for Paraphrasis categoriarum.", "The TEI identifies Hayduck's CAG 23.2 edition."),
    ("4033", "003"): tei("4033.003", "tlg4033.tlg003.1st1K-grc1", "Open First1KGreek TEI found for the Nicomachean Ethics paraphrase.", "The TEI identifies Heylbut's CAG 19.2 edition."),
    ("9004", "001"): tei("9004.001", "tlg9004.tlg001.opp-grc1", "Open First1KGreek TEI found for the anonymous commentary on Posterior Analytics II.", "The TEI identifies Wallies's CAG 13.3 edition."),
}

# Public-domain source-image leads.  An image lead supplements a licensed TEI
# when present; it is never used as an OCR source.
for key in [("4026", "001"), ("4026", "002"), ("4026", "003")]:
    OVERRIDES[key].update({
        "scan_result": "Historical CAG 21.1–21.2 series-volume image candidate: commentariaina21pt12akaduoft_jp2.zip (334 MB).",
        "scan_url": "https://archive.org/details/commentariaina21pt12akaduoft",
        "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; title-page/part and visual/reuse review required.",
        "notes": OVERRIDES[key]["notes"] + " IA source ZIP SHA-1: 91030ed93323a8aa886a3af721c3b42a7f9a615e; do not use IA OCR.",
    })
for key, identifier, filename, size, sha1 in [
    (("4033", "001"), "commentariaina20akaduoft", "commentariaina20akaduoft_jp2.zip", "159 MB", "2188eebe89504a971f4b3181c074ccab8413711a"),
    (("4033", "002"), "commentariaina20akaduoft", "commentariaina20akaduoft_jp2.zip", "159 MB", "2188eebe89504a971f4b3181c074ccab8413711a"),
]:
    OVERRIDES[key] = image_lead(identifier, filename, size, sha1, exact=False)
for key in [("4191", "001"), ("4191", "002"), ("4190", "001"), ("4190", "002"), ("4190", "003"), ("4190", "004"), ("4190", "005"), ("4027", "002"), ("4027", "003"), ("4195", "001"), ("4195", "002"), ("4195", "003"), ("4195", "004"), ("4165", "002"), ("4196", "001"), ("4196", "003"), ("4194", "001"), ("4194", "002")]:
    OVERRIDES[key] = image_lead("scholiainaristot00bran", "scholiainaristot00bran_jp2.zip", "848 MB", "a685da6bca7d3d609d7322c0bc062335d11df0f5")
for key in [("5045", "003"), ("5045", "004")]:
    OVERRIDES[key] = image_lead("rhetoresgraeciem02walzuoft", "rhetoresgraeciem02walzuoft_jp2.zip", "305 MB", "b0113ba6123faa5ba98e30e56c900106ce8f8c30", exact=False)

# The appended author heading makes this derived key unsafe for acquisition.
for key in [("1139", "021"), ("4027", "004"), ("4196", "533")]:
    OVERRIDES[key] = {
        "sources_tested": "Canon extraction quality check",
        "open_text_result": "The extracted Canon record is contaminated or split, so an exact work-level search is unsafe.",
        "confidence": "high", "proposed_status": "EXTRACTION_REVIEW",
        "next_action": "repair this Canon entry before text or scan acquisition",
        "notes": "No source or OCR was selected from an ambiguous extracted record.",
    }


def default(row: dict[str, str]) -> dict[str, str]:
    notice = row["bibliographic_notice"]
    if "FGrH" in notice:
        return {
            "sources_tested": BASE + "; FGrH inventory",
            "open_text_result": "No explicit reusable transcription found for this FGrH dossier.",
            "confidence": "low", "proposed_status": "EDITION_IDENTIFIED",
            "next_action": "locate an unrestricted FGrH scan or map earlier witnesses",
            "notes": "Papyrological publication references are not treated as reusable OCR or texts.",
        }
    return {
        "sources_tested": BASE,
        "open_text_result": "No reusable complete Greek text found.",
        "confidence": "medium", "proposed_status": "BLOCKED_RIGHTS",
        "next_action": "seek an older open edition or an individual witness",
        "notes": "The Canon edition is not treated as reusable without an explicit licence.",
    }


def main() -> None:
    with Path("data/canon_works.csv").open(encoding="utf-8", newline="") as f:
        works = list(csv.DictReader(f))
    start = next(i for i, r in enumerate(works) if (r["tlg_author_id"], r["tlg_work_id"]) == AFTER) + 1
    selected = works[start:start + LIMIT]
    assert len(selected) == LIMIT
    assert (selected[0]["tlg_author_id"], selected[0]["tlg_work_id"]) == ("0072", "011")
    assert (selected[-1]["tlg_author_id"], selected[-1]["tlg_work_id"]) == ("4194", "002")
    for batch, offset in enumerate(range(0, LIMIT, 25), 1):
        path = OUT / f"tlg_3001_4500_b4_batch_{batch:04}.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            for row in selected[offset:offset + 25]:
                result = {field: "" for field in HEADER}
                result.update({
                    "tlg_author_id": row["tlg_author_id"], "tlg_work_id": row["tlg_work_id"],
                    "author_heading": row["author_heading"], "work_title": row["work_title"],
                    "canonical_edition": row["bibliographic_notice"], "last_checked": DATE,
                })
                result.update(default(row))
                result.update(OVERRIDES.get((row["tlg_author_id"], row["tlg_work_id"]), {}))
                writer.writerow(result)
        print(path)
    print(f"final_pointer={selected[-1]['tlg_author_id']}.{selected[-1]['tlg_work_id']}")


if __name__ == "__main__":
    main()
