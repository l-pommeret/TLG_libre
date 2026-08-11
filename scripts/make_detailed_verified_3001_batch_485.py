import csv
O="data/research_batches/detailed_verified_3001_batch_485.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4239","001"):("Narrationes et ethopoeiae","Walz 1832 (repr. 1968), pp. 537–548","1960","Internal narrationes pp.537–539 and ethopoeiae pp.539–548 subdivisions are preserved."),
("4239","002"):("Narrationes vel διηγήματα","Amato 2002, pp. 3–8","500","The modern narrationes edition is explicitly Dup. 4239.001 and remains separate."),
("4239","003"):("Ethopoeiae","Amato 2002, pp. 11–29","1745","Explicit Dup. 4239.001 and cross-reference to Sententiae Sexti 1666 are preserved; trailing SEXTUS Phil. is recorded as a heading artefact."),
("4243","001"):("De figuris [Sp.]","Spengel 1856 (repr. 1966), pp. 161–170","1888","Spurious status and reprint are preserved."),
("4246","001"):("Fragmenta grammatica","Montanari 1988, pp. 89–93, fragments 1–7","","The Pap medium and seven-fragment scope are preserved; no word count is supplied."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, papyrological/rhetorical corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
