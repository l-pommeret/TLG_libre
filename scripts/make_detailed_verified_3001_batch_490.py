import csv
O="data/research_batches/detailed_verified_3001_batch_490.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4291","001"):("Verba in scripturis de Christi natale, epiphaniis et pentecoste","de Stefani, BZ 16 (1907), pp. 58–66","797","Possible authorship by a monk Theodosius and all three witnesses Coislin.345, Barocc.50 and Laur.57.26 are preserved; trailing VERSUS ALPHABETICI is a heading artefact."),
("4309","001"):("Tractatus philosophicus (sine titulo)","Roueché, JÖB 23 (1974), pp. 72–73","","Untitled status and Laurentianus Plut.IX.8 witness are preserved; no count is supplied."),
("4314","001"):("Paraphrasis institutionum","Lokin et al. 2010, even pp. 2–954","114534","The even-page restriction across the full legal paraphrase is preserved."),
("4318","001"):("Vita Sophoclis","Radt, TrGF 4 (1977), pp. 29–40","948","The Life of Sophocles is checked as the exact Radt item."),
("4319","001"):("Περὶ ὀργάνων καὶ καμίνων...","Mertens 1995, vol. 4.1 pp. 1–10","1529","Venetianus Marcianus 299 fol.189r and partial duplicate link to 4319.049 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, manuscript/alchemical corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
