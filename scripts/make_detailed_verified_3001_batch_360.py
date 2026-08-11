import csv

O="data/research_batches/detailed_verified_3001_batch_360.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3200","012"):("Imago veris in aulaeo textili","Davis 2003 pp. 411–412","470","The exact short rhetorical description of spring on a woven hanging was checked."),
("3200","013"):("Canon supplicationis","Legrand 1893 pp. 94–102","931","The supplicatory canon is preserved as a distinct hymn item."),
("3200","014"):("De periculo Turcorum","Legrand 1893 pp. 103–104","278","The short rhetorical item on the Turkish danger remains separate from adjacent works."),
("3200","015"):("Psalmus","Legrand 1893 p. 104","199","The single-page psalm is its own short hymn item, not merged with 3200.014."),
("3200","016"):("Στίχοι πρὸς ἄθεον ἄνδρα","Vassis, Byzantina 32 (2012), pp. 55–78","5758","The verses addressed to an atheist define the exact poem."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
