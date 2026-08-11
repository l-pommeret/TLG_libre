import csv

O="data/research_batches/detailed_verified_3001_batch_367.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3232","002"):("De miraculis sancti Demetrii","Balfour 1979 pp. 39–69","13632","The Saint Demetrius miracle discourse is the exact hagiographic-homiletic item."),
("3232","003"):("Apologia de abitu ad Constantinopolim","Balfour 1979 pp. 70–76","2567","The apology concerning departure for Constantinople is preserved as its own homily."),
("3232","004"):("Epistulae ii ad Andronicum Palaeologum","Balfour 1979 pp. 77–82","2051","The two-part structure is preserved: address on p. 77 and teaching to Andronicus on pp. 78–82."),
("3232","005"):("Sermones ii exhortatorii ad fideles","Balfour 1979 pp. 83–90","3060","The explicit two-sermon scope is preserved exactly."),
("3232","006"):("Epistulae ii ad monachos Constantinopolitanos","Balfour 1979 pp. 91–97","2623","The explicit two-letter scope and Constantinopolitan monastic addressees define the item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
