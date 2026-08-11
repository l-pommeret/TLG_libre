#!/usr/bin/env python3
"""Write the next four auditable 25-work research checkpoints.

This is a research register, not an ingestion script.  In particular, every
Internet Archive reference below is limited to the source image package and
its catalog metadata: IA's derivative OCR is deliberately out of scope.
"""

from __future__ import annotations

import csv
from pathlib import Path


FIRST = ("3393", "003")
LIMIT = 100
OUT = Path("data/research_batches")
DATE = "2026-08-11"

HEADER = [
    "tlg_author_id", "tlg_work_id", "author_heading", "work_title",
    "canonical_edition", "sources_tested", "open_text_result",
    "open_text_url", "open_text_license", "scan_result", "scan_url",
    "scan_rights", "confidence", "proposed_status", "next_action",
    "notes", "last_checked",
]

BASE = "base-3 (Perseus, First1KGreek, PTA); exact-edition catalog search"


def candidate(identifier: str, file: str, sha1: str, size: str, action: str) -> dict[str, str]:
    return {
        "sources_tested": BASE + "; Internet Archive metadata API",
        "open_text_result": "No reusable complete text found in base-3.",
        "scan_result": f"Exact historical image-package candidate: {file} ({size}).",
        "scan_url": f"https://archive.org/details/{identifier}",
        "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
        "confidence": "high",
        "proposed_status": "SCAN_CANDIDATE",
        "next_action": action,
        "notes": f"IA source ZIP SHA-1: {sha1}. Do not retain or rely on IA OCR.",
    }


# Exact textual counterparts already sparse-checked locally.  The source
# repositories carry CC BY-SA 4.0; status remains unverified until the Canon
# editorial boundaries have been compared with the TEI.
ANDOCIDES = {
    "001": ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0027.tlg001.perseus-grc2", "De mysteriis"),
    "002": ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0027.tlg002.perseus-grc2", "De reditu suo"),
    "003": ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0027.tlg003.perseus-grc2", "De pace"),
    "004": ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0027.tlg004.perseus-grc2", "In Alcibiadem"),
}

OVERRIDES: dict[tuple[str, str], dict[str, str]] = {}

for work, (url, title) in ANDOCIDES.items():
    OVERRIDES[("0027", work)] = {
        "sources_tested": "base-3; local Perseus TEI exact TLG identifier",
        "open_text_result": f"Open Greek Perseus TEI found for {title}.",
        "open_text_url": url,
        "open_text_license": "CC BY-SA 4.0 (Perseus repository license; TEI license recorded locally).",
        "confidence": "high",
        "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare Canon editorial boundaries and source edition",
        "notes": "Existing sparse checkout already contains the TEI; no OCR involved.",
    }

# The newer Dilts/Murphy records are duplicates of the same works; the open
# Perseus witnesses are useful text sources but not that 2018 edition.
for work, url in {
    "006": ANDOCIDES["001"][0], "007": ANDOCIDES["002"][0],
    "008": ANDOCIDES["003"][0], "009": ANDOCIDES["004"][0],
}.items():
    OVERRIDES[("0027", work)] = {
        "sources_tested": "base-3; local Perseus TEI exact underlying TLG work",
        "open_text_result": "Open Greek Perseus TEI exists for the same work, but not the Canon's 2018 edition.",
        "open_text_url": url,
        "open_text_license": "CC BY-SA 4.0 (Perseus repository license; TEI license recorded locally).",
        "confidence": "high",
        "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare work boundaries; retain edition provenance",
        "notes": "Do not label the Perseus text as the 2018 Dilts/Murphy edition.",
    }

OVERRIDES[("9005", "001")] = {
    "sources_tested": "base-3; Perseus Greek Anthology TEI",
    "open_text_result": "The cited Anthologia Graeca locus 15.28 is in the open Paton TEI.",
    "open_text_url": "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg7000.tlg001.perseus-grc8:15.28/",
    "open_text_license": "CC BY-SA 4.0 (Perseus repository license; TEI license recorded locally).",
    "confidence": "high",
    "proposed_status": "TEXT_OPEN_UNVERIFIED",
    "next_action": "compare the cited locus and attribution",
    "notes": "A cited anthology locus, not a separate IA OCR source.",
}

