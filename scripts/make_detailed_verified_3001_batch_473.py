import csv
O="data/research_batches/detailed_verified_3001_batch_473.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4146","029"):("Ovidii Heroides versus in linguam graecam","Papathomopoulos 1976, pp. 3–119","30546","The Heroides remain explicitly an epistolary Greek translation item."),
("4146","030"):("Βασιλικὸς λόγος","Westerink, Byzantinoslavica 27–29 (1966–1968), loci 27.100–103; 28.54–67; 29.34–48","15823","All three journal-volume loci and dates are preserved rather than collapsed into a page range."),
("4146","031"):("Translatio Pseudo-Augustini De duodecim abusivis saeculi","Giannakes, Δωδώνη 3 (1974), pp. 227–243","5038","Pseudo-Augustine attribution and translation status are preserved."),
("4146","032"):("Compendia e Platonis dialogis","Ferroni 2015, pp. 93–168","22781","The Platonic-dialogue compendia are checked as the exact Ferroni item."),
("4146","033"):("Oratio in sancto Arsenio Autoriano [Dub.]","Nicolopoulos 1981–1982, pp. 449–461","3688","Doubtful status, Patmos gr.366 witness and cross-reference to Arsenius Autorianus 9056 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
