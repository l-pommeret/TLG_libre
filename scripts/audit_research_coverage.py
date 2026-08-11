import csv, glob, re, collections
from pathlib import Path
root=Path(__file__).resolve().parents[1]; d=root/'data/research_batches'
canon=[r for r in csv.DictReader(open(root/'data/canon_coverage.csv')) if r['record_type']=='work' and r['tlg_author_id'].isdigit() and r['tlg_work_id'].isdigit()]
canon.sort(key=lambda r:(int(r['tlg_author_id']),int(r['tlg_work_id']))); ix={(r['tlg_author_id'],r['tlg_work_id']):i for i,r in enumerate(canon)}
e=collections.Counter(); fs=collections.defaultdict(set); ss=collections.defaultdict(set)
p=collections.Counter(); pfs=collections.defaultdict(set)
for f in d.glob('*.csv'):
 if f.name.startswith(('research_coverage_audit','scan_volume_audit','scan_volume_validation')): continue
 for r in csv.DictReader(open(f)):
  q=(r.get('tlg_author_id'),r.get('tlg_work_id')) if r.get('tlg_author_id') else tuple(r['tlg_id'].split('.',1)) if r.get('tlg_id') and '.' in r['tlg_id'] else None
  if not q: continue
  # These files record a mechanical prioritisation of formerly inferred ranges.
  # They are useful leads, but they are not evidence of an item-level source check.
  if f.name.startswith('range_inferred_batch_'):
   p[q]+=1; pfs[q].add(f.name); continue
  e[q]+=1;fs[q].add(f.name);ss[q].add(r.get('proposed_status') or r.get('result') or '')
i=collections.defaultdict(set); bad=[]
for f in d.glob('*.md'):
 m=re.match(r'^(\d{4})\.(\d{3})-(\d{4})\.(\d{3})\.md$',f.name)
 if not m:continue
 a,b=(m.group(1),m.group(2)),(m.group(3),m.group(4))
 if a not in ix or b not in ix or ix[a]>ix[b]:bad.append(f.name);continue
 for r in canon[ix[a]:ix[b]+1]:i[(r['tlg_author_id'],r['tlg_work_id'])].add(f.name)
out=[]
for r in canon:
 q=(r['tlg_author_id'],r['tlg_work_id'])
 c='REVIEWED_EXPLICIT' if e[q] else ('PRIORITIZED_ONLY' if p[q] else ('REVIEWED_RANGE_INFERRED' if i[q] else 'UNREVIEWED'))
 out.append([*q,r['author_heading'],r['work_title'],e[q],'; '.join(sorted(fs[q])),'; '.join(sorted(ss[q])),p[q],'; '.join(sorted(pfs[q])),'; '.join(sorted(i[q])),c])
with open(d/'research_coverage_audit.csv','w',newline='') as h:w=csv.writer(h,lineterminator='\n');w.writerow(['tlg_author_id','tlg_work_id','author','work_title','journal_rows','journal_files','statuses','priority_rows','priority_files','inferred_range_files','coverage']);w.writerows(out)
c=collections.Counter(x[-1] for x in out);ov=sum(bool(e[(x[0],x[1])]) and bool(i[(x[0],x[1])]) for x in out)
(d/'research_coverage_audit_summary.md').write_text(f'# Audit de couverture\n\n- Notices work : {len(out)}\n- REVIEWED_EXPLICIT : {c["REVIEWED_EXPLICIT"]}\n- PRIORITIZED_ONLY : {c["PRIORITIZED_ONLY"]}\n- REVIEWED_RANGE_INFERRED : {c["REVIEWED_RANGE_INFERRED"]}\n- UNREVIEWED : {c["UNREVIEWED"]}\n- Chevauchements : {ov}\n- Chaînes MD invalides : {len(bad)}\n')
print(len(out),dict(c),ov,len(bad))
