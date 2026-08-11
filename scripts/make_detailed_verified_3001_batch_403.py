import csv

O="data/research_batches/detailed_verified_3001_batch_403.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3344","018"):("Liber onirocriticus, Drexl edition","Drexl 1922 pp. 100–118","1953","This dream book edition remains separate from Guidorizzi duplicate-title record 3344.013."),
("3350","001"):("Vita sancti Andreae Cretensis","Papadopoulos-Kerameus 1898 pp. 169–179","2501","The Andrew of Crete 3005 cross-reference is contextual and remains separate."),
("3352","001"):("Paulicianorum historia brevis","Astruc, Travaux et mémoires 4 (1970), pp. 80–92","1122","The concise Paulician history is the exact item."),
("3355","001"):("Oratio antirrhetica","Schminck 1977 pp. 223–230","2603","Cross-references to Michael III 3078.003 and Manuel I 3331.002 remain separate contextual records."),
("3356","001"):("Tomus de duobus fratribus et consobrinis","MPG 119 cols. 728–741","2293","The exact matrimonial decision concerning two brothers and two female cousins was checked."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
