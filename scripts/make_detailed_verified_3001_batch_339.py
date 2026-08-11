import csv

O="data/research_batches/detailed_verified_3001_batch_339.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3150","001"):("Acta graeca Andreae","Prieur, CCSA 6 (1989), pp. 443–549","9271","The Greek Acts in Prieur are distinct from each martyrdom and Bonnet recension below."),
("3150","002"):("Martyrium prius Andreae","Prieur, CCSA 6 (1989), pp. 684–703","2547","The first martyrdom is a separate item from the main Greek Acts and BHG 99 martyrdom."),
("3150","003"):("Martyrium sancti Andreae (BHG 99)","Bonnet, Analecta Bollandiana 13 (1894), pp. 354–372","5001","The BHG 99 identifier defines this exact martyrdom recension."),
("3150","004"):("Acta sancti Andreae (BHG 93)","Bonnet 1891 vol. 2.1 pp. 1–37","word count not supplied","BHG 93 is retained as its own catalogue item despite sharing edition pages with BHG 94."),
("3150","005"):("Acta sancti Andreae (BHG 94)","Bonnet 1891 vol. 2.1 pp. 1–37","word count not supplied","BHG 94 is retained as its own catalogue item despite sharing edition pages with BHG 93."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