for work, title, url in [
    ("001", "Liber Syntipae", "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg3118.tlg001.1st1K-grc1:1.1"),
    ("002", "Liber Syntipae (recensio altera)", "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg3118.tlg002.1st1K-grc1:praef"),
]:
    OVERRIDES[("3118", work)] = {
        "sources_tested": "base-3; local First1KGreek TEI exact TLG identifier",
        "open_text_result": f"Open Greek First1KGreek TEI found for {title}.",
        "open_text_url": url,
        "open_text_license": "CC BY-SA 4.0 (First1KGreek repository license).",
        "confidence": "high",
        "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare Canon recension boundaries and edition",
        "notes": "Existing sparse checkout already contains the TEI; no OCR involved.",
    }

# Exact scan candidates, all deliberately left un-ingested until a visual
# quality sample and provider/reuse assessment have passed.
for key in [("0405", "001"), ("0406", "001")]:
    OVERRIDES[key] = candidate("comicorumatticor02kockuoft", "comicorumatticor02kockuoft_jp2.zip", "b954eba45a0dff5cd553d3884bde6a771c8e9ee0", "257 MB", "inspect relevant pages and image quality; then remote-stage only if approved")
for key in [("0405", "002"), ("0406", "002")]:
    OVERRIDES[key] = candidate("fragmentacomicor03meinuoft", "fragmentacomicor03meinuoft_jp2.zip", "784189d4a24da5e7d1ce9c4460931db6eaf6be99", "296 MB", "inspect relevant pages and image quality; then remote-stage only if approved")
OVERRIDES[("0405", "003")] = candidate("supplementumcomi00demiuoft", "supplementumcomi00demiuoft_jp2.zip", "6fd943c56b73365b236d73720631d38d6801f786", "88 MB", "inspect the single fragment page and image quality; then remote-stage only if approved")
OVERRIDES[("0407", "001")] = candidate("comicorumatticor03kockuoft", "comicorumatticor03kockuoft_jp2.zip", "aca3d383868ac11e7786ebd3630f5bbe493ad0f8", "376 MB", "inspect relevant pages and image quality; then remote-stage only if approved")
OVERRIDES[("0407", "002")] = candidate("fragmentacomicor04meinuoft", "fragmentacomicor04meinuoft_jp2.zip", "c19acea5ce375cb4ff4d11408ba51829bf6709fd", "375 MB", "inspect relevant pages and image quality; then remote-stage only if approved")
OVERRIDES[("2577", "003")] = candidate("CatalogusCodicumAstrologorumGraec8p3", "Catalogus_codicum_astrologorum_graec_8p3_jp2.zip", "8f1514a2a5c21cf5c1d55e6ff4308a2f3ea49862", "51 MB", "inspect p.188 and image quality; then remote-stage only if approved")
OVERRIDES[("2896", "008")] = candidate("patrologicursus105migngoog", "patrologicursus105migngoog_jp2.zip", "6b3879991d64975f83090d69746512c9e9c3a972", "527 MB", "inspect MPG 89 cols.851–1077A and quality; then remote-stage only if approved")
for key in [("3393", "006"), ("2897", "003")]:
    OVERRIDES[key] = candidate("patrologicursus105migngoog", "patrologicursus105migngoog_jp2.zip", "6b3879991d64975f83090d69746512c9e9c3a972", "527 MB", "inspect the stated MPG 89 columns and quality; then remote-stage only if approved")
OVERRIDES[("2896", "012")] = candidate("OriensChristianus3", "Oriens_Christianus_jp2.zip", "f498f437e66e8e3edf4a2bc43581c5348c909521", "774 MB", "inspect pp.61–88 and image quality; then remote-stage only if approved")
OVERRIDES[("3118", "001")].update({
    "scan_result": "Exact 1912 image-package candidate also found: michandreopulili00sind_jp2.zip (127 MB).",
    "scan_url": "https://archive.org/details/michandreopulili00sind",
    "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
    "notes": "TEI already available. IA source ZIP SHA-1: afd8f4a2ad8f59b3f5fd5c667c81c85374625540. Do not retain IA OCR.",
})
OVERRIDES[("3118", "002")].update({
    "scan_result": "The same exact 1912 source volume is an image-package candidate: michandreopulili00sind_jp2.zip (127 MB).",
    "scan_url": "https://archive.org/details/michandreopulili00sind",
    "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
    "notes": "TEI already available. IA source ZIP SHA-1: afd8f4a2ad8f59b3f5fd5c667c81c85374625540. Do not retain IA OCR.",
})
OVERRIDES[("3118", "003")] = candidate("fabulaeromanense01eberuoft", "fabulaeromanense01eberuoft_jp2.zip", "36f72bf6b7314f741bcdb8c52fb559f08371fc6f", "142 MB", "inspect pp.1–196 and image quality; then remote-stage only if approved")
OVERRIDES[("1121", "001")] = candidate("epistolographoih00hercuoft", "epistolographoih00hercuoft_jp2.zip", "457c9f2eda89d2cfcd7071cb56cf9332031bdb9d", "1.03 GB", "inspect p.106 and image quality; then remote-stage only if approved")

