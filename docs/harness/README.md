# Harness Output Specs

Harness-generated artifacts should be small, durable, and easy to audit.

## Default Output Set

```text
.agents/skills/<domain>-orchestrator/SKILL.md
.agents/skills/<specialist>/SKILL.md
docs/harness/<domain>/team-spec.md
_workspace/<task-slug>/<phase>_<role>_<artifact>.md
```

## Team Spec

A team spec should include:

- Goal
- Roles
- Pattern
- Handoff files
- Review gates
- Failure policy
- Verification commands

## Workspace Handoffs

Use `_workspace/` for intermediate evidence and coordination artifacts.

Required handoff fields:

- Objective
- Inputs
- Decisions
- Files inspected or changed
- Remaining work
- Verification

Do not put final user-facing deliverables only in `_workspace/`.

## Skill Requirements

Every generated skill must:

- Start with YAML frontmatter
- Include `name` and `description`
- Explain when to use it
- Define inputs and outputs
- Include validation expectations

## AGENTS.md Boundary

Only update `AGENTS.md` when a target repository needs durable repo-wide guidance. Keep details in skills, `docs/harness/`, or references.
