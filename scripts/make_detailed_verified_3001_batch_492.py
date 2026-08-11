import csv
O="data/research_batches/detailed_verified_3001_batch_492.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","007"):("Περὶ τῆς ἐξατμίσεως ὕδατος θείου","Berthelot–Ruelle 1888, pp. 138–140","619","Marcianus 299 fol.112r and partial duplicate links to 4319.062–063 are preserved."),
("4319","008"):("Περὶ τοῦ θείου ὕδατος, fol.113v","Berthelot–Ruelle 1888, pp. 141–143","680","Marcianus 299 fol.113v and duplicate 4319.064 are preserved."),
("4319","009"):("Περὶ τοῦ θείου ὕδατος, fol.188r","Berthelot–Ruelle 1888, pp. 143–144","111","The equivalent expanded title, Marcianus 299 fol.188r and duplicate 4319.060 are preserved separately from 4319.008."),
("4319","010"):("Παραινέσεις συστατικαί","Berthelot–Ruelle 1888, pp. 144–145","284","Marcianus 299 fol.115r and the exhortatory item are preserved without assigning a duplicate."),
("4319","011"):("Γνησία γραφὴ περὶ τῆς ἱερᾶς καὶ θείας τέχνης","Berthelot–Ruelle 1888, pp. 145–148","568","The complete long title and Paris BnF gr.2327 fol.112r witness are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
