# Codex Compatibility

## Skill Locations

Codex discovers skills from `.agents/skills/` in the current directory, parent folders up to the repository root, `$HOME/.agents/skills/`, and admin/system locations.

Use:

- Repo-local skills: `.agents/skills/harness/`
- User-level skills: `$HOME/.agents/skills/harness/`
- Plugin-packaged skills: `skills/harness/` referenced by `.codex-plugin/plugin.json`

## Custom Agents

Use custom agents only when spawned work needs a distinct profile.

Project custom agents:

```text
.codex/agents/<agent>.toml
```

User custom agents:

```text
$HOME/.codex/agents/<agent>.toml
```

Each custom agent file should define at least:

- `name`
- `description`
- `developer_instructions`

## AGENTS.md

Use `AGENTS.md` for short, always-loaded repository guidance. Put bulky workflow details in skills and docs.

## Plugin Packaging

Codex plugins require:

```text
.codex-plugin/plugin.json
```

The manifest should point to `./skills/` when bundling skills.
