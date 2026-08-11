import csv

FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()


def build(output, works):
    canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
    matches = list(csv.DictReader(open("data/corpus_matches.csv", encoding="utf-8")))
    verified = list(csv.DictReader(open("data/text_verification.csv", encoding="utf-8")))
    with open(output, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
        for work in works:
            source = canon[("0031", work)]
            candidates = [r for r in matches if r["tlg_author_id"] == "0031" and r["tlg_work_id"] == work and r["corpus"] == "PTA"]
            checks = [r for r in verified if r["tlg_author_id"] == "0031" and r["tlg_work_id"] == work and r["corpus"] == "PTA"]
            if len(candidates) != 1 or len(checks) != 1 or checks[0]["automated_check"] != "AUTOMATED_TEI_CHECK_PASSED":
                raise RuntimeError((work, len(candidates), len(checks)))
            candidate = candidates[0]; row = {field: "" for field in FIELDS}
            row.update(tlg_author_id="0031", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"],
                       sources_tested="Exact Canon notice; local PTA SBL Greek New Testament TEI, embedded bibliography and CC BY 4.0 statement; local automated Greek-content verification.",
                       open_text_result="Complete licensed Greek text verified in the SBL Greek New Testament 2010 edition; this is an open alternative to Aland et al. 1968 cited by the Canon.",
                       open_text_url=candidate["text_url"], open_text_license="CC BY 4.0",
                       scan_result="No scan acquisition is needed because a complete licensed Greek TEI is available.", confidence="high",
                       proposed_status="OPEN_TEXT_COMPLETE_ALTERNATE_EDITION",
                       next_action="Prepare the licensed TEI for normalized ingestion while preserving SBL edition provenance.",
                       notes=f"Exact PTA URN {candidate['cts_urn']}; explicit CC BY 4.0; {checks[0]['greek_characters']} Greek characters; automated TEI check passed. No provider OCR or images used.",
                       last_checked="2026-08-11")
            writer.writerow(row)
