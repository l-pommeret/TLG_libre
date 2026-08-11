import csv

O="data/research_batches/detailed_verified_3001_batch_336.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3141","006"):("In imaginem beatae virginis","Heisenberg vol. 2 pp. 6–7","115","The exact two-page iambic item was checked separately from adjacent works."),
("3141","007"):("Praefatio in epistulas Theodori Lascaris","Heisenberg vol. 2 pp. 7–9","345","The preface to Theodore Lascaris' letters is its own short iambic item."),
("3141","008"):("Carmen in magnum sabbatum","Heisenberg vol. 2 pp. 9–11","198","The Holy Saturday liturgical poem is preserved as a distinct short item."),
("3141","009"):("Epitaphius in Joannem Ducam","Heisenberg vol. 2 pp. 12–29","4805","The exact epitaph for John Ducas was checked independently."),
("3141","010"):("Contra Latinos","Heisenberg vol. 2 pp. 30–66","10338","The anti-Latin oration and its exact locus define this item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
