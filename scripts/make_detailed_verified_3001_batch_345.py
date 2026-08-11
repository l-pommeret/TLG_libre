import csv

O="data/research_batches/detailed_verified_3001_batch_345.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3181","001"):("De velitatione bellica","Dagron and Mihaescu 1986 pp. 29–135","15657","The attribution under Nicephorus II and cross-reference to Anonymous Tactica 3234.002 are preserved; trailing Niceratus is a heading artefact."),
("3181","002"):("Novellae","Hase, CSHB (1828), pp. 309–323","word count not supplied","The legal novellae remain distinct from the tactical works 3181.001 and .003."),
("3181","003"):("Στρατηγικὴ Ἔκθεσις καὶ Σύνταξις","McGeer 1995 pp. 12–58","7149","The exact strategic exposition is distinct from De velitatione bellica."),
("3182","001"):("Chronographia e cod. Paris. gr. 1712","Bekker, CSHB (1838), pp. 603–760","30498","The catalogue specifies partial publication from Paris gr. 1712; that witness scope is preserved."),
("3186","001"):("Anonymus dialogus cum Judaeis","Declerck, CCSG 30 (1994), pp. 3–111","27958","The former attribution to John Damascene and anonymous status are both preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
