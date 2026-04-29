from __future__ import annotations

import argparse
from typing import Any


def build_cli() -> argparse.ArgumentParser:
    """Return the public command-line interface for the audit tool."""
    raise NotImplementedError("Public minimal interface only.")


def audit_user(user_name: str, *, profile: str = "DEFAULT", config_file: str = "~/.oci/config") -> dict[str, Any]:
    """Run a user audit and return a structured report."""
    raise NotImplementedError("Public minimal interface only.")


def render_report(report: dict[str, Any], *, as_json: bool = False) -> str:
    """Convert a report into text or JSON output."""
    raise NotImplementedError("Public minimal interface only.")
