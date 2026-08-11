import csv

O="data/research_batches/detailed_verified_3001_batch_383.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3274","002"):("Responsio Graecorum de igne purgatorio","Petit, PO 15.1 (1920), pp. 61–79","5301","The response recited by Bessarion and Bessarion 3229 cross-reference are preserved."),
("3274","003"):("Latinorum responsio circa purgatorium ignem","Petit, PO 15.1 (1920), pp. 80–107","8426","The Latin response is distinct from the preceding Greek response."),
("3274","004"):("Acta Graecorum concilii Florentini Pars I","Gill 1953 pp. 1–228","52581","Part I remains separate from Part II and its distinct page locus."),
("3274","005"):("Acta Graecorum concilii Florentini Pars II","Gill 1953 pp. 241–472","55656","Part II remains separate from Part I; the page gap is preserved."),
("3274","012"):("catalogue continuation fragment","– 013)","word count not supplied","INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT","This artificial work key contains only the end of the Marcus Eugenicus cross-reference begun in 3274.001; no independent work, title, or edition was inferred."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,status,note) in {k:(*v[:3],'NO_EXACT_OPEN_TEXT',v[3]) if len(v)==4 else v for k,v in D.items()}.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; catalogue locus {locus} and marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at the stated locus was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status=status,next_action=('Recover and verify the complete catalogue cross-reference before treating this artificial key as an independent work.' if status.startswith('INCOMPLETE') else f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.'),notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
