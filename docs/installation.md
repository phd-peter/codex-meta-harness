# Installation

## Repo-Local Skill Install

From this repository:

```shell
python3 scripts/install_harness.py --scope project --target /path/to/repo
```

This installs the Harness skill into:

```text
/path/to/repo/.agents/skills/harness/
```

## User-Level Skill Install

```shell
python3 scripts/install_harness.py --scope user
```

This installs the Harness skill into:

```text
$HOME/.agents/skills/harness/
```

## Plugin Install During Development

The repository root is plugin-ready because it includes:

```text
.codex-plugin/plugin.json
skills/harness/SKILL.md
```

Use Codex plugin development commands for local marketplace testing once a GitHub repository exists.

## Notes

- Skills should live under `.agents/skills/` for repo-local discovery.
- Personal skills should live under `$HOME/.agents/skills/`.
- Custom spawned agents, when needed, live under `.codex/agents/` or `$HOME/.codex/agents/`.
- Plugin distribution uses `.codex-plugin/plugin.json`.
