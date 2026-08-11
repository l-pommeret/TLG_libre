import csv
O="data/research_batches/detailed_verified_3001_batch_427.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4036","010"):("In Platonis Timaeum commentaria","Diehl 1903–1906, vol. 1 pp. 1–458; vol. 2 pp. 1–317; vol. 3 pp. 1–358","315888","All three volumes, dates, loci, and the 1965 reprint are preserved."),
("4036","011"):("In primum Euclidis elementorum librum commentarii","Friedlein 1873, pp. 3–436","81631","Only the commentary on Euclid's first book is included."),
("4036","012"):("De decem dubitationibus circa providentiam","Boese, Tria opuscula (1960), pp. 5–108","13107","The embedded PROCLUS heading that splits 'providentiam' in the extracted canon title is recorded as an extraction artefact, without altering canonical_edition."),
("4036","013"):("De providentia et fato et eo quod in nobis ad Theodorum mechanicum","Boese 1960, pp. 117–137, 141–155, 159–163, 169–171","5308","All four discontinuous page spans and the addressee Theodorus mechanicus are preserved."),
("4036","014"):("De malorum subsistentia","Boese 1960, pp. 173–191 and 211–265","9238","Both discontinuous page spans are preserved and remain separate from the other two Boese opuscula."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
