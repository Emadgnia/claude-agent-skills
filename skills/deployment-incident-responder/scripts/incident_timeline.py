#!/usr/bin/env python3
"""Create a compact timeline from timestamped log lines."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

TIME_RE = re.compile(r"\b(\d{2}:\d{2}:\d{2}|\d{4}-\d{2}-\d{2}[T ][0-9:.+-Z]+)\b")


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract timeline entries from logs")
    parser.add_argument("log_file", help="Path to log file")
    args = parser.parse_args()

    path = Path(args.log_file)
    if not path.exists():
        raise SystemExit(f"file not found: {path}")

    print("# Incident Timeline")
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = TIME_RE.search(line)
            if m:
                print(f"- {m.group(1)} | {line.strip()[:220]}")


if __name__ == "__main__":
    main()
