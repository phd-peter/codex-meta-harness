#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILL_DIR = ROOT / ".agents" / "skills" / "harness"
PACKAGED_SKILL_DIR = ROOT / "skills" / "harness"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Sync the plugin-packaged Harness skill mirror from the canonical .agents copy."
    )
    parser.add_argument("--dry-run", action="store_true")
    return parser


def fail(message: str) -> int:
    print(f"ERROR: {message}", file=sys.stderr)
    return 1


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def sync(source: Path, destination: Path) -> None:
    if not source.exists() or not source.is_dir():
        raise FileNotFoundError(f"Missing canonical source skill: {source}")
    if source.resolve() == destination.resolve():
        raise ValueError("Source and destination must be different paths")

    destination.parent.mkdir(parents=True, exist_ok=True)
    remove_path(destination)
    shutil.copytree(source, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))


def main() -> int:
    args = build_parser().parse_args()

    print(f"Canonical source: {SOURCE_SKILL_DIR}")
    print(f"Packaged mirror: {PACKAGED_SKILL_DIR}")

    if args.dry_run:
        print("Dry run only; no files changed.")
        return 0

    try:
        sync(SOURCE_SKILL_DIR, PACKAGED_SKILL_DIR)
    except (FileNotFoundError, ValueError) as exc:
        return fail(str(exc))

    print("Synced packaged Harness skill mirror.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
