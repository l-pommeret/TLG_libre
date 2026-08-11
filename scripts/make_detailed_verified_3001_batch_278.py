import csv
OUTPUT="data/research_batches/detailed_verified_3001_batch_278.csv";FIELDS="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
ITEMS={
("3038","021"):("I John","Kalogeras vol. 2 pp. 590–638","12198","The first Johannine commentary is distinct from 3038.022 and .023."),
("3038","022"):("II John","Kalogeras vol. 2 pp. 639–642","720","This short second Johannine commentary has its own exact boundary."),
("3038","023"):("III John","Kalogeras vol. 2 pp. 643–646","876","This third Johannine commentary is distinct from 3038.022 despite equal page-span length."),
("3038","024"):("Jude","Kalogeras vol. 2 pp. 647–664","4632","This Jude component ends the Catholic-epistle sequence in the cited edition."),
("3038","025"):("Laudatio Hierothei","Gatsioufa 2012 pp. 335–343","3730","The Canon's doubtful-attribution marker [Dub.] is preserved and no authorship certainty is inferred.")}
c={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8"))};assert all(k in c for k in ITEMS)
with open(OUTPUT,"w",newline="",encoding="utf-8")as h:
 w=csv.DictWriter(h,fieldnames=FIELDS);w.writeheader()
 for k,(label,locus,wc,note) in ITEMS.items():
  s=c[k];r={f:""for f in FIELDS};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s["author_heading"],work_title=s["work_title"],canonical_edition=s["bibliographic_notice"],sources_tested=f"Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} item checked; local scan register checked.",open_text_result=f"No exact licensed TEI of {label} in {locus} was found.",scan_result=f"No reusable page images verified for {locus} are registered locally.",confidence="high",proposed_status="NO_EXACT_OPEN_TEXT",next_action=f"Locate rights-cleared images of {locus} and verify the exact {wc}-word item before transcription or OCR.",notes=note+" No image or OCR used.",last_checked="2026-08-11");w.writerow(r)
