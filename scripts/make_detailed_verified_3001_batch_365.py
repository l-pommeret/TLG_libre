import csv

O="data/research_batches/detailed_verified_3001_batch_365.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3219","001"):("Liber medicus","Ieraci Bio 1996 pp. 45–231","31618","The Paul of Nicaea medical manual is the exact item."),
("3220","001"):("Vita Stephani Iunioris","Auzépy 1997 pp. 87–177","22545","The life of Stephen the Younger by Stephen the Deacon is the exact hagiographic item."),
("3222","001"):("Epistulae XII","Loenertz 1956 pp. 130–162","8619","The explicit twelve-letter scope is preserved exactly."),
("3223","001"):("Epistulae","Darrouzès 1970 pp. 190–201 and 336–353","4878","Both discontinuous loci are preserved; embedded Georgius Tornices text is a catalogue heading artefact."),
("3225","001"):("Epistulae ad Joannem VI Cantacuzenum","Voordeckers and Tinnefeld 1987 pp. 190 and 213","word count not supplied","The two separate page loci and cross-reference to Cantacuzenus 3169.003 are preserved without merging records."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
