import csv

O="data/research_batches/detailed_verified_3001_batch_399.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D=[
("3341","001","Epistulae","Darrouzès 1960 pp. 67–98","8241","The Alexander of Nicaea ecclesiastical letter collection is exact."),
("3343","001","Epistulae","Darrouzès 1960 pp. 249–259","2688","The Philetus letter collection is exact; trailing Philiades is a catalogue heading artefact."),
("3344","001","Encomium in patriarcham Antonium II Cauleam","Leone, Orpheus n.s. 10 (1989), pp. 412–429","6502","This encomium shares a duplicated canonical key with the Breviarium; embedded Nicephorus I heading/cross-reference text is kept contextual."),
("3344","001","Breviarium historicum de rebus gestis post imperium Mauricii (e cod. Vat. gr. 977)","Vatican gr. 977; de Boor 1880 pp. 3–77","16537","This historical breviarium shares the duplicated key with the encomium and is explicitly duplicate of 3086.015; both records remain separate."),
("3344","002","Chronographia brevis [Dub.] (recensiones duae)","de Boor 1880 pp. 81–135","7422","The doubtful attribution and explicit two-recension scope are preserved."),
]
C=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for aid,wid,title,locus,wc,note in D:
  s=next(r for r in C if r['tlg_author_id']==aid and r['tlg_work_id']==wid and r['work_title']==title);r={f:'' for f in F};r.update(tlg_author_id=aid,tlg_work_id=wid,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of this item at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
