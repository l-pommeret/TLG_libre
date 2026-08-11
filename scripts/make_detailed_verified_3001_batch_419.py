import csv
O="data/research_batches/detailed_verified_3001_batch_419.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4017","004"):("Commentarium in Hermogenis librum περὶ στάσεων","Rabe, Syriani in Hermogenem commentaria 2 (1893), pp. 1–203","38590","The volume-2 commentary on περὶ στάσεων is checked independently from the volume-1 items."),
("4019","001"):("Prolegomena","Busse, CAG 12.1 (1902), pp. 1–25","9891","The prolegomena remain separate from the Categories commentary beginning on page 26; the First1KGreek candidate is not exact licensed verification."),
("4019","002"):("In Aristotelis categorias commentarium","Busse, CAG 12.1 (1902), pp. 26–148","49566","The Categories commentary remains separate from the preceding prolegomena; the First1KGreek candidate is not exact licensed verification."),
("4019","003"):("In Aristotelis meteora commentaria","Stuve, CAG 12.2 (1900), pp. 1–338","111168","A First1KGreek candidate exists, but exact Stuve edition and license verification is not established locally."),
("4019","004"):("In Platonis Alcibiadem commentarii","Westerink 1956 (repr. 1982), pp. 1–144","50014","The first-Alcibiades commentary is checked as the exact Westerink item and not conflated with the Aristotelian commentaries."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
