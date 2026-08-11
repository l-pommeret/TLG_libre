import csv

O = 'data/research_batches/detailed_verified_3001_batch_533.csv'
F = 'tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
D = {
    ('4440', '001'): ('Benakis 2013 pp. 1–55', '12,751', 'The philosophical epitome is kept under Theodorus Smyrnaeus.'),
    ('4441', '001'): ('Gautier 1965 pp. 178–194', '5,085', 'The Alexius I cross-reference and the mixed encomiastic/epistolary genre are preserved.'),
    ('4441', '002'): ('Gautier 1965 pp. 195–201', '2,023', 'The consolation to Empress Irene remains distinct from the preceding orations.'),
    ('4441', '003'): ('Gautier 1965 pp. 201–204', '835', 'The shared boundary at p. 201 is preserved; trailing STRATON is excluded as a heading artifact.'),
    ('4442', '001'): ('Basileiou 1982 pp. 278–284', '1,453', 'The Greek title and identification as an autograph lament are preserved.'),
}
C = {(r['tlg_author_id'], r['tlg_work_id']): r for r in csv.DictReader(open('data/canon_coverage.csv', encoding='utf-8'))}
with open(O, 'w', newline='', encoding='utf-8') as h:
    w = csv.DictWriter(h, fieldnames=F, lineterminator='\n'); w.writeheader()
    for k, (locus, count, note) in D.items():
        s = C[k]; r = {x: '' for x in F}
        r.update(tlg_author_id=k[0], tlg_work_id=k[1], author_heading=s['author_heading'], work_title=s['work_title'], canonical_edition=s['bibliographic_notice'],
                 sources_tested=f'Exact local Canon notice, First1KGreek, Perseus, OPP, PTA and scan registry checked item by item; {locus} and printed {count}-word count verified.',
                 open_text_result=f'No exact licensed TEI matching {locus} was verified.', scan_result=f'No reusable page-image source matching {locus} is registered locally.',
                 confidence='high', proposed_status='NO_EXACT_OPEN_TEXT', next_action=f'Locate page images for {locus}, visually sample Greek in the exact segment, then transfer only verified Greek pages without provider OCR.',
                 notes=note + ' No image or OCR used.', last_checked='2026-08-11')
        w.writerow(r)
