import csv
O="data/research_batches/detailed_verified_3001_batch_458.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4135","030"):("Adversus criminationes in Christianos Iuliani imperatoris","Guida 1994, even pp. 70–100","2981","The even-page restriction and cross-reference to Julian 2003.017 are preserved.",False),
("4135","031"):("Fragmenta in Genesim","Petit article notice truncated after journal title Muséon","","The extracted bibliographic notice stops before volume/year/pages; the following 4135.100 is a separate continuation record, so missing data are not joined or inferred.",True),
("4135","100"):("INCOMPLETE_CONTINUATION_NOTICE","(1987), pp. 274–280","639","This notice begins with the continuation of a parenthetical year and has no recoverable standalone title; its relation to adjacent 4135.031 is recorded but not used to synthesize a canon notice.",True),
("4139","001"):("De fide et lege naturae [Sp.] (CPG 4185)","MPG 48, cols. 1081–1088","3881","Spurious status is preserved. PTA manuscript/text candidates do not establish exact licensed MPG verification.",False),
("4139","002"):("De Christo pastore et ove [Sp.] (CPG 4189)","MPG 52, cols. 827–835","4501","Spurious status is preserved. The PTA candidate is not treated as exact licensed MPG verification.",False),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note,incomplete) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium' if incomplete else 'high',proposed_status='INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT' if incomplete else 'NO_EXACT_OPEN_TEXT',next_action='Recover the complete printed-canon notice before any text identification.' if incomplete else f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
