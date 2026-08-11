import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_298.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3105","005"):("Interpretationes divinorum mandatorum","MPG 106 cols. 1360–1381","4642","This exact locus also appears inside the multi-volume Pandecte notice 3105.001; overlap is preserved without collapsing records."),
("3106","001"):("Hymni sancti Nili Junioris","Gassisi 1906 pp. 39–54","2195","The hymns of Nilus Junior are distinguished from neighbouring Italo-Greek hymnographers."),
("3107","001"):("Narrationes","Wortley 1987 pp. 28–137","14127","Only the Paul of Monemvasia narratives within the multi-author volume define this item."),
("3108","001"):("Fragmentum from Mutinensis 42 fol. 131","Cumont 1903 pp. 96–98","649","The [Dub.] attribution and exact manuscript folio are preserved."),
("3108","002"):("Epistula ad Michaelem I Cerularium","Will 1861 pp. 189–204 / MPG 120 cols. 796–816","3025","The stated MPG textual equivalence and reference to 3077.004 are preserved, but no independent holdings are merged.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
