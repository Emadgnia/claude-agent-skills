#!/usr/bin/env python3
"""Generate Obsidian daily or weekly note scaffolds."""

from __future__ import annotations

import argparse
from datetime import date, datetime, timedelta


def daily_markdown(target: date) -> str:
    weekday = target.strftime("%A")
    yesterday = target - timedelta(days=1)
    iso_year, iso_week, _ = target.isocalendar()
    return f"""# {target.isoformat()} ({weekday})

## Focus
- 

## Work Tasks
- [ ]

## Personal Tasks
- [ ]

## Schedule
- 09:00-
- 11:00-
- 14:00-

## Notes
- 

## Carry Over
- [ ]

## Links
- Yesterday: [[{yesterday.isoformat()}]]
- Weekly: [[Week {iso_week:02d} {iso_year}]]
"""


def weekly_markdown(target: date) -> str:
    # Monday-based ISO week
    start = target - timedelta(days=target.weekday())
    end = start + timedelta(days=6)
    iso_year, iso_week, _ = target.isocalendar()
    monday = start.isoformat()
    friday = (start + timedelta(days=4)).isoformat()
    return f"""# Week {iso_week:02d} ({start.isoformat()} - {end.isoformat()})

## Weekly Goals
- [ ]

## Work Priorities
- [ ]

## Personal Priorities
- [ ]

## Wins
- 

## Risks
- 

## Carry Over to Next Week
- [ ]

## Links
- Monday: [[{monday}]]
- Friday: [[{friday}]]
"""


def parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Obsidian note markdown")
    parser.add_argument("mode", choices=["daily", "weekly"], help="Note type")
    parser.add_argument("--date", dest="date_str", help="Target date (YYYY-MM-DD). Defaults to today")
    args = parser.parse_args()

    target = parse_date(args.date_str) if args.date_str else date.today()

    if args.mode == "daily":
        print(daily_markdown(target).rstrip())
    else:
        print(weekly_markdown(target).rstrip())


if __name__ == "__main__":
    main()
