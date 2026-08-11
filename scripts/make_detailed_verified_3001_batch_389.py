import csv

O="data/research_batches/detailed_verified_3001_batch_389.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3295","004"):("Encomium ad sanctam Annam","Kyriakopoulos 1976 pp. 116–128","2147","The Anne encomium remains distinct from the conception sermon 3295.001."),
("3295","005"):("Sermo ad annuntiationem Theotoci","Kyriakopoulos 1976 pp. 134–146","2298","The Annunciation sermon remains distinct from the Entry sermon."),
("3295","006"):("Sermo ad ingressum Theotoci","Kyriakopoulos 1976 pp. 152–176","4612","The Entry of the Theotokos sermon remains distinct from the Annunciation sermon."),
("3295","007"):("Encomium ad sanctam Barbaram","Kyriakopoulos 1976 pp. 186–214","4851","The great martyr Barbara defines this exact encomium."),
("3295","008"):("Oratio funebris in Athanasium (BHG 196)","Kaldellis and Polemis 2019 pp. 70–114 (even pages)","4186","BHG 196, even-page printing, and equivalence to Mai IX pp. 31–51 are preserved; record 3295.002 remains separate."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
