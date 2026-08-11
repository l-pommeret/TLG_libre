import csv
O="data/research_batches/detailed_verified_3001_batch_448.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","017"):("Homilia in nativitate Joannis Baptistae [Sp.]","Latysev 1910, pp. 3–14","","Spurious status and the Theodore Daphnopates wording in the edition title are preserved without resolving authorship; no word count is inferred."),
("4089","020"):("De sancta trinitate","MPG 75, cols. 1148–1189","8462","The Trinity treatise is checked at its exact MPG locus."),
("4089","021"):("De incarnatione domini","MPG 75, cols. 1420–1477","11447","The Incarnation treatise is checked at its exact MPG locus."),
("4089","022"):("Quaestiones in Octateuchum","Fernández Marcos–Sáenz-Badillos 1979, pp. 3–318","68244","All eight book subdivisions and their exact page spans from Genesis through Ruth are preserved."),
("4089","023"):("Quaestiones in libros Regnorum et Paralipomenon","MPG 80, cols. 528–858","51346","The Regnorum and Paralipomenon questions remain separate from the following Psalms interpretation despite adjacent/overlapping boundary columns."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
