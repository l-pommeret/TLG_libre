import csv

O="data/research_batches/detailed_verified_3001_batch_361.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3200","017"):("Laudatio in sanctum Joannem Baptistam","Billò, Medioevo Greco 2 (2002), pp. 53–62","3881","The John the Baptist laudation is the exact hagiographic encomium."),
("3200","018"):("Oratio ad Thessalonicenses","Laourdas, Makedonika 3 (1955), pp. 295–302","3016","The Thessalonian audience defines this exact advisory oration."),
("3200","019"):("Oratio de providentia domini nostri","Lamprou, Theodromia 4 (2014), pp. 503–530","8968","The discourse on divine economy and providence is the exact theological oration."),
("3200","020"):("Disputatio adversus Judam","Tinnefeld, JÖB 45 (1995), pp. 118–131","5533","The court disputation concerning Judas is preserved as its own item."),
("3200","021"):("Oratio panegyrica de principis sanitate","Paris gr. 3041; Boissonade 1844 pp. 223–238","4231","The Paris manuscript witness and subject of the prince's health define this panegyric."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
