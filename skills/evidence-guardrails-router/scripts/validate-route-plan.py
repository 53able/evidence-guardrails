#!/usr/bin/env python3
import argparse, pathlib, re, sys
parser=argparse.ArgumentParser(); parser.add_argument('--template', action='store_true'); parser.add_argument('plan'); args=parser.parse_args()
p=pathlib.Path(args.plan)
if not p.is_file(): print(f'ERROR: route plan not found: {p}', file=sys.stderr); sys.exit(2)
t=p.read_text(encoding='utf-8')
required=['# Evidence Guardrails Route Plan','## Route','Classification evidence','Stop condition','## Unresolved information','## Router result','Next confirmation']
missing=[x for x in required if x not in t]
if missing: print('ERROR: route plan is missing: '+', '.join(missing), file=sys.stderr); sys.exit(1)
if args.template: print('OK: route-plan template has route, evidence, stop, and handoff contracts.'); sys.exit(0)
rows=[x for x in t.splitlines() if re.match(r'\|\s*\d+\s*\|',x)]
if not rows: print('ERROR: completed route plan needs at least one ordered route.', file=sys.stderr); sys.exit(1)
for row in rows:
 c=[x.strip() for x in row.strip('|').split('|')]
 if len(c)<7 or any(not x for x in (c[1],c[2],c[4],c[5],c[6])):
  print('ERROR: each route needs skill, classification evidence, expected output, stop condition, and status.', file=sys.stderr);sys.exit(1)
 if c[1]=='skipped' and 'low' not in c[2].lower():
  print('ERROR: skipped requires explicit low-risk, reversible classification evidence.', file=sys.stderr);sys.exit(1)
if not re.search(r'(?m)^- Status:\s*(continue|blocked)\b',t): print('ERROR: router result needs continue or blocked status.',file=sys.stderr);sys.exit(1)
if re.search(r'(?m)^- Next confirmation:\s*$',t): print('ERROR: completed route plan needs a next confirmation or explicit none.',file=sys.stderr);sys.exit(1)
print('OK: completed route plan has evidence-bearing routes, stop states, and a next confirmation.')
