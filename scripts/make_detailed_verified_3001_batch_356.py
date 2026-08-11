import csv

O="data/research_batches/detailed_verified_3001_batch_356.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3196","006"):("Vita sancti Zotici","Miller, Analecta Bollandiana 112 (1994), pp. 346–368","3313","The Menologia Imperialia 5059.003 cross-reference is contextual and remains separate."),
("3196","007"):("Sermo in s. martyrem Theodosiam","Kotzabassi 2009 pp. 123–140","7280","The Vitae Theodosiae 5131 cross-reference remains separate; equivalence to MPG 140 cols. 893–936 is preserved."),
("3196","008"):("Oratio in sanctum Eudocimum (BHG 606)","Taxidis 2013 pp. 14–40","9087","The edition identifies BHG 606, defining the exact Eudocimus encomium."),
("3196","009"):("Oratio in sanctum Barbarum","Jerusalem Patriarchate 40 ff. 88v–104v; Papadopoulos-Kerameus 1891 pp. 405–420","4567","The exact manuscript folio span is preserved alongside the printed locus."),
("3196","010"):("Laudatio sanctae Horeozelae","Ambrosian H 81 sup.; Halkin 1987 pp. 6–13","1928","The named Ambrosian witness and exact edition locus define this item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
