import csv
O="data/research_batches/detailed_verified_3001_batch_452.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","041"):("Ex sermone Chalcedone contra Cyrillum habito 1","Schwartz–Straub, ACO 4.1, pp. 132–133","The first Chalcedon sermon extract remains separate from extract 2 and ends where it begins."),
("4089","042"):("Ex sermone Chalcedone contra Cyrillum habito 2","Schwartz–Straub, ACO 4.1, p. 133","The second extract is a separate single-page item sharing page 133 with extract 1."),
("4089","043"):("Ex allocutione Antiochiae dicta 1","Schwartz–Straub, ACO 1.5.1 p. 173 and 4.1 p. 136","Both witnesses/loci in two ACO volumes and their separate dates are preserved."),
("4089","044"):("Ex allocutione Antiochiae dicta 2","Schwartz–Straub, ACO 4.1, p. 136","The second Antioch allocution extract remains separate despite sharing page 136 with 4089.043."),
("4089","062"):("Ad Abundium episcopum Comensem (epistula 181)","MPG 83, cols. 1492–1494","The letter number, recipient and MPG locus are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, ACO/MPG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' The canon notice ends with bare Q and supplies no word count or genre; none is inferred. No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
