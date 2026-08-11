#!/usr/bin/env python3
"""Repair stale First1K URNs and materialize their pinned, non-OCR TEI files."""

from __future__ import annotations

import csv
import subprocess
import tempfile
from pathlib import Path


REPO = "https://github.com/OpenGreekAndLatin/First1KGreek.git"
REVISION = "bfea9acd07ee1b7cea70cdd927c8f092d5637695"
DESTINATION = Path("sources/upstream/first1kgreek")

# Old catalog URN -> actual edition suffix at the pinned revision.
REPAIRS = {
    "urn:cts:greekLit:tlg0059.tlg037.First1K-grc1": "1st1K-grc1",
    **{f"urn:cts:greekLit:tlg0527.tlg{work}.opp-grc2":
       ("1st1K-grc2" if work in {"034", "048"} else "1st1K-grc1")
       for work in ("001", "002", "003", "004", "005", "006", "008", "010", "011", "012", "013", "014", "034", "048")},
    "urn:cts:greekLit:tlg2050.tlg001.opp-grc1": "1st1K-grc1",
    "urn:cts:greekLit:tlg2200.tlg001.opp-grc1": "1st1K-grc1",
    "urn:cts:greekLit:tlg2200.tlg008.opp-grc1": "1st1K-grc1",
    "urn:cts:greekLit:tlg4017.tlg001.opp-grc1": "1st1K-grc1",
}

# No distributable data/ TEI exists at the pinned revision. The tlg9006 split
# artifact explicitly declares third-party OCR and is intentionally excluded.
DROP = {
    "urn:cts:greekLit:tlg0086.tlg034.1st1K-grc1",
    "urn:cts:greekLit:tlg0555.tlg004.1st1K-grc1",
    "urn:cts:greekLit:tlg9006.tlg011.opp-grc1",
}


def relative_path(urn: str) -> Path:
    group, work, version = urn.rsplit(":", 1)[1].split(".")[:3]
    return Path("data") / group / work / f"{group}.{work}.{version}.xml"


def main() -> None:
    catalog = Path("data/corpus_matches.csv")
    with catalog.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames
        rows = list(reader)
    repaired: list[tuple[str, Path]] = []
    retained = []
    for row in rows:
        old = row["cts_urn"]
        if old in DROP:
            continue
        if old in REPAIRS:
            prefix = old.rsplit(".", 1)[0]
            new = f"{prefix}.{REPAIRS[old]}"
            row["cts_urn"] = new
            row["text_url"] = row["text_url"].replace(old, new)
            repaired.append((new, relative_path(new)))
        retained.append(row)
    if len(repaired) != len(REPAIRS):
        raise RuntimeError(f"expected {len(REPAIRS)} stale rows, found {len(repaired)}")
    if len(rows) - len(retained) != len(DROP):
        raise RuntimeError(f"expected {len(DROP)} non-materializable rows")

    with tempfile.TemporaryDirectory(prefix="tlg-first1k-repair-") as raw:
        clone = Path(raw) / "repo"
        subprocess.run(["git", "clone", "--filter=blob:none", "--no-checkout", "--quiet",
                        REPO, str(clone)], check=True)
        subprocess.run(["git", "-C", str(clone), "fetch", "--quiet", "--depth", "1",
                        "origin", REVISION], check=True)
        for urn, relative in repaired:
            blob = subprocess.check_output(["git", "-C", str(clone), "show",
                                            f"FETCH_HEAD:{relative.as_posix()}"])
            destination = DESTINATION / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(blob)
            if b"OCR-ed" in blob or b"OCRed" in blob:
                raise RuntimeError(f"OCR-derived TEI rejected: {urn}")

    with catalog.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(retained)
    print(f"repaired={len(repaired)} dropped={len(DROP)} catalog_rows={len(retained)}")


if __name__ == "__main__":
    main()
