import csv

O='data/research_batches/detailed_verified_3001_batch_534.csv'; F='tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked'.split()
D={
('4442','002'):('Cantarella 1934 pp.153–185','1,501','The attribution embedded in the edition title to Joseph of Methone is retained as edition context, not silently resolved against the Canon author.'),
('4442','003'):('MPG 159 cols.960–1024','12,440','The Canon title includes its MPG locus and word count; both are preserved without duplication.'),
('4444','001'):('Mastrodemetres 1965 pp.205–207','1,038','The unnamed friend and consolatory character are preserved.'),
('4444','002'):('Mastrodemetres 1970 pp.234–237','1,011','The cross-reference to Matthaeus Palaeologus Asanes is retained.'),
('4444','003'):('MPG 161 cols.691–696','1,387','The Canon title embeds the locus and count; the letter to Andronicus Callistus remains a separate item.'),}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F,lineterminator='\n');w.writeheader()
 for k,(l,c,n) in D.items():
  s=C[k];r={x:'' for x in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local Canon notice, First1KGreek, Perseus, OPP, PTA and scan registry checked item by item; {l} and printed {c}-word count verified.',open_text_result=f'No exact licensed TEI matching {l} was verified.',scan_result=f'No reusable page-image source matching {l} is registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate page images for {l}, visually confirm Greek in the exact segment, then transfer only verified Greek pages without provider OCR.',notes=n+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
