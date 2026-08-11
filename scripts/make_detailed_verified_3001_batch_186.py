"""Verified register for five canonical rows beginning at 0087.042."""
import csv

START = ("0087", "042")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_186.csv"
FIELDS = "tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
coverage=list(csv.DictReader(open("data/canon_coverage.csv",encoding="utf-8")))
scans={(r["tlg_author_id"],r["tlg_work_id"]):r for r in csv.DictReader(open("data/scan_sources.csv",encoding="utf-8"))}
start=next(n for n,row in enumerate(coverage) if (row["tlg_author_id"],row["tlg_work_id"])==START)
works=coverage[start:start+5]; assert len(works)==5
with open(OUTPUT,"w",newline="",encoding="utf-8") as handle:
 writer=csv.DictWriter(handle,fieldnames=FIELDS);writer.writeheader()
 for work in works:
  key=(work["tlg_author_id"],work["tlg_work_id"]);row={f:"" for f in FIELDS}
  row.update(tlg_author_id=key[0],tlg_work_id=key[1],author_heading=work["author_heading"],work_title=work["work_title"],canonical_edition=work["bibliographic_notice"],last_checked="2026-08-11")
  if key==("0087","045"):
   scan=scans[key];row.update(sources_tested="Exact scan_sources match checked against the Cramer 1836 Canon edition and page span.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="Exact remote page-image candidate: Internet Archive JPEG set; sampled visually good.",scan_url=scan["source_url"],scan_rights=scan["rights"],confidence="high",proposed_status="SCAN_CANDIDATE",next_action="Retrieve the 9 exact page images from the remote source only when scheduled; no provider OCR.",notes="Exact title/pages 228–236; remote-only storage; no image acquired.")
  elif key==("0087","046"):
   row.update(sources_tested="Canon partial-duplication relation checked against 0087.037–039 and 0087.047.",open_text_result="Partial overlap: no acquisition decision until text-by-text comparison.",scan_result="No separate scan candidate confirmed.",confidence="medium",proposed_status="PARTIAL_DUPLICATION_REVIEW",next_action="Compare excerpts with 0087.037–039 and 0087.047; retain only non-overlapping material; no OCR.",notes="No image acquired.")
  else:
   row.update(sources_tested="Exact TLG/First1K lookup; cited TGL, Bekker, Nauck, or Cramer bibliographic record checked.",open_text_result="No exact licensed TEI match in local corpus.",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan of the cited edition; do not substitute OCR.",notes="No image acquired.")
  writer.writerow(row)
