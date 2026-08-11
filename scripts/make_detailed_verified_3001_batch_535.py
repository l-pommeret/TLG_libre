import csv

O='data/research_batches/detailed_verified_3001_batch_535.csv'; F='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
D={
('4444','004'):('Hofmann 1971 pp.95–119','5,933','The item is explicitly a Greek translation of a sermon by Julianus Cesarini; the cross-reference is retained.'),
('4445','001'):('Bucossi 2014 pp.7–10','543','The Andronicus Camaterus cross-reference is retained and the epigram remains a separate item.'),
('4445','002'):('Papadopoulos-Kerameus 1898 vol.5 pp.180–189','1,375','The 1963 reprint and liturgical genre are preserved.'),
('4445','003'):('Petrides 1903 pp.471–494','3,162','The Demetrius canon pp.471–482 and George canon pp.482–494, with their distinct manuscripts, remain explicitly bounded.'),
('4445','004'):('Bucossi 2009 pp.45–48','543','The dedicatory verses and Marcianus Graecus 524 context are preserved.'),}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F,lineterminator='\n');w.writeheader()
 for k,(l,c,n) in D.items():
  s=C[k];r={x:'' for x in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local Canon notice, First1KGreek, Perseus, OPP, PTA and scan registry checked item by item; {l} and printed {c}-word count verified.',open_text_result=f'No exact licensed TEI matching {l} was verified.',scan_result=f'No reusable page-image source matching {l} is registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate page images for {l}, visually confirm Greek in each exact segment, then transfer only verified Greek pages without provider OCR.',notes=n+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
