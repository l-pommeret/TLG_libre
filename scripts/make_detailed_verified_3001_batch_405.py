import csv

O="data/research_batches/detailed_verified_3001_batch_405.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3366","001"):("Chrysobullum","Alexander, Byzantion 15 (1940–1941), pp. 177–183","1446","The grant for the see of Kanina is exact; the truncated canonical author heading is retained."),
("3367","001"):("Vita sancti Benedicti","Rigotti 2001 pp. 1–113","17264","The Greek translation by Pope Zacharias under Gregory the Great's name is preserved as the exact attribution history."),
("3371","001"):("De monacho superbo (BHG 1450x)","Wortley, Analecta Bollandiana 100 (1982), pp. 357–363","960","The BHG 1450x identifier from the edition defines this exact narrative."),
("3371","002"):("Didascalia Iacobi (BHG 1322m)","Déroche 1991 p. 71 and pp. 75–219 (odd pages)","27822","The isolated p. 71, discontinuity, odd-page convention and BHG 1322m are all preserved."),
("3373","001"):("Orationes in Georgium Xiphilinum (1192)","Loukaki 2005 pp. 73–135","12674","The dated Tornices orations remain distinct from Phrangopulus 3365.001."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
