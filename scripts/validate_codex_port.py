#!/usr/bin/env python3

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "NOTICE",
    "LICENSE",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    ".agents/skills/harness/SKILL.md",
    "skills/harness/SKILL.md",
    "docs/installation.md",
    "docs/compatibility/codex.md",
    "docs/harness/README.md",
    "scripts/install_harness.py",
    "scripts/sync_packaged_skill.py",
    "scripts/test_install_harness.py",
    "scripts/validate_codex_port.py",
]

REQUIRED_REFERENCES = [
    "agents-md-guide.md",
    "agent-design-patterns.md",
    "autonomous-experimentation.md",
    "orchestrator-template.md",
    "qa-agent-guide.md",
    "skill-testing-guide.md",
    "skill-writing-guide.md",
    "team-examples.md",
]

BANNED_ACTIVE_TOKENS = [
    ".claude/",
    ".claude-plugin/",
    "CLAUDE.md",
    "TeamCreate",
    "SendMessage",
    "TaskCreate",
    "TaskUpdate",
    "TeamDelete",
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS",
    'model: "opus"',
    "claude plugin",
]

ATTRIBUTION_ALLOWED = {
    "NOTICE",
    "README.md",
    "CHANGELOG.md",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(failures: list[str], message: str) -> None:
    failures.append(message)


def check_required_files(failures: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            fail(failures, f"Missing required file: {relative}")

    for base in [".agents/skills/harness/references", "skills/harness/references"]:
        for name in REQUIRED_REFERENCES:
            path = ROOT / base / name
            if not path.exists():
                fail(failures, f"Missing required reference: {path.relative_to(ROOT)}")


def parse_frontmatter(path: Path, failures: list[str]) -> dict[str, str]:
    text = read(path)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail(failures, f"Missing YAML frontmatter: {path.relative_to(ROOT)}")
        return {}

    closing = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing = index
            break
    if closing is None:
        fail(failures, f"Unclosed YAML frontmatter: {path.relative_to(ROOT)}")
        return {}

    data: dict[str, str] = {}
    for line in lines[1:closing]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    for key in ["name", "description"]:
        if not data.get(key):
            fail(failures, f"Frontmatter missing {key}: {path.relative_to(ROOT)}")
    return data


def iter_text_files() -> list[Path]:
    paths: list[Path] = []
    for pattern in ["*.md", "NOTICE", ".codex-plugin/*.json", ".agents/**/*.md", "skills/**/*.md", "docs/**/*.md", "scripts/*.py"]:
        paths.extend(ROOT.glob(pattern))
    return sorted({path for path in paths if path.is_file()})


def check_banned_tokens(failures: list[str]) -> None:
    for path in iter_text_files():
        relative = str(path.relative_to(ROOT))
        if relative == "scripts/validate_codex_port.py":
            continue
        text = read(path)
        lower_text = text.lower()
        for token in BANNED_ACTIVE_TOKENS:
            if token.lower() in lower_text and relative not in ATTRIBUTION_ALLOWED:
                fail(failures, f"Removed runtime-specific token found in {relative}: {token}")


def check_plugin_manifest(failures: list[str]) -> None:
    path = ROOT / ".codex-plugin" / "plugin.json"
    if not path.exists():
        return
    try:
        data = json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(failures, f"Invalid plugin.json: {exc}")
        return

    for key in ["name", "version", "description", "skills"]:
        if not data.get(key):
            fail(failures, f"plugin.json missing {key}")
    if data.get("skills") != "./skills/":
        fail(failures, "plugin.json skills must be ./skills/")


def check_marketplace(failures: list[str]) -> None:
    path = ROOT / ".agents" / "plugins" / "marketplace.json"
    if not path.exists():
        return
    try:
        data = json.loads(read(path))
    except json.JSONDecodeError as exc:
        fail(failures, f"Invalid marketplace.json: {exc}")
        return

    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail(failures, "marketplace.json must contain plugins[]")
        return
    entry = plugins[0]
    if entry.get("name") != "codex-meta-harness":
        fail(failures, "marketplace plugin name must be codex-meta-harness")
    source = entry.get("source") or {}
    if source.get("path") != "./":
        fail(failures, "marketplace source.path must be ./ for this single-plugin repository")


def iter_relative_files(base: Path) -> set[Path]:
    if not base.exists():
        return set()
    return {
        path.relative_to(base)
        for path in base.rglob("*")
        if path.is_file()
    }


def check_packaged_skill_mirror(failures: list[str]) -> None:
    canonical = ROOT / ".agents" / "skills" / "harness"
    packaged = ROOT / "skills" / "harness"

    canonical_files = iter_relative_files(canonical)
    packaged_files = iter_relative_files(packaged)

    for relative in sorted(canonical_files - packaged_files):
        fail(failures, f"Packaged skill mirror missing file: {relative}")
    for relative in sorted(packaged_files - canonical_files):
        fail(failures, f"Packaged skill mirror has extra file: {relative}")
    for relative in sorted(canonical_files & packaged_files):
        if (canonical / relative).read_bytes() != (packaged / relative).read_bytes():
            fail(failures, f"Packaged skill mirror differs: {relative}")


def iter_local_links(text: str) -> list[str]:
    links: list[str] = []
    markdown = r"!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)"
    html = r"""(?:href|src)=["']([^"']+)["']"""
    for match in re.finditer(markdown, text):
        target = match.group(1) or match.group(2)
        if target:
            links.append(target.strip())
    for match in re.finditer(html, text):
        links.append(match.group(1).strip())
    return links


def is_local_link(target: str) -> bool:
    return not (
        target.startswith("#")
        or "://" in target
        or target.startswith("mailto:")
        or target.startswith("data:")
    )


def check_links(failures: list[str]) -> None:
    for path in iter_text_files():
        if path.suffix not in {".md", ".json"} and path.name != "README.md":
            continue
        text = read(path)
        for target in iter_local_links(text):
            if not is_local_link(target):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            resolved = (path.parent / clean).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(failures, f"Local link escapes repo in {path.relative_to(ROOT)}: {target}")
                continue
            if not resolved.exists():
                fail(failures, f"Broken local link in {path.relative_to(ROOT)}: {target}")


def main() -> int:
    failures: list[str] = []
    check_required_files(failures)
    check_packaged_skill_mirror(failures)
    parse_frontmatter(ROOT / ".agents" / "skills" / "harness" / "SKILL.md", failures)
    parse_frontmatter(ROOT / "skills" / "harness" / "SKILL.md", failures)
    check_plugin_manifest(failures)
    check_marketplace(failures)
    check_banned_tokens(failures)
    check_links(failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1

    print("Codex port validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
