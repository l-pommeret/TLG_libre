import csv
O="data/research_batches/detailed_verified_3001_batch_454.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4092","005"):("Epigrammata","Hunger, Analecta Bollandiana 100 (1982), pp. 638–646","697","The Dodekaorton feast epigrams are checked as the exact item."),
("4095","151"):("INCOMPLETE_CONTINUATION_NOTICE","Koster, pp. 151–164 (incomplete extracted continuation)","","The notice begins mid-sentence, carries doubtful status and refers to Georgius Choeroboscus 4093.013; no missing title or antecedent is inferred."),
("4115","029"):("Fragmenta in Matthaeum (in catenis)","Reuss, TU 61 (1957), pp. 151–152","220","The short Matthaean catena fragments remain separate from the Johannine item."),
("4115","030"):("Fragmenta in Joannem (in catenis)","Reuss, TU 89 (1966), p. 187","73","The trailing THEOPHILUS et NARCISSUS text is recorded as a heading artefact, not part of the exact fragment item."),
("4118","001"):("Narrationes septem de monachis in Sina","Conca 1983, pp. 1–52","13312","All seven Sinai monk narratives are preserved as the scope of the item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  incomplete=k==('4095','151')
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='medium' if incomplete else 'high',proposed_status='INCOMPLETE_CONTINUATION_NOTICE_NO_EXACT_TEXT' if incomplete else 'NO_EXACT_OPEN_TEXT',next_action='Recover the preceding printed-canon context before any text identification.' if incomplete else f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
