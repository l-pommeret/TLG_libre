import csv

FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()


def build(output, works):
    canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
    matches = list(csv.DictReader(open("data/corpus_matches.csv", encoding="utf-8")))
    verified = list(csv.DictReader(open("data/text_verification.csv", encoding="utf-8")))
    with open(output, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
        for work in works:
            source = canon[("0032", work)]
            candidates = [r for r in matches if r["tlg_author_id"] == "0032" and r["tlg_work_id"] == work and r["corpus"] == "Perseus"]
            checks = [r for r in verified if r["tlg_author_id"] == "0032" and r["tlg_work_id"] == work and r["corpus"] == "Perseus"]
            if work == "015":
                row = {field: "" for field in FIELDS}
                row.update(tlg_author_id="0032", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"],
                           sources_tested="Exact Canon notice; local Perseus and First1K registries; Xenophon Marchant corpus boundaries checked without extending neighbouring works.",
                           open_text_result="No exact licensed Greek TEI under this Canon item was verified in the local registries.",
                           scan_result="No exact rights-cleared and Greek-sampled scan was verified for this separate pseudo-Xenophontic item.", confidence="medium",
                           proposed_status="NO_EXACT_OPEN_TEXT", next_action="Search the work under Pseudo-Xenophon identifiers and collate any candidate to Marchant vol. 5.",
                           notes="The fourteen neighbouring Xenophontic TEIs are not extended to this [Sp.] notice. No provider OCR or images used.", last_checked="2026-08-11")
                writer.writerow(row)
                continue
            if len(candidates) != 1 or len(checks) != 1 or checks[0]["automated_check"] != "AUTOMATED_TEI_CHECK_PASSED":
                raise RuntimeError((work, len(candidates), len(checks)))
            candidate = candidates[0]; row = {field: "" for field in FIELDS}
            row.update(tlg_author_id="0032", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"],
                       sources_tested="Exact Canon notice; local Perseus Greek TEI; embedded Marchant volume/year; explicit CC BY-SA 4.0; automated Greek-content verification.",
                       open_text_result="Complete licensed Greek text verified in the exact E. C. Marchant Oxford edition cited by the Canon.",
                       open_text_url=candidate["text_url"], open_text_license="CC BY-SA 4.0",
                       scan_result="No scan acquisition is needed because the exact canonical Greek edition is available as licensed TEI.", confidence="high",
                       proposed_status="OPEN_TEXT_COMPLETE_EXACT_EDITION",
                       next_action="Prepare the exact licensed TEI for normalized ingestion.",
                       notes=f"Exact CTS URN {candidate['cts_urn']}; {checks[0]['greek_characters']} Greek characters; automated TEI check passed. No provider OCR or images used.",
                       last_checked="2026-08-11")
            writer.writerow(row)
