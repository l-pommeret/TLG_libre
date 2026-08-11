import csv

O="data/research_batches/detailed_verified_3001_batch_379.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3263","002"):("Epistulae","Eustratiades and Spyridon 1925 pp. 412–421","6586","The Agallianus letter collection is distinct from the following providence treatise."),
("3263","003"):("De providentia","Eustratiades and Spyridon 1925 pp. 421–434","11291","The providence treatise remains separate despite sharing boundary page 421 with the letters."),
("3263","004"):("Refutatio Joannis Argyropuli","Lampros 1910 pp. 234–303","16890","The catalogue's split typography in Refutatio is noted without altering the canonical title field."),
("3263","005"):("Dialogus cum monacho contra Latinos","Blanchet 2013 pp. 31–97","11185","The 1442 dialogue with a monk is distinct from the shorter Contra Latinos sylloge."),
("3263","006"):("Contra Latinos","Levrie, JÖB 65 (2015), pp. 139–148","3304","The anti-Latin sylloge is preserved separately from the dialogue 3263.005."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
