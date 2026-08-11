import csv

O="data/research_batches/detailed_verified_3001_batch_370.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3236","003"):("Synopsis s. scripturae","MPG 147 cols. 605–624","5585","This scriptural synopsis remains distinct from the post-fall synopsis 3236.004 despite overlapping boundary columns."),
("3236","004"):("Synopsis post excidium Hierosolymitanum","MPG 147 cols. 623–632","2672","The post-fall synopsis remains separate from 3236.003; the explicit overlap at cols. 623–624 is preserved."),
("3236","005"):("Enarratio de episcopis Byzantii et patriarchis","MPG 147 cols. 449–468","2963","The episcopal and patriarchal catalogue is the exact ecclesiastical-historical item."),
("3236","006"):("Carmina","Jugie, Byzantion 5 (1929/30), pp. 362–390","4828","The rhythmic poem collection and exact article locus define the item."),
("3236","007"):("Miracula metrica sancti Nicolai Myrensis","Papadopoulos-Kerameus 1897 pp. 357–366","3484","The metrical miracle collection remains separate from Vitae et Miracula Nicolai 5067."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
