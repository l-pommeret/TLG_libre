import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_589.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = [("0011", "015"), ("0011", "016"), ("0011", "017"), ("0018", "001"), ("0018", "002")]
HOSTS = {"015": "001", "016": "006", "017": "007"}
PERSEUS_COMMIT = "790c84289edbdbe289dd7b752bfea29f0af4299d"; FIRST1K_COMMIT = "bfea9acd07ee1b7cea70cdd927c8f092d5637695"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for key in WORKS:
        source = canon[key]; row = {field: "" for field in FIELDS}
        if key[0] == "0011":
            host = HOSTS[key[1]]; url = f"https://raw.githubusercontent.com/PerseusDL/canonical-greekLit/{PERSEUS_COMMIT}/data/tlg0011/tlg{host}/tlg0011.tlg{host}.perseus-grc2.xml"
            row.update(open_text_result=f"The same complete tragedy is available as the verified open Storr edition under canonical host 0011.{host}; it is not the Lloyd-Jones–Wilson 1990 text.", open_text_url=url, open_text_license="CC BY-SA 4.0", scan_result="No scan needed for the open alternate edition.", confidence="high", proposed_status=f"CROSS_REFERENCE_OPEN_ALTERNATE_0011.{host}", next_action="Reuse the verified Storr TEI only as an alternate edition; retain this Oxford edition record separately.", notes="Exact title identity and distinct edition checked. No provider OCR or image used.")
        else:
            work = key[1]; url = f"https://raw.githubusercontent.com/OpenGreekAndLatin/First1KGreek/{FIRST1K_COMMIT}/data/tlg0018/tlg{work}/tlg0018.tlg{work}.1st1K-grc1.xml"
            row.update(open_text_result="Complete licensed Greek TEI in the exact canonical Cohn edition.", open_text_url=url, open_text_license="CC BY-SA 4.0", scan_result="No scan needed because the exact canonical Greek text is openly available.", confidence="high", proposed_status="OPEN_TEXT_AVAILABLE", next_action="Ingest the immutable First1K TEI and retain Cohn pagination and attribution.", notes="Immutable file fetched; exact CTS URN, editor Leopold Cohn and Greek body sampled. Not provider OCR; no image used.")
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact Canon edition, immutable upstream TEI, embedded editor/URN, repository CC BY-SA licence, local corpus and scan registry checked.", last_checked="2026-08-11"); writer.writerow(row)
