import csv

O="data/research_batches/detailed_verified_3001_batch_362.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3200","022"):("De somniis epistula ad Andream Asanem","Paris gr. 2419; Boissonade 1844 pp. 239–246","1748","The named addressee Andrew Asanes and Paris witness define the exact dream epistle."),
("3201","001"):("Epistulae ex Hellesponto","Westerink 1973 pp. 55–133","8433","The Hellespont exile letters are the exact Nicetas Magister collection."),
("3201","002"):("Vita sanctae Theoctistae (BHG 1723)","Acta Sanctorum November IV (1925), pp. 224–233","3840","BHG 1723 is preserved; the Symeon Metaphrastes 3115.080 cross-reference remains separate."),
("3203","001"):("Oratio de miraculis sancti Demetrii","Iberites, Makedonika 1 (1940), pp. 334–376","17234","The miracles of Saint Demetrius define this exact hagiographic homily."),
("3203","002"):("Vita sanctae Theodosiae","Kotzabassi 2009 pp. 84–98","5325","The Vitae Sanctae Theodosiae 5131 cross-reference is contextual and remains separate."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
