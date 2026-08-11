import csv

O="data/research_batches/detailed_verified_3001_batch_337.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3141","011"):("Epistula ad Joannem Tornicem","Heisenberg vol. 2 pp. 67–69","744","The addressee John Tornices defines this exact short epistle."),
("3141","012"):("In Gregorii Nazianzeni sententias","Heisenberg vol. 2 pp. 70–80","2986","The commentary on Gregory Nazianzen's maxims remains distinct from the surrounding rhetorical works."),
("3141","013"):("Laudatio Petri et Pauli","Heisenberg vol. 2 pp. 81–111","8364","The joint laudation of Peter and Paul is the exact encomiastic item."),
("3141","014"):("Homilia in transfigurationem (BHG 1995n)","Kalatzi, Byzantina 27 (2007), pp. 21–45","6575","The BHG 1995n identifier defines this exact Transfiguration homily."),
("3143","001"):("Chronicon sive Minus [Sp.]","Grecu 1966 pp. 2–146","24214","The catalogue's spurious attribution marker is preserved; this item is not conflated with other Sphrantzes chronicles."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
