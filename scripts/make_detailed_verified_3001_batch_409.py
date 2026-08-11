import csv

O="data/research_batches/detailed_verified_3001_batch_409.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3400","001"):("Epistula ad Basilium I","Sinai gr. 1117; Grumel, REB 11 (1953), pp. 137–147","3673","The Sinai witness and Emperor Basil I addressee define the exact letter; embedded Stephanus Byzantius is a heading artefact."),
("3408","001"):("Laudatio Joannis Prodromi (BHG 861p) [Dub.]","Datema and Allen 1986 pp. 388–395","word count not supplied","BHG 861p, doubtful attribution, and possible Leontius authorship are preserved without resolution."),
("3410","001"):("Oratio contra Agnoetas","Diekamp 1938 pp. 154–156","word count not supplied","CPG 7005 and BHG Novum Auctarium 434g are preserved; trailing Stephanus Junior/cross-references are catalogue heading material."),
("3411","001"):("De iis qui ad ecclesiam accedunt","MPG 86.1 cols. 12–68","word count not supplied","The CPG 7016 identifier and exact MPG locus are preserved without inventing a word count."),
("3413","001"):("Quaestiones quibus respondet Maximus","MPG 91 cols. 216–217","word count not supplied","The CPG 7632 identifier and exact two-column locus define this short question item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
