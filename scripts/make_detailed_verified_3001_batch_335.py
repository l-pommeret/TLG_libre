import csv

O="data/research_batches/detailed_verified_3001_batch_335.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3136","001"):("Lexicon","Tittmann 1808: vol. 1 pp. 1–1070; vol. 2 pp. 1077–1900","229291","Both explicit volume loci define the Pseudo-Zonaras lexicon."),
("3141","001"):("Annales (Bekker edition)","Bekker, CSHB (1836), pp. 3–198","word count not supplied","This Bekker edition record remains separate from Heisenberg duplicate-title record 3141.002."),
("3141","002"):("Annales (Heisenberg edition)","Heisenberg 1903 vol. 1 pp. 3–189","38487","This Heisenberg edition record remains separate from Bekker duplicate-title record 3141.001."),
("3141","003"):("Historia in brevius redacta","Heisenberg 1903 vol. 1 pp. 193–274","15520","The trailing Acta Alexandrinorum text is a catalogue heading artefact, not part of this history."),
("3141","005"):("Epitaphius in Irenam imperatricem","Heisenberg 1903 vol. 2 pp. 3–6","712","The exact short epitaph for Empress Irene was checked as its own item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and catalogue marker {wc} for {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
