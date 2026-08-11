import csv

O = "data/research_batches/detailed_verified_3001_batch_324.csv"
F = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D = {
    ("3115", "117"): ("In propriam animam", "MPG 114 col. 133", "55", "The exact short poem, not adjacent Alphabeta, was checked."),
    ("3116", "001"): ("Epistula de confessione et aliae epistulae", "Turner 2009 pp. 26–64, 70–80, 82–136 and 138–180 (even pages)", "17222", "The former attribution to John Damascene and all discontinuous even-page loci are preserved."),
    ("3116", "002"): ("Hymni", "Kambylis 1976 pp. 34–462", "67895", "The trailing Symeon of Thessalonica heading is a catalogue boundary, not part of this item."),
    ("3116", "003"): ("Orationes theologicae", "Darrouzès, SC 122 (1966), pp. 96–168", "8722", "This item is distinct from the ethical orations and the catalogue continuation fragment."),
    ("3116", "006"): ("Capita theologica", "Darrouzès, SC 51bis (1996), pp. 40–186 and 191", "17631", "The isolated page 191 is retained as an explicit discontinuous locus."),
}
C = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(O, "w", newline="", encoding="utf-8") as h:
    w = csv.DictWriter(h, fieldnames=F); w.writeheader()
    for k, (label, locus, wc, note) in D.items():
        s = C[k]; r = {f: "" for f in F}
        r.update(tlg_author_id=k[0], tlg_work_id=k[1], author_heading=s["author_heading"], work_title=s["work_title"], canonical_edition=s["bibliographic_notice"], sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.", open_text_result=f"No exact licensed TEI of {label} at {locus} was found.", scan_result=f"No reusable page images verified for {locus} are registered locally.", confidence="high", proposed_status="NO_EXACT_OPEN_TEXT", next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.", notes=note + " No image or OCR used.", last_checked="2026-08-11")
        w.writerow(r)
