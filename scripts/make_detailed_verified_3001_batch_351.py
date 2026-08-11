import csv

O="data/research_batches/detailed_verified_3001_batch_351.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3191","009"):("Laudatio in urbem Nicaiam","Mineva 1994–1995 pp. 314–325","4102","The city of Nicaea defines this exact encomium."),
("3191","010"):("Carmen xii ad Nicephorum Callistum Xanthopulum","Cunningham, Featherstone and Georgiopoulou 1983 pp. 103–111","2424","Poem xii and its named addressee are preserved exactly."),
("3191","011"):("Ἠθικὸς ἢ περὶ παιδείας","Polemis 1995 pp. 52–274","23162","The ethical discourse on education is distinct from Metochites' poem collections."),
("3191","012"):("Carmina","Polemis, CCSG 83 (2015), pp. 5–73, 98–114, 116–138 and 140–212","36198","All four explicit discontinuous page loci are preserved without filling the gaps."),
("3191","013"):("Carmen xiii ad Leonem Bardalem","Featherstone 1994 pp. 459–468","2151","Poem xiii and its named addressee Leo Bardales define the exact item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
