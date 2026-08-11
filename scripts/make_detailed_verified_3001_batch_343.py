import csv

O="data/research_batches/detailed_verified_3001_batch_343.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3161","003"):("Epitome vitae sancti Maximi (BHG 1236)","Epifanovic 1907 pp. 21–22","691","The BHG 1236 epitome remains a distinct short item."),
("3161","004"):("In vitam ac certamen (BHG 1234)","MPG 90 cols. 68–109","8118","The possible Michael Studites authorship is preserved as uncertainty, not resolved by inference."),
("3165","001"):("Libellus ad Theodosium imperatorem","MPG 91 cols. 1472–1480; Schwartz 1.1.5 pp. 7–10","word count not supplied","Joint authorship with Basil and the ACO 5000.003 cross-reference are preserved without merging the records."),
("3175","001"):("Notitiae episcopatuum","Darrouzès 1981 pp. 204–421","30761","The exact Constantinopolitan episcopal-notitia collection was checked."),
("3176","001"):("Chronicon sive Maius","Grecu 1966 pp. 150–448 and 456–590","88072","The discontinuous loci and partial attribution to Macarius Melissenus are both preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
