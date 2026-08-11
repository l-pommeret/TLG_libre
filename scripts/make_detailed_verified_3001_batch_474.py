import csv
O="data/research_batches/detailed_verified_3001_batch_474.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4149","001"):("Excerpta ex Joannis Characis commentariis","Hilgard, Grammatici Graeci 4.2 (1894, repr. 1965), pp. 375–434","21628","The excerpts from John Charax on Theodosius's canons and the reprint are preserved."),
("4150","001"):("Anacreontea","West 1984, pp. 1–49","3855","The Anacreontea collection is checked as the exact West item."),
("4153","001"):("Chronographia (lib. 1–6)","Bekker, CSHB (1838), pp. 1–481","94432","The six-book Bekker record remains separate from the later four-book duplicate edition."),
("4153","002"):("Chronographia (lib. 1–4)","Featherstone–Codoñer, CFHB 53 (2015), even pp. 8–300","","The four-book scope, even-page restriction and explicit duplicate link to 4153.001 are preserved; no count is inferred."),
("4154","001"):("Prooemium et commentarius in Apocalypsin","Cramer 1840 (repr. 1967), pp. 173–175 and 497–582","","The Coislinianus 224 witness, two discontinuous loci and reprint are preserved; no count is supplied."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
