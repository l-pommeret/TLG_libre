import csv
O="data/research_batches/detailed_verified_3001_batch_484.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4231","002"):("Circa Helenam et Alexandrum","Meschini 1977, pp. 35–49","2999","The Helen and Alexander narrative is checked as the exact item."),
("4231","003"):("Declamationes","Stefec, Byzantion 83 (2013), pp. 380–394","5087","The two additional declamations are checked as the exact journal item."),
("4233","001"):("Commentarium in Hermogenis περὶ στάσεων, part 1","Romano 1987–1989, pp. 271–274","903","The Paris supplementum graecum 670 fols.1r–2v item remains separate from the fols.36v–65r item."),
("4233","002"):("Commentarium in Hermogenis περὶ στάσεων, part 2","Rychlewska, Eos 41–42, loci 41:173–184 and 42:195–211","","Both Eos volume/date/locus pairs and Paris suppl.gr.670 fols.36v–65r are preserved; no count is supplied."),
("4236","001"):("Prolegomena in artem rhetoricam","Rabe, Rhetores Graeci 14 (1931), pp. 1–14","2946","The rhetorical prolegomena are checked as the exact Rabe item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
