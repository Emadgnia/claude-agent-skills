#!/usr/bin/env python3
"""Generate a markdown migration checklist for Supabase to Firebase projects."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate migration checklist")
    parser.add_argument("--project", default="Project", help="Project name")
    args = parser.parse_args()

    print(f"# {args.project}: Supabase -> Firebase Migration Checklist")
    print()
    print("## Discovery")
    print("- [ ] Inventory Supabase auth/data/storage/function dependencies")
    print("- [ ] Identify Firebase replacements and gaps")
    print()
    print("## Data and Auth Parity")
    print("- [ ] Data model mapping validated")
    print("- [ ] Auth flows validated")
    print("- [ ] Access policy parity validated")
    print()
    print("## Cutover")
    print("- [ ] Backups verified")
    print("- [ ] Final sync plan approved")
    print("- [ ] Smoke checks defined")
    print("- [ ] Rollback trigger documented")
    print()
    print("## Post Cutover")
    print("- [ ] Error and latency monitoring stable")
    print("- [ ] Legacy endpoints disabled in controlled sequence")


if __name__ == "__main__":
    main()
