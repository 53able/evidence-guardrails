#!/usr/bin/env python3
import argparse, pathlib, re, sys
parser=argparse.ArgumentParser()
parser.add_argument('--template', action='store_true')
parser.add_argument('ledger')
a=parser.parse_args(); p=pathlib.Path(a.ledger)
if not p.is_file(): print(f'ERROR: ledger not found: {p}', file=sys.stderr); sys.exit(2)
t=p.read_text(encoding='utf-8')
required=['# Boundary Ledger','## Scope','## Boundaries','## Stop decision','Boundary ID','Source evidence','Confidence','Status']
missing=[x for x in required if x not in t]
if missing: print('ERROR: boundary ledger is missing: '+', '.join(missing),file=sys.stderr);sys.exit(1)
if a.template: print('OK: boundary ledger template has the required contract.');sys.exit(0)
rows=[x for x in t.splitlines() if x.startswith('| BND-')]
if not rows: print('ERROR: completed ledger needs at least one BND-* record.',file=sys.stderr);sys.exit(1)
for row in rows:
 cells=[x.strip() for x in row.strip('|').split('|')]
 if len(cells)<12 or any(not x for x in (cells[0],cells[1],cells[9],cells[10],cells[11])):
  print('ERROR: every BND record needs ID, boundary, source evidence, confidence, and status.',file=sys.stderr);sys.exit(1)
 if cells[10] not in {'observed','inferred','unknown'} or cells[11] not in {'continue','blocked','unknown'}:
  print('ERROR: BND confidence/status uses an unsupported value.',file=sys.stderr);sys.exit(1)
if re.search(r'- Impact class:\s*(high|unknown)',t) and not re.search(r'- Status:\s*blocked\b',t):
 print('ERROR: high/unknown impact requires a blocked stop decision until evidence resolves it.',file=sys.stderr);sys.exit(1)
print('OK: completed boundary ledger has evidence-bearing boundary records and a valid stop decision.')
