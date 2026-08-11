import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_599.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
TARGETS = [
    ("0022", "006", "Epigrammata, AG: 7.435, 526; 9.503b. Q: 79: Epigr. AG 11.7: Cf. NICARCHUS II Epigr. (1532 001). Dup. partim 0022 001 (p. 76, v. 741) et 0022"),
    ("0023", "001", "Halieutica"),
    ("0024", "001", "Cynegetica"),
    ("0025", "001", "Testimonium"),
    ("0026", "001", "In Timarchum"),
]
OPEN = {
    ("0023", "001"): ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0023.tlg001.perseus-grc2", "Exact Mair 1928 edition used by the Canon."),
    ("0024", "001"): ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0024.tlg001.perseus-grc2", "Exact Mair 1928 edition used by the Canon."),
    ("0026", "001"): ("https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0026.tlg001.perseus-grc2", "Complete Adams 1919 Greek text; open alternative to Martin–de Budé 1927."),
}
rows = list(csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8")))

def source_for(author, work, title):
    matches = [r for r in rows if r["tlg_author_id"] == author and r["tlg_work_id"] == work and r["work_title"] == title]
    if len(matches) != 1:
        raise RuntimeError((author, work, title, len(matches)))
    return matches[0]

with open(OUTPUT, "w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n"); writer.writeheader()
    for author, work, title in TARGETS:
        source = source_for(author, work, title); row = {field: "" for field in FIELDS}
        row.update(tlg_author_id=author, tlg_work_id=work, author_heading=source["author_heading"], work_title=title,
                   canonical_edition=source["bibliographic_notice"],
                   sources_tested="Exact Canon notice; local Perseus/First1K registries and TEI verification; AG and fragment boundaries checked item by item.",
                   scan_result="No scan needed where a complete licensed Greek TEI exists; otherwise no exact rights-cleared, Greek-sampled item-level scan was verified.",
                   last_checked="2026-08-11")
        key = (author, work)
        if key in OPEN:
            url, relation = OPEN[key]
            row.update(open_text_result=f"Complete licensed Greek TEI verified. {relation}", open_text_url=url,
                       open_text_license="CC BY-SA 4.0", confidence="high",
                       proposed_status="OPEN_TEXT_COMPLETE_EXACT_EDITION" if author in {"0023", "0024"} else "OPEN_TEXT_COMPLETE_ALTERNATE_EDITION",
                       next_action="Prepare the licensed TEI for normalized ingestion while retaining edition provenance.",
                       notes="Local TEI has an explicit Greek identifier, embedded CC BY-SA 4.0 licence, and passed the existing automated Greek TEI check; no provider OCR used.")
        elif author == "0022":
            row.update(open_text_result="The listed Anthologia Graeca loci are concrete open-text leads, but the full set and attribution were not promoted without an item-level concordance.", confidence="medium",
                       proposed_status="PARTIAL_OPEN_TEXT_REQUIRES_AG_CONCORDANCE",
                       next_action="Verify each AG locus and attribution against the open Anthologia Graeca data before promotion.",
                       notes="Duplicate-part relationships to Theriaca and other epigrammatists are preserved; no aggregate completeness inferred.")
        else:
            row.update(open_text_result="No exact reusable Greek transcription of Lasserre's isolated testimony was verified.", confidence="medium",
                       proposed_status="EDITION_IDENTIFIED_NO_OPEN_TEXT",
                       next_action="Identify the ancient host passage behind Lasserre p.77 before acquisition.",
                       notes="The modern 1987 edition is not copied; no testimony is guessed from neighbouring mathematical notices.")
        writer.writerow(row)
