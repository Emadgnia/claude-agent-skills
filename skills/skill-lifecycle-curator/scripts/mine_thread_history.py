#!/usr/bin/env python3
"""Summarize Codex session JSONL history into intent clusters for skill design."""

from __future__ import annotations

import argparse
import glob
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

REQUEST_MARKER_RE = re.compile(r"##\s*my request\s*for\s*codex\s*:\s*", re.IGNORECASE)

SECRET_PATTERNS = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{12,}\b"),
    re.compile(r"\bkey_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b"),
    re.compile(r"\b[0-9a-f]{32,}\b", re.IGNORECASE),
]

CONFIG_VALUE_PATTERNS = [
    re.compile(
        r"(?i)\b(apiKey|authDomain|projectId|storageBucket|messagingSenderId|appId|measurementId|databaseURL)\b\s*[:=]\s*(\"[^\"]*\"|'[^']*'|[^,\s]+)"
    ),
    re.compile(
        r"\b([A-Z][A-Z0-9_]*(?:KEY|TOKEN|SECRET|PASSWORD|PRIVATE|APP_ID|PROJECT_ID|AUTH_DOMAIN|STORAGE_BUCKET|MESSAGING_SENDER_ID)[A-Z0-9_]*)\b\s*[:=]\s*(\"[^\"]*\"|'[^']*'|[^,\s]+)"
    ),
]

CATEGORIES = {
    "plan-gating": [r"\bplan\b", r"roadmap", r"implement this plan", r"plan first", r"requirements?"],
    "debug-build-run": [r"\berror\b", r"failing", r"not working", r"build and run", r"run locally", r"fix"],
    "git-ship": [r"commit and push", r"\bpush\b", r"\bpr\b", r"merge", r"branch"],
    "deploy-release": [r"\bdeploy\b", r"vercel", r"firebase", r"testflight", r"app store", r"release"],
    "skills-management": [r"\bskill\b", r"skill\.md", r"install.*skill", r"create.*skill", r"extend the skill"],
    "obsidian-notes": [r"obsidian", r"daily", r"weekly", r"today file", r"carry over", r"vault"],
    "ui-design": [r"\bui\b", r"design", r"tailwind", r"landing page", r"sidebar", r"css"],
}

IGNORE_EXACT = {
    "yes",
    "ok",
    "done",
    "go",
    "approve",
    "approved",
    "next",
    "do it",
    "do",
    "?",
    "ready",
    "run it",
    "push it",
    "and push",
    "<turn_aborted>",
    "<image>",
}


@dataclass
class Request:
    text: str
    file: Path


@dataclass
class Summary:
    scanned_files: int
    request_files: int
    earliest: str
    latest: str
    total_requests: int
    classified_counts: Counter
    examples: dict[str, list[str]]


def extract_text(payload: dict) -> str:
    parts = []
    for item in payload.get("content", []):
        if item.get("type") in {"input_text", "output_text"} and item.get("text"):
            parts.append(item["text"])
    return "\n".join(parts).strip()


def extract_request(text: str) -> str:
    match = REQUEST_MARKER_RE.search(text)
    if match:
        return text[match.end() :].strip()
    return text.strip()


def sanitize(text: str) -> str:
    cleaned = text
    for pattern in SECRET_PATTERNS:
        cleaned = pattern.sub("[REDACTED]", cleaned)
    for pattern in CONFIG_VALUE_PATTERNS:
        cleaned = pattern.sub(lambda m: f"{m.group(1)}: [REDACTED]", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def iter_requests(files: Iterable[str]) -> list[Request]:
    requests: list[Request] = []
    for file_path in files:
        path = Path(file_path)
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if obj.get("type") != "response_item":
                    continue
                payload = obj.get("payload", {})
                if payload.get("role") != "user":
                    continue
                text = extract_text(payload)
                if not text:
                    continue
                low = text.lower().strip()
                if low.startswith("# agents.md instructions for "):
                    continue
                if low.startswith("<environment_context>"):
                    continue
                request_text = extract_request(text)
                if request_text:
                    requests.append(Request(text=request_text, file=path))
    return requests


def classify(requests: list[Request], scanned_files: int) -> Summary:
    classified_counts: Counter = Counter()
    examples: dict[str, list[str]] = defaultdict(list)

    for req in requests:
        raw = sanitize(req.text)
        low = raw.lower()
        if low in IGNORE_EXACT or len(low) <= 3:
            continue
        matched = False
        for category, patterns in CATEGORIES.items():
            if any(re.search(pattern, low) for pattern in patterns):
                classified_counts[category] += 1
                if len(examples[category]) < 5:
                    examples[category].append(raw[:220])
                matched = True
        if not matched:
            classified_counts["other"] += 1

    file_list = sorted({str(r.file) for r in requests})
    earliest = Path(file_list[0]).name if file_list else "n/a"
    latest = Path(file_list[-1]).name if file_list else "n/a"

    return Summary(
        scanned_files=scanned_files,
        request_files=len(file_list),
        earliest=earliest,
        latest=latest,
        total_requests=len(requests),
        classified_counts=classified_counts,
        examples=dict(examples),
    )


def to_markdown(summary: Summary, source_glob: str) -> str:
    lines = []
    lines.append("# Thread History Mining Report")
    lines.append("")
    lines.append(f"Generated: {datetime.now(timezone.utc).isoformat()}")
    lines.append(f"Source glob: `{source_glob}`")
    lines.append(f"Session files scanned: {summary.scanned_files}")
    lines.append(f"Session files with user requests: {summary.request_files}")
    lines.append(f"Earliest session file: `{summary.earliest}`")
    lines.append(f"Latest session file: `{summary.latest}`")
    lines.append(f"Total extracted user requests: {summary.total_requests}")
    lines.append("")
    lines.append("## Intent Counts")
    lines.append("")
    for category, count in summary.classified_counts.most_common():
        lines.append(f"- {category}: {count}")
    lines.append("")
    lines.append("## Sample Requests (Sanitized)")
    lines.append("")
    for category in sorted(summary.examples):
        lines.append(f"### {category}")
        for sample in summary.examples[category]:
            lines.append(f"- {sample}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Mine Codex JSONL session history for skill opportunities")
    parser.add_argument(
        "--sessions-glob",
        default="/Users/emad/.codex/sessions/**/*.jsonl",
        help="Glob for session JSONL files",
    )
    parser.add_argument("--output", help="Output markdown file path (default: stdout)")
    args = parser.parse_args()

    files = sorted(glob.glob(args.sessions_glob, recursive=True))
    requests = iter_requests(files)
    summary = classify(requests, scanned_files=len(files))
    report = to_markdown(summary, args.sessions_glob)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
    else:
        print(report)


if __name__ == "__main__":
    main()
