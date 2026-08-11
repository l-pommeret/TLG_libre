"""Verified register for 2017.048--052; no page image or OCR is downloaded."""
import csv

IDS=("048","049","050","051","052")
OUTPUT="data/research_batches/detailed_verified_3001_batch_114.csv"
PG46="https://archive.org/details/patrologiaecursu46mignuoft"
BSB="https://nbn-resolving.org/urn:nbn:de:bvb:12-bsb00125535-2"
HEIDELBERG="https://digi.ub.uni-heidelberg.de/diglit/dobschuetz1899"
FIELDS=("tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked").split()
works=list(csv.DictReader(open("data/canon_works.csv",encoding="utf-8")))
with open(OUTPUT,"w",newline="",encoding="utf-8") as fh:
 out=csv.DictWriter(fh,fieldnames=FIELDS);out.writeheader()
 for wid in IDS:
  w=next(r for r in works if (r['tlg_author_id'],r['tlg_work_id'])==('2017',wid));r={f:"" for f in FIELDS}
  r.update(tlg_author_id='2017',tlg_work_id=wid,author_heading=w['author_heading'],work_title=w['work_title'],canonical_edition=w['bibliographic_notice'],open_text_result='No exact licensed TEI match in local corpus.',last_checked='2026-08-11')
  if wid=='048':
   r.update(sources_tested=f'Pinakes item record; alternative Migne PG 46 {PG46}',scan_result='ALTERNATIVE_SCAN_CANDIDATE: PG 46, cols. 788--817; not cited critical edition.',scan_url=PG46,scan_rights='Internet Archive metadata: NOT_IN_COPYRIGHT; verify concordance before transfer.',confidence='medium',proposed_status='ALTERNATIVE_SCAN_CANDIDATE',next_action='Collate PG 46 against cited edition; use original images only, never supplied OCR.',notes='No images downloaded.')
  elif wid=='049':
   r.update(sources_tested=f'Biblissima/BSB witness catalogue; full BSB manuscript digitisation {BSB}',scan_result='ALTERNATIVE_MANUSCRIPT_CANDIDATE: BSB Cod. graec. 65 contains the work; not the Mann 1975 edition.',scan_url=BSB,scan_rights='Institutional digitisation: verify reuse terms before transfer.',confidence='medium',proposed_status='ALTERNATIVE_SCAN_CANDIDATE',next_action='Verify exact folios and manuscript rights before acquiring original images; no OCR.',notes='A British Library record has no current digital images; no images downloaded.')
  elif wid=='052':
   r.update(sources_tested=f'Heidelberg digitisation of cited Dobschütz 1899 edition {HEIDELBERG}',scan_result='EXACT_SCAN_CANDIDATE: cited Dobschütz 1899 edition, Beilage I pp. 12**--18**.',scan_url=HEIDELBERG,scan_rights='Public-domain 1899 source; verify repository reuse terms before transfer.',confidence='high',proposed_status='SCAN_CANDIDATE',next_action='Use Heidelberg original page images for cited appendix pages; do not use OCR.',notes='No images downloaded; IIIF page images only if later acquired.')
  else:
   r.update(sources_tested='Exact TLG/First1K lookup; cited-edition catalogue check',scan_result='No edition-matching reusable page-image source verified.',confidence='medium',proposed_status='EDITION_IDENTIFIED',next_action='Locate a rights-cleared scan of the cited edition; do not substitute OCR.',notes='No image acquired.')
  out.writerow(r)
