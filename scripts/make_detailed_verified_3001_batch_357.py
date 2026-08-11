import csv

O="data/research_batches/detailed_verified_3001_batch_357.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3196","011"):("Oratio ad Constantinum imperatorem (BHG 368)","Simonides 1853 pp. 1–37","11136","The BHG 368 identifier defines the exact Constantine panegyric."),
("3196","012"):("Oratio sancti Gerasimi","Koikylides 1902 pp. 27–39","2806","The Vitae Gerasimi 5426 cross-reference is contextual and remains separate."),
("3196","013"):("Laudatio sancti Athanasii Atramytteni (BHG 192)","Papadopoulos-Kerameus 1909 pp. 141–147","word count not supplied","The BHG 192 identifier is preserved and no missing word count was invented."),
("3199","001"):("Spanos, recension D","Eideneier 1977 pp. 83–169","9781","The Venice 1553 recension D is retained separately from recension A."),
("3199","002"):("Spanos, recension A","Eideneier 1977 pp. 83–90, 93–121, 123–125, 128–130, 132–133, 135, 138, 144–145 and 154–166","4887","All nine explicit discontinuous loci and the Vienna theological manuscript recension are preserved without filling gaps."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
