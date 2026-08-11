import csv
O="data/research_batches/detailed_verified_3001_batch_507.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4328","005"):("Ἡ τοῦ μυθικοῦ ὕδατος ποίησις","Berthelot–Ruelle 1888, vol. 2, pp. 402–405","617","Venetian Marcianus 299 fol.102r is preserved; this item remains separate from 4328.004 sharing that folio and page 402."),
("4328","006"):("Ἀντίθεσις λέγουσα ὅτι τὸ θεῖον ὕδωρ ἕν ἐστι τῷ εἴδει καὶ ἡ λύσις αὐτῆς","Berthelot–Ruelle 1888, vol. 2, pp. 405–407","361","Venetian Marcianus 299 fol.119r and the objection-and-solution scope are preserved."),
("4328","007"):("Ἀπορία. Τὸ ἓν ἀβύσσαιον ὕδωρ ἐν τῷ ἀριθμῷ δεικνύειν ἐθέλουσα ἡ τούτου ἐπίλυσις","Berthelot–Ruelle 1888, vol. 2, pp. 407–408","366","Venetian Marcianus 299 fol.120r and the problem-and-resolution scope are preserved."),
("4328","008"):("Τοῦ Χριστιανοῦ σύνοψις. τίς ἡ αἰτία τῆς προκειμένης συγγραφῆς","Berthelot–Ruelle 1888, vol. 2, p. 409","85","Venetian Marcianus 299 fol.121r is preserved; this synopsis remains separate from 4328.009 sharing page 409."),
("4328","009"):("Ὅτι τετραχῶς διαιρουμένης τῆς ὕλης, διάφοροι ἀπογίνονται τῶν ποιήσεων αἱ τάξεις","Berthelot–Ruelle 1888, vol. 2, pp. 409–410","168","Venetian Marcianus 299 fol.121v is preserved; this item remains separate from 4328.008 sharing page 409."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
