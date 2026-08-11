import csv

O="data/research_batches/detailed_verified_3001_batch_369.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3232","012"):("Benedictiones","Phountoules 1968 pp. 3–72","18130","The notice prints 18,130 without the usual Cod label; the extraction anomaly is recorded without inventing other metadata."),
("3232","013"):("Hymni","Phountoules 1968 pp. 75–118, 119–122, 129–137, 139–142, 143–261 and 263–266","36959","All six named hymn-section loci are preserved; trailing Symeon Messalianus/cross-reference text is a new heading."),
("3233","001"):("Opsarologos","Winterwerb 1992 pp. 252–253","433","The fish-themed parody is distinct from the Poricologos redactions."),
("3236","001"):("Historia ecclesiastica","MPG 145 cols. 560–1332; 146 cols. 9–1273; 147 cols. 9–448","460075","All three explicit MPG volume loci define the exact large ecclesiastical history."),
("3236","002"):("Carmen iambicum de excidio Hierosolymitano","MPG 147 cols. 601–606","887","The short iambic poem on Jerusalem's fall remains distinct from the ecclesiastical history."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
