import csv
O="data/research_batches/detailed_verified_3001_batch_496.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","027"):("Περὶ οἰκονομίας τοῦ τῆς μαγνησίας σώματος","Berthelot–Ruelle 1888, pp. 188–191","789","Possible Χειρόμηκτα membership and Marcianus 299 fol.157v are preserved."),
("4319","028"):("Περὶ σώματος μαγνησίας καὶ οἰκονομίας","Berthelot–Ruelle 1888, pp. 191–198","1444","Possible Χειρόμηκτα membership and Marcianus 299 fol.159r are preserved; the item remains separate from 4319.027 despite the related title and shared page 191."),
("4319","029"):("Περὶ τοῦ λίθου τῆς φιλοσοφίας","Berthelot–Ruelle 1888, pp. 198–204","1266","Possible Χειρόμηκτα membership and Paris BnF gr.2327 fol.136v are preserved."),
("4319","030"):("Περὶ ἀφορμῶν συνθέσεως","Berthelot–Ruelle 1888, p. 204","113","Possible Χειρόμηκτα membership and Marcianus 299 fol.161v are preserved; the single-page item remains separate from 4319.029."),
("4319","031"):("Περὶ ξηρίου","Berthelot–Ruelle 1888, p. 205","73","Possible Χειρόμηκτα membership and Marcianus 299 fol.136v are preserved; the item remains separate from 4319.032 sharing page and folio."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
