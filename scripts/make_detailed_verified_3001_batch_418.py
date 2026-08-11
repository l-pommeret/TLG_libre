import csv
O="data/research_batches/detailed_verified_3001_batch_418.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4016","004"):("In Aristotelis analyticorum priorum librum i commentarium","Wallies, CAG 4.6 (1899), pp. 1–36","14106","A First1KGreek candidate exists, but exact Wallies edition and license verification is not established locally."),
("4016","005"):("In Aristotelis analytica priora [Sp.]","Wallies, CAG 4.6 (1899), pp. 37–76","19421","The spurious item is kept separate from 4016.004 despite occupying the following pages; its First1KGreek candidate remains unverified at edition/license level."),
("4017","001"):("In Aristotelis metaphysica commentaria","Kroll, CAG 6.1 (1902), pp. 1–195","75704","An Open Greek and Latin/OPP identifier candidate exists, but exact Kroll edition and license verification is not established locally."),
("4017","002"):("Commentarium in Hermogenis librum περὶ ἰδεῶν","Rabe, Syriani in Hermogenem commentaria 1 (1892), pp. 1–95","15845","The main commentary on περὶ ἰδεῶν remains separate from the following spurious preface."),
("4017","003"):("Praefatio in Hermogenis librum περὶ ἰδεῶν [Sp.]","Rabe, Syriani in Hermogenem commentaria 1 (1892), pp. 96–112","3117","Spurious status and possible partial authorship by Phoebammon are preserved without resolution."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
