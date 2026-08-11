import csv
O="data/research_batches/detailed_verified_3001_batch_483.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4172","135"):("INCOMPLETE_CONTINUATION_NOTICE","Mazal, Wiener Studien 80 (1967), p. 118","293","The notice begins mid-manuscript citation ('in Bibl. nat. in Vindob.') and continues 4172.002; no standalone title is invented.",True),
("4173","001"):("Vita Dionysii","Kassel, Catalepton (1985), pp. 70–73","851","The Chisian Life context and Antimachus study are preserved.",False),
("4174","001"):("In Dionysii periegetae orbis descriptionem","Müller 1861 (repr. 1965), vol. 2 pp. 409–425","13158","The embedded PARAPHRASES IN HOMERI OPERA heading splitting 'descriptionem' is recorded as an artefact; partial duplicate 4174.002 and First1K candidate are preserved without merging.",False),
("4174","002"):("In Dionysii periegetae orbis descriptionem","Ludwich 1885 (repr. 1971), vol. 2 pp. 556–574","2599","This Ludwich edition record remains separate from the Müller partial duplicate 4174.001.",False),
("4225","001"):("Epistula ad Gregorium papam","Sakkelion 1965, pp. 50–53","1251","The emperor's letter to Pope Gregory is checked as the exact item.",False),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note,incomplete) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium' if incomplete else 'high',proposed_status='INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT' if incomplete else 'NO_EXACT_OPEN_TEXT',next_action='Recover the complete printed-canon notice before text identification.' if incomplete else f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
