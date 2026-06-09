# Orchestrator Template

Use this template when creating `.agents/skills/{domain}-orchestrator/SKILL.md` or `docs/harness/{domain}/team-spec.md`.

```markdown
# <Domain> Orchestrator

## Goal

Describe the reusable workflow and final deliverables.

## Roles

| Role | Form | Responsibility | Output |
| --- | --- | --- | --- |
| lead | skill | Coordinates phases | `_workspace/01_lead_plan.md` |

## Phase Order

1. Intake
2. Analysis
3. Generation
4. Review
5. Revision
6. Final validation

## Handoff Contract

- Intermediate files live under `_workspace/<task-slug>/`.
- Each handoff includes objective, inputs, decisions, open questions, and next action.
- Final user-facing artifacts live outside `_workspace/`.

## Failure Policy

- Retry deterministic setup failures once.
- Preserve conflicting findings with source labels.
- Stop and report when a required external dependency is missing.

## Verification

List exact commands, manual checks, or review scenarios.
```
