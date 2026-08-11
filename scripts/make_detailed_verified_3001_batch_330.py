import csv

O="data/research_batches/detailed_verified_3001_batch_330.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3129","010"):("Epistulae 4–133 and 135","Gautier, CFHB 16.2 (1986), pp. 137–597","43627","The explicit selection omits epistle 134; that discontinuity is preserved."),
("3129","011"):("Epistulae ad Bryennium","Gautier, CFHB 9 (1975), pp. 317–337","2339","This Bryennius dossier is distinct from the general letter collection 3129.010."),
("3129","012"):("Vita Clementis Ochridensis","Milev 1966 pp. 76–146","10109","The cross-reference to Demetrius Chomatenus 3216.002 is contextual and remains separate."),
("3129","013"):("Encomium quindecim martyrum Tiberiopolitensium (BHG 1199)","Vlachakos 2008 pp. 214–378","12754","The modern edition is explicitly equated by the catalogue with MPG 126 cols. 151–222."),
("3129","014"):("Enarrationes in evangelia","MPG 123 cols. 140–1348 and 124 cols. 10–317","324717","Both explicit MPG volume loci define the exact large commentary item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
