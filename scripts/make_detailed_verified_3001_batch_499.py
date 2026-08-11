import csv
O="data/research_batches/detailed_verified_3001_batch_499.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","042"):("Βίβλος ἀληθὴς Σοφὲ Αἰγυπτίου...","Berthelot–Ruelle 1888, pp. 213–214","353","The shorter title and Paris BnF gr.2327 fol.260r keep this record separate from 4319.041."),
("4319","043"):("Ζωσίμου πρὸς Θεόδωρον κεφάλαια","Berthelot–Ruelle 1888, pp. 215–218","877","Marcianus 299 fol.179r and the addressee Theodore are preserved."),
("4319","044"):("Excerptum de partibus alchimiae (sine titulo)","Berthelot–Ruelle 1888, pp. 219–220","326","Untitled status and both witnesses—Paris BnF gr.2327 fol.238v and Marcianus 299 fol.181r—are preserved."),
("4319","045"):("Ὑδραργύρου ποίησις","Berthelot–Ruelle 1888, pp. 220–222","427","Marcianus 299 fol.107r is preserved; the item remains separate despite shared page 220 with 4319.044."),
("4319","046"):("Περὶ διαφορᾶς χαλκοῦ κεκαυμένου","Berthelot–Ruelle 1888, pp. 222–223","266","Paris BnF gr.2327 fol.249v and cross-reference to 4319.013 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
