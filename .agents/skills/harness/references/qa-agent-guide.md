# QA Agent Guide

Use QA roles for cross-boundary verification, not superficial existence checks.

## Good QA Targets

- API response shape vs frontend assumptions
- Generated spec vs implementation
- Test command output vs claimed behavior
- Security boundary vs data flow
- Plugin manifest vs packaged files

## QA Output

QA findings should include:

- Finding
- Evidence
- Affected file or artifact
- Severity
- Suggested next action

## Subagent Use

Spawn QA subagents only for bounded review lanes. Give each QA agent a narrow surface and a required structured result. Do not let a QA agent rewrite shared files unless explicitly assigned.
