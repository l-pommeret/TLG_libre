import csv

O = "data/research_batches/detailed_verified_3001_batch_325.csv"
F = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D = {
    ("3116", "007"): ("Gratiarum actiones II", "Krivochéine, SC 113 (1965), pp. 304–356", "5304", "NO_EXACT_OPEN_TEXT", "The two thanksgivings are treated as the exact combined item."),
    ("3116", "008"): ("Orationes ethicae", "truncated canon notice: Darrouzès, SC 122", "83834", "INCOMPLETE_NOTICE_NO_EXACT_TEXT", "The canonical notice ends after the series number; no missing volume or page data were inferred."),
    ("3116", "009"): ("Catecheses 1–34", "SC 96 (1963) pp. 206–468; SC 104 (1964) pp. 12–392; SC 113 (1965) pp. 12–302", "90627", "NO_EXACT_OPEN_TEXT", "All three explicit volume loci were checked as one numbered catechesis collection."),
    ("3116", "011"): ("Capitula alphabetica [Dub.]", "Athos Stavronikita 2005 pp. 28–360", "40809", "NO_EXACT_OPEN_TEXT", "The catalogue's doubtful attribution is preserved."),
    ("3116", "129"): ("catalogue continuation fragment", "(1966, 1967) 1:170–440; 2:8–458", "83834", "INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT", "This artificial key is retained independently: it is a continuation fragment adjacent to 3116.008, but no title, editor, or merger was inferred."),
}
C = {(r["tlg_author_id"], r["tlg_work_id"]): r for r in csv.DictReader(open("data/canon_coverage.csv", encoding="utf-8"))}
with open(O, "w", newline="", encoding="utf-8") as h:
    w = csv.DictWriter(h, fieldnames=F); w.writeheader()
    for k, (label, locus, wc, status, note) in D.items():
        s = C[k]; r = {f: "" for f in F}
        r.update(tlg_author_id=k[0], tlg_work_id=k[1], author_heading=s["author_heading"], work_title=s["work_title"], canonical_edition=s["bibliographic_notice"], sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue {wc}-word marker checked; local scan register checked.", open_text_result=f"No exact licensed TEI of {label} at the stated locus was found.", scan_result=f"No reusable page images verified for {locus} are registered locally.", confidence="high", proposed_status=status, next_action=("Recover and verify the complete catalogue/source notice before acquisition; then locate rights-cleared images and verify the exact item." if status.startswith("INCOMPLETE") else f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR."), notes=note + " No image or OCR used.", last_checked="2026-08-11")
        w.writerow(r)
