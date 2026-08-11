import csv
O="data/research_batches/detailed_verified_3001_batch_438.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","036"):("De schismate Graecorum [Dub.]","Pavlov 1878, pp. 132–134","773","Doubtful status, possible Nicetas Chartophylax authorship and equivalence to MPG 120, cols. 713–720 are preserved."),
("4040","037"):("Opusculum contra Francos","Hergenroether 1869, pp. 62–71","1102","The anti-Frankish opusculum is checked as its exact short item."),
("4040","038"):("Opuscula de origine schismatis [Dub.]","Hergenroether 1869, pp. 154–181","3976","Doubtful status and the mixed Cod/Q source designation are preserved."),
("4040","039"):("Adversus primatum Romae [Dub.]","Gordillo, OCP 6 (1940), pp. 11–17","1590","Doubtful status is preserved. The embedded PHOTIUS Diaconus heading in the article title is recorded as an extraction artefact, not normalized in canonical_edition."),
("4040","040"):("Versus ad Basilium I imperatorem [Dub.]","Markopoulos, DOP 46 (1992), pp. 230–231","","Doubtful status, Laurentianus Plut. IX.23 witness and anonymous-poem edition title are preserved; the canon gives no word count."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
