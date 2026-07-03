# Vocal help center — project instructions

> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

## About this project

- This is Vocal's customer-facing help center (support.vocal.solutions), built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter; configuration lives in `docs.json`
- Pushing to `main` deploys to production automatically
- The product codebase lives in a separate repo (`SelfServe`) — this repo is content only

## Terminology

- **workspace** — not "organization" or "company"
- **member** — not "user" or "seat" (plans are billed per member)
- **AI agent** (or just "agent") — the AI that answers calls
- **call flow** — number-level routing (what happens when a call comes in)
- **workflow** — the agent's conversation flow (stages, tools, outcomes). Never mix these two up.
- **number** — not "phone line"
- **connected call** — an answered call; the unit AI usage is billed in

## Style preferences

- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references
- Write for a small-business owner, not a developer. No jargon.

## Content boundaries

- **Never claim an unbuilt integration is live.** Integrations have two honest states: "Live" and "Building". Check with the team before moving one to Live.
- Never name internal vendors (Twilio, ElevenLabs, LiveKit, Deepgram, model providers) in user-facing docs. Describe capabilities, not suppliers.
- Prices in `billing/plans.mdx` mirror `SelfServe/convex/billingCatalog.ts` (the pricing source of truth). Verify against it before editing any price.
- Don't document: the `/admin` area, dev unlock codes, internal tooling, or unreleased features.
- Support contact is team@vocal.solutions.
