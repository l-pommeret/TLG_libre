#!/usr/bin/env python3
"""Create exact TLG/CTS matches against major open Greek corpora.

Only explicit TLG identifiers are accepted.  Title-only similarities belong in
a later candidate table and must never change a work's pipeline status.
"""

from __future__ import annotations

import argparse
import csv
from html import unescape
import json
from pathlib import Path
import re


TLG_URN = re.compile(r"urn:cts:[^:]+:tlg(\d{4})\.tlg([0-9x]\d{2})(?:\.([^:\s\"']+))?")
TLG_IDENTIFIER = re.compile(r"TLG:tlg(\d{4})\.tlg([0-9x]\d{2})", re.I)


def plain(xml: str) -> str:
    return re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", "", xml))).strip()


def tag_text(xml: str, local: str) -> str:
    match = re.search(rf"<(?:\w+:)?{local}\b[^>]*>(.*?)</(?:\w+:)?{local}>", xml, re.S | re.I)
    return plain(match.group(1)) if match else ""


def attr(tag: str, name: str) -> str:
    match = re.search(rf"\b{name}=[\"']([^\"']+)", tag, re.I)
    return unescape(match.group(1)) if match else ""


def revision(repo: Path) -> str:
    head = repo / ".git" / "refs" / "heads" / "master"
    if not head.exists():
        head = repo / ".git" / "refs" / "heads" / "public"
    if not head.exists():
        head = repo / ".git" / "refs" / "heads" / "main"
    return head.read_text().strip() if head.exists() else ""


def first1k(path: Path) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for item in data["catalog"]:
        match = TLG_URN.search(item.get("urn", ""))
        if not match or not match.group(3) or "grc" not in match.group(3).lower():
            continue
        rows.append({
            "tlg_author_id": match.group(1), "tlg_work_id": match.group(2),
            "corpus": "First1KGreek", "cts_urn": item["urn"],
            "corpus_author": item.get("group_name", ""),
            "corpus_title": item.get("work_name", ""),
            "edition_description": "", "language": item.get("language", ""),
            "word_count": str(item.get("wordcount", "")),
            "text_url": item.get("scaife", ""),
            "metadata_url": "https://github.com/OpenGreekAndLatin/First1KGreek",
            "license": "REVIEW_REQUIRED", "source_revision": "bfea9acd07ee1b7cea70cdd927c8f092d5637695",
        })
    return rows


def cts_repo(repo: Path, corpus: str, web_repo: str) -> list[dict[str, str]]:
    rows = []
    rev = revision(repo)
    groupnames: dict[str, str] = {}
    for path in repo.glob("data/*/__cts__.xml"):
        xml = path.read_text(encoding="utf-8")
        urn = attr(re.search(r"<(?:\w+:)?textgroup\b[^>]*>", xml, re.I).group(0), "urn") if "textgroup" in xml else ""
        groupnames[urn] = tag_text(xml, "groupname")
    for path in repo.glob("data/*/*/__cts__.xml"):
        xml = path.read_text(encoding="utf-8")
        work_tag_match = re.search(r"<(?:\w+:)?work\b[^>]*>", xml, re.I)
        if not work_tag_match:
            continue
        work_tag = work_tag_match.group(0)
        work_urn = attr(work_tag, "urn")
        direct = TLG_URN.search(work_urn)
        explicit = TLG_IDENTIFIER.search(xml)
        match = direct or explicit
        if not match:
            continue
        group_urn = attr(work_tag, "groupUrn")
        title = tag_text(xml, "title")
        for edition_match in re.finditer(r"<(?:(?:\w+):)?edition\b([^>]*)>(.*?)</(?:(?:\w+):)?edition>", xml, re.S | re.I):
            edition_tag, body = edition_match.groups()
            urn = attr(edition_tag, "urn")
            if "grc" not in attr(edition_tag, "lang").lower() and "grc" not in urn.lower():
                continue
            rights = tag_text(body, "rights")
            license_value = rights or ("CC BY-SA 4.0 (repository default; verify file)" if corpus == "Perseus" else "REVIEW_REQUIRED")
            rel = path.relative_to(repo).as_posix()
            rows.append({
                "tlg_author_id": match.group(1), "tlg_work_id": match.group(2),
                "corpus": corpus, "cts_urn": urn, "corpus_author": groupnames.get(group_urn, ""),
                "corpus_title": tag_text(body, "label") or title,
                "edition_description": tag_text(body, "description") or tag_text(body, "source"),
                "language": "grc", "word_count": "",
                "text_url": (f"https://pta.bbaw.de/text/{urn}" if corpus == "PTA" else f"https://scaife.perseus.org/reader/{urn}"),
                "metadata_url": f"{web_repo}/blob/{rev}/{rel}",
                "license": license_value, "source_revision": rev,
            })
    return rows


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--canon", type=Path, default=Path("data/canon_works.csv"))
    ap.add_argument("--output", type=Path, default=Path("data/corpus_matches.csv"))
    ap.add_argument("--coverage-output", type=Path, default=Path("data/canon_coverage.csv"))
    args = ap.parse_args()
    rows = first1k(Path("sources/catalogs/first1kgreek_catalog.json"))
    rows += cts_repo(Path("sources/upstream/perseus-canonical-greekLit"), "Perseus", "https://github.com/PerseusDL/canonical-greekLit")
    rows += cts_repo(Path("sources/upstream/pta_data"), "PTA", "https://github.com/PatristicTextArchive/pta_data")
    with args.canon.open(encoding="utf-8") as src:
        canon_rows = list(csv.DictReader(src))
    canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in canon_rows}
    for row in rows:
        key = (row["tlg_author_id"], row["tlg_work_id"])
        row["in_printed_inventory"] = "yes" if key in canon else "no"
        row["match_method"] = "explicit_tlg_identifier"
        row["match_confidence"] = "exact_identifier"
        row["verification_status"] = "METADATA_MATCH_UNVERIFIED_TEXT"
    rows.sort(key=lambda r: (r["tlg_author_id"], r["tlg_work_id"], r["corpus"], r["cts_urn"]))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fields = ["tlg_author_id", "tlg_work_id", "corpus", "cts_urn", "corpus_author",
              "corpus_title", "edition_description", "language", "word_count", "text_url",
              "metadata_url", "license", "source_revision", "in_printed_inventory",
              "match_method", "match_confidence", "verification_status"]
    with args.output.open("w", encoding="utf-8", newline="") as dst:
        writer = csv.DictWriter(dst, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    by_key: dict[tuple[str, str], list[dict[str, str]]] = {}
    for row in rows:
        by_key.setdefault((row["tlg_author_id"], row["tlg_work_id"]), []).append(row)
    coverage_fields = list(canon_rows[0]) + ["exact_match_count", "matched_corpora", "matched_urns"]
    for row in canon_rows:
        found = by_key.get((row["tlg_author_id"], row["tlg_work_id"]), [])
        row["exact_match_count"] = str(len(found))
        row["matched_corpora"] = ";".join(sorted({m["corpus"] for m in found}))
        row["matched_urns"] = ";".join(m["cts_urn"] for m in found)
        if found:
            row["pipeline_status"] = "TEXT_OPEN_UNVERIFIED"
            row["next_action"] = "verify_text_edition_license"
    with args.coverage_output.open("w", encoding="utf-8", newline="") as dst:
        writer = csv.DictWriter(dst, fieldnames=coverage_fields)
        writer.writeheader(); writer.writerows(canon_rows)
    print(f"wrote {len(rows)} exact edition matches to {args.output}")


if __name__ == "__main__":
    main()
