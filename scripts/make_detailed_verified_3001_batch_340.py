import csv

O="data/research_batches/detailed_verified_3001_batch_340.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3150","006"):("Martyrium sancti Andreae (BHG 97)","Bonnet 1891 vol. 2.1 pp. 58–64","word count not supplied","BHG 97 is retained as its own catalogue item despite sharing its locus with BHG 98."),
("3150","007"):("Martyrium sancti Andreae (BHG 98)","Bonnet 1891 vol. 2.1 pp. 58–64","word count not supplied","BHG 98 remains separate from BHG 97; the trailing Acta Andreae et Matthiae is a catalogue heading artefact."),
("3152","001"):("Vita Theophanis Confessoris","de Boor 1885 vol. 2 pp. 13–27","4903","The cross-reference to Vitae Theophanis Confessoris 3153 is contextual; this Nicephorus life remains distinct."),
("3153","001"):("Anonymi vita Theophanis","de Boor 1885 vol. 2 pp. 3–12","3162","The anonymous life is distinct from the Paris office extract catalogued as 3153.002."),
("3153","002"):("Vita Theophanis ex officio festi","de Boor 1885 vol. 2 pp. 3–12 and 28–30","715","Both explicit discontinuous loci are preserved; this office-derived extract is not merged with 3153.001."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
