import csv
O="data/research_batches/detailed_verified_3001_batch_457.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4135","015"):("Romans catena fragments","Staab 1933, pp. 113–172","19165","The embedded THEODORUS Alaniensis heading after the locus is recorded as an extraction artefact, not part of this item."),
("4135","016"):("1 Corinthians catena fragments","Staab 1933, pp. 172–196","5598","The item remains separate despite shared boundary pages with Romans and 2 Corinthians."),
("4135","017"):("2 Corinthians catena fragments","Staab 1933, pp. 196–200","942","The short item remains separate despite shared boundary pages with adjacent catena fragments."),
("4135","018"):("Hebrews catena fragments","Staab 1933, pp. 200–212","3547","The Hebrews item remains separate despite sharing page 200 with 2 Corinthians."),
("4135","025"):("Theodori lapsi responsio [Sp.]","Dumortier, SC 117 (1966), pp. 220–238","1882","Spurious status and publication within Jean Chrysostome, À Théodore are preserved without reassignment."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, catena corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
