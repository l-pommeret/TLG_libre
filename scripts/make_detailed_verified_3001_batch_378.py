import csv

O="data/research_batches/detailed_verified_3001_batch_378.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3254","019"):("Epistula in dictum Basilii Caesarensis","Pseftonkas 1988 pp. 382–389","1768","The letter on a saying of Basil of Caesarea is the exact item."),
("3255","001"):("Callimachus et Chrysorrhoe","Pichard 1956 pp. 1–92","18765","The Callimachus and Chrysorrhoe romance is the exact fictional narrative."),
("3259","001"):("Vita Euthymii patriarchae (BHG 651)","Karlin-Hayter 1970 pp. 3–147","21168","The BHG 651 identifier defines the complete patriarchal life."),
("3259","002"):("Fragmentum vitae Euthymii","Flusin, Travaux et mémoires 9 (1985), pp. 123–131","1297","The questioned unpublished fragment remains distinct from the complete BHG 651 life."),
("3263","001"):("Sermones duo apologetici","Patrineles 1966 pp. 91–152","23767","The explicit two-sermon scope is preserved exactly."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
