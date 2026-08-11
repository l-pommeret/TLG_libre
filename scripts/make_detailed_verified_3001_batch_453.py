import csv
O="data/research_batches/detailed_verified_3001_batch_453.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","063"):("Ad Joannem Aegeatem","Nau, PO 13 (1919), pp. 190–191","","The letter is checked at its exact PO locus; the notice ends with bare Q and supplies no word count or genre."),
("4092","001"):("De dialectis","Schäfer 1811, pp. 1–623","12405","The full dialect treatise locus is preserved."),
("4092","002"):("Commentarium in Hermogenis librum περὶ μεθόδου δεινότητος","Walz, Rhetores Graeci 7.2 (1834, repr. 1968), pp. 1090–1352","55105","The high page span in volume 7.2 and the 1968 reprint are preserved."),
("4092","003"):("Περὶ συντάξεως λόγου","Donnet 1967, pp. 165–229","5805","The Greek-title syntax treatise is checked as the exact Donnet item."),
("4092","004"):("Exegesis in canonem iambicum de festo die spiritus sancti","Montana 1995, pp. 2–84","3563","The attribution of the Pentecost canon to John Damascene in the edition title is preserved without changing the commentator record."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
