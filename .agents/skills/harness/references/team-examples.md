# Team Examples

## Research Harness

- Pattern: Fan-out/Fan-in
- Roles: research lead, web researcher, source checker, synthesis reviewer
- Outputs: `docs/harness/research/team-spec.md`, `_workspace/research/*`

## Code Review Harness

- Pattern: Producer-Reviewer plus Expert Pool
- Roles: path explorer, correctness reviewer, security reviewer, test reviewer
- Outputs: consolidated review with evidence and missing tests

## Documentation Harness

- Pattern: Pipeline
- Roles: code mapper, API writer, example writer, completeness reviewer
- Outputs: docs PR and verification checklist

## Experiment Harness

- Pattern: Pipeline or Supervisor
- Roles: baseline runner, proposer, evaluator, ledger keeper
- Outputs: `_workspace/experiments/{run}/results.tsv`
