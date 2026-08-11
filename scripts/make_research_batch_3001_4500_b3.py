#!/usr/bin/env python3
"""Create the next 100 work-level research records after TLG 2412.002.

The CSVs are an auditable research log only.  A scan reference is a lead to
source images, never provider OCR, and is deliberately not downloaded here.
"""

from __future__ import annotations

import csv
from pathlib import Path


AFTER = ("2412", "002")
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
DFHG_LICENSE = "CC BY-SA 4.0 (DFHG volume README)."


def open_tei(url: str, description: str, note: str = "") -> dict[str, str]:
    return {
        "sources_tested": BASE + "; local First1KGreek TEI",
        "open_text_result": description,
        "open_text_url": url,
        "open_text_license": F1K_LICENSE,
        "confidence": "high",
        "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare Canon editorial boundaries and source edition",
        "notes": note or "TEI present locally; no provider OCR used.",
    }


def scan(identifier: str, filename: str, size: str, sha1: str, action: str) -> dict[str, str]:
    return {
        "sources_tested": BASE + "; Internet Archive metadata API",
        "open_text_result": "No reusable complete Greek text found in base-3.",
        "scan_result": f"Exact historical image-package candidate: {filename} ({size}).",
        "scan_url": f"https://archive.org/details/{identifier}",
        "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
        "confidence": "high",
        "proposed_status": "SCAN_CANDIDATE",
        "next_action": action,
        "notes": f"IA source ZIP SHA-1: {sha1}. Do not retain or rely on IA OCR.",
    }


OVERRIDES: dict[tuple[str, str], dict[str, str]] = {
    # Host works: these are deliberately not independent acquisition targets.
    **{("0772", work): {
        "sources_tested": "Canon cross-reference; host-work records checked",
        "open_text_result": "No independent acquisition: Canon directs the fragment to Galen, Oribasius, or Aëtius.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow the cited host-work record; do not duplicate",
        "notes": "A standalone source would duplicate the host text.",
    } for work in ("x01", "x02", "x03", "x04", "x05")},
    **{("0678", work): {
        "sources_tested": "Canon cross-reference; host-work records checked",
        "open_text_result": "No independent acquisition: Canon directs the fragment to Galen or Oribasius.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow the cited host-work record; do not duplicate",
        "notes": "A standalone source would duplicate the host text.",
    } for work in ("x01", "x02")},
    ("0773", "x01"): {
        "sources_tested": "Canon cross-reference; Galen host-work record checked",
        "open_text_result": "No independent acquisition: Canon directs the fragment to Galen.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow the Galen host-work record; do not duplicate",
        "notes": "A standalone source would duplicate the host text.",
    },
    ("1124", "x01"): {
        "sources_tested": "Canon cross-reference; 4033.003 is the host record",
        "open_text_result": "No independent acquisition: Canon reassigns the paraphrase to the anonymous Ethics commentary.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow 4033.003; do not duplicate",
        "notes": "The former attribution to Andronicus is not a separate text target.",
    },
    ("2737", "x01"): {
        "sources_tested": "Canon cross-reference; Syncellus host-work record checked",
        "open_text_result": "No independent acquisition: Canon directs the chronography to George Syncellus.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow 3045.001; do not duplicate",
        "notes": "A standalone Anianus acquisition would duplicate the host text.",
    },
    **{("7056", work): {
        "sources_tested": "Canon cross-reference; Anthologiae Graecae Appendix host records checked",
        "open_text_result": "No independent acquisition: Canon directs this anonymous group to an Appendix host record.",
        "confidence": "high", "proposed_status": "CROSS_REFERENCE",
        "next_action": "follow the cited 7052 host-work record; do not duplicate",
        "notes": "The anonymous classification is not a separate edition target.",
    } for work in ("x01", "x02", "x03", "x04", "x05", "x06", "x07")},

    # Complete open transcriptions whose identifiers and embedded licences were
    # checked in the local corpus checkout.
    ("0092", "001"): open_tei(
        "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0092.tlg001.1st1K-grc1",
        "Open First1KGreek TEI found for Geographiae expositio compendiaria.",
        "The TEI identifies Karl Müller's Geographi Graeci minores vol. 2; no provider OCR used."),
    ("1129", "001"): open_tei(
        "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg1129.tlg001.1st1K-grc1",
        "Open First1KGreek TEI found for De barbarismo et soloecismo.",
        "The TEI identifies Valckenaer's 1822 edition; no provider OCR used."),
    ("1129", "002"): open_tei(
        "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg1129.tlg001.1st1K-grc1",
        "Open First1KGreek TEI exists for the same work, but not the Canon's 1867 Nauck edition.",
        "Retain the distinct 1867 edition provenance; no provider OCR used."),
    ("2029", "001"): open_tei(
        "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg2029.tlg001.1st1K-grc1",
        "Open First1KGreek TEI found for the Anonymi summaria ratio geographiae.",
        "The TEI identifies Karl Müller's Geographi Graeci minores vol. 2; no provider OCR used."),
    ("2972", "001"): open_tei(
        "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg2972.tlg001.1st1K-grc1",
        "Open First1KGreek TEI found for De terrae motibus.",
        "The TEI identifies Wachsmuth's 1897 Lydus edition; no provider OCR used."),
    ("3156", "001"): open_tei(
        "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg3156.tlg001.1st1K-grc1",
        "Open First1KGreek TEI found for Exegesis in Hesiodi theogoniam.",
        "The TEI identifies Flach's 1876 edition; no provider OCR used."),

    ("0111", "001"): {
        "sources_tested": "base-3; Perseus Greek Anthology TEI",
        "open_text_result": "The cited Anthologia Graeca locus 7.181 is in the open Paton TEI.",
        "open_text_url": "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg7000.tlg001.perseus-grc7:7.181/",
        "open_text_license": "CC BY-SA 4.0 (Perseus repository licence; TEI licence recorded locally).",
        "confidence": "high", "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare AG 7.181 and attribution",
        "notes": "Content-level locus match, not an author-URN match; no OCR involved.",
    },
    ("0138", "001"): {
        "sources_tested": "base-3; Perseus Greek Anthology TEI",
        "open_text_result": "The Canon's listed Anthologia Graeca loci are represented across the open Paton TEI volumes.",
        "open_text_url": "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg7000.tlg001.perseus-grc6:6.6/",
        "open_text_license": "CC BY-SA 4.0 (Perseus repository licence; TEI licence recorded locally).",
        "confidence": "high", "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare every cited locus and anonymous attribution",
        "notes": "Content-level collection match; it is not an author-URN match and needs boundary checking.",
    },
}

