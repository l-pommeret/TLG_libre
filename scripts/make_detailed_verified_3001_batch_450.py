import csv
O="data/research_batches/detailed_verified_3001_batch_450.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","029"):("Interpretatio in xii prophetas minores","MPG 81, cols. 1545–1988","80255","The twelve-minor-prophets interpretation begins one column before the Daniel item ends; the exact overlapping loci are preserved without merging."),
("4089","030"):("Interpretatio in xiv epistulas sancti Pauli","MPG 82, cols. 36–877","154967","All fourteen Pauline epistles are preserved as the scope of the item."),
("4089","031"):("Haereticarum fabularum compendium","MPG 83, cols. 336–556","39853","The heresiological compendium remains separate from the providence orations sharing boundary column 556."),
("4089","032"):("De providentia orationes decem","MPG 83, cols. 556–773","41795","All ten orations and the shared boundary column 556 are preserved."),
("4089","033"):("Libellus contra Nestorium ad Sporacium [Sp.]","MPG 83, cols. 1153–1164","2065","The spurious attribution is preserved without resolution."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
