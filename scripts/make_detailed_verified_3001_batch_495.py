import csv
O="data/research_batches/detailed_verified_3001_batch_495.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","022"):("Περὶ σταθμῶν","Berthelot–Ruelle 1888, pp. 177–179","308","Possible Χειρόμηκτα membership and Marcianus 299 fol.153r are preserved."),
("4319","023"):("Περὶ καύσεως σωμάτων","Berthelot–Ruelle 1888, pp. 179–181","470","Possible Χειρόμηκτα membership and Marcianus 299 fol.154r are preserved."),
("4319","024"):("Περὶ σταθμοῦ ξανθώσεως","Berthelot–Ruelle 1888, pp. 181–183","561","This notice supplies neither a manuscript witness nor possible Χειρόμηκτα relation, so neither is inferred."),
("4319","025"):("Περὶ θείου ὕδατος","Berthelot–Ruelle 1888, pp. 184–186","534","Possible Χειρόμηκτα membership and Marcianus 299 fol.156r are preserved."),
("4319","026"):("Περὶ σκευασίας ὤχρας","Berthelot–Ruelle 1888, pp. 186–187","260","Possible Χειρόμηκτα membership and Marcianus 299 fol.157r are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
