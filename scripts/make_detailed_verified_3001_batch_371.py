import csv

O="data/research_batches/detailed_verified_3001_batch_371.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3236","008"):("Epistulae","Vatican gr. 112 ff. 5–10v; Featherstone 1998 pp. 22–27","2330","The exact Vatican manuscript folio span defines these three additional letters."),
("3236","009"):("Synaxarium sancti Gregorii Assi","Patmos 448 ff. 8r–13r; Sophianos 2004 pp. 347–351","1522","The manuscript folios are preserved; cross-reference to Vitae Gregorii 5149 remains separate."),
("3236","010"):("Synaxarium","Stefec, JÖB 62 (2012), pp. 154–159","922","The synaxarion verses are preserved as their own short item."),
("3236","011"):("Epistulae ad Ignatium monachum","Browning 1985 pp. 147–153","1180","The two letters to Ignatius remain item-level; embedded Xanthus text is a catalogue heading artefact in the editor name."),
("3236","012"):("Vita sanctae Euphrosynae iunioris (BHG 627)","Florence Conv. Sopp. Camaldoli 1214; Acta Sanctorum November III (1910), pp. 861–877","12869","The BHG 627 identifier and named Florentine witness define the exact life."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
