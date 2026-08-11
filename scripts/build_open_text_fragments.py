#!/usr/bin/env python3
"""Materialize high-confidence partial host texts without calling them complete works."""

from __future__ import annotations

import csv
import glob
from pathlib import Path

from build_open_text_aliases import urns, verified_text_url


PASSED = "AUTOMATED_TEI_CHECK_PASSED"


def main() -> None:
    verification = list(csv.DictReader(Path("data/text_verification.csv").open(encoding="utf-8")))
    passed = {row["cts_urn"]: row for row in verification if row["automated_check"] == PASSED}
    records = {}
    for filename in sorted(glob.glob("data/research_batches/*.csv")):
        try:
            rows = csv.DictReader(Path(filename).open(encoding="utf-8"))
            for row in rows:
                status = row.get("proposed_status", "")
                if "PARTIAL" not in status or row.get("confidence", "").lower() != "high":
                    continue
                target = (row.get("tlg_author_id", ""), row.get("tlg_work_id", ""))
                for source_urn in sorted(urns(row.get("open_text_url", ""))):
                    source = passed.get(source_urn)
                    if not source:
                        continue
                    key = target + (source_urn,)
                    records[key] = {
                        "tlg_author_id": target[0],
                        "tlg_work_id": target[1],
                        "coverage": "PARTIAL_HOST_TEXT_VERIFIED",
                        "journal_status": status,
                        "source_urn": source_urn,
                        "source_url": verified_text_url(source),
                        "source_local_path": source["local_path"],
                        "source_sha256": source["sha256"],
                        "source_license": source["tei_license"] or source["license"],
                        "evidence_file": filename,
                        "scope_note": row.get("open_text_result", ""),
                    }
        except (csv.Error, UnicodeDecodeError):
            continue

    manual_path = Path("data/open_text_partial_manual.csv")
    for row in csv.DictReader(manual_path.open(encoding="utf-8")):
        source_urn = row["source_urn"]
        source = passed.get(source_urn)
        if not source:
            raise SystemExit(f"manual partial source did not pass TEI verification: {source_urn}")
        target = (row["tlg_author_id"], row["tlg_work_id"])
        key = target + (source_urn,)
        records[key] = {
            "tlg_author_id": target[0],
            "tlg_work_id": target[1],
            "coverage": "PARTIAL_HOST_TEXT_VERIFIED",
            "journal_status": "MANUALLY_CLASSIFIED_PARTIAL_HOST_WITNESS",
            "source_urn": source_urn,
            "source_url": verified_text_url(source),
            "source_local_path": source["local_path"],
            "source_sha256": source["sha256"],
            "source_license": source["tei_license"] or source["license"],
            "evidence_file": row["evidence_file"],
            "scope_note": row["scope_note"],
        }

    fields = (
        "tlg_author_id", "tlg_work_id", "coverage", "journal_status", "source_urn",
        "source_url", "source_local_path", "source_sha256", "source_license",
        "evidence_file", "scope_note",
    )
    output = Path("data/open_text_fragments.csv")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(records[key] for key in sorted(records))
    print(f"partial_host_rows={len(records)} target_keys={len({key[:2] for key in records})}")


if __name__ == "__main__":
    main()
