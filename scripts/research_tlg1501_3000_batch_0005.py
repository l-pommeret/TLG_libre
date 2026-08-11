#!/usr/bin/env python3
"""Create the reviewed discovery log for the 1567.001--2767.003 tranche.

The log is deliberately conservative: an open text is recorded only when a
specific reusable digital source was found; otherwise it records the exact
print edition and (where appropriate) a scan lead.  It never downloads OCR.
"""
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "data/canon_coverage.csv"
OUT = ROOT / "data/research_batches/tlg_1501_3000_batch_0005.csv"

AG = {
    ("1573", "001"): ("10", "16.236"),
    ("1575", "001"): ("6", "6.112"),
    ("1577", "001"): ("6", "6.271"),
    ("1579", "001"): ("7", "7.197"),
    ("1581", "001"): ("6", "6.165"),
    ("1582", "001"): ("6", "6.294"),
    ("1589", "001"): ("6", "4.2"),
}
FHG_SCAN = {
    "1": "https://archive.org/details/fragmentahistori01mueluoft",
    "2": "https://books.google.com/books?id=UckWAAAAQAAJ",
    "3": "https://archive.org/details/fragmentahistor00antgoog",
    "4": "https://books.google.com/books?id=quBFAQAAMAAJ",
}
PG18 = "https://commons.wikimedia.org/wiki/File:Patrologia_Graeca_Vol._18.djvu"
PG36 = "https://commons.wikimedia.org/wiki/Category:Patrologiae_Cursus_Completus,_Series_Graeca"


def selected_rows():
    selected, started = [], False
    with CANON.open(newline="") as handle:
        for row in csv.DictReader(handle):
            if (row["tlg_author_id"], row["tlg_work_id"]) == ("1567", "001"):
                started = True
            if not started:
                continue
            if (
                row["record_type"] == "work"
                and row["pipeline_status"] == "NOT_CHECKED"
                and 1501 <= int(row["tlg_author_id"]) <= 3000
            ):
                selected.append(row)
                if len(selected) == 100:
                    return selected
    raise RuntimeError(f"expected 100 rows, found {len(selected)}")


