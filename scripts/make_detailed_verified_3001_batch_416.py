import csv
O="data/research_batches/detailed_verified_3001_batch_416.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4015","017"):("De usu astrolabii eiusque constructione","Hase, Rheinisches Museum 6 (1839), pp. 129–156","7755","The Hase edition is preserved as its own canon item despite the later duplicate 4015.020."),
("4015","018"):("De vocabulis... (additamenta)","Daly 1983, pp. 10, 30, 148–149, 155, 161, 163, 165, 170, 173, 181, 185, 192, 194, 210–211, 215, 222, 224, 228","375","Every isolated addendum locus and the cross-reference to 4015.012 are preserved."),
("4015","019"):("De Paschate (fort. auctore Nicetae David) [Sp.]","Walter, Commentationes Philologicae Jenenses 6.2 (1899), pp. 209–222","4000","The spurious status, possible Nicetas David authorship, and cross-reference to TLG 2705 are preserved without resolution."),
("4015","020"):("De usu astrolabii","Jarry 2015, pp. 1–45","7939","The canon's explicit duplicate link to 4015.017 is preserved while retaining both edition records."),
("4015","021"):("Scholia in cap. VI–VII De usu astrolabii (recensio Φ)","Jarry 2015, pp. 46–48","507","The recension Φ scholia to chapters VI–VII remain separate from the main work and additamenta."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
