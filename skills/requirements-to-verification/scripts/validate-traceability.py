#!/usr/bin/env python3
import argparse, pathlib, re, sys
parser=argparse.ArgumentParser();parser.add_argument('--template',action='store_true');parser.add_argument('traceability');a=parser.parse_args();p=pathlib.Path(a.traceability)
if not p.is_file(): print(f'ERROR: traceability file not found: {p}',file=sys.stderr);sys.exit(2)
t=p.read_text(encoding='utf-8'); required=['# Requirements Traceability Table','## Traceability records','Need ID','Requirement ID','Design decision ID','Verification ID','Evidence reference','Evidence timestamp','## Open questions and residual risks']
missing=[x for x in required if x not in t]
if missing: print('ERROR: traceability table is missing: '+', '.join(missing),file=sys.stderr);sys.exit(1)
if a.template: print('OK: traceability template has stable IDs and evidence fields.');sys.exit(0)
rows=[x for x in t.splitlines() if re.match(r'\| N-[^|]+\| R-[^|]+\|',x)]
if not rows: print('ERROR: completed traceability needs at least one N-* to R-* record.',file=sys.stderr);sys.exit(1)
for row in rows:
 c=[x.strip() for x in row.strip('|').split('|')]
 if len(c)<11 or any(not x for x in (c[0],c[1],c[4],c[5],c[9])): print('ERROR: each record needs stable IDs and status.',file=sys.stderr);sys.exit(1)
 if c[9]=='passed' and (not c[7].startswith(('path:','command:')) or c[8] in {'','n/a'}): print('ERROR: passed requires a path:/command: evidence reference and timestamp.',file=sys.stderr);sys.exit(1)
print('OK: completed traceability records have stable IDs and evidence rules.')
