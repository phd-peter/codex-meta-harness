#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import shutil
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INSTALLER_PATH = ROOT / "scripts" / "install_harness.py"


def load_installer():
    spec = importlib.util.spec_from_file_location("install_harness", INSTALLER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load installer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def assert_exists(path: Path) -> None:
    if not path.exists():
        raise AssertionError(f"Expected path to exist: {path}")


def main() -> int:
    installer = load_installer()
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

    print("install_harness smoke test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
