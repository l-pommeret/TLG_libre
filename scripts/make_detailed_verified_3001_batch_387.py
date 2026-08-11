import csv

O="data/research_batches/detailed_verified_3001_batch_387.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D=[
("3294","001","Fragmenta","Thesleff 1965 pp. 116–121","1428","These philosophical fragments share a duplicated canonical key with Dogmatic History book I; both records are retained explicitly."),
("3294","002","Historiae dogmaticae liber II","Cozza-Luzi 1871 pp. 179–227","21309","Book II remains separate from books I and III; trailing METOPUS text is a catalogue heading artefact."),
("3294","003","Historiae dogmaticae liber III","Cozza-Luzi 1905 pp. 319–370","25669","Book III and its later volume locus remain separate from books I and II."),
("3294","004","Ref utatio trium capitum a Maximo Planude Monacho editorum, MPG 141: 1276–1305. Cod: 6,962: Theol","MPG 141 cols. 1276–1305","6962","The catalogue's split typography in Refutatio is preserved in the canonical field and noted without correction."),
("3294","005","Ref utatio eorum quae scripsit Manuel Cretensis (Moschopulus), MPG 141: 1308– 1405. Cod: 21,793: Theol","MPG 141 cols. 1308–1405","21793","This anti-Moschopulus refutation remains separate from the anti-Planudes refutation; split typography is preserved."),
]
C=list(csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8')))
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for aid,wid,title,locus,wc,note in D:
  s=next(r for r in C if r['tlg_author_id']==aid and r['tlg_work_id']==wid and r['work_title']==title);r={f:'' for f in F};r.update(tlg_author_id=aid,tlg_work_id=wid,author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of the item at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
