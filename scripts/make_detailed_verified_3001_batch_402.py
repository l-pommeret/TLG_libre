import csv

O="data/research_batches/detailed_verified_3001_batch_402.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3344","013"):("Liber Onirocriticus, Guidorizzi edition","Guidorizzi 1980 pp. 51–82","2039","This dream book edition remains separate from the Drexl duplicate-title edition 3344.018."),
("3344","014"):("De cherubinis","Declerck 2004 pp. 127–144","4478","The attribution among seven image-making opuscules is preserved as given, without resolution."),
("3344","015"):("Breviarium historicum, Mango main text","Mango, CFHB 13 (1990), pp. 34–162","16623","Equivalence to MPG 100 cols. 876–994 and partial duplicate 3086.016 chapters 1–11 are preserved."),
("3344","016"):("Breviarium chapters i–xi","London Add. 19390; Mango 1990 pp. 165–172","2093","The London witness and explicit chapters i–xi remain separate; partial duplicate 3086.015 is preserved."),
("3344","017"):("Canones","MPG 100 cols. 852–864","1823","The ecclesiastical canons are the exact item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
