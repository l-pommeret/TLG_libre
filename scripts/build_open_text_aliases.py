#!/usr/bin/env python3
"""Validate journaled alternate-edition links against local verified TEI files."""

from __future__ import annotations

import csv
import glob
import re
from pathlib import Path
from urllib.parse import unquote


ALTERNATE_MARKERS = ("DIFFERENT_EDITION", "ALTERNATE_EDITION", "CROSS_REFERENCE_OPEN_ALTERNATE")
URN = re.compile(r"urn:cts:(?:greekLit|pta):[A-Za-z0-9_-]+[.][A-Za-z0-9_-]+[.][A-Za-z0-9_-]+")
GITHUB_TEI = re.compile(r"/data/([^/]+)/([^/]+)/\1[.]\2[.]([^/.]+(?:-[^/.]+)*)[.]xml")


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


def main() -> None:
    verification = list(csv.DictReader(Path("data/text_verification.csv").open(encoding="utf-8")))
    passed = {row["cts_urn"]: row for row in verification
              if row["automated_check"] == "AUTOMATED_TEI_CHECK_PASSED"}
    records = {}
    for filename in sorted(glob.glob("data/research_batches/*.csv")):
        try:
            rows = csv.DictReader(Path(filename).open(encoding="utf-8"))
            for row in rows:
                status = row.get("proposed_status", "")
                if not any(marker in status for marker in ALTERNATE_MARKERS):
                    continue
                target = (row.get("tlg_author_id", ""), row.get("tlg_work_id", ""))
                url = row.get("open_text_url", "")
                for source_urn in urns(url):
                    source = passed.get(source_urn)
                    if not source:
                        continue
                    key = target + (source_urn,)
                    records[key] = {
                        "tlg_author_id": target[0], "tlg_work_id": target[1],
                        "relationship": "VERIFIED_ALTERNATE_EDITION",
                        "journal_status": status, "source_urn": source_urn,
                        "source_url": verified_text_url(source), "source_local_path": source["local_path"],
                        "source_sha256": source["sha256"],
                        "source_license": source["tei_license"] or source["license"],
                        "evidence_file": filename,
                    }
        except (csv.Error, UnicodeDecodeError):
            continue
    output = Path("data/open_text_aliases.csv")
    fields = ("tlg_author_id", "tlg_work_id", "relationship", "journal_status", "source_urn",
              "source_url", "source_local_path", "source_sha256", "source_license", "evidence_file")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader(); writer.writerows(records[key] for key in sorted(records))
    print(f"verified_alternate_aliases={len(records)} target_keys={len({key[:2] for key in records})}")


if __name__ == "__main__":
    main()
