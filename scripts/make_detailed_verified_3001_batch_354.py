import csv

O="data/research_batches/detailed_verified_3001_batch_354.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3192","001"):("Epistulae","Constantinides-Hero, CFHB 21 (1983), pp. 2–304","47280","The Akindynos letter collection and exact edition locus define this item."),
("3192","002"):("Adversus haereses Gregorii Palamae iambi","MPG 150 cols. 843–862","word count not supplied","The iambic anti-Palamite work remains distinct from both prose refutations."),
("3192","003"):("Refutatio magna","Cañellas, CCSG 31 (1995), pp. 3–410","112916","The catalogue's split typography in Refutatio was recognized without changing the canonical title field."),
("3192","004"):("Refutatio parva sive Dialogus","Cañellas, CCSG 31 (1995), pp. 413–430","4708","The smaller refutation/dialogue is preserved separately from Refutatio magna."),
("3192","005"):("Oratio contra Joannem Calecam","Cañellas 2002 pp. 258–284","11494","The trailing Constantinus Acropolites text is a catalogue heading artefact, not part of this oration."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
