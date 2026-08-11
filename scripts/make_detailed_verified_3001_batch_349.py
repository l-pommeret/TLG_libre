import csv

O="data/research_batches/detailed_verified_3001_batch_349.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3190","007"):("Seditio Joanni Comneni","Heisenberg 1907 pp. 19–49","9639","The palace revolution of John Comnenus is the exact historical-rhetorical item."),
("3190","008"):("Ethopoeia","Flusin, Travaux et mémoires 14 (2002), pp. 235–241","1465","The astrologer ethopoeia is preserved as a distinct short rhetorical item."),
("3191","001"):("Miscellanea 8 and 93","Smith, Agapitos and Hult 1996 pp. 28–41","1581","The two nonconsecutive miscellanea numbers 8 and 93 are preserved exactly as the combined catalogue item."),
("3191","002"):("Comparatio Demosthenis et Aristidis","Gigante 1969 pp. 47–83","6892","The exact comparison of Demosthenes and Aristides was checked independently."),
("3191","003"):("Carmina xiv–xx","Featherstone 2000 pp. 20–143","16981","The explicit poem-number span xiv through xx defines the item; no surrounding poems were included."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
