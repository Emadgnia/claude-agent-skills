#!/usr/bin/env python3
"""Rank PR rows from CSV by risk and dependency weighting."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass


@dataclass
class Item:
    id: str
    title: str
    reliability_risk: int
    user_impact: int
    dependency_impact: int
    rollback_complexity: int
    test_confidence: int

    @property
    def score(self) -> int:
        # Higher confidence lowers urgency.
        return (
            self.reliability_risk
            + self.user_impact
            + self.dependency_impact
            + self.rollback_complexity
            + max(0, 10 - self.test_confidence)
        )


def parse_int(value: str) -> int:
    n = int(value)
    if not 0 <= n <= 10:
        raise ValueError("scores must be 0-10")
    return n


def main() -> None:
    parser = argparse.ArgumentParser(description="Rank PRs by risk-aware priority")
    parser.add_argument("csv_path", help="Input CSV with scoring columns")
    args = parser.parse_args()

    items: list[Item] = []
    with open(args.csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = [
            "id",
            "title",
            "reliability_risk",
            "user_impact",
            "dependency_impact",
            "rollback_complexity",
            "test_confidence",
        ]
        for col in required:
            if col not in reader.fieldnames:
                raise SystemExit(f"missing column: {col}")

        for row in reader:
            items.append(
                Item(
                    id=row["id"],
                    title=row["title"],
                    reliability_risk=parse_int(row["reliability_risk"]),
                    user_impact=parse_int(row["user_impact"]),
                    dependency_impact=parse_int(row["dependency_impact"]),
                    rollback_complexity=parse_int(row["rollback_complexity"]),
                    test_confidence=parse_int(row["test_confidence"]),
                )
            )

    ordered = sorted(items, key=lambda x: x.score, reverse=True)
    print("priority,score,id,title")
    for i, item in enumerate(ordered, start=1):
        print(f"{i},{item.score},{item.id},{item.title}")


if __name__ == "__main__":
    main()
