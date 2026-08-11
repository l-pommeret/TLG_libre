import csv
O="data/research_batches/detailed_verified_3001_batch_417.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4015","022"):("Additamenta in De usu astrolabii","Jarry 2015, pp. 49–50","313","The additamenta remain a separate item from 4015.020 and the recension Φ scholia 4015.021."),
("4015","151"):("INCOMPLETE_CONTINUATION_NOTICE","Koster, pp. 151–164 (incomplete extracted continuation)","","The extracted notice begins mid-sentence, carries doubtful status and a cross-reference to Georgius Choeroboscus 4093.013; no missing title or antecedent is inferred."),
("4016","001"):("In Porphyrii isagogen sive quinque voces","Busse, CAG 4.3 (1891), pp. 1–128","33650","A First1KGreek candidate exists, but exact Busse edition and license verification is not established locally."),
("4016","002"):("In Aristotelis categorias commentarius","Busse, CAG 4.4 (1895), pp. 1–106","28007","A First1KGreek candidate exists, but exact Busse edition and license verification is not established locally."),
("4016","003"):("In Aristotelis librum de interpretatione commentarius","Busse, CAG 4.5 (1897), pp. 1–272","94510","A First1KGreek candidate exists, but exact Busse edition and license verification is not established locally."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k]; count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT' if wc else 'INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.' if wc else 'Recover the preceding printed-canon context before any text identification.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
