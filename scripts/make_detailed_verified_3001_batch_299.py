import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_299.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3108","003"):("Epistula ad Dominicum Gradensem","Will 1861 pp. 208–228 / MPG 120 cols. 756–781","4086","The stated MPG equivalence and reference to 4453.001 are preserved without merging holdings."),
("3108","004"):("Epistulae quattuor","Michel 1930 pp. 432–456","4644","Four explicit letters are preserved: Alexandria 432–438, Jerusalem 438–446, and two distinct Leo IX letters 446–454 and 454–456; shared boundary pages require visual separation."),
("3108","005"):("Epistula ad clericos from Vatopedi 555","Michel 1938 pp. 116–118","393","The manuscript Vatopedi 555 and the clerical addressees define this short letter; the Canon's 'ad clericis' form is retained."),
("3109","001"):("Historia et refutatio Manichaeorum/Paulicianorum","Papachryssanthou 1970 pp. 7–67","11557","The split 'ref utatio' is retained in canonical_edition but treated as a spacing artefact for matching."),
("3111","001"):("Cletorologion","Oikonomidès 1972 pp. 81–235","unstated","The reference to Constantine VII 3023.010 is contextual; no word count is supplied or inferred.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];wcdesc=(f"{wc}-word"if wc!="unstated"else"word-count-unstated");r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wcdesc} {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
