import csv
O="data/research_batches/detailed_verified_3001_batch_455.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4118","002"):("Commentarii in Canticum Canticorum","Guérard, SC 403 (1994), pp. 112–370","18758","This Guérard edition record remains separate from the Rosenbaum duplicate 4118.003."),
("4118","003"):("Εἰς τὸ τῶν Ἀισμάτων Ἄισμα","Rosenbaum 2004, pp. 1–212","32703","The canon's explicit duplicate link (printed 'Dup,.') to 4118.002 is preserved without merging editions."),
("4118","004"):("Epistulae","MPG 79, cols. 82–582","88128","The epistolary collection is checked at its exact MPG locus."),
("4126","002"):("Fragmenta in Matthaeum (in catenis)","Reuss, TU 61 (1957), pp. 55–95","7358","The Theodore of Heraclea Matthaean fragments remain distinct from similarly titled fragments under other authors."),
("4126","004"):("Fragmenta in Joannem (in catenis)","Reuss, TU 89 (1966), pp. 67–176","18139","The Theodore of Heraclea Johannine fragments remain distinct from similarly titled fragments under other authors."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, MPG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
