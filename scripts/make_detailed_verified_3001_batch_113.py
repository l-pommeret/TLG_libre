"""Verified register for 2017.042--047; no page image or OCR is downloaded."""
import csv

IDS = ("042", "043", "044", "046", "047")
OUTPUT = "data/research_batches/detailed_verified_3001_batch_113.csv"
PG44 = "https://archive.org/details/patrologiaecursu44mignuoft"
PG45 = "https://archive.org/details/patrologiaecursu45mignuoft"
PG46 = "https://archive.org/details/patrologiaecursu46mignuoft"
ERARA = "https://www.e-rara.ch/bau_1/content/structure/1127567"
GNOO = "https://scholarlyeditions.brill.com/gnoo/"
FIELDS = (
    "tlg_author_id tlg_work_id author_heading work_title canonical_edition "
    "sources_tested open_text_result open_text_url open_text_license scan_result "
    "scan_url scan_rights confidence proposed_status next_action notes last_checked"
).split()
MATCHES={"042":(PG44,"PG 44, cols. 297--430"),"043":(PG46,"PG 46, cols. 317--416"),"046":(PG45,"PG 45, cols. 11--105")}

works=list(csv.DictReader(open("data/canon_works.csv",encoding="utf-8")))
with open(OUTPUT,"w",newline="",encoding="utf-8") as fh:
    out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
    for work_id in IDS:
        work=next(r for r in works if (r["tlg_author_id"],r["tlg_work_id"])==("2017",work_id))
        row={field:"" for field in FIELDS}
        row.update(tlg_author_id="2017",tlg_work_id=work_id,author_heading=work["author_heading"],work_title=work["work_title"],canonical_edition=work["bibliographic_notice"],open_text_result="No exact licensed TEI match in local corpus.",last_checked="2026-08-11")
        if work_id in MATCHES:
            scan,detail=MATCHES[work_id]
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; alternative Migne source {scan}",scan_result=f"ALTERNATIVE_SCAN_CANDIDATE: {detail}; not the cited critical edition.",scan_url=scan,scan_rights="Internet Archive metadata: NOT_IN_COPYRIGHT; verify page/Greek-text concordance before transfer.",confidence="medium",proposed_status="ALTERNATIVE_SCAN_CANDIDATE",next_action="Collate historical printing against cited edition; use original images only, never supplied OCR.",notes="No images downloaded.")
        elif work_id=="044":
            row.update(sources_tested=f"GNOO marks this recension outside GNO; cited SC 119 record",scan_result="No edition-matching reusable page-image source verified.",confidence="medium",proposed_status="EDITION_IDENTIFIED",next_action="Locate a rights-cleared scan matching the alternate recension; no OCR.",notes="Alternate recension retained distinctly; no scan acquired.")
        else:
            row.update(sources_tested=f"GNOO TLG concordance {GNOO}; 1571 Basel table of contents {ERARA}",scan_result="ALTERNATIVE_SCAN_CANDIDATE: historical edition listed; Greek-text and page coverage require verification.",scan_url=ERARA,scan_rights="Public-domain 1571 source; verify Greek-text content and image reuse before transfer.",confidence="medium",proposed_status="ALTERNATIVE_SCAN_CANDIDATE",next_action="Verify the historical text against the cited work before any image transfer; never use OCR.",notes="No images downloaded.")
        out.writerow(row)
