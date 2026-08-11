import csv
O="data/research_batches/detailed_verified_3001_batch_425.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4034","009"):("In Aristotelis sophisticos elenchos commentarius (selecta)","Ebbesen, CLCAG 7.2 (1981), pp. 153–199","5677","The selecta designation and equivalence to Pseudo-Alexander 2 plus commentary 5 are preserved."),
("4036","001"):("In Platonis rem publicam commentarii","Kroll 1899–1901, vol. 1 pp. 1–296; vol. 2 pp. 1–368","162763","Both volumes and the 1965 reprint are preserved; an OPP candidate is not exact Kroll edition/license verification."),
("4036","002"):("Hypotyposis astronomicarum positionum","Manitius 1909 (repr. 1974), pp. 2–238","24378","The astronomical Hypotyposis is checked independently from Proclus's philosophical commentaries."),
("4036","003"):("Epigramma AG 7.341","Anthologia Graeca 7.341","27","The single epigram and the canon's partial-duplicate cross-reference to 4036.017 are preserved."),
("4036","004"):("Theologia Platonica (lib. 1–6)","Saffrey–Westerink 1968–1997, explicit loci in vols. 1–6","146906","All six volume dates and loci remain in canonical_edition; the partial-duplicate cross-reference to 4036.020 is preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
