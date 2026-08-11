#!/usr/bin/env python3
"""Summarize verified open-text and archived-scan coverage of Canon work notices."""

from __future__ import annotations

import csv
from collections import Counter
from datetime import date
from pathlib import Path


TEXT_STATUSES = {
    "TEXT_OPEN_VERIFIED_IDENTIFIER_MATCH",
    "TEXT_OPEN_VERIFIED_ALTERNATE_EDITION",
}


def pct(value: int, total: int) -> str:
    return f"{100 * value / total:.2f} %".replace(".", ",")


def main() -> None:
    canon = [
        row for row in csv.DictReader(Path("data/canon_coverage.csv").open(encoding="utf-8"))
        if row["record_type"] == "work"
    ]
    scans = list(csv.DictReader(Path("data/scan_work_coverage.csv").open(encoding="utf-8")))
    scan_keys = {(row["tlg_author_id"], row["tlg_work_id"]) for row in scans}
    fragments = list(csv.DictReader(Path("data/open_text_fragments.csv").open(encoding="utf-8")))
    fragment_keys = {(row["tlg_author_id"], row["tlg_work_id"]) for row in fragments}
    if any(not row["hf_archives"] for row in scans):
        raise SystemExit("a scan mapping lacks a verified HF archive")

    categories = Counter()
    exact_text = 0
    alternate_text = 0
    partial_without_complete = 0
    partial_without_complete_or_scan = 0
    for row in canon:
        key = (row["tlg_author_id"], row["tlg_work_id"])
        text = row["pipeline_status"] in TEXT_STATUSES
        scan = key in scan_keys
        categories[(text, scan)] += 1
        exact_text += row["pipeline_status"] == "TEXT_OPEN_VERIFIED_IDENTIFIER_MATCH"
        alternate_text += row["pipeline_status"] == "TEXT_OPEN_VERIFIED_ALTERNATE_EDITION"
        partial_without_complete += key in fragment_keys and not text
        partial_without_complete_or_scan += key in fragment_keys and not text and not scan

    total = len(canon)
    text_only = categories[(True, False)]
    scan_only = categories[(False, True)]
    both = categories[(True, True)]
    neither = categories[(False, False)]
    assert text_only + scan_only + both + neither == total

    output = Path("data/coverage_summary.md")
    output.write_text(
        "\n".join([
            "# Couverture vérifiée du Canon TLG",
            "",
            f"Mise à jour : {date.today().isoformat()}",
            "",
            "Le dénominateur est constitué des notices `record_type=work`; les 1 536 renvois "
            "ne sont pas comptés comme œuvres autonomes.",
            "",
            "| Couverture | Notices | Pourcentage |",
            "|---|---:|---:|",
            f"| Texte grec ouvert vérifié, sans scan archivé | {text_only} | {pct(text_only, total)} |",
            f"| Scan grec archivé sur HF, sans texte vérifié | {scan_only} | {pct(scan_only, total)} |",
            f"| Texte vérifié et scan archivé | {both} | {pct(both, total)} |",
            f"| Ni texte vérifié ni scan archivé | {neither} | {pct(neither, total)} |",
            f"| **Total** | **{total}** | **100,00 %** |",
            "",
            "## Totaux transversaux",
            "",
            f"- Texte vérifié : {text_only + both} / {total} ({pct(text_only + both, total)}), "
            f"dont {exact_text} correspondances d’identifiant exactes et {alternate_text} éditions alternatives vérifiées.",
            f"- Scan archivé et rattaché explicitement : {scan_only + both} / {total} "
            f"({pct(scan_only + both, total)}).",
            f"- Texte hôte partiel vérifié, sans texte complet : {partial_without_complete} / {total} "
            f"({pct(partial_without_complete, total)}). Ces fragments ne sont pas comptés comme œuvres textuelles complètes.",
            f"- Au moins une ressource exploitable, fragments partiels inclus : "
            f"{total - neither + partial_without_complete_or_scan} / {total} "
            f"({pct(total - neither + partial_without_complete_or_scan, total)}).",
            "",
            "Les scans ne sont comptés que si leur mapping READY pointe vers une notice du Canon, "
            "si l’archive distante est enregistrée `MIGRATED_PUBLIC`, et si chaque archive HF est résolue. "
            "Une édition alternative textuelle reste séparée d’une correspondance exacte.",
            "",
        ]),
        encoding="utf-8",
    )
    print(
        f"works={total} text_only={text_only} scan_only={scan_only} both={both} "
        f"neither={neither}"
    )


if __name__ == "__main__":
    main()
