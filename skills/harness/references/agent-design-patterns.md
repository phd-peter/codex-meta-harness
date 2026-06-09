# Agent Design Patterns

Use the smallest architecture that preserves quality.

- Pipeline: sequential dependent phases
- Fan-out/Fan-in: independent lanes followed by synthesis
- Expert Pool: route to relevant specialists
- Producer-Reviewer: generation followed by quality review
- Supervisor: coordinator manages changing backlog
- Hierarchical Delegation: shallow layered decomposition

Codex mapping:

- Prefer skills for reusable behavior.
- Use custom agents only for spawned workers with distinct instructions or policy.
- Use `_workspace/` for durable handoffs.
- Use `.codex-plugin/plugin.json` for distribution.
