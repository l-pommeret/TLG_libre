import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_585.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
WORKS = [("0007", "148"), ("0007", "149"), ("0009", "001"), ("0009", "002"), ("0009", "003")]
AG = "https://anthologiagraeca.org/passages/urn%3Acts%3AgreekLit%3Atlg7000.tlg001.ag%3A{}/"
canon = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for key in WORKS:
        source = canon[key]; sappho_epigrams = key == ("0009", "002"); row = {field: "" for field in FIELDS}
        if sappho_epigrams:
            urls = "; ".join(AG.format(p) for p in ("6.269", "7.489", "7.505"))
            row.update(open_text_result="Exact Greek text is openly available for all three listed AG loci; the Canon's question mark on AG 6.269 is preserved.", open_text_url=urls, open_text_license="CC BY 4.0 (Anthologia Graeca Project data)", scan_result="No scan needed because the exact Greek passages are available as licensed data.", confidence="high", proposed_status="OPEN_TEXT_AVAILABLE", next_action="Ingest the three exact AG passages with attribution and preserve the doubtful marker on 6.269.", notes="All three passage pages were opened, Greek-script sampled and checked for Sappho attribution. No provider OCR or image used.")
        else:
            modern = key in {("0007", "148"), ("0009", "001"), ("0009", "003")}
            row.update(open_text_result="No complete licensed Greek transcription matching this canonical fragment collection was verified.", scan_result=("The canonical fragment collection is modern and no reusable exact-edition scan was verified." if modern else "Crusius 1887 is bibliographically identified, but no exact scan with verified page mapping and reuse metadata was established."), confidence="medium", proposed_status="NO_EXACT_OPEN_TEXT", next_action="Map each fragment to its ancient citing text or primary papyrus before acquiring text or images.", notes="Aggregate modern editions were not copied. No provider OCR or image used.")
        row.update(tlg_author_id=key[0], tlg_work_id=key[1], author_heading=source["author_heading"], work_title=source["work_title"], canonical_edition=source["bibliographic_notice"], sources_tested="Exact TLG item, local corpus index, Perseus/First1KGreek identifiers, Anthologia Graeca Project where applicable, Internet Archive catalogue and local scan registry checked.", last_checked="2026-08-11"); writer.writerow(row)
