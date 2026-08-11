import csv
O="data/research_batches/detailed_verified_3001_batch_505.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4321","007"):("Capitula selecta (ex Rhetorii Thesauris)","Cumont, CCAG 8.4 (1921), pp. 118–225","24,927","high","Paris gr.2425 fol.88v and the selected-chapters scope are preserved."),
("4321","009"):("Περὶ σπορᾶς ἐκ τοῦ Ρητορίου","Olivieri, CCAG 2 (1900), pp. 186–187","207","high","Venetian Marcianus 335 fol.112v and the excerpt attribution are preserved."),
("4321","010"):("Ρητορίου πόθεν δεῖ ἐκβαλλεῖν τὰ ἔτη ἐπί τῆς <περὶ> γονέων σκέψεως","Olivieri, CCAG 2 (1900), pp. 212–213","93","high","Venetian Marcianus 335 fol.174 and the supplied angle-bracketed word are preserved."),
("4322","001"):("Testimonia","Radermacher, Artium scriptores (1951), pp. 129–132","word count not supplied","medium","The discontinuous NQ testimony selection Test. 2–7 and 9–13 is preserved; no word count is invented."),
("4324","001"):("Συνεσίου φιλοσόφου πρὸς Διόσκορον εἰς τὴν βίβλον Δημοκρίτου, ὡς ἐν σχολίοις","Berthelot–Ruelle 1888, vol. 2, pp. 56–69","2,677","high","Venetian Marcianus 299 fol.72v, the commentary/dialogue genres, and the trailing SYNESIUS cross-reference token are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,conf,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, relevant manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc} item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence=conf,proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
