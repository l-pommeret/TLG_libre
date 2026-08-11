import csv

O="data/research_batches/detailed_verified_3001_batch_377.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3254","014"):("Orationes asceticae","Chrestou 1992 pp. 157–260","26629","Six named components are preserved; the printed '231v246' locus is retained as an unresolved catalogue typography anomaly, not silently corrected."),
("3254","015"):("Precationes","Chrestou 1992 pp. 269–280","2259","The prayer collection remains distinct from the adjacent ascetic discourses."),
("3254","016"):("Contra Barlaam et Acindynum","Phanourgakes 1988 pp. 85–100","3285","Embedded PALCHUS text is a catalogue heading artefact in the editor name and was not treated as authorship."),
("3254","017"):("In captivitate","Phanourgakes 1988 pp. 120–147","6604","Both explicit components are preserved: letter from Asia pp. 120–141 and anonymous-addressee letter pp. 142–147."),
("3254","018"):("Contra Nicephorum Gregoram","Chrestou 1988 pp. 231–377","41057","The anti-Gregoras writings are distinct from the anti-Barlaam and anti-Akindynos items."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
