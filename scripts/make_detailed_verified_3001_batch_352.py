import csv

O="data/research_batches/detailed_verified_3001_batch_352.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3191","014"):("Στοιχείωσις ἀστρονομική","Bydén 2003 pp. 417–474","14809","The astronomical Stoicheiosis and its exact edition locus define the item."),
("3191","015"):("Γνωμικαί σημειώσεις 1–26 and 71","Hult 2002 pp. 5–242","31112","The nonconsecutive selection 1–26 and 71 is preserved exactly; intervening chapters were not assumed."),
("3191","016"):("Orationes in Andronicum II","Vienna phil. gr. 95 ff. 81–96v and 145v–158; Polemis 2007 pp. 128–420","14618","Both discontinuous manuscript folio spans and the two-orations scope are preserved."),
("3191","017"):("Περὶ τοῦ μαθηματικοῦ εἴδους τῆς φιλοσοφίας","Polemis 2006 pp. 4–150 (even pages)","7082","The even-page printing convention and identification as poem 10 are retained exactly."),
("3191","018"):("Paraphrasis in De memoria et reminiscentia","Bloch 2005 pp. 11–30","5353","The exact Aristotelian paraphrase remains distinct from the broader philosophical works."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
