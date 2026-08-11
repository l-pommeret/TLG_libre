import csv
O="data/research_batches/detailed_verified_3001_batch_446.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","001"):("Graecarum affectionum curatio","Canivet, SC 57 (1958), vol. 1 pp. 100–287; vol. 2 pp. 296–446","67184","Both volumes and their separate loci are preserved."),
("4089","002"):("Eranistes","Ettlinger 1975, pp. 61–266","55540","The apologetic/theological dialogue is checked as the exact Ettlinger item."),
("4089","003"):("Historia ecclesiastica","Parmentier–Scheidweiler, 2nd ed. (1954), pp. 1–349","68392","First1KGreek, OPP and PTA identifier candidates exist, but exact second-edition and license verification is not established locally."),
("4089","004"):("Historia religiosa (= Philotheus)","Canivet–Leroy-Molinghen, SC 234/257 (1977–1979), all explicit loci","49926","All discontinuous loci and the Philotheus 31 equivalence are preserved. The embedded THEODORETUS heading is recorded as an artefact; the First1K candidate remains unverified."),
("4089","005"):("Epistulae: Collectio Patmensis (1–52)","Azéma, SC 40 (1955), pp. 74–121","8608","The Patmos collection and its exact letters 1–52 remain separate from the Sirmondiana collections."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
