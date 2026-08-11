import csv

O="data/research_batches/detailed_verified_3001_batch_326.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3117","001"):("Oratio ascetica","Alfeyev, SC 460 (2001), pp. 72–130","5276","The Symeon Studites ascetic discourse was checked independently of works by Symeon the New Theologian."),
("3119","001"):("Oratio in dei matrem in templum deductam (BHG 1149)","MPG 98 cols. 1481–1500","3535","The BHG 1149 identifier and Tarasius attribution define the exact homily."),
("3120","001"):("Παραστάσεις σύντομοι χρονικαί","Preger 1901, part 1, pp. 19–73","8090","Cross-references to the Hesychius and Pseudo-Codinus Patria remain separate catalogue records."),
("3120","002"):("Διήγησις περὶ τῆς Ἁγίας Σοφίας","Preger 1901, pp. 74–108","4698","The main narrative was checked separately from its 304-word variant readings."),
("3120","003"):("Διήγησις περὶ τῆς Ἁγίας Σοφίας (variae lectiones)","Preger 1901, pp. 84–85 and 91","304","These variant readings are preserved as a distinct short item, not merged into 3120.002."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
