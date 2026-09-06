<p align="center">
  <a href="README.md">日本語</a> · <strong>English</strong>
</p>

# evidence-guardrails

A small collection of agent skills for exposing missing evidence during AI-driven greenfield development and changes to existing software. Each skill uses the standard `SKILL.md` layout under `skills/`.

## Why this exists

AI can accelerate implementation and testing, but code generation alone does not answer these questions:

- What is actually inside the change boundary?
- What must be true before the work is complete?
- How does passing a test differ from meeting a user or operational objective?
- Are external sends, durable data, authorization, or rollback still unknown?

This project treats those unknowns as conditions that can stop work, rather than as notes to revisit later. It does not implement a solution; it makes missing evidence visible before implementation proceeds.

## Why four skills

A single checklist blurs requirements, design, tests, and user confirmation. The project separates them into four steps:

1. `evidence-guardrails` selects the first necessary check.
2. `map-observable-boundaries` records external boundaries, state, side effects, failures, and owners.
3. `requirements-to-verification` connects needs to requirements, verification methods, and evidence.
4. `separate-verification-validation` separates conformance to specifications from fitness for user and operational objectives.

In particular, an unknown external send or durable-data boundary must not be treated as low risk.

## Included skills

- `evidence-guardrails`: Classifies a new project or change by impact and evidence gaps, then orders only the necessary downstream skills.
- `map-observable-boundaries`: Records a new design or change's external boundaries, state, side effects, failures, and owners.
- `requirements-to-verification`: Separates and traces needs, requirements, design decisions, verification methods, and evidence.
- `separate-verification-validation`: Separates conformance to specifications from fitness for user and operational objectives.

## Use

```bash
npx skills add 53able/evidence-guardrails --list
npx skills add 53able/evidence-guardrails --skill map-observable-boundaries
```

For a local checkout:

```bash
npx skills add ./ --list
```

## Validation

```bash
npm test
```

The test suite checks frontmatter, directory names, descriptions, relative paths, line limits, and validators against valid and invalid evidence fixtures. It does not establish that generated evidence is true or that the skills improve outcomes on real projects. `evals/` contains the evaluation rubric, comparison protocol, and cases for such testing.

## Out of scope

This project does not generate SysML, replace a full requirements-management system, or automatically approve production changes. When evidence is absent, it records `unknown` or `blocked` rather than filling the gap with an assumption. A completed template alone does not establish safety or fitness for purpose.

## Language scope

The project README is available in Japanese and English. The operational `SKILL.md` instructions are currently authored in Japanese.
