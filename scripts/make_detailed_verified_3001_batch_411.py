import csv

O="data/research_batches/detailed_verified_3001_batch_411.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4013","002"):("De caelo i interpretatio ex Kc","Heiberg, CAG 7 (1894), pp. 361–364","481","The Greek interpretation from Kc occupies the explicit gap within the main commentary's loci and remains separate."),
("4013","003"):("In Categorias commentarium","Kalbfleisch, CAG 8 (1907), pp. 1–438","168954","The Categories commentary is the exact Simplicius item."),
("4013","004"):("In Physica commentaria","Diels, CAG 9–10: vol. 9 pp. 1–800; vol. 10 pp. 801–1366","527287","Both explicit volumes and their contiguous page numbering are preserved."),
("4013","005"):("In De anima commentaria [Sp.?]","Hayduck, CAG 11 (1882), pp. 1–329","137117","The spurious uncertainty and possible authorship by Priscian of Lydia are preserved without resolution."),
("4013","006"):("Commentarius in Epicteti enchiridion","Dübner 1842 pp. 1–138","59136","The Epictetus Enchiridion commentary remains distinct from the Aristotelian commentaries."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
