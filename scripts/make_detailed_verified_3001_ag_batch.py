import csv
FIELDS='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
def build(output,authors):
 canon={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
 with open(output,'w',newline='',encoding='utf-8') as h:
  w=csv.DictWriter(h,fieldnames=FIELDS,lineterminator='\n');w.writeheader()
  for author in authors:
   s=canon[(author,'001')];row={f:'' for f in FIELDS};row.update(tlg_author_id=author,tlg_work_id='001',author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested='Exact Canon AG notice; printed locus list and cross-references preserved; open Anthologia Graeca data identified as item-level source.',open_text_result='The listed Anthologia Graeca loci are concrete open-text leads, but the full attribution-level concordance has not yet been promoted as complete.',scan_result='No scan needed before text-level AG concordance.',confidence='medium',proposed_status='PARTIAL_OPEN_TEXT_REQUIRES_AG_CONCORDANCE',next_action='Verify every printed AG locus and author attribution against the open AG dataset.',notes='Cross-referenced, anonymous and homonymous epigrams are not merged; no OCR/images used.',last_checked='2026-08-11');w.writerow(row)
