import csv

O = 'data/research_batches/detailed_verified_3001_batch_531.csv'
F = 'tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
D = [
    ('4428', '003', 'Questiones et responsiones', 'Kalogeropoulou-Metallinou 1996 pp. 409–527', '26,852', 'The Canon spelling Questiones is retained without silent normalization.'),
    ('4428', '004', 'Tetrasticha iambica', 'Kalogeropoulou-Metallinou 1996 pp. 529–544', '2,043', 'Tetrasticha pp. 529–543 and Pros angelon p. 544 remain explicitly bounded components.'),
    ('4428', '005', 'Remediorum collectio alphabetica', 'Lundstrom, Eranos 5 (1903–1904), pp. 132–149', '', 'The alphabetic botanical-remedy collection remains a lexicographical item; no absent word count is invented.'),
    ('4431', '001', 'Adversus Palamam', 'Polemis 2012 pp. 3–51', '13,631', 'This theological work is one of two distinct canonical notices sharing key 4431.001.'),
    ('4431', '001', 'Fragmenta', 'Thesleff 1965 pp. 141–142', '220', 'This philosophical fragment notice is preserved separately from Adversus Palamam despite the duplicate canonical key.'),
]
C = list(csv.DictReader(open('data/canon_coverage.csv', encoding='utf-8')))
with open(O, 'w', newline='', encoding='utf-8') as h:
    w = csv.DictWriter(h, fieldnames=F, lineterminator='\n')
    w.writeheader()
    for aid, wid, title, locus, count, note in D:
        matches = [r for r in C if r['tlg_author_id'] == aid and r['tlg_work_id'] == wid and r['work_title'] == title]
        if len(matches) != 1:
            raise RuntimeError(f'Expected one Canon row for {(aid, wid, title)}, got {len(matches)}')
        s = matches[0]
        count_note = f' and printed {count}-word count' if count else ''
        r = {x: '' for x in F}
        r.update(
            tlg_author_id=aid, tlg_work_id=wid, author_heading=s['author_heading'],
            work_title=s['work_title'], canonical_edition=s['bibliographic_notice'],
            sources_tested=f'Exact local Canon notice, First1KGreek, Perseus, OPP, PTA and scan registry checked at item level; {locus}{count_note} verified.',
            open_text_result=f'No exact licensed TEI matching {locus} was verified.',
            scan_result=f'No reusable page-image source matching {locus} is registered locally.',
            confidence='high', proposed_status='NO_EXACT_OPEN_TEXT',
            next_action=f'Locate page images for {locus}, visually sample Greek in the exact segment, then transfer only those pages without provider OCR.',
            notes=note + ' No image or OCR used.', last_checked='2026-08-11')
        w.writerow(r)
