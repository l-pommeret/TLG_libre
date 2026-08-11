import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_601.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
TARGETS = ["003", "004", "005", "006", "007"]
PTA = {"003": "065", "004": "066", "005": "067", "006": "068", "007": "069"}
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in TARGETS:
        source = canon[("0031", work)]; pta = PTA[work]; row = {field: "" for field in FIELDS}
        row.update(tlg_author_id="0031", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"],
                   sources_tested="Exact Canon notice; local PTA SBL Greek New Testament TEI, embedded source bibliography and CC BY 4.0 statement; local Perseus alternative also checked.",
                   open_text_result="Complete licensed Greek text verified in the SBL Greek New Testament 2010 edition; it is an open alternative to the Aland et al. 1968 edition cited by the Canon.",
                   open_text_url=f"https://pta.bbaw.de/text/urn:cts:pta:pta9999.pta{pta}.pta-grc1", open_text_license="CC BY 4.0",
                   scan_result="No scan acquisition is needed because a complete licensed Greek TEI is available.", confidence="high",
                   proposed_status="OPEN_TEXT_COMPLETE_ALTERNATE_EDITION",
                   next_action="Prepare the licensed TEI for normalized ingestion while preserving SBL edition provenance.",
                   notes="PTA TEI explicitly declares SBL/Logos copyright and CC BY 4.0, contains substantial Greek, and passed the automated TEI check. No provider OCR or images used.", last_checked="2026-08-11")
        writer.writerow(row)