def result(row, ordinal):
    key = (row["tlg_author_id"], row["tlg_work_id"])
    notice, title = row["bibliographic_notice"], row["work_title"]
    base = "base-3; exact-title/edition web lookup"
    # URL/licence fields for an unsuccessful text-and-scan check.
    blank = ("", "", "", "", "")

    if key in AG:
        vol, locus = AG[key]
        url = f"https://scaife.perseus.org/reader/urn:cts:greekLit:tlg7000.tlg001.perseus-grc{vol}:{locus}/"
        return ("Anthologia Graeca (Paton) TEI contains the cited locus/loci.", url,
                "CC-BY-SA-4.0", "", "", "", "high", "TEXT_OPEN_UNVERIFIED",
                "compare every cited AG locus to the Canon selection",
                "content-level match; it is not an author-URN match", "base-3; Perseus Greek Anthology TEI")

    # The two adjacent PHIDALIUS records share a malformed duplicate id in the
    # Canon.  Only the papyrus record has an item-level open-text lead.
    if ordinal == 72:
        return ("P.Oxy. 39.2891 has an item-level DCLP/papyri.info transcription lead.",
                "https://papyri.info/editions/p.oxy/39/2891", "CC-BY-3.0 (DCLP)",
                "", "", "", "medium", "TEXT_OPEN_UNVERIFIED",
                "verify Canon delimitation against the papyrus edition",
                "do not retain provider OCR", "base-3; Papyri.info DCLP")
    if ordinal == 58:
        return ("P.Oxy. 17.2082 is an open witness for one cited testimony, not the whole dossier.",
                "https://papyri.info/editions/p.oxy/17/2082", "CC-BY-3.0 (DCLP)",
                "", "", "", "medium", "TEXT_PARTIAL",
                "map the single papyrus testimony before reuse",
                "FGrH #325 itself remains unlocated", "base-3; Papyri.info DCLP")
    if key == ("1584", "003"):
        return ("DFHG supplies a structured transcription of the FHG dossier.",
                "https://www.dfhg-project.org/DFHG/digger.php?onoffswitch=on&what%5B%5D=author%7CPHERECYDES",
                "CC-BY-SA-4.0", "", "", "", "high", "TEXT_OPEN_UNVERIFIED",
                "compare FHG pp.70–99 and vol.4 p.639",
                "older FHG, not the Canon's separate FGrH dossier", "base-3; DFHG")

    if "FHG" in title:
        volume = next((v for v in FHG_SCAN if f"FHG {v}" in title), "")
        url = FHG_SCAN.get(volume, "")
        return ("No author-specific reusable transcription verified; exact historical FHG volume is digitized.",
                "", "", "full-view historical FHG scan candidate", url,
                "public-domain printing; provider image-reuse terms require confirmation", "medium", "SCAN_CANDIDATE",
                "inspect cited pages and image quality before remote ingestion",
                "no provider OCR accepted", base)

    if "FGrH" in title:
        return ("No exact reusable FGrH transcription or rights-cleared scan verified.", *blank,
                "low", "EDITION_IDENTIFIED", "locate FGrH scan or concord individual witnesses",
                "do not substitute FHG without a concordance", base)

    if key == ("2019", "001"):
        return ("Exact 1888 Greek edition is digitized; no transcription accepted.", "", "",
                "Collection des anciens alchimistes grecs, vol.2, image candidate",
                "https://archive.org/details/collectiondesan04bertgoog",
                "1888 printing public domain; IA item has no explicit rights declaration", "high", "SCAN_CANDIDATE",
                "inspect TIFF/JPEG image quality and source rights before remote ingestion",
                "no IA OCR may be retained", "base-3; IA/Open Library; Wikimedia/Wikisource")
    if key == ("1574", "001"):
        return ("No reusable transcription found; von Arnim's 1905 SVF is a scan lead.", "", "",
                "Stoicorum veterum fragmenta vol.1 scan candidate", "https://archive.org/search?query=Stoicorum%20veterum%20fragmenta%201905",
                "public-domain printing; item-specific image rights and quality unreviewed", "medium", "SCAN_CANDIDATE",
                "identify a complete 1905 item and inspect pages 96–102", "no OCR retained", base)
    if key == ("1585", "001"):
        return ("No reusable transcription found; Hercher 1873 is a historical scan lead.", "", "",
                "Epistolographi Graeci (1873) scan candidate", "https://archive.org/search?query=Epistolographi%20Graeci%20Hercher%201873",
                "public-domain printing; item-specific image rights and quality unreviewed", "medium", "SCAN_CANDIDATE",
                "locate p.460 and inspect image quality", "no OCR retained", base)
    if key in {("2053", "001"), ("2053", "002"), ("2592", "004"), ("2592", "005"), ("2592", "007"), ("2592", "008")}:
        return ("No reusable open Greek text or rights-cleared scan verified for the cited modern edition.", *blank,
                "medium", "BLOCKED_RIGHTS", "seek an older independent edition or individual ancient witnesses",
                "modern scholarly edition excluded; no third-party OCR used", base)
    if key in {("2592", "001"), ("2592", "003")}:
        return ("No reusable transcription found; the nineteenth-century cited edition is a scan lead.", "", "",
                "exact historical edition scan candidate", "https://books.google.com/", "provider reuse not cleared", "medium", "SCAN_CANDIDATE",
                "locate the cited pages and assess a rights-cleared image source", "no OCR retained", base)
    if key == ("2592", "002"):
        return ("Exact 1866 edition digitized at BSB/DDB, but the image service is non-commercial only.", "", "",
                "Die Geometrie des Pediasimus", "https://www.deutsche-digitale-bibliothek.de/item/TSESDGGQDUWIALKD3C54EALHSLZQN7YR",
                "No Copyright – Non-Commercial Use Only", "high", "SCAN_RESTRICTED",
                "find an unrestricted duplicate or secure clearance", "do not ingest restricted image files", base)
    if key in {("2718", "001"), ("2718", "002"), ("2718", "003")}:
        url = "https://archive.org/details/carminaexcodicib01philuoft" if key == ("2718", "001") else "https://archive.org/search?query=Manuelis%20Philae%20Carmina"
        return ("Exact nineteenth-century edition has a complete digitized scan lead.", "", "",
                "historical edition scan candidate", url, "public-domain printing; provider image-reuse terms and quality unreviewed", "high", "SCAN_CANDIDATE",
                "verify cited range and stage remotely only after quality review", "no OCR retained", base)
    if key == ("1576", "001"):
        return ("Kinkel's 1877 collection is a historical scan lead; no transcription verified.", "", "",
                "Epicorum Graecorum fragmenta vol.1 scan candidate", "https://archive.org/search?query=Epicorum%20Graecorum%20fragmenta%20Kinkel%201877",
                "public-domain printing; item-specific image rights and quality unreviewed", "medium", "SCAN_CANDIDATE",
                "locate p.214 and inspect images", "no OCR retained", base)
    if key in {("1781", "001"), ("1781", "002")}:
        return ("Nineteenth-century comic-fragment edition is a scan lead; no transcription verified.", "", "",
                "exact historical edition scan candidate", "https://archive.org/search?query=Comicorum%20Atticorum%20fragmenta%20Kock",
                "public-domain printing; item-specific image rights and quality unreviewed", "medium", "SCAN_CANDIDATE",
                "locate the cited page and inspect images", "no OCR retained", base)
    if key in {("2962", "002"), ("2962", "004"), ("2962", "005")}:
        return ("The cited content is in PG 18, whose Commons scan is explicitly public domain.", "", "",
                "Patrologia Graeca 18 scan candidate", PG18, "Public Domain Mark 1.0", "high", "SCAN_CANDIDATE",
                "inspect target columns and source-image quality before remote ingestion", "historical PG witness, not the modern selection", "base-3; PG/Commons")
    if key == ("2962", "013"):
        return ("The cited content is in PG 36; a Commons volume collection is the scan lead.", "", "",
                "Patrologia Graeca 36 scan candidate", PG36, "Commons item-level rights must be checked", "medium", "SCAN_CANDIDATE",
                "identify the PG36 item, columns 895, and inspect images", "historical PG witness", "base-3; PG/Commons")

    # Current scholarly editions and articles are not treated as source texts.
    if any(year in notice for year in ("1926", "1928", "1933", "1938", "1941", "1950", "1951", "1958", "1963", "1964", "1969", "1971", "1972", "1973", "1976", "1980", "1981", "1983", "1987", "1989", "1992", "1995", "1998", "1999", "2004", "2011", "2013", "2020")):
        return ("No reusable open Greek text or rights-cleared scan verified for the cited modern edition.", *blank,
                "medium", "BLOCKED_RIGHTS", "seek an older independent edition or individual ancient witnesses",
                "modern scholarly edition excluded; no third-party OCR used", base)

    return ("No reusable open Greek text or exact high-quality scan verified.", *blank,
            "medium", "EDITION_IDENTIFIED", "continue item-level scan and witness search",
            "no third-party OCR used", base)


def main():
    fields = [
        "tlg_author_id", "tlg_work_id", "author_heading", "work_title", "canonical_edition",
        "sources_tested", "open_text_result", "open_text_url", "open_text_license", "scan_result",
        "scan_url", "scan_rights", "confidence", "proposed_status", "next_action", "notes", "last_checked",
    ]
    with OUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for ordinal, row in enumerate(selected_rows(), 1):
            (open_result, open_url, open_license, scan_result, scan_url, scan_rights,
             confidence, status, next_action, notes, sources) = result(row, ordinal)
            writer.writerow({
                "tlg_author_id": row["tlg_author_id"], "tlg_work_id": row["tlg_work_id"],
                "author_heading": row["author_heading"], "work_title": row["work_title"],
                "canonical_edition": row["bibliographic_notice"], "sources_tested": sources,
                "open_text_result": open_result, "open_text_url": open_url,
                "open_text_license": open_license, "scan_result": scan_result,
                "scan_url": scan_url, "scan_rights": scan_rights, "confidence": confidence,
                "proposed_status": status, "next_action": next_action, "notes": notes,
                "last_checked": "2026-08-11",
            })


if __name__ == "__main__":
    main()
