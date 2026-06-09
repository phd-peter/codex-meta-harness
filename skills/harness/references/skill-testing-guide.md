# Skill Testing Guide

Test skills through realistic prompts and structural checks.

## Structural Checks

- `SKILL.md` exists.
- Frontmatter contains `name` and `description`.
- References linked from the skill exist.
- Scripts mentioned by the skill exist and are executable where needed.

## Scenario Checks

Run at least:

- One normal prompt that should trigger the skill.
- One nearby prompt that should not trigger it.
- One failure case where required input is missing.

## Quality Checks

- The skill produces named outputs.
- The workflow can be followed without hidden context.
- Validation is explicit.
- The skill does not duplicate another skill's scope.

Record durable findings under `_workspace/<task-slug>/verification.md` when the test matters later.
