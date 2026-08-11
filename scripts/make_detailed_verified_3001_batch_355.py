import csv

O="data/research_batches/detailed_verified_3001_batch_355.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3196","001"):("Epistulae","Romano 1991 pp. 109–268","28146","The Constantine Acropolites letter collection is the exact item."),
("3196","002"):("Encomium Euphrosynae iunioris","Halkin, Byzantion 57 (1987), pp. 56–65","2971","The younger Euphrosyne defines this exact hagiographic encomium."),
("3196","003"):("Testamentum Constantini Acropolitae","Delehaye, Analecta Bollandiana 51 (1933), pp. 279–284","1855","The Typica Monastica 5330 cross-reference is contextual and remains separate."),
("3196","004"):("Oratio in Anicetum et Photium (BHG 1544f)","Ambrosian gr. 442 ff. 261–267v; Kalatzi 2003 pp. 394–399","2236","The manuscript folios and BHG 1544f identifier both define this exact oration."),
("3196","005"):("Oratio in Florum et Laurum","Kalatzi, Byzantion 71 (2001), pp. 513–516","915","The paired saints Florus and Laurus define this distinct short oration."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
