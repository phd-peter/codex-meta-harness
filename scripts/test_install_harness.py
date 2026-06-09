#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER_PATH = ROOT / "scripts" / "install_harness.py"
SYNCER_PATH = ROOT / "scripts" / "sync_packaged_skill.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Could not load {name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_exists(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"Expected path to exist: {path}")


def main() -> int:
    installer = load_module("install_harness", INSTALLER_PATH)
    syncer = load_module("sync_packaged_skill", SYNCER_PATH)
    source = ROOT / ".agents" / "skills" / "harness"
    assert_exists(source / "SKILL.md")

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp)
        destination = target / ".agents" / "skills" / "harness"
        installer.install(source, destination, "copy")
        assert_exists(destination / "SKILL.md")
        assert_exists(destination / "references" / "agent-design-patterns.md")
        shutil.rmtree(destination)
        installer.install(source, destination, "symlink")
        assert destination.is_symlink(), "Expected symlink install"

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp)
        source_copy = target / ".agents" / "skills" / "harness"
        destination = target / "skills" / "harness"
        shutil.copytree(source, source_copy)
        destination.mkdir(parents=True)
        (destination / "stale.md").write_text("stale", encoding="utf-8")
        syncer.sync(source_copy, destination)
        assert_exists(destination / "SKILL.md")
        assert_exists(destination / "references" / "agent-design-patterns.md")
        if (destination / "stale.md").exists():
            raise AssertionError("Expected sync to remove stale packaged files")

    print("install_harness smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
