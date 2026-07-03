# Vocal help center

Customer-facing support docs for [Vocal](https://vocal.solutions), served at **support.vocal.solutions** via Mintlify.

## How it works

- Every page is an `.mdx` file; navigation and branding live in `docs.json`.
- Pushing to `main` deploys to production automatically (Mintlify GitHub App).
- Non-engineers can edit through the [Mintlify web editor](https://app.mintlify.com) — no git required.

## Local preview

```bash
npm i -g mint
mint dev          # http://localhost:3000
```

## Structure

```
index.mdx              — help center landing page
getting-started/       — quickstart + core concepts
numbers/               — buying, porting, SMS registration
agent/                 — behavior, voice, knowledge, workflow
calls/                 — call flows, ring groups
messaging/             — texting
campaigns/             — outbound campaigns
integrations/          — live vs building states
apps/                  — desktop app
billing/               — plans & pricing
help/                  — FAQ
```

## Rules

See `AGENTS.md` for terminology, style, and content boundaries. Two that matter most:

1. **Prices** in `billing/plans.mdx` mirror `SelfServe/convex/billingCatalog.ts` — verify before editing.
2. **Integrations** are documented honestly as Live or Building — never claim unbuilt as live.
