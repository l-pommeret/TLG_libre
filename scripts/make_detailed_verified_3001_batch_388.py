import csv

O="data/research_batches/detailed_verified_3001_batch_388.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3294","006"):("Fragmenta de processione, book IV","MPG 141 cols. 1405–1413","1225","Book IV fragments remain separate from book V; their shared boundary column 1413 is preserved."),
("3294","007"):("Fragmenta de processione, book V","MPG 141 cols. 1413–1420","1055","Book V remains separate from book IV; shared col. 1413 is preserved and trailing METOPUS text is a catalogue heading."),
("3295","001"):("Sermo ad conceptionem sanctae Annae","Kyriakopoulos 1976 pp. 22–34","2445","The conception of Saint Anne defines this exact homily."),
("3295","002"):("Epitaphius ad Athanasium Methonis","Kyriakopoulos 1976 pp. 44–66","4190","This Athanasius epitaph record remains separate from the BHG 196 funeral-oration edition at 3295.008."),
("3295","003"):("Encomium Cosmae et Damiani","Kyriakopoulos 1976 pp. 82–108","4848","The paired Anargyroi Cosmas and Damian define this exact encomium."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
