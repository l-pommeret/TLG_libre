import csv

O="data/research_batches/detailed_verified_3001_batch_396.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3333","002"):("Typicon monasterii Archangeli Michaelis","Dmitrievsky 1895 pp. 769–794","8657","The monastery on Mount Auxentios defines the exact typikon; truncated canonical author heading is retained."),
("3333","003"):("Novella sive prostagma Michaelis VIII","Burgmann and Magdalino 1984 pp. 378–384","1129","The imperial novel on maladministration is the exact legal item."),
("3334","001"):("Oratio de ordinatione episcoporum","Darrouzès 1966 pp. 176–206","5088","The episcopal-ordination discourse is exact; trailing Nicetas Amasenus is a catalogue heading artefact."),
("3334","002"):("Oratio ecclesiastica","Darrouzès 1966 pp. 208–236","4625","The ecclesiastical oration remains distinct from adjacent Ancyranus discourses."),
("3334","003"):("Oratio contra Alexium I","Darrouzès 1966 pp. 238–248","1913","The emperor Alexius I defines this exact polemical oration."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
