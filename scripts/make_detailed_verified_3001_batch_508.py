import csv
O="data/research_batches/detailed_verified_3001_batch_508.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4328","010"):("Πόσαι εἰσὶν αἱ κατ’ εἶδος καὶ γένος διαφοραὶ τῶν ποιήσεων","Berthelot–Ruelle 1888, vol. 2, pp. 410–414","818","high","Venetian Marcianus 299 fol.122r and the commentary classification are preserved."),
("4328","011"):("Πῶς δεῖ νοεῖν διαφορὰς τῶν ποιήσεων καὶ σχήμασι γεωμετρικοῖς","Berthelot–Ruelle 1888, vol. 2, pp. 414–415","163","high","Venetian Marcianus 299 fol.124r is preserved; the item remains distinct at the shared page-414 boundary."),
("4328","012"):("Τίς ἡ ἐν ἀποκρύφοις τῶν παλαιῶν ἐκδιδομένη τάξις","Berthelot–Ruelle 1888, vol. 2, pp. 415–421","1,195","high","Venetian Marcianus 299 fol.124v is preserved; the item remains distinct at the shared page-415 boundary."),
("4329","001"):("Ἀνεπιγράφου φιλοσόφου περὶ θείου ὕδατος τῆς λευκώσεως","Berthelot–Ruelle 1888, vol. 2, pp. 421–424","504","high","Anonymous attribution and Venetian Marcianus 299 fol.78r are preserved."),
("4329","002"):("Ἀνεπιγράφου φιλοσόφου κατὰ ἀκολουθίαν χρήσεως ἐμφαῖνον τὸ τῆς χρυσοποιίας συνεπτυγμένον σὺν θεῷ","Berthelot–Ruelle 1888, vol. 2, pp. 424–433","1,709","high","Anonymous attribution and Venetian Marcianus 299 fol.79r are preserved; the item remains distinct at page 424."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,conf,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, relevant manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence=conf,proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
