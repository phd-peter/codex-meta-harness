<p align="center">
  <img src="assets/meta_harness_banner.svg" alt="Codex Meta Harness" width="600">
</p>

# Codex Meta Harness

Codex Meta Harness is a Codex-native meta-skill for designing repo-local agent harnesses: reusable skills, optional custom agents, team specs, validation loops, and deterministic handoff artifacts.

This project is adapted from [revfactory/harness](https://github.com/revfactory/harness) and distributed under the same Apache 2.0 license.

## What This Adds

- Codex-first skill layout using `.agents/skills/`
- Short repo-wide guidance through `AGENTS.md`
- Plugin-ready packaging through `.codex-plugin/plugin.json`
- Optional custom-agent guidance through `.codex/agents/*.toml`
- Deterministic `_workspace/` handoffs for auditability
- Validation scripts that reject leftover Claude-specific runtime assumptions

## Repository Layout

```text
codex-meta-harness/
├── AGENTS.md
├── README.md
├── NOTICE
├── LICENSE
├── .codex-plugin/
│   └── plugin.json
├── .agents/skills/harness/
│   ├── SKILL.md
│   └── references/
├── skills/harness/
│   ├── SKILL.md
│   └── references/
├── docs/
│   ├── installation.md
│   ├── sample-prompts.md
│   ├── compatibility/codex.md
│   └── harness/
├── scripts/
│   ├── install_harness.py
│   ├── test_install_harness.py
│   └── validate_codex_port.py
└── assets/
```

The canonical authoring copy lives under `.agents/skills/harness/`. The `skills/harness/` copy is packaged by the Codex plugin manifest.

## Install

Add the GitHub marketplace source:

```shell
codex plugin marketplace add phd-peter/codex-meta-harness --ref main
```

Then open the plugin directory and install `Codex Meta Harness`:

```text
codex
/plugins
```

Install the skill into another repository:

```shell
python3 scripts/install_harness.py --scope project --target /path/to/repo
```

Install as a user-level skill:

```shell
python3 scripts/install_harness.py --scope user
```

For plugin distribution, use the repository root as the plugin folder. The manifest is `.codex-plugin/plugin.json` and points to `./skills/`.

## Use

Ask Codex for work that should become reusable structure:

```text
Build a reusable research harness for this repository.
Design a review workflow with explicit QA handoffs.
Define specialist skills and a team spec for this domain.
Create an experiment harness with a fixed metric and results ledger.
```

Codex Meta Harness generates the smallest useful durable artifact set:

- `.agents/skills/<domain>-orchestrator/SKILL.md`
- `.agents/skills/<specialist>/SKILL.md`
- `docs/harness/<domain>/team-spec.md`
- `_workspace/{phase}_{role}_{artifact}.md`

## Validation

```shell
python3 scripts/test_install_harness.py
python3 scripts/validate_codex_port.py
```

The validator checks required files, skill frontmatter, README links, Codex plugin metadata, and removed runtime-specific tokens.

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
