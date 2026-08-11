import csv
O="data/research_batches/detailed_verified_3001_batch_506.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4326","001"):("Πάππου φιλοσόφου <ὅρκος>","Berthelot–Ruelle 1888, vol. 2, pp. 27–28","186","The supplied oath title and Venetian Marcianus 299 fol.184v witness are preserved."),
("4328","001"):("Τοῦ Χριστιανοῦ περὶ εὐσταθείας τοῦ χρυσοῦ","Berthelot–Ruelle 1888, vol. 2, pp. 395–399","833","Venetian Marcianus 299 fol.110r and the trailing PHILOSTEPHANUS cross-reference token are preserved."),
("4328","002"):("Τοῦ Χριστιανοῦ περὶ τοῦ θείου ὕδατος","Berthelot–Ruelle 1888, vol. 2, pp. 399–400","133","Venetian Marcianus 299 fol.101r and the commentary classification are preserved."),
("4328","003"):("Τίς ἡ τῶν ἀρχαίων διαφωνία","Berthelot–Ruelle 1888, vol. 2, pp. 400–401","231","Venetian Marcianus 299 fol.101v and the commentary classification are preserved."),
("4328","004"):("Τίς ἡ καθόλου τοῦ ὕδατος οἰκονομία","Berthelot–Ruelle 1888, vol. 2, pp. 401–402","37","Venetian Marcianus 299 fol.102r is preserved; this 37-word item remains separate from 4328.005 sharing that folio and page 402."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, alchemical manuscript corpora, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
