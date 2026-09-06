#!/usr/bin/env bash
set -euo pipefail
ok() { "$@" >/dev/null; }
bad() { if "$@" >/dev/null 2>&1; then echo "ERROR: invalid fixture unexpectedly passed: $*" >&2; exit 1; fi; }
ok python3 skills/map-observable-boundaries/scripts/validate-boundary-ledger.py tests/fixtures/boundary-valid.md
bad python3 skills/map-observable-boundaries/scripts/validate-boundary-ledger.py tests/fixtures/boundary-invalid.md
ok python3 skills/requirements-to-verification/scripts/validate-traceability.py tests/fixtures/traceability-valid.md
bad python3 skills/requirements-to-verification/scripts/validate-traceability.py tests/fixtures/traceability-invalid.md
ok python3 skills/separate-verification-validation/scripts/validate-vv-evidence.py tests/fixtures/vv-valid.md
bad python3 skills/separate-verification-validation/scripts/validate-vv-evidence.py tests/fixtures/vv-invalid.md
ok python3 skills/evidence-guardrails-router/scripts/validate-route-plan.py tests/fixtures/router-valid.md
bad python3 skills/evidence-guardrails-router/scripts/validate-route-plan.py tests/fixtures/router-invalid.md
echo 'VALIDATOR TESTS PASSED: valid evidence passed and safety-negative fixtures failed.'
