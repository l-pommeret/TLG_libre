import csv

O="data/research_batches/detailed_verified_3001_batch_397.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3334","004"):("Oratio antirrhetica","Darrouzès 1966 pp. 250–264","2293","The antirrhetic discourse remains a separate item."),
("3334","005"):("De matrimoniis [Dub.]","Darrouzès 1966 pp. 268–275","2549","The doubtful attribution and possible authorship by Demetrius of Cyzicus are preserved without resolution."),
("3335","001"):("Oratio de suffragiis","Darrouzès 1966 pp. 160–174","2487","The Nicetas Amasenus suffrage discourse remains distinct from the Ancyranus items."),
("3336","001"):("Laudatio Theodori Grapti (BHG 1745z)","Featherstone, Analecta Bollandiana 98 (1980), pp. 104–150","12863","BHG 1745z is preserved; Theodorus Graptus 3124 remains a contextual cross-reference."),
("3337","001"):("Encomium in dormitionem Deiparae","Jugie, PO 16.3 (1922), pp. 457–462","1584","The Dormition of the Theotokos defines this exact encomium."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
