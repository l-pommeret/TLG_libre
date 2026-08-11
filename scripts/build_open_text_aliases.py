#!/usr/bin/env python3
"""Validate journaled alternate-edition links against local verified TEI files."""

from __future__ import annotations

import csv
import glob
import re
from pathlib import Path
from urllib.parse import unquote

from lxml import etree


ALTERNATE_MARKERS = ("DIFFERENT_EDITION", "ALTERNATE_EDITION", "CROSS_REFERENCE_OPEN_ALTERNATE")
URN = re.compile(r"urn:cts:(?:greekLit|pta):[A-Za-z0-9_-]+[.][A-Za-z0-9_-]+[.][A-Za-z0-9_-]+")
GITHUB_TEI = re.compile(r"/data/([^/]+)/([^/]+)/\1[.]\2[.]([^/.]+(?:-[^/.]+)*)[.]xml")
AG_LOCUS = re.compile(r"(\d{1,2})[.](\d{1,4})(?:\s*[–-]\s*(\d{1,4}))?")


def urns(value: str) -> set[str]:
    decoded = unquote(value)
    found = set(URN.findall(decoded))
    for group, work, version in GITHUB_TEI.findall(decoded):
        namespace = "pta" if group.startswith("pta") else "greekLit"
        found.add(f"urn:cts:{namespace}:{group}.{work}.{version}")
    return found


def verified_text_url(row: dict[str, str]) -> str:
    if row["text_url"]:
        return row["text_url"]
    if row["corpus"] == "First1KGreek" and row["source_revision"] and row["local_path"]:
        relative = row["local_path"].removeprefix("sources/upstream/first1kgreek/")
        return (
            "https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/"
            f"{row['source_revision']}/{relative}"
        )
    return ""


def anthology_loci(notice: str) -> list[tuple[int, int]]:
    if "AG:" not in notice:
        return []
    citation = notice.split("AG:", 1)[1].split(". Q:", 1)[0]
    results = []
    for match in AG_LOCUS.finditer(citation):
        book = int(match.group(1))
        start = int(match.group(2))
        end = int(match.group(3) or match.group(2))
        results.extend((book, number) for number in range(start, end + 1))
    return results


def anthology_attributions(path: str) -> dict[tuple[int, int], set[str]]:
    root = etree.parse(path).getroot()
    results: dict[tuple[int, int], set[str]] = {}
    for div in root.iter():
        if not str(div.tag).endswith("div") or div.attrib.get("subtype") != "epigram":
            continue
        base = div.attrib.get("{http://www.w3.org/XML/1998/namespace}base", "")
        book = re.search(r":(\d+)$", base)
        number = div.attrib.get("n", "")
        if not book or not number.isdigit():
            continue
        results[(int(book.group(1)), int(number))] = {
            item.attrib.get("key", "")
            for item in div.iter()
            if str(item.tag).endswith("persName") and item.attrib.get("key")
        }
    return results


def main() -> None:
    verification = list(csv.DictReader(Path("data/text_verification.csv").open(encoding="utf-8")))
    passed = {row["cts_urn"]: row for row in verification
              if row["automated_check"] == "AUTOMATED_TEI_CHECK_PASSED"}
    canon = {
        (row["tlg_author_id"], row["tlg_work_id"]): row
        for row in csv.DictReader(Path("data/canon_coverage.csv").open(encoding="utf-8"))
        if row["record_type"] == "work"
    }
    anthology_cache: dict[str, dict[tuple[int, int], set[str]]] = {}
    records = {}
    for filename in sorted(glob.glob("data/research_batches/*.csv")):
        try:
            rows = csv.DictReader(Path(filename).open(encoding="utf-8"))
            for row in rows:
                status = row.get("proposed_status", "")
                alternate = any(marker in status for marker in ALTERNATE_MARKERS)
                anthology_candidate = status in {"TEXT_OPEN_UNVERIFIED", "OPEN_TEXT_AVAILABLE"}
                if not alternate and not anthology_candidate:
                    continue
                target = (row.get("tlg_author_id", ""), row.get("tlg_work_id", ""))
                url = row.get("open_text_url", "")
                for source_urn in urns(url):
                    source = passed.get(source_urn)
                    if not source:
                        continue
                    relationship = "VERIFIED_ALTERNATE_EDITION"
                    verification_scope = "verified TEI, URN, Greek content, license and journaled edition relation"
                    if anthology_candidate:
                        if "tlg7000.tlg001" not in source_urn or target not in canon:
                            continue
                        loci = anthology_loci(canon[target]["bibliographic_notice"])
                        if not loci:
                            continue
                        if source["local_path"] not in anthology_cache:
                            anthology_cache[source["local_path"]] = anthology_attributions(
                                source["local_path"]
                            )
                        attributions = anthology_cache[source["local_path"]]
                        expected_author = f"tlg-{target[0]}"
                        if not all(expected_author in attributions.get(locus, set()) for locus in loci):
                            continue
                        relationship = "VERIFIED_ANTHOLOGY_LOCUS_AND_ATTRIBUTION"
                        verification_scope = "all Canon AG loci present with matching TEI tlg author key"
                    key = target + (source_urn,)
                    records[key] = {
                        "tlg_author_id": target[0], "tlg_work_id": target[1],
                        "relationship": relationship,
                        "journal_status": status, "source_urn": source_urn,
                        "source_url": verified_text_url(source), "source_local_path": source["local_path"],
                        "source_sha256": source["sha256"],
                        "source_license": source["tei_license"] or source["license"],
                        "verification_scope": verification_scope,
                        "evidence_file": filename,
                    }
        except (csv.Error, UnicodeDecodeError):
            continue
    output = Path("data/open_text_aliases.csv")
    fields = ("tlg_author_id", "tlg_work_id", "relationship", "journal_status", "source_urn",
              "source_url", "source_local_path", "source_sha256", "source_license",
              "verification_scope", "evidence_file")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(records[key] for key in sorted(records))
    print(f"verified_alternate_aliases={len(records)} target_keys={len({key[:2] for key in records})}")


if __name__ == "__main__":
    main()
