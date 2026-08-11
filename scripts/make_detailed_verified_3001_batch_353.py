import csv

O="data/research_batches/detailed_verified_3001_batch_353.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("3191","019"):("Carmen xi ad Theodorum Xanthopulum","Featherstone 1988 pp. 254–261","2154","Poem xi and its named addressee Theodore Xanthopulus define the exact item."),
("3191","020"):("Byzantios vel laus Constantinopolitana","Polemis 2013 pp. 110–476","36576","The Constantinopolitan city encomium is the exact rhetorical item."),
("3191","021"):("Orationes","Polemis and Kaltsogianni 2019 pp. 15–59, 60–108, 109–148, 176–266, 553–576, 577–608, 633–672 and 697–722","102403","All eight explicit edition loci are preserved without filling the intervening gaps."),
("3191","022"):("Chrysobulli prooemium","Polemis and Kaltsogianni 2019 pp. 609–610","583","The short chrysobull preamble is preserved separately from the surrounding Orationes loci."),
("3191","023"):("Laudatio sancti Demetrii (BHG 547g)","Laourdas 1960 pp. 56–82","11385","The BHG 547g identifier defines this exact Demetrius laudation."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, First1KGreek, Perseus and PTA identifier-path lookup; {locus} and {wc}-word {label} checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was found.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images of {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
