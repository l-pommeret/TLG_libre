import csv

O="data/research_batches/detailed_verified_3001_batch_374.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3252","001"):("Historiae","Laurent 1971 pp. 100–574","100965","The Syropulus memoirs of the Council of Florence define the exact history item."),
("3252","002"):("Resipiscentia","Polites 1972–1973 pp. 395–400","2152","The recantation remains distinct from Syropulus' council history."),
("3254","001"):("Capita CL","Sinkewicz 1988 pp. 82–256","23061","The explicit one-hundred-and-fifty-chapter scope is preserved."),
("3254","002"):("Contra Acindynistas","Sinkewicz 1988 pp. 263–269","1773","The quotation of Cyril of Alexandria is an identifying qualifier of this exact anti-Akindynos item."),
("3254","003"):("Pro hesychastis","Meyendorff 1973 pp. 5–727","88527","The defense of the holy hesychasts is the exact large theological item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
