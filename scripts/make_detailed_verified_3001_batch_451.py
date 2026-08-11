import csv
O="data/research_batches/detailed_verified_3001_batch_451.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","034"):("Ad eos qui... vitam monasticam degunt","MPG 83, cols. 1416–1433","3512","The first extract from epistle 151 remains separate from 4089.035 despite their shared boundary column."),
("4089","035"):("Quod unicus filius sit dominus noster Jesus Christus","MPG 83, cols. 1433–1440","1520","The second extract from epistle 151 remains separate; the embedded THEODORIDAS heading before the locus is recorded as an extraction artefact."),
("4089","036"):("Pentalogus (fragmenta Graeca)","MPG 84, cols. 65–88","","The five books against Cyril and the Council of Ephesus are represented only by Greek fragments; no absent word count is inferred."),
("4089","037"):("Contra Judaeos (fragmentum) [Sp.]","Brok, RHE 45 (1950), pp. 490–494","","The spurious 'so-called fragment' status is preserved and no absent word count is inferred."),
("4089","040"):("Pro Diodoro et Theodoro (fragmenta in actis conciliorum)","Schwartz–Straub, ACO 4.1 (1971), pp. 94–95","","The conciliar-act fragments remain an exact item. The notice ends with bare 'Q' and supplies no count or genre, so none is inferred."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG/ACO, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
