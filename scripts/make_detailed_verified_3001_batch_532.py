import csv

O = 'data/research_batches/detailed_verified_3001_batch_532.csv'
F = 'tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
D = {
    ('4431', '002'): ('Heisenberg 1905 pp. 193–233', '14,532', 'The [Dub.] attribution, BHG 933, and cross-references to Acropolites and Lascaris are preserved.'),
    ('4432', '001'): ('Bakker–van Gemert 2008 pp. 95–116', '4,773', 'The accidental PIERIUS insertion inside the printed Canon notice is treated as a trailing heading artifact.'),
    ('4434', '001'): ('Moniou 2010 pp. 147–359', '36,541', 'The homiletic collection remains a single item under Nicetas Myrsiniotes.'),
    ('4434', '002'): ('Moniou 2015 pp. 93–119', '9,480', 'The encomium of Saint Matrona remains distinct from the Homiliae.'),
    ('4436', '001'): ('Festa 1912–1915, Bessarione 16–18, discontinuous loci', '23,656', 'All six discontinuous journal loci are preserved; the trailing NICETAS David Paphlagonius heading is excluded.'),
}
C = {(r['tlg_author_id'], r['tlg_work_id']): r for r in csv.DictReader(open('data/canon_coverage.csv', encoding='utf-8'))}
with open(O, 'w', newline='', encoding='utf-8') as h:
    w = csv.DictWriter(h, fieldnames=F, lineterminator='\n'); w.writeheader()
    for k, (locus, count, note) in D.items():
        s = C[k]; r = {x: '' for x in F}
        r.update(tlg_author_id=k[0], tlg_work_id=k[1], author_heading=s['author_heading'], work_title=s['work_title'], canonical_edition=s['bibliographic_notice'],
                 sources_tested=f'Exact local Canon notice, First1KGreek, Perseus, OPP, PTA and scan registry checked item by item; {locus} and printed {count}-word count verified.',
                 open_text_result=f'No exact licensed TEI matching {locus} was verified.', scan_result=f'No reusable page-image source matching {locus} is registered locally.',
                 confidence='high', proposed_status='NO_EXACT_OPEN_TEXT', next_action=f'Locate page images for {locus}, visually sample Greek in every discontinuous segment, then transfer only verified Greek pages without provider OCR.',
                 notes=note + ' No image or OCR used.', last_checked='2026-08-11')
        w.writerow(r)
