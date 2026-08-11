import csv
O="data/research_batches/detailed_verified_3001_batch_481.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4161","013"):("Prooemium in Arati phaenomena","Maass 1898, pp. 102–104, every even isolated page 106–124, and 124–133","3229","Every discontinuous page locus is preserved explicitly; no continuous range is substituted."),
("4161","014"):("Sphaera","Maass 1898, pp. 154–170","1070","Former attribution to Empedocles is preserved."),
("4163","001"):("Telegonia (fragmentum)","Bernabé 1987, p. 103, fragment 1","9","The nine-word first fragment is the complete exact item."),
("4166","001"):("Vitae Aeschinis","Dindorf 1852, all explicit loci pp. 1–6 and 166–512","1124","All discontinuous loci, Apollonius/anonymous subdivisions and duplicate link of the Apollonius Life to 1167.001 are preserved."),
("4170","001"):("Vitae Pindari et varia de Pindaro","Drachmann 1903 (repr. 1969), pp. 1–11","1480","The 1969 reprint is preserved; the author heading ending 'PIN-' is retained as an extraction truncation rather than expanded."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
