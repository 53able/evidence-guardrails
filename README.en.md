<p align="center">
  <a href="README.md">日本語</a> · <strong>English</strong>
</p>

# evidence-guardrails

A small collection of agent skills for exposing missing evidence before and after AI-driven software changes. Each skill uses the standard `SKILL.md` layout under `skills/`.

## Included skills

- `evidence-guardrails`: Classifies a change's impact and evidence gaps, then orders only the necessary downstream skills.
- `map-observable-boundaries`: Records a change's external boundaries, state, side effects, failures, and owners.
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

This project does not generate SysML, replace a full requirements-management system, or automatically approve production changes. A completed template alone does not establish safety or fitness for purpose.

## Language scope

The project README is available in Japanese and English. The operational `SKILL.md` instructions are currently authored in Japanese.
