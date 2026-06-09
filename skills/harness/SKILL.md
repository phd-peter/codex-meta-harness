---
name: harness
description: Design Codex-native repo-local agent harnesses with reusable skills, optional custom agents, team specs, validation loops, and deterministic workspace handoffs.
---

# Codex Harness

Use this skill when the user asks to build, redesign, audit, or extend a reusable harness for a repository or domain. A harness is the durable support system around Codex work: skills, repo guidance, optional custom agents, specs, handoff files, validation commands, and review loops.

Do not use this skill for one-off work that can be handled directly without creating reusable structure.

## Required Inputs

Discover or ask only when necessary:

- Target domain or repository goal
- Expected final deliverables
- Existing repo guidance, skills, scripts, and docs
- Quality bar, failure tolerance, and verification commands
- Whether the output should be repo-local skills, a distributable plugin, or both

## Generated Artifacts

Generate the smallest durable artifact set that fits the workflow:

- `AGENTS.md` for short repo-wide guidance, only when the target repo needs it
- `.agents/skills/{domain}-orchestrator/SKILL.md` for reusable orchestration
- `.agents/skills/{specialist}/SKILL.md` for specialist behavior
- `.agents/skills/{specialist}/references/*` for progressive disclosure
- `.codex/agents/{agent}.toml` only when a spawned custom agent needs a distinct profile
- `docs/harness/{domain}/team-spec.md` for topology, handoffs, and failure policy
- `_workspace/{phase}_{role}_{artifact}.md` for intermediate handoff evidence

If distribution is requested, package the reusable skill tree with `.codex-plugin/plugin.json` and a root `skills/` directory.

## Portable Defaults

- Prefer repo-local skills under `.agents/skills/`.
- Keep `AGENTS.md` short, repo-wide, and pointer-heavy.
- Use one main Codex thread by default.
- Use subagents only when the user explicitly asks or when a bounded parallel task is clearly useful.
- Use `_workspace/` handoffs instead of hidden chat state for intermediate artifacts.
- Do not pin models or require custom MCP servers unless the target repository already depends on them.
- Require YAML frontmatter with `name` and `description` in every generated `SKILL.md`.
- Keep temporary retry logic isolated so it can be removed as Codex improves.

## 6-Phase Workflow

### Phase 1: Domain Analysis

Inspect the request, repository, and existing guidance. Identify:

- Domain and user goal
- Core task types
- Expected outputs
- Quality and verification requirements
- Existing reusable material
- Runtime or tool assumptions that should be preserved or removed

Output a concise domain summary and task inventory before generating files.

### Phase 2: Team Architecture Design

Choose the smallest coordination pattern that preserves quality:

- Pipeline: sequential dependent phases
- Fan-out/Fan-in: independent parallel work followed by synthesis
- Expert Pool: selective routing to relevant specialists
- Producer-Reviewer: generation followed by explicit quality review
- Supervisor: one coordinator manages a changing backlog
- Hierarchical Delegation: shallow layered decomposition

Prefer skills and markdown contracts first. Add custom agents only when distinct spawned behavior is needed.

### Phase 3: Role and Artifact Definition

For each role, choose one durable form:

- Specialist skill
- Orchestrator skill
- Role spec under `docs/harness/{domain}/roles/`
- Custom agent TOML under `.codex/agents/` for spawned work

Define responsibilities, inputs, outputs, handoffs, review edges, and failure policy. Avoid creating files for roles that are too narrow or single-use.

### Phase 4: Skill Generation

Generate each reusable skill under `.agents/skills/`.

Each `SKILL.md` must:

- Start with YAML frontmatter containing `name` and `description`
- Explain when to use the skill
- List required inputs
- Provide imperative workflow steps
- Define expected outputs
- Mention validation or review expectations

Move bulky detail to `references/`. Add scripts only when deterministic automation beats instructions.

### Phase 5: Integration and Orchestration

Write the end-to-end workflow as an orchestrator skill or team spec.

Specify:

- Phase order
- Owners and role boundaries
- Handoff file names
- Review gates
- Failure policy
- Verification commands
- Any bounded subagent usage

Preserve intermediate files in `_workspace/` when they are useful for auditability.

### Phase 6: Validation and Testing

Verify:

- Paths are real and internally consistent
- Skills and team specs agree on artifact names
- Each phase has at least one named output
- QA steps are explicit when quality risk is high
- `AGENTS.md` remains short and repo-wide
- Generated skills include valid frontmatter
- Removed runtime-specific assumptions do not reappear

Run narrow tests or scenario checks. Report what passed, what was not run, and any remaining risk.

## Subagent Guidance

Codex can spawn subagents for specialized work. Use them sparingly:

- Spawn only for bounded parallel work such as independent reviews, broad research lanes, or disjoint implementation slices.
- Give each subagent a narrow objective, ownership boundary, and expected output.
- Require a deterministic handoff file or a concise structured result.
- Do not let subagents rewrite shared files without coordination.
- Close or integrate completed subagent work before final reporting.

## Reference Pointers

- `references/agents-md-guide.md`
- `references/agent-design-patterns.md`
- `references/orchestrator-template.md`
- `references/skill-writing-guide.md`
- `references/skill-testing-guide.md`
- `references/qa-agent-guide.md`
- `references/team-examples.md`
- `references/autonomous-experimentation.md`
