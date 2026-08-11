import csv
O="data/research_batches/detailed_verified_3001_batch_430.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4038","001"):("Fragmenta (P. Vindob. 29788 A–C)","Heitsch, 2nd ed. (1963), pp. 109–120","1575","The three Vienna papyrus parts A–C and Pap medium are preserved as the exact fragment item."),
("4038","002"):("Testimonium","FGrH 749, 3C:732","","The NQ Test. record is retained separately from the title record at the same FGrH locus; no word count is inferred."),
("4038","003"):("Titulus","FGrH 749, 3C:732","","The NQ Hist. title record is retained separately from the testimony at the same FGrH locus; no word count is inferred."),
("4039","001"):("Descriptio Sanctae Sophiae","Veh, Prokop Werke 5 (1977), pp. 306–358","6272","The Veh edition record remains separate from its later duplicate 4039.005."),
("4039","002"):("Descriptio ambonis","Veh 1977, pp. 358–374","1868","The ambo description remains separate from Sancta Sophia and from its later duplicate 4039.006."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];count=f' and {wc}-word item' if wc else ''
  r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, papyrological/FGrH citation, First1KGreek, Perseus and PTA identifier-path lookup; {locus}{count} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high' if wc else 'medium',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
