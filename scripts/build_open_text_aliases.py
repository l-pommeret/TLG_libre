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
        # Paton volumes 2–5 encode entries as ``epigram``; volume 1 uses
        # ``chapter`` while its CTS declaration still defines them as epigrams.
        if (
            not str(div.tag).endswith("div")
            or div.attrib.get("subtype") not in {"epigram", "chapter"}
        ):
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
    anthology_index: dict[tuple[int, int], dict[str, set[str]]] = {}
    for source_urn, source in passed.items():
        if "tlg7000.tlg001" not in source_urn:
            continue
        for locus, authors in anthology_attributions(source["local_path"]).items():
            anthology_index.setdefault(locus, {})[source_urn] = authors
    records = {}
    anthology_rejections: dict[tuple[str, str], dict[str, str]] = {}
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
                            anthology_rejections[target] = {
                                "tlg_author_id": target[0], "tlg_work_id": target[1],
                                "required_loci": "", "unresolved_loci": "",
                                "observed_attributions": "",
                                "reason": "NO_PARSEABLE_AG_LOCUS_IN_CANON_NOTICE",
                                "evidence_file": filename,
                            }
                            continue
                        expected_author = f"tlg-{target[0]}"
                        matching_sources = {
                            locus: {
                                urn for urn, authors in anthology_index.get(locus, {}).items()
                                if expected_author in authors
                            }
                            for locus in loci
                        }
                        if not all(matching_sources.values()):
                            unresolved = [locus for locus, sources in matching_sources.items() if not sources]
                            observed = {
                                f"{book}.{number}": sorted(set().union(*anthology_index.get((book, number), {}).values()))
                                for book, number in unresolved
                            }
                            anthology_rejections[target] = {
                                "tlg_author_id": target[0], "tlg_work_id": target[1],
                                "required_loci": ";".join(f"{book}.{number}" for book, number in loci),
                                "unresolved_loci": ";".join(
                                    f"{book}.{number}" for book, number in unresolved
                                ),
                                "observed_attributions": ";".join(
                                    f"{locus}={'|'.join(values) if values else 'MISSING'}"
                                    for locus, values in observed.items()
                                ),
                                "reason": "LOCUS_MISSING_OR_TLG_ATTRIBUTION_MISMATCH",
                                "evidence_file": filename,
                            }
                            continue
                        relationship = "VERIFIED_ANTHOLOGY_LOCUS_AND_ATTRIBUTION"
                        verification_scope = "all Canon AG loci present with matching TEI tlg author key"
                        for contributor_urn in sorted(set().union(*matching_sources.values())):
                            contributor = passed[contributor_urn]
                            key = target + (contributor_urn,)
                            records[key] = {
                                "tlg_author_id": target[0], "tlg_work_id": target[1],
                                "relationship": relationship,
                                "journal_status": status, "source_urn": contributor_urn,
                                "source_url": verified_text_url(contributor),
                                "source_local_path": contributor["local_path"],
                                "source_sha256": contributor["sha256"],
                                "source_license": contributor["tei_license"] or contributor["license"],
                                "verification_scope": verification_scope,
                                "evidence_file": filename,
                            }
                        continue
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

    manual_path = Path("data/open_text_manual_promotions.csv")
    for row in csv.DictReader(manual_path.open(encoding="utf-8")):
        source_urn = row["source_urn"]
        source = passed.get(source_urn)
        if not source:
            raise SystemExit(f"manual promotion source did not pass TEI verification: {source_urn}")
        target = (row["tlg_author_id"], row["tlg_work_id"])
        if target not in canon:
            raise SystemExit(f"manual promotion target is absent from Canon works: {target}")
        key = target + (source_urn,)
        records[key] = {
            "tlg_author_id": target[0], "tlg_work_id": target[1],
            "relationship": row["relationship"],
            "journal_status": "MANUALLY_PROMOTED_COMPLETE_HOST_WITNESS",
            "source_urn": source_urn,
            "source_url": verified_text_url(source),
            "source_local_path": source["local_path"],
            "source_sha256": source["sha256"],
            "source_license": source["tei_license"] or source["license"],
            "verification_scope": row["verification_scope"],
            "evidence_file": row["evidence_file"],
        }
    output = Path("data/open_text_aliases.csv")
    fields = ("tlg_author_id", "tlg_work_id", "relationship", "journal_status", "source_urn",
              "source_url", "source_local_path", "source_sha256", "source_license",
              "verification_scope", "evidence_file")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(records[key] for key in sorted(records))
    accepted_anthology = {
        (row["tlg_author_id"], row["tlg_work_id"])
        for row in records.values()
        if row["relationship"] == "VERIFIED_ANTHOLOGY_LOCUS_AND_ATTRIBUTION"
    }
    rejection_path = Path("data/open_text_anthology_rejections.csv")
    rejection_fields = (
        "tlg_author_id", "tlg_work_id", "required_loci", "unresolved_loci",
        "observed_attributions", "reason", "evidence_file",
    )
    with rejection_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=rejection_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(
            anthology_rejections[key]
            for key in sorted(anthology_rejections)
            if key not in accepted_anthology
        )
    print(f"verified_alternate_aliases={len(records)} target_keys={len({key[:2] for key in records})}")


if __name__ == "__main__":
    main()
