import csv

O="data/research_batches/detailed_verified_3001_batch_398.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D=[
("3337","002","Encomium in omnes sanctos, MPG 105: 849–856. Cod: Encom., Homilet","MPG 105 cols. 849–856","word count not supplied","The All Saints encomium is exact; no missing word count was invented."),
("3337","003","Theognosti libellus ad Nicolaum I papam in causa Ignatii Constantinopolitani, MPG 105: 856–861. Cod: Eccl., Epist","MPG 105 cols. 856–861","word count not supplied","The Pope Nicholas I addressee and Ignatius case define this exact libellus."),
("3338","001","Typicon monasterii Machaerados in Cypro","Tsiknopoullos 1969 pp. 3–68","17582","The Cypriot Machaeras monastery defines the typikon; Typica Monastica 5330 remains a cross-reference."),
("3339","001","Vita Theophanis et Theodori Grapti (e cod. Metochii S. Sepulcri 244, f. 130–154)","Holy Sepulchre Metochion 244 ff. 130–154; Papadopoulos-Kerameus 1897 pp. 185–223","10552","This life shares a duplicated key with an unrelated plague treatise; Graptus cross-references and the truncated canonical heading are preserved."),
("3339","001","Libellus de pestilentia","Kouzes 1909 pp. 3–18","8227","This translated medical plague treatise shares a duplicated key with the Grapti life; the Rhazes heading contamination is recorded without merging."),
]
C=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for aid,wid,title,locus,wc,note in D:
  s=next(r for r in C if r['tlg_author_id']==aid and r['tlg_work_id']==wid and r['work_title']==title);r={f:'' for f in F};r.update(tlg_author_id=aid,tlg_work_id=wid,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of this item at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
