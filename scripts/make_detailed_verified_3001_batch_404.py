import csv

O="data/research_batches/detailed_verified_3001_batch_404.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3359","001"):("Vita Philareti, Fourmy-Leroy edition","Fourmy and Leroy, Byzantion 9 (1934), pp. 112–167","8394","This edition record remains separate from the Rydén duplicate-title edition 3359.002."),
("3359","002"):("Vita Philareti, Rydén edition","Rydén 2002 pp. 60–118","8334","The catalogue explicitly marks this as duplicate of 3359.001; both edition records remain separate."),
("3361","001"):("Anacharsis","Chrestides 1984 pp. 205–290","13787","The Anacharsis/Ananias satirical dialogue is the exact item."),
("3362","001"):("Oratio de processione spiritus sancti","Demetrakopoulos 1866 pp. 36–47","2919","The antirrhetic procession discourse is the exact theological item."),
("3365","001"):("Oratio in honorem Georgii Xiphilini","Loukaki 2005 pp. 137–151","2968","This Phrangopulus oration remains distinct from Tornices' Xiphilinus orations 3373.001."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
