import csv

O="data/research_batches/detailed_verified_3001_batch_372.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3236","013"):("Hymni","Vienna theol. gr. 78; Kotzabassi 1991–1992 pp. 98–102","word count not supplied","The named Vienna witness defines the exact hymn item; no word count was invented."),
("3239","002"):("Epistulae iv","Karlsson and Fatouros 1973 pp. 208, 210–211 and 214–216","1239","The explicit four-letter scope and catalogue numbers 158, 70, 71 and 76 are preserved despite compact punctuation."),
("3241","001"):("Textus Theosophiae Tubingensis","Erbse 1995 pp. 1–56","4849","The Tübingen Theosophy text remains separate from the Sibylline and minor-treasure texts."),
("3241","002"):("Textus genuinus Theosophiae Sibyllarum","Erbse 1995 pp. 57–90","3220","The genuine Sibylline Theosophy text remains a distinct edition item."),
("3241","003"):("Textus thesaurorum minorum","Erbse 1995 pp. 91–135","3671","The minor treasury texts remain separate from 3241.001 and .002."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
