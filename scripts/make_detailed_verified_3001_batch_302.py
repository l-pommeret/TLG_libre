import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_302.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3115","007"):("Hypomnema sancti Joannis Chrysostomi","Halkin 1977 pp. 474–486","3264","Only this Chrysostom narrative within the twelve-récits volume defines the item."),
("3115","008"):("Martyrium Andreae in Crisi","Acta Sanctorum Oct. VIII 1853 pp. 142–149","3278","Paris Coislin gr. 145 and reference to 5165.001 are preserved without merging holdings."),
("3115","009"):("Martyrium sancti Vari et sociorum, BHG 1863","MPG 115 cols. 1141–1160","3881","The embedded SYMEON Metaphrastes string in the manuscript phrase is a heading artefact; Paris gr. 1480 and reference 5166.001 are preserved."),
("3115","010"):("Martyrium sancti Artemii, BHG 172","MPG 115 cols. 1160–1264","10658","Shared MPG col. 1160 with 3115.009 requires visual item separation; reference 5168.001 is contextual."),
("3115","011"):("Martyrium Guriae, Samonae et Abibi, BHG 736–737","von Gebhardt–von Dobschütz 1911 pp. 103–147 odd pages","3610","Only odd-page Greek text is canonical; duplicate printing MPG 116 cols. 128–161 is retained as an alternate witness.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];status="DUPLICATE_PRINTING_NO_EXACT_TEXT"if k==("3115","011")else"NO_EXACT_OPEN_TEXT";r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status=status,next_action=f"Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
