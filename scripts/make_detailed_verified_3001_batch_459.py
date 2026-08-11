import csv
O="data/research_batches/detailed_verified_3001_batch_459.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4139","003"):("In illud Dominus regnavit... [Sp.] (CPG 4190)","MPG 55, cols. 603–612","5420","Both scriptural incipits and the baptismal-mystery clause are preserved; the PTA candidate is not exact licensed MPG verification."),
("4139","004"):("Quomodo animam acceperit Adamus [Dub.] (CPG 4195)","Savile 1611, vol. 5 pp. 648–653","2707","Doubtful attribution and publication under Chrysostom are preserved; PTA witnesses do not resolve authorship or exact edition/license."),
("4139","005"):("In Genesim sermo II [Sp.] (CPG 4197)","MPG 56, cols. 522–526","1837","Spurious status is preserved; the PTA candidate is not exact licensed MPG verification."),
("4139","006"):("In filium prodigum [Sp.] (CPG 4200)","MPG 59, cols. 627–636","4561","Spurious status is preserved; the PTA candidate is not exact licensed MPG verification."),
("4139","007"):("Homilia de legislatore [Dub.]","MPG 56, cols. 397–410","5209","Doubtful status and the embedded SEVERIANUS heading before the locus are preserved as an extraction artefact; PTA witnesses do not resolve it."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, PTA, First1KGreek, OPP and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
