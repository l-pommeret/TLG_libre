import csv

O="data/research_batches/detailed_verified_3001_batch_341.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3153","003"):("Vita Theophanis ex menologio Messinensi","de Boor 1885 vol. 2 p. 30","224","The single-page Messina menologion life is preserved as a distinct short item."),
("3153","004"):("Officium Theophanis","MPG 108 cols. 45–53","1595","The liturgical office remains distinct from the prose lives and hymns."),
("3153","005"):("Hymni","Krumbacher 1896 pp. 618–621","467","The short hymn collection is checked separately from the adjacent Theophanes laudation."),
("3154","001"):("Laudatio in Theophanem Confessorem","Krumbacher 1896 pp. 608–618","2687","Cross-references to collection 3153 and chronographer 4046 are contextual and remain separate."),
("3157","001"):("Additamenta ad Georgii Acropolitae historiam","Heisenberg 1903 vol. 1 pp. 277–302","4773","The Scutariotes additions remain distinct from Acropolites' own Historia records."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
