#!/usr/bin/env python3
"""Build an auditable Canon-work mapping for scans already archived on HF."""

from __future__ import annotations

import csv
import glob
import re
from collections import defaultdict
from pathlib import Path


ID = re.compile(
    r"(?<!\d)(\d{4})[.](\d{3}|x\d{2})(?:\s*[-–—]\s*[.]?(\d{3}|x\d{2}))?"
    r"|(?<!\w)[.](\d{3}|x\d{2})(?:\s*[-–—]\s*[.]?(\d{3}|x\d{2}))?"
)


def expand_ids(text: str) -> list[tuple[str, str]]:
    """Expand full identifiers and printed shorthand such as 3115.009–010, .018."""
    results: list[tuple[str, str]] = []
    current_author = ""
    for match in ID.finditer(text):
        if match.group(1):
            author, start, end = match.group(1), match.group(2), match.group(3)
            current_author = author
        else:
            if not current_author:
                continue
            author, start, end = current_author, match.group(4), match.group(5)
        if end and start.isdigit() and end.isdigit():
            results.extend((author, f"{value:03d}") for value in range(int(start), int(end) + 1))
        else:
            results.append((author, start))
    return results


def expand_registry_ids(author_field: str, work_field: str) -> list[tuple[str, str]]:
    authors = author_field.split("|")
    work_groups = work_field.split("|")
    if len(authors) != len(work_groups):
        raise ValueError(f"unpaired registry identifiers: {author_field!r} {work_field!r}")
    results = []
    for author, group in zip(authors, work_groups):
        synthetic = f"{author}." + group.replace(";", f"; {author}.")
        results.extend(expand_ids(synthetic))
    return results


def report_mappings(path: Path) -> set[tuple[str, str]]:
    """Read only positive mapping tables/prose; REVIEW and exclusion rows are ignored."""
    results: set[tuple[str, str]] = set()
    active_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        lower = line.lower()
        if line.startswith("#"):
            active_table = (
                any(marker in lower for marker in ("mapping", "concordance"))
                and not any(marker in lower for marker in ("review", "exclu", "non reten"))
            )
            continue
        if active_table and line.startswith("|"):
            if any(marker in lower for marker in ("review", "exclu", "non reten")):
                continue
            first_cell = line.split("|")[1]
            # Parenthetical "sauf .109" is an exclusion, not another mapping.
            first_cell = re.split(r"\bsauf\b", first_cell, flags=re.IGNORECASE)[0]
            results.update(expand_ids(first_cell))
            continue
        if any(marker in lower for marker in ("mapping direct :", "mapping :", "concordance :")):
            positive = re.split(
                r"\b(?:les textes|exclu(?:re|s)?|review|ne sont que)\b",
                line,
                maxsplit=1,
                flags=re.IGNORECASE,
            )[0]
            results.update(expand_ids(positive))
    return results


def pg_report(identifier: str) -> Path:
    match = re.search(r"Vol[.]_(\d{3})", identifier)
    if not match:
        raise ValueError(f"cannot derive PG volume from {identifier}")
    volume = str(int(match.group(1)))
    matches = [Path(item) for item in glob.glob(f"data/research_batches/scan_validation_pg{volume}_*.md")]
    if len(matches) != 1:
        raise ValueError(f"expected one PG{volume} report, found {matches}")
    return matches[0]


def main() -> None:
    canon_rows = list(csv.DictReader(Path("data/canon_coverage.csv").open(encoding="utf-8")))
    all_canon = {(row["tlg_author_id"], row["tlg_work_id"]) for row in canon_rows}
    canon = {
        (row["tlg_author_id"], row["tlg_work_id"])
        for row in canon_rows if row["record_type"] == "work"
    }
    migrations = list(csv.DictReader(Path("data/hf_scan_migrations.csv").open(encoding="utf-8")))
    archives_by_root: dict[str, list[str]] = defaultdict(list)
    for row in migrations:
        if row["status"] == "MIGRATED_PUBLIC":
            archives_by_root[row["source_root"]].append(row["archive"])

    def archived_descendants(root: str) -> list[str]:
        archives = []
        prefix = root.rstrip("/") + "/"
        for migrated_root, names in archives_by_root.items():
            if migrated_root == root or migrated_root.startswith(prefix):
                archives.extend(names)
        return sorted(set(archives))

    records: dict[tuple[str, str, str], dict[str, str]] = {}
    missing: list[tuple[str, str, str]] = []
    for source in csv.DictReader(Path("data/scan_sources.csv").open(encoding="utf-8")):
        if source["storage_status"] != "HF_ARCHIVED_PUBLIC":
            continue
        if source["tlg_author_id"] == "multiple":
            report = pg_report(source["scan_identifier"])
            keys = report_mappings(report)
            evidence = str(report)
            mapping_type = "READY_REPORT_EXACT_MAPPING"
        else:
            keys = set(expand_registry_ids(source["tlg_author_id"], source["tlg_work_id"]))
            evidence = "data/scan_sources.csv"
            mapping_type = "ARCHIVED_DIRECT_REGISTRY_MAPPING"
        for author, work in keys:
            if (author, work) not in canon:
                if (author, work) not in all_canon:
                    missing.append((author, work, evidence))
                continue
            key = (author, work, source["scan_identifier"])
            records[key] = {
                "tlg_author_id": author,
                "tlg_work_id": work,
                "mapping_type": mapping_type,
                "scan_identifier": source["scan_identifier"],
                "hf_repo": "Zual/TLG_libre_scans",
                "source_root": source["github_path"],
                "hf_archives": ";".join(archived_descendants(source["github_path"])),
                "rights": source["rights"],
                "quality_status": source["quality_status"],
                "evidence_file": evidence,
            }
    if missing:
        preview = ", ".join(f"{a}.{w} ({e})" for a, w, e in missing[:10])
        raise SystemExit(f"scan mappings absent from Canon: {preview}")

    fields = (
        "tlg_author_id", "tlg_work_id", "mapping_type", "scan_identifier", "hf_repo",
        "source_root", "hf_archives", "rights", "quality_status", "evidence_file",
    )
    output = Path("data/scan_work_coverage.csv")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records[key] for key in sorted(records))
    works = {(row[0], row[1]) for row in records}
    print(f"scan_mappings={len(records)} unique_canon_keys={len(works)}")


if __name__ == "__main__":
    main()
