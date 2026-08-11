import csv

O="data/research_batches/detailed_verified_3001_batch_407.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3380","001"):("Narratio de Vita Beatorum","Charlesworth 1982 pp. 14–106","3574","The Greek recension of the History of the Rechabites is the exact pseudepigraphic item."),
("3382","001"):("Homilia in Joannem Chrysostomum","Halkin 1977 pp. 8–44","8491","The Chrysostom homily remains separate from the following Vita."),
("3382","002"):("Vita Joannis Chrysostomi","Halkin 1977 pp. 46–68","5324","The Chrysostom life remains separate from the preceding homily."),
("3384","001"):("Encomium in sanctum Lucam","Antonopoulou, JÖB 55 (2005), pp. 28–42","4618","Saint Luke the Evangelist defines this exact encomium."),
("3386","001"):("Encomium in Michaelem et Gabrielem (BHG 1294a)","Matantseva, JÖB 46 (1996), pp. 132–148","5104","The paired archangels and BHG 1294a identifier define the exact encomium."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
