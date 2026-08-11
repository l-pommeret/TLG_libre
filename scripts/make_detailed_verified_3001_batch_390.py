import csv

O="data/research_batches/detailed_verified_3001_batch_390.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3296","001"):("Opus alphabeticum de eutaxia","Mai and Cozza-Luzi 1905 pp. 253–265","490","The alphabetic structure and eutaxia subject define this short theological item."),
("3298","001"):("Homiliae","Rossi Taibbi 1969 pp. 1–244","67232","The annual Sunday-gospel and feast homily collection is the exact Philagathus item."),
("3299","001"):("Chronica de imperatoribus Comnenis","Lampsides 1958 pp. 61–81","5999","The Grand Komnenoi chronicle is exact; trailing Pancharious text is a catalogue heading artefact."),
("3303","001"):("Epistulae","Legrand 1892 pp. 351–358","2062","All five named letters and loci are preserved: 351–352, 353–354, 355, 355, and 356–358."),
("3303","002"):("Epigramma ad Hieronymum Castellum","Legrand 1892 p. 359","57","The single-page epigram to Hieronymus Castellus remains separate from the letters."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
