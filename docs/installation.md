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
.agents/plugins/marketplace.json
```

Add the GitHub marketplace source:

```shell
codex plugin marketplace add phd-peter/codex-meta-harness --ref main
```

Open Codex and install the plugin:

```text
codex
/plugins
```

In the plugin browser, choose the `phd-peter-codex-meta-harness` marketplace and install `Codex Meta Harness`.

## Notes

- Skills should live under `.agents/skills/` for repo-local discovery.
- Personal skills should live under `$HOME/.agents/skills/`.
- Custom spawned agents, when needed, live under `.codex/agents/` or `$HOME/.codex/agents/`.
- Plugin distribution uses `.codex-plugin/plugin.json`.
