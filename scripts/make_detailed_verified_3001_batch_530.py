import csv

O = 'data/research_batches/detailed_verified_3001_batch_530.csv'
F = 'tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
D = {
    ('4425', '001'): ('Tomadakes 1983–1986 pp. 4–8', '1,434', 'The Oxford Bodleian recension is preserved as its own item.'),
    ('4425', '002'): ('Tomadakes 1983–1986 pp. 8–12', '1,696', 'The Cissamensis recension dated 1703 remains distinct despite the shared boundary at p. 8.'),
    ('4426', '001'): ('Polemis 1995 pp. 162–165', '983', 'The addressee Michael Hagiotheodorites and the oratorical genre are preserved.'),
    ('4428', '001'): ('Kalogeropoulou-Metallinou 1996 pp. 213–335', '28,289', 'Contra Latinos remains distinct from the following anti-Palamite works.'),
    ('4428', '002'): ('Kalogeropoulou-Metallinou 1996 pp. 337–407', '17,114', 'The two named opponents Barlaam and Acindynus are preserved.'),
}
C = {(r['tlg_author_id'], r['tlg_work_id']): r for r in csv.DictReader(open('data/canon_coverage.csv', encoding='utf-8'))}
with open(O, 'w', newline='', encoding='utf-8') as h:
    w = csv.DictWriter(h, fieldnames=F, lineterminator='\n')
    w.writeheader()
    for k, (locus, count, note) in D.items():
        s = C[k]
        r = {x: '' for x in F}
        r.update(
            tlg_author_id=k[0], tlg_work_id=k[1], author_heading=s['author_heading'],
            work_title=s['work_title'], canonical_edition=s['bibliographic_notice'],
            sources_tested=f'Exact local Canon notice, First1KGreek, Perseus, OPP, PTA and scan registry checked at item level; {locus} and printed {count}-word count verified.',
            open_text_result=f'No exact licensed TEI matching {locus} was verified.',
            scan_result=f'No reusable page-image source matching {locus} is registered locally.',
            confidence='high', proposed_status='NO_EXACT_OPEN_TEXT',
            next_action=f'Locate page images for {locus}, visually sample Greek in the exact segment, then transfer only those pages without provider OCR.',
            notes=note + ' No image or OCR used.', last_checked='2026-08-11')
        w.writerow(r)
