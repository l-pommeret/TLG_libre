import csv

O="data/research_batches/detailed_verified_3001_batch_359.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3200","005"):("Dialogus de matrimonio","Angelou 1991 pp. 60–116","10891","The dialogue with the empress-mother on marriage remains distinct from Manuel's other dialogues."),
("3200","008"):("Chrysobullum de ecclesia Monembasiae","Lampros 1926 pp. 122–123","451","The Monembasia church grant is a distinct short legal document."),
("3200","009"):("Chrysobullum Paris 1402","Escorial gr. omega IV–19; Dennis 1982 section VIII pp. 400–401","359","The 1402 date, Paris issue place, Escorial witness and section VIII locus define this document."),
("3200","010"):("Chrysobullum Paris 1401","Gennadius Library 39; Dennis 1982 section VIII p. 403","332","The 1401 chrysobull and Gennadius witness remain separate from the 1402 Escorial document."),
("3200","011"):("Oratio in dormitionem Deiparae","Jugie, PO 16.3 (1922), pp. 543–566","7338","The Dormition homily is the exact Marian theological item."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
