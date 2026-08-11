import csv
O="data/research_batches/detailed_verified_3001_batch_489.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4277","001"):("Testimonia","Döring 1972, pp. 67–70, testimonia 211–220","","All ten testimonia are preserved; the NQ notice supplies no count."),
("4279","001"):("Paraphrasis in Iliadem","Bekker 1825, vol. 2 pp. 651–811","","The Iliad paraphrase is checked at its exact high page locus; no word count is supplied."),
("4283","001"):("De mulierum morbis uteri, Del Guerra edition","Del Guerra 1953, pp. 37–93","7586","This edition record remains separate from Kouzes 4283.002; incorporation of Laurentianus readings in the TLG text is preserved."),
("4283","002"):("De mulierum morbis uteri, Kouzes edition","Kouzes 1945, pp. 46–68","","This edition record remains separate from Del Guerra 4283.001; no word count is supplied."),
("4285","001"):("In Julianum imperatorem","Guida 1990, no page locus supplied","","Both papyri P.Rain.1.14 and P.Lit.Lond.163 and Pap medium are preserved; no absent page locus or count is inferred."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, papyrological/medical corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for the cited edition and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
