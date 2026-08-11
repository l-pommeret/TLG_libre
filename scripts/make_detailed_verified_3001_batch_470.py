import csv
O="data/research_batches/detailed_verified_3001_batch_470.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4146","013"):("Disticha Catonis in Graecum translata","Ortoleva 1992, pp. 1–19","2483","This Greek translation record remains separate from the Munich-manuscript version 4146.014."),
("4146","014"):("Disticha Catonis graece versa","Ortoleva 1992, pp. 21–32","2092","The Monacensis graecus 551 version remains separate from 4146.013; no unprinted duplicate relation is asserted."),
("4146","015"):("Canones","Gallavotti, Bollettino dei Classici 3/8 (1987), pp. 98–114","2340","The hymn canons are checked as the exact Anecdota Planudea item."),
("4146","016"):("Epigrammata X","Lampros 1916, pp. 415–421","1096","The explicit collection of ten epigrams is preserved as one item."),
("4146","017"):("Idyllium","Pontani 1973, pp. 12–26","1954","The Idyllium is checked as the exact Pontani item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
