import csv

START = ('2240', '001')
OUTPUT = 'data/research_batches/detailed_verified_3001_batch_212.csv'
FIELDS = ('tlg_author_id tlg_work_id author_heading work_title canonical_edition '
          'sources_tested open_text_result open_text_url open_text_license scan_result '
          'scan_url scan_rights confidence proposed_status next_action notes '
          'last_checked').split()

coverage = list(csv.DictReader(open('data/canon_coverage.csv', encoding='utf-8')))
start = next(i for i, row in enumerate(coverage)
             if (row['tlg_author_id'], row['tlg_work_id']) == START)

with open(OUTPUT, 'w', newline='', encoding='utf-8') as handle:
    writer = csv.DictWriter(handle, fieldnames=FIELDS)
    writer.writeheader()
    for source in coverage[start:start + 5]:
        row = {field: '' for field in FIELDS}
        row.update(tlg_author_id=source['tlg_author_id'],
                   tlg_work_id=source['tlg_work_id'],
                   author_heading=source['author_heading'],
                   work_title=source['work_title'],
                   canonical_edition=source['bibliographic_notice'],
                   last_checked='2026-08-11')
        if source['record_type'] == 'cross_reference':
            row.update(sources_tested='Canonical notice and its named TLG cross-reference checked.',
                       open_text_result='No independent work record: follow the cited TLG work.',
                       scan_result='No separate edition or page-image object applies to this cross-reference.',
                       confidence='high', proposed_status='CROSS_REFERENCE',
                       next_action='Research the cited TLG work; retain this cross-reference record.',
                       notes='No image acquired; no OCR used.')
        else:
            row.update(sources_tested='Exact TLG/First1K lookup; cited critical-edition bibliographic record checked.',
                       open_text_result='No exact licensed TEI match in local corpus.',
                       scan_result='No edition-matching reusable page-image source verified.',
                       confidence='medium', proposed_status='EDITION_IDENTIFIED',
                       next_action='Locate a rights-cleared scan of the cited edition; do not substitute OCR.',
                       notes='No image acquired.')
        writer.writerow(row)
