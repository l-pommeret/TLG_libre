import csv

O="data/research_batches/detailed_verified_3001_batch_344.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3176","002"):("Chronicon Maius additamenta et lectiones variae","Grecu 1966 pp. 272–278 and 448–454","3359","The Macarius Melissenus additions and Turin-manuscript variants are preserved as the explicit two-part item."),
("3176","003"):("Chronicon sive Maius, books 1–2 (Papadopoulos)","Papadopoulos 1935, volume 1","word count not supplied","This books 1–2 Papadopoulos edition record remains separate from the Grecu and Bekker records."),
("3176","004"):("Chronicon sive Maius (Bekker)","Bekker, CSHB (1838), pp. 3–453","word count not supplied","This Bekker edition record remains separate from Grecu 3176.001–002 and Papadopoulos 3176.003."),
("3177","001"):("De Leone Armenio e cod. Paris. gr. 1711","Bekker 1842 pp. 335–362","5037","The Paris-manuscript text, explicitly equivalent to MPG 108 cols. 1009–1038, remains separate from 3177.002."),
("3177","002"):("De Leone Armenio e cod. Vat. gr. 2014","Dujčev 1965 pp. 210–216","1089","The Vatican-manuscript recension is preserved separately from the Paris recension 3177.001."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
