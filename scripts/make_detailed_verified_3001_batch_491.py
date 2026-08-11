import csv
O="data/research_batches/detailed_verified_3001_batch_491.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","002"):("Περὶ ἀρετῆς, praxis 1","Berthelot–Ruelle 1888, pp. 107–113","1140","Venetianus Marcianus 299 fol.92v and explicit duplicate 4319.065 are preserved."),
("4319","003"):("Περὶ τῆς ἀσβέστου","Berthelot–Ruelle 1888, pp. 113–115","373","Both witnesses—Marc.299 fol.95r and Paris BnF gr.2327 fol.8v—and duplicate 4319.068 are preserved."),
("4319","004"):("Πρᾶξις βʹ","Berthelot–Ruelle 1888, pp. 115–117","397","Paris BnF gr.2327 fol.87v and duplicate 4319.066 are preserved."),
("4319","005"):("Ποίημα Ζωσίμου, πρᾶξις γʹ","Berthelot–Ruelle 1888, pp. 117–118","184","Paris BnF gr.2327 fol.88r and duplicate 4319.067 are preserved."),
("4319","006"):("Περὶ ἀρετῆς καὶ ἑρμηνείας","Berthelot–Ruelle 1888, pp. 118–138","3714","Paris BnF gr.2327 fol.168v is preserved; this record has no printed duplicate link."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
