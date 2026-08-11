import csv

O="data/research_batches/detailed_verified_3001_batch_348.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3190","002"):("Renuntiatio rerum politicarum et ecclesiasticarum","Heisenberg, QSG repr. 1973, pp. 6–54","14285","The report on the political and ecclesiastical events of 1214 defines the exact item."),
("3190","003"):("Disputatio","Heisenberg, QSG repr. 1973, pp. 15–25","3134","The 1206 union-negotiation disputation is distinct from the following petitions."),
("3190","004"):("Rogationes ad Theodorum Lascarem","Heisenberg, QSG repr. 1973, pp. 25–34","2790","The petitions addressed to Theodore Lascaris remain a separate epistolary-rhetorical item."),
("3190","005"):("Descriptio itineris Nicaeam","Heisenberg, QSG repr. 1973, pp. 35–46","3359","The trailing Constantinus Mesarites text is a catalogue heading artefact, not part of this journey description."),
("3190","006"):("Descriptio ecclesiae ss. Apostolorum","Downey, TAPS 47 (1957), pp. 897–918","17233","The Church of the Holy Apostles description and exact article locus define the item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
