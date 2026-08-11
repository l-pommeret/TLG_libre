import csv

O="data/research_batches/detailed_verified_3001_batch_380.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D=[
("3264","001","Vita sancti Cyrilli Phileotae","Caracalla 42; Sargologos 1964 pp. 43–264","69841","The Athonite witness defines the exact life; embedded Nicolaus Methonaeus text is a catalogue heading artefact."),
("3269","001","Epistula ad Aretham","Westerink 1968 vol. 1 pp. 184–185","210","The Thomas letter remains distinct from Stephanus 3270.001; the Arethas 2130.033 cross-reference remains separate."),
("3270","001","Epistula ad Aretham","Westerink 1968 vol. 1 p. 295","98","The Stephanus letter remains distinct from Thomas 3269.001; the Arethas 2130.033 cross-reference remains separate."),
("3271","001","Oratio ad sanctum martyrem Nicetam iuniorem","Halkin, CCSG 21 (1989), pp. 129–154","7352","This hagiographic oration and the separate Epistula ad Phyllidem share a duplicated canonical key; both rows are retained explicitly."),
("3271","001","Epistula ad Phyllidem","Thesleff 1965 pp. 123–124","297","This philosophical epistle and the separate Nicetas oration share a duplicated canonical key; both rows are retained explicitly."),
]
C=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for aid,wid,title,locus,wc,note in D:
  candidates=[r for r in C if r['tlg_author_id']==aid and r['tlg_work_id']==wid]
  s=candidates[0] if len(candidates)==1 else next(r for r in candidates if r['work_title']==title)
  r={f:'' for f in F};r.update(tlg_author_id=aid,tlg_work_id=wid,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {title} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {title} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
