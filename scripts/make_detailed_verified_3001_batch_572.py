import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_572.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
VERSIONS = {"081": ["tlg081.perseus-grc4"], "082": ["tlg082.perseus-grc4"], "083": ["tlg083.perseus-grc4"], "084": ["tlg084a.perseus-grc4", "tlg084b.perseus-grc4"], "085": ["tlg085.perseus-grc4"]}
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work, versions in VERSIONS.items():
        source = canon[("0007", work)]; urns = [f"urn:cts:greekLit:tlg0007.{v}" for v in versions]; urls = [f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0007/{v.split('.')[0]}/tlg0007.{v}.xml" for v in versions]
        row = {field: "" for field in FIELDS}; row.update(tlg_author_id="0007", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested=f"Perseus canonical-greekLit at immutable commit {COMMIT}: exact CTS component URNs {', '.join(urns)}, Greek XML bodies, edition metadata and CC BY-SA 4.0 checked.", open_text_result=("Complete open Greek TEI under the exact TLG identifier, split into the Roman and Greek Aetia components." if work == "084" else "Complete open Greek TEI under the exact TLG identifier, in an open historical edition distinct from the canonical edition."), open_text_url="; ".join(urls), open_text_license="CC BY-SA 4.0", scan_result="No scan needed: complete licensed Greek TEI available.", confidence="high", proposed_status="OPEN_TEXT_DIFFERENT_EDITION", next_action="Ingest the open edition and preserve its component and edition boundaries.", notes="All immutable XML components fetched and Greek-script sampled; not provider OCR. No image used.", last_checked="2026-08-11"); writer.writerow(row)
