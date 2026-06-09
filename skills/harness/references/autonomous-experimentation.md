# Autonomous Experimentation

Use this profile only when the user asks for iterative experiments on user-controlled compute.

## Required Contract

- Immutable evaluation surface
- Mutable proposal surface
- Baseline result
- Fixed metric
- Budget or stop condition
- Results ledger

## Directory Shape

```text
_workspace/experiments/<run>/
├── baseline.md
├── proposals/
├── results.tsv
└── summary.md
```

## Keep Or Discard

Keep a proposal only when it improves the fixed metric without violating the immutable surface or write scope. Record crashes, timeouts, no-change runs, and scope violations explicitly.
