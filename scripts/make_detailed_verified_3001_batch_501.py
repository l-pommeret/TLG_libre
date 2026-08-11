import csv
O="data/research_batches/detailed_verified_3001_batch_501.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","052"):("Ἑρμηνεία περὶ πάντων... καὶ περὶ τῶν φώτων","Berthelot–Ruelle 1888, pp. 247–248","302","Paris BnF gr.2327 fol.264r and the expanded interpretation title are preserved."),
("4319","053"):("Excerptum de cerussa (sine titulo)","Berthelot–Ruelle 1888, p. 248","72","Untitled status and Paris BnF gr.2327 fol.265 are preserved; the item remains separate from 4319.052 sharing page 248."),
("4319","054"):("Περὶ λευκώσεως","Berthelot–Ruelle 1888, p. 249","121","Paris BnF gr.2327 fol.265 is preserved; the item remains separate from 4319.055 sharing page 249."),
("4319","055"):("Ἑρμηνεία περὶ τῶν φώτων","Berthelot–Ruelle 1888, pp. 249–250","153","Paris BnF gr.2327 fol.265v and the shorter interpretation title distinguish it from 4319.052."),
("4319","056"):("Περὶ αἰθαλῶν","Berthelot–Ruelle 1888, pp. 250–252","480","Marcianus 299 fol.116v is preserved; the item remains separate despite sharing page 250 with 4319.055."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
