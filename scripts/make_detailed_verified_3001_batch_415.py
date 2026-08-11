import csv
O="data/research_batches/detailed_verified_3001_batch_415.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4015","012"):("De vocabulis quae diversum significatum exhibent secundum differentiam accentus","Daly 1983, pp. 3–53, 55–139, 141–195, 197–238","12421","All four discontinuous page spans and the canon cross-reference to 4015.018 are preserved."),
("4015","013"):("Περὶ Αἰολίδος (pars operis De dialectis)","Hoffmann, Die griechischen Dialekte 2 (1893), pp. 206–208 and 213–222","1380","The Aeolic fragment remains explicitly a part of De dialectis, with both discontinuous loci preserved."),
("4015","014"):("In Nicomachi arithmeticam introductionem (lib. 1)","Giardina 1999, pp. 105–181","32252","Book 1 is preserved as a separate canon item from book 2."),
("4015","015"):("In Nicomachi arithmeticam introductionem (lib. 2)","Giardina 1999, pp. 183–241","24370","Book 2 remains separate; the embedded PHILOSOPHICA ANONYMA heading artefact is not interpreted as part of the title or locus."),
("4015","016"):("Praecepta tonica","Xenis, Teubner 2015, pp. 1–176","10930","The canon cross-reference to Aelius Herodianus and Pseudo-Herodianus 0087.001 is preserved without merging records."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
