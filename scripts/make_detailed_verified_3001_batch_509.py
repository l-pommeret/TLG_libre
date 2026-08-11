import csv
O="data/research_batches/detailed_verified_3001_batch_509.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4329","003"):("Ἀνεπιγράφου φιλοσόφου περὶ τῆς θείας καὶ ἱερᾶς τέχνης φιλοσόφων","Berthelot–Ruelle 1888, vol. 2, pp. 433–441","1,671","high","Anonymous attribution and both Venetian and Parisian manuscript witnesses are preserved."),
("4338","001"):("Θεοφράστου φιλοσόφου περὶ τῆς θείας τέχνης διὰ στίχων ἰάμβων","Goldschmidt 1923, pp. 34–42","1,560","high","The tentative Heliodorus attribution, Cassel witness, and cross-references to 4332.001, 4337.001, and 4339.001 are preserved."),
("4340","001"):("Μέθοδος δι’ ἧς ἀποτελεῖται ἡ σφαιροειδὴς χάλαζα κατασκευασθεῖσα παρὰ τοῦ ἐν τεχνουργίᾳ περιβοήτου Ἄραβος τοῦ Σαλμανᾶ","Berthelot–Ruelle 1888, vol. 2, pp. 364–367","929","high","Paris BnF gr.2327 fol.141r and the Arab Salmanas attribution are preserved."),
("4349","001"):("Testimonia","Radermacher 1951, pp. 11–12, 15–19, 28–35","word count not supplied","medium","The discontinuous page spans and exact NQ selections A 5.5–7, 16–17, 20, 23 and B 2.1–5, 7–9, 13–26 are preserved; no word count is invented."),
("4351","001"):("Ex Palchi libro apotelesmatico","Cumont, CCAG 1 (1898), pp. 80–81","279","high","Tentative compilation by Eleutherius, fragment status, and Angelicus 29 fol.141v are preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,conf,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, relevant manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc} item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence=conf,proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
