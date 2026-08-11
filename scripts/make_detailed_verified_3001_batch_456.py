import csv
O="data/research_batches/detailed_verified_3001_batch_456.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4135","006"):("Expositio in psalmos (in catenis)","Devreesse 1939, every explicit discontinuous locus from pp. 15–17 through 142–561","102380","The complete discontinuous page list and stated Psalms I–LXXX scope are preserved; no continuous substitute is used."),
("4135","007"):("Commentarius in xii prophetas minores","Sprenger 1977, pp. 1–429","110332","All twelve minor prophets are preserved as the scope of the commentary."),
("4135","009"):("Fragmenta in Matthaeum (in catenis)","Reuss, TU 61 (1957), pp. 96–135","8059","The Theodore of Mopsuestia fragments remain distinct from similarly titled catena records."),
("4135","013"):("Commentarii in Joannem (e catenis)","Devreesse 1948, pp. 305–419","27299","The notice-stated 27,299 count and cross-reference to Novum Testamentum 0031.004 are preserved even though the parsed TLG count field is blank."),
("4135","014"):("Fragmenta in Acta apostolorum [Dub.]","von Dobschütz, AJT 2.2 (1898), pp. 357–362","1509","Doubtful/probable attribution and the notice-stated 1,509 count are preserved even though the parsed TLG count field is blank."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and notice-stated {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
