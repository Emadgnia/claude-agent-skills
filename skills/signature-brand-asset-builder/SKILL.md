---
name: signature-brand-asset-builder
description: Build polished email signature assets and related brand prompts from profile/company inputs. Use when users request signature design, contact card formatting, icon/link cleanup, or matching prompt text for generated brand imagery.
---

# Signature Brand Asset Builder

Use this skill for consistent signature and micro-brand asset generation.

## Workflow

1. Collect required identity fields and approved links.
2. Normalize title, contact lines, and URL formatting.
3. Generate HTML/plain-text signature variants.
4. Generate companion image prompt for avatar/banner/logo style.
5. Validate readability and mobile compatibility.

Use [scripts/signature_template.py](scripts/signature_template.py) for deterministic HTML scaffolding.

## Required Inputs

- full name
- role/title
- company
- primary contact channels
- website and social link(s)
- brand color preference (optional)

## Output Package

- HTML signature
- plain text fallback
- image prompt for matching visual style

## References

- [references/signature-spec.md](references/signature-spec.md)
- [references/asset-prompt-guide.md](references/asset-prompt-guide.md)
