import csv
O="data/research_batches/detailed_verified_3001_batch_511.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4351","007"):("<Πάλχου> περὶ στάσεως καὶ ἐμφυλίων πολέμων καὶ σφαγῆς","Cumont, CCAG 8.1 (1929), p. 248","110","The supplied Palchus attribution, Parisinus 2506 fol.57r, and tentative Eleutherius compilation are preserved."),
("4351","008"):("<Πάλχου> περὶ τροπῆς ἔαρος","Cumont, CCAG 8.1 (1929), pp. 261–263","676","The supplied Palchus attribution, Parisinus 2506 fol.139v, and tentative Eleutherius compilation are preserved."),
("4351","009"):("<Πάλχου> περὶ τροπῶν τῶν δʹ καιρῶν","Cumont, CCAG 9.1 (1951), pp. 157–161","1,148","The supplied Palchus attribution, Cromwellianus 12 p.416, and tentative Eleutherius compilation are preserved."),
("4351","010"):("<Πάλχου> περὶ ἀποδημίας ἐξ ἀνεπιγράφου","Cumont, CCAG 8.1 (1929), pp. 250–252","680","The supplied Palchus attribution, anonymous-source wording, Parisinus 2506 fol.71v, and tentative Eleutherius compilation are preserved."),
("4351","011"):("<Πάλχου> περὶ ἀφροδισίων ἵνα ἔρωτες γένωνται","Weinstock, CCAG 9.1 (1951), pp. 183–184","191","The supplied Palchus attribution, Arch. Seldenianus sup.17 fol.120v, and tentative Eleutherius compilation are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, astrological manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
