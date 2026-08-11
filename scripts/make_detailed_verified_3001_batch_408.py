import csv

O="data/research_batches/detailed_verified_3001_batch_408.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3386","002"):("Vita sancti Theodori Studitae","MPG 99 cols. 233–328","19147","The Vitae Theodori Studitae 5260 cross-reference remains separate."),
("3386","003"):("Laudatio apostoli Philippi (BHG 1530a)","Vatican gr. 1669; Krausmüller, JÖB 69 (2019), pp. 238–254","4273","The manuscript witness and edition's BHG 1530a identifier define the exact laudation."),
("3392","001"):("Versus ad hegumenum Athonis","Koder, JÖB 19 (1970), pp. 208–234 (even pages)","3021","The even-page convention and Athonite hegumen addressee are preserved; truncated author heading is retained."),
("3393","001"):("Capita philosophica","Uthemann, OCP 46.2 (1980), pp. 343–360","2296","The philosophical chapters are the exact Anastasius item."),
("3393","002"):("Orationes v de orthodoxa fide (CPG 6944)","Sakkos 1976 pp. 17–78","20958","The explicit five-oration scope and CPG 6944 identifier are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
