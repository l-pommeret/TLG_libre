import csv

O="data/research_batches/detailed_verified_3001_batch_333.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3135","002"):("Epitome historiarum, books 13–18","Büttner-Wobst 1897 pp. 1–768","114741","This continuation remains distinct from books 1–12 and the doubtful alternate close."),
("3135","003"):("Epitome historiarum, book 12 alternate close [Dub.]","Dindorf vol. 3 (1870), pp. 169–171","622","The doubtful alternate close is retained as a separate short item, not merged into 3135.001."),
("3135","004"):("Epitome historiarum, books 1–12 (Pinder)","Pinder 1841–1844: vol. 1 pp. 3–562; vol. 2 pp. 3–628","word count not supplied","This Pinder edition record remains separate from the Dindorf duplicate-title edition 3135.001."),
("3135","005"):("Vita s. Eupraxiae (BHG 631m)","Kaltsogianni 2013 pp. 508–528","6998","The BHG 631m identifier defines this exact hagiographic item."),
("3135","006"):("Vita s. Silvestri (BHG 1633–1634)","Kaltsogianni 2013 pp. 530–558","10057","Both BHG identifiers belong to this exact Silvester life and are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
