# Skill Writing Guide

Every generated `SKILL.md` must begin with YAML frontmatter:

```markdown
---
name: skill-name
description: Front-load exactly when this skill should be used.
---
```

## Rules

- Keep each skill focused on one job.
- Write imperative workflow steps.
- Define required inputs and expected outputs.
- Move bulky details into `references/`.
- Add scripts only for deterministic repeated work.
- Make descriptions concise and triggerable.
- Avoid broad claims that overlap with other skills.

## Structure

```markdown
# Skill Name

## When to Use
## Required Inputs
## Workflow
## Outputs
## Validation
## Reference Pointers
```

Use repository-friendly names: lowercase, hyphenated, stable.
