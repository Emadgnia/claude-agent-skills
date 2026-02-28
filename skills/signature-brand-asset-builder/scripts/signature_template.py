#!/usr/bin/env python3
"""Generate simple HTML email signature from key profile fields."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate email signature HTML")
    parser.add_argument("--name", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--company", required=True)
    parser.add_argument("--email", required=True)
    parser.add_argument("--phone", default="")
    parser.add_argument("--website", default="")
    parser.add_argument("--linkedin", default="")
    args = parser.parse_args()

    lines = [
        f"<strong>{args.name}</strong><br>",
        f"{args.title} | {args.company}<br>",
        f"<a href=\"mailto:{args.email}\">{args.email}</a><br>",
    ]
    if args.phone:
        lines.append(f"{args.phone}<br>")
    if args.website:
        lines.append(f"<a href=\"{args.website}\">{args.website}</a><br>")
    if args.linkedin:
        lines.append(f"<a href=\"{args.linkedin}\">LinkedIn</a><br>")

    print("<div style=\"font-family:Arial,sans-serif;font-size:14px;line-height:1.4;\">")
    for line in lines:
        print(f"  {line}")
    print("</div>")


if __name__ == "__main__":
    main()
