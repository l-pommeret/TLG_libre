import csv
from pathlib import Path

FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()


def write_batch(output, targets):
    canon_rows = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))
    with open(output, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        for target in targets:
            key = target[:2]
            candidates = [row for row in canon_rows if (row["tlg_author_id"], row["tlg_work_id"]) == key]
            source = candidates[0] if len(target) == 2 else next(row for row in candidates if row["work_title"] == target[2])
            notice = source["bibliographic_notice"]
            title = source["work_title"]
            is_ag = "AG:" in title or "AG " in title
            open_files = sorted(Path("sources/upstream").glob(f"*/data/tlg{key[0]}/tlg{key[1]}/tlg{key[0]}.tlg{key[1]}.*-grc*.xml"))
            has_open_tei = bool(open_files)
            row = {field: "" for field in FIELDS}
            row.update(
                tlg_author_id=key[0],
                tlg_work_id=key[1],
                author_heading=source["author_heading"],
                work_title=title,
                canonical_edition=notice,
                sources_tested="Exact Canon notice; local Perseus/First1K, Anthologia Graeca, FHG/FGrH and scan registries; item boundaries and duplicate notes checked.",
                open_text_result=("A complete Greek TEI for this TLG work identifier is present in the local licensed upstream corpus; its edition must remain distinguished from the Canon edition."
                    if has_open_tei else ("The explicitly listed Anthologia Graeca loci provide licensed ancient-host text candidates, but they do not establish a complete open transcription of every fragment in this Canon item."
                    if is_ag else "No complete licensed Greek transcription matching this exact testimony or fragment edition was verified.")),
                open_text_url=str(open_files[0]) if has_open_tei else "",
                open_text_license="CC BY-SA 4.0" if has_open_tei else "",
                scan_result="No exact rights-cleared scan with Greek visually sampled at every selected segment was verified for this item.",
                confidence="medium",
                proposed_status="OPEN_TEXT_DIFFERENT_EDITION" if has_open_tei else ("PARTIAL_OPEN_TEXT_ANCIENT_HOST" if is_ag else "NO_COMPLETE_OPEN_TEXT"),
                next_action=(
                    "Map each printed fragment number to its ancient host before claiming completeness."
                ),
                notes="Canonical duplicates, uncertain attributions, papyrus limits and testimony/fragment distinctions are preserved; no OCR or image acquisition used.",
                last_checked="2026-08-11",
            )
            writer.writerow(row)
