import csv
O="data/research_batches/detailed_verified_3001_batch_482.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4172","002"):("INCOMPLETE_SPLIT_VITA_NOTICE","Vita Oppiani Anazarbensis notice truncated after 'cod. phil. gr.'","","The extracted notice stops mid-manuscript citation; adjacent 4172.135 is a separate continuation record, so no joined notice is synthesized.",True),
("4172","003"):("Vita Oppiani (e cod. Matr. XX)","Iriarte 1769, vol. 1 p. 82","","The Madrid XX witness and single-page locus are preserved; no word count is supplied.",False),
("4172","004"):("Vita Oppiani (Vita α)","Westermann 1845 (repr. 1964), pp. 63–65","258","Vita alpha and the reprint are preserved separately from Vita beta.",False),
("4172","005"):("Vita Oppiani (Vita β)","Westermann 1845, pp. 65–66","349","Vita beta remains separate from Vita alpha despite shared page 65.",False),
("4172","006"):("Vita Tzetziana","Colonna 1964, p. 40","253","All three witnesses—Laur. gr.31.3, Ambros. gr.C222 inf., Vat.gr.1345—are preserved.",False),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note,incomplete) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium' if incomplete or not wc else 'high',proposed_status='INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT' if incomplete else 'NO_EXACT_OPEN_TEXT',next_action='Recover the complete printed-canon notice before text identification.' if incomplete else f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
