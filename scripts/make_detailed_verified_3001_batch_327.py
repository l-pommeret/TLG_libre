import csv

O="data/research_batches/detailed_verified_3001_batch_327.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3120","004"):("De sepulcris imperatorum","Bekker 1843 pp. 203–208","749","This imperial-tombs excerpt remains distinct from the other Constantinopolitan Patria items."),
("3122","001"):("Oratio contra eos qui azyma offerunt","Darrouzès, REB 32 (1974), pp. 207–210","846","The excerpt from Bucharest Academy manuscript 318 defines the exact item."),
("3125","001"):("De Creta capta","Criscuolo 1979 pp. 1–39","6046","The historical poem and its exact Teubner locus were checked item by item."),
("3127","001"):("Scholia mythologica","Nimmo Smith, CCSG 27 (1992), pp. 67–272","20240","The Pseudo-Nonnus scholia on four orations of Gregory of Nazianzus were checked as the exact commentary."),
("3128","001"):("Canones sive De orthographia","Cramer, Anecdota Graeca 2 (1835), pp. 1–165","45209","This Cramer text remains distinct from the Schneider additamenta catalogued as 3128.002."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
