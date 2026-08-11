import csv
O="data/research_batches/detailed_verified_3001_batch_429.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4036","021"):("Eclogae de philosophia Chaldaica","des Places 1971, pp. 206–212","1465","The Chaldaean philosophical selections are checked as the exact item."),
("4036","023"):("Chrestomathia [Dub.] (epitome)","Severyns 1963, pp. 67–74, 77–85 and 87–97","2156","Doubtful status, Vita Homeri/Cyclicorum subdivisions, discontinuous loci and partial duplicate 1805.003 are preserved; the CTS candidate is not exact licensed verification."),
("4036","024"):("De Sphaera [Dub.]","Bainbridge 1620, no page locus or word count supplied by canon","","Doubtful status is preserved. The bibliographic notice ends at 'Cod' without a page locus or count, so none is inferred."),
("4036","030"):("In Platonis Parmenidem","Steel 2007–2009, vols. I–III: pp. 1–251, 1–274 and 1–278","172190","All three volumes are preserved; the canon explicitly marks this modern edition record as a duplicate of 4036.008."),
("4036","031"):("Libri vii finis in linguam graecam redditus a Carlos Steel","Steel, vol. III (2009), pp. 281–355","","The Greek rendering by Carlos Steel of the end of book VII remains a separate translation item; the canon supplies no word count."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus, OPP and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for the cited edition and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
