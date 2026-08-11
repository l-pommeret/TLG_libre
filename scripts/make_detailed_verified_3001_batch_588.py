import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_588.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = ["010", "011", "012", "013", "014"]
HOSTS = {"011": "003", "012": "005", "013": "004", "014": "002"}
COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for work in WORKS:
        source = canon[("0011", work)]; host = HOSTS.get(work); row = {field: "" for field in FIELDS}
        if host:
            url = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{COMMIT}/data/tlg0011/tlg{host}/tlg0011.tlg{host}.perseus-grc2.xml"
            row.update(open_text_result=f"The same complete tragedy is available as the verified open Storr edition under canonical host 0011.{host}; it is not the Lloyd-Jones–Wilson 1990 text.", open_text_url=url, open_text_license="CC BY-SA 4.0", scan_result="No scan needed for the open alternate edition.", confidence="high", proposed_status=f"CROSS_REFERENCE_OPEN_ALTERNATE_0011.{host}", next_action="Reuse the verified Storr TEI only as an alternate edition; retain this Oxford edition record separately.", notes="Exact title identity and distinct edition were checked. No provider OCR or image used.")
        else:
            row.update(open_text_result="No complete licensed Greek transcription matching Page's single melic fragment was verified.", scan_result="No exact reusable scan of the canonical modern edition was verified.", confidence="medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Resolve the single ancient witness before acquisition.", notes="No provider OCR or image used.")
        row.update(tlg_author_id="0011", tlg_work_id=work, author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact Canon title/edition, verified Perseus Sophocles TEIs 0011.001–007, local corpus and scan registry checked.", last_checked="2026-08-11"); writer.writerow(row)
