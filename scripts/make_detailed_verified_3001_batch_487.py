import csv
O="data/research_batches/detailed_verified_3001_batch_487.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4263","001"):("Testimonia","Döring 1972, p. 46, testimonia 148a–148b","The explicit equivalence to Stilpo 4262.001 is preserved."),
("4264","001"):("Testimonium","Döring 1972, p. 46, testimonium 147","The explicit equivalence to Stilpo 4262.001 is preserved."),
("4265","001"):("Fragmentum","Döring 1972, pp. 52 and 61, fragment 164a","The fragment's explicit equivalence at p.52 to Stilpo 4262.001 is preserved; no word count is supplied."),
("4266","001"):("Testimonia","Döring 1972, pp. 50, 52 and 61, testimonia 153 and 164a","The explicit Stilpo 4262.001 equivalence for testimonium 164a is preserved."),
("4267","001"):("Testimonia","Döring 1972, pp. 52 and 61, testimonium 165","The equivalence to Stilpo 4262.001, partial duplicate Alcimus 0695.001 and cross-reference to Albinus/Alcinous 0693 are all preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, Megaric fragment/testimonia corpus, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' These NQ/Q notices supply no word count. No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
