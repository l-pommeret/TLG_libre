import csv

O="data/research_batches/detailed_verified_3001_batch_394.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3321","004"):("Prostagmata","Lampros 1926 pp. 345–352","1829","The imperial ordinances remain distinct from the preceding chrysobulls."),
("3322","001"):("Epistulae","Eustratiades and Spyridon 1925 pp. 412–413, 414–415 and 416","1199","All three explicit letter loci are preserved separately."),
("3322","002"):("Epistula ad Bessarionem","Boissonade 1833 vol. 5 pp. 389–401","1480","The Bessarion addressee and equivalence to MPG 161 cols. 723–728 are preserved."),
("3322","003"):("Carmina","van Deun and Janssens 2004 pp. 314–318","715","The short poetic oeuvre remains distinct from the philosophical tractates."),
("3322","004"):("Tractatus philosophicus","Monfasani 2011 pp. 56–198","17907","The philosophical tractate collection is the exact item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
