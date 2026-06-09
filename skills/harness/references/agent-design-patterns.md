# Agent Design Patterns

Use the smallest architecture that preserves quality.

## Pipeline

Sequential dependent phases. Use when each output becomes the next input.

## Fan-out/Fan-in

Parallel independent lanes followed by synthesis. Use for broad review, research, or multi-surface audits.

## Expert Pool

Route to only the relevant specialists. Use when requests vary by domain and not every role should run.

## Producer-Reviewer

One role produces, another reviews. Use when correctness, security, legal, or user-facing polish matters.

## Supervisor

A coordinator manages a changing backlog. Use when work units shift during execution.

## Hierarchical Delegation

Top-level work breaks into nested subgoals. Keep it shallow; deep recursion raises cost and predictability risk.

## Codex Mapping

- Prefer skills for durable reusable behavior.
- Use custom agents for spawned workers with distinct instructions or model/tool policy.
- Use `_workspace/` for handoffs across agents or phases.
- Use `.codex-plugin/plugin.json` only for distribution.
