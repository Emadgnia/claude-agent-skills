---
name: social-brand-content-engine
description: Generate professional, platform-specific social content and related image prompts aligned to a consistent personal or company brand voice. Use when users request LinkedIn/X/Instagram copy, campaign content packs, CTA tuning, or prompt-ready creative briefs for image generation.
---

# Social Brand Content Engine

Use this skill to produce conversion-aware social output with brand consistency.

## Workflow

1. Capture audience, platform, objective, and offer.
2. Apply platform formatting constraints.
3. Produce caption variants with clear CTA.
4. Produce matching image prompts.
5. Run final quality pass for tone and specificity.

Use [scripts/caption_pack.py](scripts/caption_pack.py) to create baseline platform variants.

## Content Rules

- Lead with the user problem or value proposition.
- Keep one primary CTA per post.
- Avoid generic hashtags; use specific topical tags.
- Keep tone professional and concrete.

## Output Bundle

- short caption
- long caption
- CTA line
- hashtag set
- image prompt aligned with caption angle

## References

- [references/platform-voice.md](references/platform-voice.md)
- [references/image-prompt-structure.md](references/image-prompt-structure.md)
