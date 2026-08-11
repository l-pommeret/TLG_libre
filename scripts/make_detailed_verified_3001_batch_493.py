import csv
O="data/research_batches/detailed_verified_3001_batch_493.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","012"):("Περὶ τῶν ὑποστάτων καὶ τῶν δʹ σωμάτων","Berthelot–Ruelle 1888, pp. 148–153","1091","Possible membership in Χειρόμηκτα, possible joint authorship by Zosimus and Theosebeia, and Marcianus 299 fol.141v are preserved without resolution."),
("4319","013"):("Περὶ διαφορᾶς χαλκοῦ κεκαυμένου","Berthelot–Ruelle 1888, pp. 153–154","130","Possible Χειρόμηκτα membership, Marcianus 299 fol.144r and cross-reference to 4319.046 are preserved."),
("4319","014"):("Περὶ τοῦ ὅτι πάντων τῶν ὑγρῶν...","Berthelot–Ruelle 1888, pp. 154–156","299","Possible Χειρόμηκτα membership and Marcianus 299 fol.144r are preserved; embedded ZOSIMUS splitting the title is recorded as a heading artefact."),
("4319","015"):("Περὶ τοῦ ἐν παντὶ καιρῷ ἀρκτέον τὸ ἔργον","Berthelot–Ruelle 1888, pp. 156–158","612","Possible Χειρόμηκτα membership and Marcianus 299 fol.144v are preserved."),
("4319","016"):("Περὶ τῆς κατὰ πλάτος ἐκδόσεως τὸ ἔργον","Berthelot–Ruelle 1888, pp. 159–167","1920","Possible Χειρόμηκτα membership and Marcianus 299 fol.145v are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
