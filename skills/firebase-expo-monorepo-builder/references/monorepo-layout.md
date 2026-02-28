# Monorepo Layout

Recommended structure:

- `apps/app` for Expo application
- `apps/functions` for Firebase functions
- `packages/shared` for shared types/utilities
- workspace config at repo root

Principles:

- Keep shared code platform-neutral.
- Avoid importing server-only modules into app runtime.
- Keep environment boundaries explicit (`EXPO_PUBLIC_` vs server secrets).
