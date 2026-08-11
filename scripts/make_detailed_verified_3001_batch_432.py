import csv
O="data/research_batches/detailed_verified_3001_batch_432.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4040","003"):("Contra Manichaeos","Wolska-Conus 1970, pp. 121–173","10301","The journal edition and its stated equivalence to MPG 102, cols. 16–264 are both preserved."),
("4040","004"):("De spiritu sancti mystagogia","MPG 102, cols. 280–392","14211","The main Mystagogia is kept separate from the epitome beginning at column 392."),
("4040","005"):("Epitome de spiritu sancti mystagogia","MPG 102, cols. 392–400","1170","The epitome remains a separate item from 4040.004 despite their shared boundary at column 392."),
("4040","006"):("Homiliae","Laourdas 1966, pp. 1–186 and every explicitly enumerated homily locus","54176","The full homily subdivision list is retained verbatim in canonical_edition, including the anomalous 'Homilia altera, p. 51' and apparent locus discontinuities; none is normalized."),
("4040","008"):("Carmina","MPG 102, cols. 576–584","","The MPG column span and poetic classification are the full supplied item; no word count is inferred."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG citation, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
