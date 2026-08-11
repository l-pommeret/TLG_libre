import csv
O="data/research_batches/detailed_verified_3001_batch_447.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","006"):("Epistulae: Collectio Sirmondiana (1–95)","Azéma, SC 98 (1964), pp. 20–248","21752","Letters 1–95 remain a distinct collection segment from 96–147."),
("4089","007"):("Epistulae: Collectio Sirmondiana (96–147)","Azéma, SC 111 (1965), pp. 10–232","23600","Letters 96–147 remain a distinct collection segment from 1–95."),
("4089","008"):("Commentaria in Isaiam","Guinot, SC 276/295/315 (1980–1984), explicit loci in vols. 1–3","99622","All three volume identifiers, dates and loci are preserved."),
("4089","009"):("Interpretatio in Isaiam (4–20)","Möhle 1932, pp. 50–263","","The exact chapters 4–20 are preserved and no absent word count is inferred."),
("4089","016"):("Quaestiones et responsiones ad orthodoxos [Dub.]","Papadopoulos-Kerameus 1895, pp. 1–150","35955","The doubtful attribution is preserved without resolution."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
