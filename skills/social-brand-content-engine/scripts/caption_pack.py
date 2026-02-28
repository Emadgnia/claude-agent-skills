#!/usr/bin/env python3
"""Generate baseline caption variants for common social platforms."""

from __future__ import annotations

import argparse


def build(platform: str, topic: str, benefit: str, cta: str) -> str:
    if platform == "linkedin":
        return (
            f"{topic}: {benefit}.\n\n"
            f"What teams miss is execution clarity, not ideas.\n"
            f"{cta}\n\n"
            "#leadership #product #execution"
        )
    if platform == "x":
        return f"{topic}: {benefit}. {cta} #buildinpublic #product"
    if platform == "instagram":
        return (
            f"{topic}\n\n"
            f"{benefit}\n\n"
            f"{cta}\n"
            "#creator #strategy #growth"
        )
    raise ValueError("unsupported platform")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create social caption pack")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--benefit", required=True)
    parser.add_argument("--cta", required=True)
    args = parser.parse_args()

    for p in ("linkedin", "x", "instagram"):
        print(f"## {p}")
        print(build(p, args.topic, args.benefit, args.cta))
        print()


if __name__ == "__main__":
    main()
