import csv
O="data/research_batches/detailed_verified_3001_batch_449.csv"
F="tlg_author_id tlg_work_id author_heading work_title canonical_edition sources_tested open_text_result open_text_url open_text_license scan_result scan_url scan_rights confidence proposed_status next_action notes last_checked".split()
D={
("4089","024"):("Interpretatio in Psalmos","MPG 80, cols. 857–1997","186704","The canon's exact start at column 857 is preserved even though 4089.023 ends at 858; the items are not merged."),
("4089","025"):("Explanatio in Canticum canticorum","MPG 81, cols. 28–213","35418","The Song of Songs explanation is checked as its exact item."),
("4089","026"):("Interpretatio in Jeremiam","MPG 81, cols. 496–805","50578","The internal allocation is preserved: books 1–10 Jeremiah, book 11 Baruch, book 12 Lamentations, including shared boundary columns."),
("4089","027"):("Interpretatio in Ezechielem","MPG 81, cols. 808–1256","81244","The Ezekiel interpretation remains separate from Daniel despite their shared boundary column 1256."),
("4089","028"):("Interpretatio in Danielem","MPG 81, cols. 1256–1546","52894","PTA manuscript/Bibex identifiers exist, but they do not establish an exact licensed MPG item; the shared column 1256 is preserved."),
}
C={(r['tlg_author_id'],r['tlg_work_id']):r for r in csv.DictReader(open('data/canon_coverage.csv',encoding='utf-8'))}
with open(O,'w',newline='',encoding='utf-8') as h:
 w=csv.DictWriter(h,fieldnames=F);w.writeheader()
 for k,(label,locus,wc,note) in D.items():
  s=C[k];r={f:'' for f in F};r.update(tlg_author_id=k[0],tlg_work_id=k[1],author_heading=s['author_heading'],work_title=s['work_title'],canonical_edition=s['bibliographic_notice'],sources_tested=f'Exact local TLG, MPG, First1KGreek, OPP, PTA and Perseus identifier-path lookup; {locus} and {wc}-word item checked; local scan register checked.',open_text_result=f'No exact licensed TEI of {label} at {locus} was verified.',scan_result=f'No reusable page images verified for {locus} are registered locally.',confidence='high',proposed_status='NO_EXACT_OPEN_TEXT',next_action=f'Locate rights-cleared images for {locus} and verify the exact item before transcription or OCR.',notes=note+' No image or OCR used.',last_checked='2026-08-11');w.writerow(r)
