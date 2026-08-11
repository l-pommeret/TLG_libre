import csv
O="data/research_batches/detailed_verified_3001_batch_486.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4250","001"):("Fragmentum","Montanari 1988, p. 114, fragment 1","173","The single grammatical fragment and Q medium are preserved."),
("4252","001"):("Testimonia","Montanari 1988, p. 120, testimonium 2","","The NQ testimony and Greek label Πρὸς τὸ παράδοξον are preserved; no word count is supplied."),
("4260","001"):("Testimonia","Döring 1972, pp. 29, 31, 41–45","","All testimony numbers 101,104,110,135–137,141–142,144(?) and attribution splits between Diodorus Cronus 0073.001 and Philo are preserved."),
("4261","001"):("Testimonia","Döring 1972, pp. 19, 39, 45","","All testimonia 63,131,145–146 and their Diodorus Cronus/Panthoides allocation are preserved."),
("4262","001"):("Testimonia","Döring 1972, every explicit locus pp. 10–62","","The complete discontinuous testimony-number list and cross-attributions to Euclides, Euphantus, Alexinus, Diodorus Cronus and Bryson are retained in canonical_edition."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, fragment/testimonia corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
