import csv

O="data/research_batches/detailed_verified_3001_batch_358.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3199","003"):("Spanos, recension B","Eideneier 1977 pp. 105–116 and 155–167","2148","Both discontinuous loci and Vatican gr. 1139 witness define recension B, separate from A and D."),
("3200","001"):("Epistulae","Dennis, CFHB 8 (1977), pp. 3–217","27948","The Manuel II letter collection and exact edition locus define this item."),
("3200","002"):("Dialogi cum mahometano","Trapp 1966 pp. 3–302","137231","The dialogues with the Persian Muslim interlocutor are the exact theological item."),
("3200","003"):("Epitaphius in fratrem Theodorum, recension 1","Chrysostomides, CFHB 26 (1985), pp. 75–259","25763","Recension 1 is preserved separately from the shorter recension 2 in 3200.004."),
("3200","004"):("Epitaphium in Theodorum, recension 2","Chrysostomides, CFHB 26 (1985), pp. 261–285","8987","The shorter recension 2 remains separate; trailing Mattheus Palaeologus Asanes is a catalogue heading artefact."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
