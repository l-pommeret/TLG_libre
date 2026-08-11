#!/usr/bin/env python3
"""Sparse-checkout the TEI files referenced by corpus_matches.csv."""

from __future__ import annotations

import csv
from pathlib import Path
import re
import subprocess


REPOS = {
    "First1KGreek": ("https://github.com/OpenGreekAndLatin/First1KGreek.git", Path("sources/upstream/first1kgreek")),
    "Perseus": ("https://github.com/PerseusDL/canonical-greekLit.git", Path("sources/upstream/perseus-canonical-greekLit")),
    "PTA": ("https://github.com/PatristicTextArchive/pta_data.git", Path("sources/upstream/pta_data")),
}


def urn_path(urn: str) -> str:
    parts = urn.split(":")[-1].split(".")
    if len(parts) < 3:
        raise ValueError(f"edition-level CTS URN required: {urn}")
    group, work, version = parts[:3]
    return f"data/{group}/{work}/{group}.{work}.{version}.xml"


def run() -> None:
    with Path("data/corpus_matches.csv").open(encoding="utf-8") as src:
        rows = list(csv.DictReader(src))
    by_corpus: dict[str, set[str]] = {name: set() for name in REPOS}
    for row in rows:
        by_corpus[row["corpus"]].add(urn_path(row["cts_urn"]))
    for corpus, (url, repo) in REPOS.items():
        if not (repo / ".git").exists():
            repo.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", url, str(repo)], check=True)
        patterns = {"/README*", "/LICENSE*", "/license*"}
        for rel in by_corpus[corpus]:
            patterns.add("/" + rel)
            parent = Path(rel).parent
            patterns.add("/" + (parent / "__cts__.xml").as_posix())
            patterns.add("/" + (parent.parent / "__cts__.xml").as_posix())
        payload = "\n".join(sorted(patterns)) + "\n"
        subprocess.run(
            ["git", "-C", str(repo), "sparse-checkout", "set", "--no-cone", "--stdin"],
            input=payload, text=True, check=True,
        )
        missing = sum(not (repo / rel).exists() for rel in by_corpus[corpus])
        print(f"{corpus}: requested={len(by_corpus[corpus])} missing={missing}")


if __name__ == "__main__":
    run()
