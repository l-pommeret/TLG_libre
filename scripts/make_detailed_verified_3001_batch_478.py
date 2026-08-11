import csv
O="data/research_batches/detailed_verified_3001_batch_478.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4158","008"):("Vita Tzetziana 2","Koster 1975, pp. 144–145","173","The second Tzetzian Life remains separate from Vita Tzetziana 1 despite sharing page 144."),
("4158","009"):("Vita Thomana 1","Koster 1975, pp. 146–147","198","The first Thomas Life remains separate from the second."),
("4158","010"):("Vita Thomana 2","Koster 1975, p. 149","141","The second Thomas Life remains a separate single-page item."),
("4161","001"):("Excerptum praefationis in phaenomena (= Anonymus II.3)","Martin 1974, pp. 1–4","217","The Anonymus II.3 equivalence and preface-excerpt status are preserved."),
("4161","002"):("Vita Arati (= Vita 1)","Martin 1974, pp. 6–10","859","Former attribution to Achilles Tatius and Vaticanus graecus 191 witness are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