# DFHG is a separately licensed, reusable EpiDoc representation of the cited
# nineteenth-century FHG pages.  The four volume-2 page ranges were checked
# against the XML page breaks, as was Androtion in volume 1.
for key, file, pages in [
    (("2536", "003"), "ANDRON_TEJUS.xml", "FHG 2, pp.348–349"),
    (("1123", "002"), "ANDRON_HALICARNASSENSIS.xml", "FHG 2, pp.349–352"),
    (("2172", "002"), "ANDRON_ALEXANDRINUS.xml", "FHG 2, p.352"),
    (("4347", "001"), "ANDRON_EPHESIUS.xml", "FHG 2, pp.347–348"),
    (("1125", "003"), "ANDROTIO.xml", "FHG 1, pp.371–377"),
]:
    vol = "volume_1" if file == "ANDROTIO.xml" else "volume_2"
    OVERRIDES[key] = {
        "sources_tested": f"base-3; DFHG {vol} EpiDoc page-break check",
        "open_text_result": f"DFHG reusable EpiDoc transcription covers {pages} ({file}).",
        "open_text_url": f"https://github.com/DFHG-project/{vol}/blob/master/data/epidoc_xml/{file}",
        "open_text_license": DFHG_LICENSE,
        "confidence": "high", "proposed_status": "TEXT_OPEN_UNVERIFIED",
        "next_action": "compare FHG page range and fragment boundaries",
        "notes": "DFHG is a new digital representation of FHG, not provider OCR.",
    }

