import csv
O="data/research_batches/detailed_verified_3001_batch_500.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","047"):("Ζωσίμου περὶ ὀργάνων καὶ καμίνων","Berthelot–Ruelle 1888, pp. 224–227","887","Marcianus 299 fol.186r and all partial duplicate links 4319.050,057–059,062 are preserved."),
("4319","048"):("Ποίησις ἐκ τουτίας ἀργύρου","Berthelot–Ruelle 1888, pp. 227–228","61","Marcianus 299 fol.188r is preserved; this item has no printed duplicate link."),
("4319","049"):("Περὶ ὀργάνων καὶ καμίνων... ω στοιχείου","Berthelot–Ruelle 1888, pp. 228–235","1819","Marcianus 299 fol.189r and partial duplicate links 4319.001 and 4319.057 are preserved."),
("4319","050"):("Περὶ τοῦ τριβίκου καὶ τοῦ σωλῆνος","Berthelot–Ruelle 1888, pp. 236–238","665","Marcianus 299 fol.194r and all partial duplicate links 4319.047,058–059,062 are preserved."),
("4319","051"):("Τὸ πρῶτον βιβλίον τῆς τελευταίας ἀποχῆς","Berthelot–Ruelle 1888, pp. 239–246","1663","Paris BnF gr.2327 fol.251v and the first-book designation are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
