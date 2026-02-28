#!/usr/bin/env python3
"""Compute overlap windows between two simple schedules."""

from __future__ import annotations

import argparse
from datetime import datetime


FMT = "%Y-%m-%d %H:%M"


def parse_window(raw: str) -> tuple[datetime, datetime]:
    start_raw, end_raw = raw.split(",", 1)
    start = datetime.strptime(start_raw.strip(), FMT)
    end = datetime.strptime(end_raw.strip(), FMT)
    if end <= start:
        raise ValueError("end must be after start")
    return start, end


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge two time windows")
    parser.add_argument("window_a", help="'YYYY-MM-DD HH:MM,YYYY-MM-DD HH:MM'")
    parser.add_argument("window_b", help="'YYYY-MM-DD HH:MM,YYYY-MM-DD HH:MM'")
    args = parser.parse_args()

    a_start, a_end = parse_window(args.window_a)
    b_start, b_end = parse_window(args.window_b)

    start = max(a_start, b_start)
    end = min(a_end, b_end)

    if end <= start:
        print("no-overlap")
        return

    print(f"overlap,{start.strftime(FMT)},{end.strftime(FMT)}")


if __name__ == "__main__":
    main()
