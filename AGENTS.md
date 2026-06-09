# Repository Agents Guide

Keep this file short and repo-wide. Put conditional or bulky workflow guidance in linked docs and skills.

## What

- Codex Meta Harness is a Codex-native repository for designing repo-local agent harnesses.
- The canonical Harness skill lives in `.agents/skills/harness/`.
- The plugin-packaged copy lives in `skills/harness/` and must remain an exact mirror.
- Durable output contracts live in `docs/harness/`; `_workspace/` is for intermediate handoffs.

## Why

- The project keeps harness design portable, auditable, and easy to revise as Codex evolves.
- Prefer simple skills, explicit artifacts, and bounded subagents over hidden orchestration.

## How

- When changing `.agents/skills/harness/`, run `python3 scripts/sync_packaged_skill.py` before validating.
- When changing skill paths, generated artifact contracts, or plugin metadata, update `README.md`, `.codex-plugin/plugin.json`, and `docs/harness/README.md` together.
- Validate with `python3 scripts/test_install_harness.py` and `python3 scripts/validate_codex_port.py`.
- Use subagents only when the task is explicitly parallel, bounded, and worth the token cost.
