import csv

O="data/research_batches/detailed_verified_3001_batch_329.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3129","005"):("Λόγος εἰς τὸν αὐτοκράτορα κῦριν Ἀλέξιον τὸν Κομνηνόν","Gautier 1980 pp. 215–243","3466","The trailing Theophylactus Simocatta text is a catalogue heading artefact, not part of this oration."),
("3129","006"):("Προσλαλιά περὶ ὧν ἐγκαλοῦνται Λατῖνοι","Gautier 1980 pp. 247–285","5227","The exact interlocutory address concerning accusations against Latins was checked."),
("3129","007"):("Λόγος περὶ εὐνουχισμοῦ","Gautier 1980 pp. 289–331","5382","The iambic preface, prose preface, and apology subdivisions remain within this single catalogue item."),
("3129","008"):("Πρὸς Δημήτριον περὶ τῆς λειτουργίας","Gautier 1980 pp. 335–343","1239","The addressee Demetrius and liturgical subject define the exact epistle."),
("3129","009"):("Poemata","Gautier 1980 pp. 347–377","2236","The poetry collection is distinct from the preceding prose orations and epistles."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
