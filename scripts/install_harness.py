#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILL_DIR = ROOT / ".agents" / "skills" / "harness"
SCOPES = ("project", "user")
MODES = ("copy", "symlink")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install Codex Meta Harness into a repo-local or user-level .agents/skills directory."
    )
    parser.add_argument("--scope", choices=SCOPES, required=True)
    parser.add_argument("--target", help="Project root for --scope project")
    parser.add_argument("--mode", choices=MODES, default="copy")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force", action="store_true")
    return parser


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def resolve_root(scope: str, target: str | None) -> Path:
    if scope == "project":
        if not target:
            raise SystemExit(fail("--target is required when --scope project"))
        root = Path(target).expanduser().resolve()
        if not root.exists() or not root.is_dir():
            raise SystemExit(fail(f"Project target is not a directory: {root}"))
        return root

    if target:
        raise SystemExit(fail("--target is only valid when --scope project"))
    return Path.home().resolve()


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def install(source: Path, destination: Path, mode: str) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if mode == "copy":
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        return
    destination.symlink_to(source, target_is_directory=True)


def main() -> int:
    if not SOURCE_SKILL_DIR.exists():
        return fail(f"Missing canonical source skill: {SOURCE_SKILL_DIR}")

    args = build_parser().parse_args()
    root = resolve_root(args.scope, args.target)
    destination = root / ".agents" / "skills" / "harness"

    print(f"Install source: {SOURCE_SKILL_DIR}")
    print(f"Install target: {destination}")
    print(f"Mode: {args.mode}")

    if args.dry_run:
        print("Dry run only; no files changed.")
        return 0

    if destination.exists() or destination.is_symlink():
        if not args.force:
            return fail(f"Destination already exists; rerun with --force: {destination}")
        remove_path(destination)

    install(SOURCE_SKILL_DIR, destination, args.mode)
    print("Installed Codex Meta Harness skill.")
    print("AGENTS.md remains target-repo owned. Create or revise it intentionally when needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