# Exact image-package leads: no image file is fetched by this script.
for key in [("0092", "001"), ("2029", "001")]:
    OVERRIDES[key].update({
        "scan_result": "Exact historical image-package candidate: 71426_jp2.zip (634 MB).",
        "scan_url": "https://archive.org/details/india.history.resource.71426",
        "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
        "notes": OVERRIDES[key]["notes"] + " IA source ZIP SHA-1: 3ffef6f61d31ce178dec7f51cc08b972486c57b6; do not use IA OCR.",
    })
for key, identifier, filename, size, sha1 in [
    (("4374", "001"), "anonymichristian00herm", "anonymichristian00herm_jp2.zip", "51 MB", "d4abd1db21acd10b32f9924f3e7d5e12fd34481c"),
    (("2584", "001"), "comicorumgraecor11kaib", "comicorumgraecor11kaib_jp2.zip", "146 MB", "2d4c12bc09236904f04a76d214f5df6766cbbab4"),
    (("1128", "001"), "anonymerkommenta00diel", "anonymerkommenta00diel_jp2.zip", "50 MB", "2a6d863bdfe533c3c50ad11787b6c312096f9852"),
]:
    OVERRIDES[key] = scan(identifier, filename, size, sha1, "inspect cited pages and image quality; then remote-stage only if approved")
for key, identifier, filename, size, sha1 in [
    (("2972", "001"), "ioannislaurentii00lydu", "ioannislaurentii00lydu_jp2.zip", "210 MB", "337b849dc52f80d51cc49e7d2154271f66cb1dc0"),
    (("3156", "001"), "bub_gb_wc5fAAAAMAAJ", "bub_gb_wc5fAAAAMAAJ_jp2.zip", "154 MB", "bc15639606fc5c90f576db9401e0ddd6921b541d"),
]:
    OVERRIDES[key].update({
        "scan_result": f"Exact historical image-package candidate: {filename} ({size}).",
        "scan_url": f"https://archive.org/details/{identifier}",
        "scan_rights": "Public-domain-era item; IA metadata has no explicit rights field; visual/reuse review required.",
        "notes": OVERRIDES[key]["notes"] + f" IA source ZIP SHA-1: {sha1}; do not use IA OCR.",
    })


def default(row: dict[str, str]) -> dict[str, str]:
    if row["extraction_status"] == "needs_review":
        return {
            "sources_tested": "Canon extraction quality check",
            "open_text_result": "The Canon record is split/truncated, so an exact work-level search is unsafe.",
            "confidence": "high", "proposed_status": "EXTRACTION_REVIEW",
            "next_action": "repair this Canon entry before text or scan acquisition",
            "notes": "No source or OCR was selected from an ambiguous extracted record.",
        }
    notice = row["bibliographic_notice"]
    if "FGrH" in notice:
        return {
            "sources_tested": BASE + "; FGrH inventory",
            "open_text_result": "No explicit reusable transcription found for this FGrH dossier.",
            "confidence": "low", "proposed_status": "EDITION_IDENTIFIED",
            "next_action": "locate an unrestricted FGrH scan or map earlier witnesses",
            "notes": "Do not infer content from a non-concordant FHG overlap.",
        }
    if "FHG" in notice:
        return {
            "sources_tested": BASE + "; DFHG/FHG inventory",
            "open_text_result": "No author-specific reusable transcription confirmed for this FHG dossier.",
            "confidence": "medium", "proposed_status": "EDITION_IDENTIFIED",
            "next_action": "locate an unrestricted complete FHG volume and inspect the cited pages",
            "notes": "No provider OCR may be used.",
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
    start = next(i for i, row in enumerate(works) if (row["tlg_author_id"], row["tlg_work_id"]) == AFTER) + 1
    selected = works[start:start + LIMIT]
    assert len(selected) == LIMIT
    assert (selected[0]["tlg_author_id"], selected[0]["tlg_work_id"]) == ("0280", "001")
    assert (selected[-1]["tlg_author_id"], selected[-1]["tlg_work_id"]) == ("0072", "010")
    for batch, offset in enumerate(range(0, LIMIT, 25), start=1):
        path = OUT / f"tlg_3001_4500_b3_batch_{batch:04}.csv"
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
