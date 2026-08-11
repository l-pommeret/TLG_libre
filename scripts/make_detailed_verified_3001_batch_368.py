import csv

O="data/research_batches/detailed_verified_3001_batch_368.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3232","007"):("Homilia festalis in sanctum Demetrium","Balfour, Analecta Vlatadon 34 (1981), pp. 187–194","2581","The festal Demetrius homily remains separate from the earlier miracle discourse."),
("3232","008"):("Epistulae","Balfour, Analecta Vlatadon 34 (1981), pp. 84–184 and 199–246","43785","Both discontinuous epistolary loci are preserved without filling the gap."),
("3232","009"):("Laudationes quattuor","Balfour, Analecta Vlatadon 34 (1981), pp. 247–248","485","The explicit four-laudation scope is preserved as one short catalogue item."),
("3232","010"):("Expositio de divino templo","Hawkes-Teeples 2011 pp. 80–162 (even pages)","10636","The even-page printing convention and equivalence to MPG 155 cols. 697–749 are preserved."),
("3232","011"):("De sacra liturgia","Hawkes-Teeples 2011 pp. 166–264 (even pages)","12286","The even-page printing convention and equivalence to MPG 155 cols. 253–304 are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
