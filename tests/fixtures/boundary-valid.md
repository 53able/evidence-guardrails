# Boundary Ledger
## Scope
- Change ID: CHG-001
- Change: retry payment API
- Impact class: high
## Boundaries
| Boundary ID | Boundary | Entry | Output | Persistent state | Side effect | Failure / retry | Dependency | Owner | Source evidence | Confidence | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BND-001 | payment API | job | receipt | payment record | charge | idempotency key | PSP | billing | path: docs/api.md | observed | blocked |
## Stop decision
- Status: blocked
- Missing information: reversal procedure
- Next investigation or owner confirmation: billing
