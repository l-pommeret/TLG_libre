#!/usr/bin/env python3
"""Perform reproducible structural checks on matched TEI editions."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import re

from lxml import etree

from fetch_matched_texts import REPOS, urn_path


GREEK = re.compile(r"[\u0370-\u03ff\u1f00-\u1fff]")


def check(row: dict[str, str]) -> dict[str, str]:
    repo = REPOS[row["corpus"]][1]
    rel = urn_path(row["cts_urn"])
    path = repo / rel
    result = dict(row)
    result.update({"local_path": str(path), "sha256": "", "file_bytes": "0",
                   "greek_characters": "0", "tei_license": "", "automated_check": "MISSING_FILE",
                   "quality_notes": "file_not_found"})
    if not path.exists():
        return result
    raw = path.read_bytes()
    result["sha256"] = hashlib.sha256(raw).hexdigest()
    result["file_bytes"] = str(len(raw))
    try:
        root = etree.fromstring(raw, parser=etree.XMLParser(resolve_entities=False, no_network=True, huge_tree=True))
    except etree.XMLSyntaxError as exc:
        result["automated_check"] = "INVALID_XML"
        result["quality_notes"] = str(exc).replace("\n", " ")[:500]
        return result
    body_text = " ".join(root.xpath("//*[local-name()='text']//text()"))
    greek_count = len(GREEK.findall(body_text))
    result["greek_characters"] = str(greek_count)
    licenses = root.xpath("//*[local-name()='availability']//*[local-name()='licence']/@target | //*[local-name()='availability']//*[local-name()='licence']//text()")
    result["tei_license"] = " ".join(str(x).strip() for x in licenses if str(x).strip())
    notes = []
    if root.tag.split("}")[-1].lower() != "tei":
        notes.append("root_not_tei")
    if greek_count == 0:
        notes.append("no_greek_in_text")
    elif greek_count < 100:
        notes.append("very_short_fragment_manual_review")
    declared = row["cts_urn"]
    urn_values = root.xpath("//@* | //*[local-name()='idno']//text()")
    if not any(declared in str(value) for value in urn_values):
        notes.append("edition_urn_not_found_in_tei")
    if not result["tei_license"] and row["license"] == "REVIEW_REQUIRED":
        notes.append("license_not_declared_in_tei")
    result["quality_notes"] = ";".join(notes)
    result["automated_check"] = "AUTOMATED_TEI_CHECK_PASSED" if not notes else "MANUAL_REVIEW_REQUIRED"
    return result


def main() -> None:
    with Path("data/corpus_matches.csv").open(encoding="utf-8") as src:
        rows = list(csv.DictReader(src))
    checked = [check(row) for row in rows]
    fields = list(checked[0])
    with Path("data/text_verification.csv").open("w", encoding="utf-8", newline="") as dst:
        writer = csv.DictWriter(dst, fieldnames=fields)
        writer.writeheader(); writer.writerows(checked)
    print(f"checked {len(checked)} TEI editions")


if __name__ == "__main__":
    main()