for key in [("0713", "001"), ("0713", "002"), ("0714", "001"), ("0714", "002")]:
    OVERRIDES[key] = candidate("diefragmenteder02diel", "diefragmenteder02diel_jp2.zip", "2614a214b38be74587e58d1c151117f4b4c58d61", "225 MB", "map the historical predecessor to the 1952 Canon edition; inspect quality before staging")
for key in [("0725", "001"), ("0725", "002"), ("0617", "001"), ("0617", "002")]:
    OVERRIDES[key] = candidate("diefragmenteder01krangoog", "diefragmenteder01krangoog_jp2.zip", "4cec4339e6c9a41cf394b3d580657be50c6ff07f", "168 MB", "map the 1903 predecessor to the 1951 Canon edition; inspect quality before staging")

# These entries only point at a different host work in the Canon and should
# never become duplicate acquisition targets.
for key in [("2577", "x01"), ("2759", "x01"), ("2759", "x02"), ("2759", "x03"),
            ("0405", "x01"), ("0547", "x01"), ("0677", "x01"), ("0677", "x02"),
            ("0677", "x03"), ("0677", "x04")]:
    OVERRIDES[key] = {
        "sources_tested": "Canon cross-reference; base-3 not treated as a separate work",
        "open_text_result": "No independent acquisition: Canon directs this material to a host work.",
        "confidence": "high",
        "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow the stated host-work record; do not duplicate",
        "notes": "Excluded from standalone text/scan acquisition by design.",
    }


def default(row: dict[str, str]) -> dict[str, str]:
    notice = row["bibliographic_notice"]
    if "FGrH" in notice:
        return {
            "sources_tested": BASE + "; FGrH/DFHG inventory",
            "open_text_result": "No explicit reusable transcription found for this FGrH dossier.",
            "confidence": "low", "proposed_status": "EDITION_IDENTIFIED",
            "next_action": "locate an unrestricted FGrH scan or map earlier witnesses",
            "notes": "Do not infer content from a non-concordant FHG overlap.",
        }
    if "FHG" in notice:
        return {
            "sources_tested": BASE + "; FHG volume inventory; full-view catalog search",
            "open_text_result": "No author-specific reusable transcription found.",
            "scan_result": "A historical FHG volume may contain the cited pages; direct unrestricted image source not yet confirmed.",
            "confidence": "medium", "proposed_status": "EDITION_IDENTIFIED",
            "next_action": "locate an unrestricted complete FHG volume and inspect stated pages",
            "notes": "No provider OCR may be used.",
        }
    return {
        "sources_tested": BASE,
        "open_text_result": "No reusable complete Greek text found.",
        "confidence": "medium", "proposed_status": "BLOCKED_RIGHTS",
        "next_action": "seek an older open edition or an individual witness",
        "notes": "Modern Canon edition is not treated as reusable without an explicit license.",
    }


def main() -> None:
    with Path("data/canon_works.csv").open(encoding="utf-8", newline="") as f:
        works = list(csv.DictReader(f))
    start = next(i for i, r in enumerate(works) if (r["tlg_author_id"], r["tlg_work_id"]) == FIRST)
    selected = works[start:start + LIMIT]
    if len(selected) != LIMIT:
        raise SystemExit(f"expected {LIMIT} rows, got {len(selected)}")
    for batch, offset in enumerate(range(0, LIMIT, 25), start=1):
        path = OUT / f"tlg_3001_4500_b2_batch_{batch:04}.csv"
        with path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            for row in selected[offset:offset + 25]:
                result = {field: "" for field in HEADER}
                result.update({
                    "tlg_author_id": row["tlg_author_id"],
                    "tlg_work_id": row["tlg_work_id"],
                    "author_heading": row["author_heading"],
                    "work_title": row["work_title"],
                    "canonical_edition": row["bibliographic_notice"],
                    "last_checked": DATE,
                })
                result.update(default(row))
                result.update(OVERRIDES.get((row["tlg_author_id"], row["tlg_work_id"]), {}))
                writer.writerow(result)
        print(path)
    print(f"final_pointer={selected[-1]['tlg_author_id']}.{selected[-1]['tlg_work_id']}")


if __name__ == "__main__":
    main()
