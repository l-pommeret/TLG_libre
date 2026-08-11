import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_308.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","037"):("Passio Clementis Ancyrani et sociorum, BHG 353","MPG 114 cols. 816–893","15274","Clement's Ancyra qualifier and companions define the item."),
("3115","038"):("Passio Panteleemonis, BHG 1414","MPG 115 cols. 448–477","6329","Shared col. 477 with 3115.030 requires visual separation."),
("3115","039"):("De sancta trinitate","Koder 1965 pp. 133–138","891","The Trinity hymn in Koder's edition is the exact short item."),
("3115","040"):("Vita Symeonis Stylitae, BHG 1686–1687","MPG 114 cols. 336–392","10881","The item explicitly comprises prologue BHG 1686 at col. 336 and narrative BHG 1687 at cols. 337–392."),
("3115","041"):("Vita sancti Mamantis, BHG 1018","Ioannou 1884 pp. 338–351","3505","Reference to Vitae 5120.001 is contextual and does not merge holdings.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
