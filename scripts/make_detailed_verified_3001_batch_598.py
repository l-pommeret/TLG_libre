import csv

OUTPUT = "data/research_batches/detailed_verified_3001_batch_598.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
TARGETS = [
    ("0022", "001", "Theriaca"),
    ("0022", "002", "Alexipharmaca"),
    ("0022", "003", "Fragmenta"),
    ("0022", "003", "(pp. 162–164)"),
    ("0022", "005", "Fragmenta"),
]
OPEN = {
    "001": ("urn:cts:greekLit:tlg0022.tlg001.1st1K-grc1", "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0022.tlg001.1st1K-grc1"),
    "002": ("urn:cts:greekLit:tlg0022.tlg002.1st1K-grc1", "https://scaife.perseus.org/reader/urn:cts:greekLit:tlg0022.tlg002.1st1K-grc1"),
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
                   sources_tested="Exact Canon notice; local First1KGreek TEI and embedded source bibliography/licence; corpus match registry; neighbouring fragments checked without extension.",
                   scan_result="No scan is needed for the two complete open texts; no exact rights-cleared and Greek-sampled aggregate scan was verified for the fragment notices.",
                   confidence="high" if work in OPEN else "medium", last_checked="2026-08-11")
        if work in OPEN:
            urn, url = OPEN[work]
            row.update(open_text_result="Complete Greek TEI verified for this work, based on Otto Schneider, Nicandrea (Teubner, 1856); it is an open alternative edition, not the Canon's Gow–Scholfield 1953 edition.",
                       open_text_url=url, open_text_license="CC BY-SA 4.0",
                       proposed_status="OPEN_TEXT_COMPLETE_ALTERNATE_EDITION",
                       next_action="Retain edition distinction and prepare the licensed TEI for later normalization/OCR-independent ingestion.",
                       notes=f"Exact CTS identifier {urn}; TEI declares Schneider 1856 and CC BY-SA 4.0. Greek content passed the existing automated TEI check.")
        else:
            row.update(open_text_result="No complete licensed Greek transcription matching this exact fragment aggregate was verified.",
                       proposed_status="NO_COMPLETE_OPEN_TEXT",
                       next_action="Map each fragment to its ancient witness or papyrus before claiming coverage.",
                       notes="The duplicate 0022.003 catalogue occurrence is preserved by its distinct printed title. No neighbouring complete poem is extended to these fragments; no provider OCR used.")
        writer.writerow(row)
