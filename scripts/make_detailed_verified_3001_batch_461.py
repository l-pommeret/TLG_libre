import csv
O="data/research_batches/detailed_verified_3001_batch_461.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","013"):("In Chananaeam et in Pharaonem [Sp.] (CPG 4202)","MPG 59, cols. 653–664","6473","Spurious status and the overlap at cols. 663–664 with 4139.014 are preserved; the PTA candidate remains unverified."),
("4139","014"):("In dictum apostoli: Non quod volo facio [Sp.] (CPG 4203)","MPG 59, cols. 663–674","5872","Spurious status and the overlap at cols. 663–664 with 4139.013 are preserved; the PTA candidate remains unverified."),
("4139","015"):("In proditionem servatoris [Sp.] (CPG 4205)","MPG 59, cols. 713–720","2963","Spurious status is preserved; the PTA candidate is not exact licensed MPG verification."),
("4139","016"):("In illud: In principio erat verbum [Dub.] (CPG 4210)","MPG 63, cols. 543–550","2914","Doubtful status is preserved; numerous PTA witnesses and text identifiers do not resolve authorship or exact MPG edition/license."),
("4139","017"):("In dei apparitionem (CPG 4212)","MPG 65, cols. 16–25","1934","Multiple PTA witnesses/text variants are recorded as candidates only, without treating them as exact licensed MPG verification."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
