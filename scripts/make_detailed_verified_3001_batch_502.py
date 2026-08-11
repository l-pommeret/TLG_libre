import csv
O="data/research_batches/detailed_verified_3001_batch_502.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","057"):("Excerptum alchemicum (sine titulo)","Mertens, pp. 11–13","305","All five manuscript loci are preserved, as are the partial-duplicate links to 4319.047 and 4319.049."),
("4319","058"):("Περὶ του τριβίκου καὶ τοῦ σωλῆνος","Mertens, pp. 14–15","213","The composite manuscript loci and partial-duplicate links to 4319.047 and 4319.050 are preserved."),
("4319","059"):("Excerptum alchemicum (sine titulo)","Mertens, pp. 16–20","678","Untitled status, discontinuous Marcianus loci, and partial-duplicate links to 4319.047 and 4319.050 are preserved."),
("4319","060"):("Περὶ τοῦ θείου ὕδατος","Mertens, p. 21","102","All Marcianus, Parisinus, and Laurentianus manuscript loci are preserved."),
("4319","061"):("Diagramma","Mertens, p. 22","35","The diagram is treated as its own 35-word canon item; the anomalous embedded ZOSIMUS token in the Parisinus locus is preserved verbatim."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
