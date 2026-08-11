import csv
O="data/research_batches/detailed_verified_3001_batch_504.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4319","067"):("Ποίημα τοῦ Ζωσίμου (πρᾶξις γʹ)","Mertens, pp. 46–47","183","high","Both manuscript loci and the full-duplicate link to 4319.005 are preserved."),
("4319","068"):("Ζώσιμος λέγει περὶ τῆς ἀσβέστου","Mertens, pp. 48–49","305","high","All three manuscript loci, including Paris BnF gr.2327 fol.8r, are preserved."),
("4321","001"):("Rhetorii quaestiones astrologicae ex Antiochi thesauris excerptae","Boll, CCAG 1 (1898), pp. 142–164","6,218","high","The Laurentianus 28.34 base witness and the notice's additional unspecified codices are preserved."),
("4321","005"):("De planetarum natura ac vi","Boll, CCAG 7 (1908), pp. 214–226","3,379","high","The Berlin 173 manuscript witness is preserved."),
("4321","006"):("Excerpta (ex Rhetorii Thesauris)","Cumont, CCAG 8.1 (1929), pp. 221–248","7,296","high","The Paris gr.2506 witness and attribution to the Thesauri are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,conf,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, relevant manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence=conf,proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
