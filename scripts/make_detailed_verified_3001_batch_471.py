import csv
O="data/research_batches/detailed_verified_3001_batch_471.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4146","018"):("Ovidii Metamorphoseon libri XV graece versi","Papathomopoulos–Tsavare 2002, pp. 3–600","112441","All fifteen Metamorphoses books and their Greek translation status are preserved."),
("4146","020"):("Dialogus de grammatica","Bachmann, Anecdota Graeca 2 (1828), pp. 2–101","24975","The grammar dialogue is checked independently from the construction treatise."),
("4146","021"):("Dialogus de verborum constructione","Bachmann 1828 (repr. 1965), pp. 105–166","15953","The embedded PLATO heading between title elements is recorded as an extraction artefact; the 1965 reprint is preserved."),
("4146","022"):("Vita Boethii","Megas 1996, pp. 58–61","280","The short Life remains separate from the scholia and the translated Consolation volume context."),
("4146","023"):("Scholia in Boethii de philosophiae consolatione","Megas 1996, pp. 357–378","6671","The scholia remain separate from Vita Boethii despite their common edition volume."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
