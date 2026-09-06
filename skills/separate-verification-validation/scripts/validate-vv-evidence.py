#!/usr/bin/env python3
import argparse, pathlib, re, sys
parser=argparse.ArgumentParser();parser.add_argument('--template',action='store_true');parser.add_argument('evidence');a=parser.parse_args();p=pathlib.Path(a.evidence)
if not p.is_file(): print(f'ERROR: evidence file not found: {p}',file=sys.stderr);sys.exit(2)
t=p.read_text(encoding='utf-8'); required=['# Verification and Validation Evidence','## Verification evidence','## Validation evidence','## Residual risks and approval','Representative scenario','Observation','Human approver','Untested scope','Rollback','Required human approver']
missing=[x for x in required if x not in t]
if missing: print('ERROR: V&V evidence is missing: '+', '.join(missing),file=sys.stderr);sys.exit(1)
if a.template: print('OK: V&V template has distinct verification and validation contracts.');sys.exit(0)
valrows=[x for x in t.splitlines() if re.match(r'\| O-[^|]+\| VAL-[^|]+\|',x)]
if not valrows: print('ERROR: completed evidence needs at least one O-* to VAL-* validation record.',file=sys.stderr);sys.exit(1)
for row in valrows:
 c=[x.strip() for x in row.strip('|').split('|')]
 if len(c)<9 or not c[7]: print('ERROR: each validation record needs a status.',file=sys.stderr);sys.exit(1)
 if c[7]=='passed' and (not c[2] or not c[3] or not c[4].startswith(('path:','command:')) or c[5] in {'','n/a'} or not c[8]): print('ERROR: passed validation needs scenario, observation, evidence, timestamp, and human approver.',file=sys.stderr);sys.exit(1)
if re.search(r'(?m)^- Required human approver:\s*$',t): print('ERROR: completed evidence requires a human approver or an explicit blocked status.',file=sys.stderr);sys.exit(1)
print('OK: completed V&V evidence keeps validation evidence and human approval explicit.')
