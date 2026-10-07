# Vocal help center — project instructions

> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

## About this project

- This is Vocal's customer-facing help center (support.vocal.solutions), built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter; configuration lives in `docs.json`
- Pushing to `main` deploys to production automatically
- The product codebase lives in a separate repo (`SelfServe`) — this repo is content only
- The app deep-links into this site through `SelfServe/lib/help-links.ts`. Never rename or delete a page in that map without adding a redirect in `docs.json`.

## What Vocal is

Vocal is an AI-native business phone that connects information scattered across conversations into a shared understanding of the business. People make calls and send texts; AI connects what's said so the team stays informed without chasing updates. The canonical wording lives in the product repo's root `PRODUCT.md` — use it, don't invent new slogans.

- The first customers are logistics teams — recruiters, dispatchers, and their managers — moving off RingCentral. Use their situations in examples (a recruiter texting a driver applicant, a dispatcher confirming a load). Don't write for dentists, plumbers, or "small-business owners" in general.
- **AI agents, Lola, and Campaigns are hidden from the help center for now (Bek, 2026-10-07).** Their pages (`agent/`, `campaigns/`) stay in the repo but are excluded by `.mintignore`, and `docs.json` redirects their URLs to the home page. Don't link to them or describe AI answering, AI calling, AI minutes, or agent settings on any other page until Bek turns the section back on. A new number rings its people, then goes to voicemail.

## Terminology

- **workspace** — not "organization" or "company"
- **member** — a person in the workspace (plans are billed per member). Roles are **Owner**, **Admin**, and **Member**. A **manager** is someone who manages a group, not a role.
- **number** — not "phone line". The people on a number are its **Users** (the number's Users tab); they're who it rings.
- **Inbox** — where calls, texts (**Chats**), and **Tasks** live. **Messages** in the app is internal team chat — never use "Messages" for customer texts.
- **Iris** — the assistant behind **Ask anything**
- **call flow** — number-level routing (what happens when a call comes in)
- **AI agent** (or "agent") — an AI that answers or makes calls when you turn it on. **Lola** is the built-in AI you can put on a number.
- **steps** — an agent's conversation plan (the **Steps** section of the agent editor). Say "steps", not "workflow", for agents. CRM is different: its Owner/Admin side calls the team sequence **Workflow**, while recruiters' screens say **Follow-up plan**; match whichever screen you're describing. Never mix up call flows and steps.
- **AI minutes** — the billing unit for AI calls (not "credits" or "connected calls")

## Style

- Plain and concrete. Active voice, second person ("you"), contractions.
- One idea per sentence, but vary sentence length; don't stack three short declaratives.
- Sentence case for headings. Bold for UI labels exactly as they appear: click **Settings**.
- Code formatting for file names, paths, and code.
- No hype words (seamless, powerful, effortless, supercharge, unlock). No em-dash chains — one per page at most.
- Say what a feature does and where it lives. Don't pad with benefits paragraphs.

## Content boundaries

- **Only document what a customer can use today.** Check the code before claiming a button, path, or default exists. A UI that saves a setting isn't proof the setting works — find the runtime code that reads it.
- **Prices live in `billing/plans.mdx` only** (plus registration fees on `numbers/sms-registration.mdx`). Other pages link there. Seat and number prices mirror `SelfServe/convex/billingCatalog.ts`. AI calls (20¢ per AI minute) and texts (1¢ per SMS segment) were set by Bek on 2026-09-30.
- **Never claim an unbuilt integration is live.** Document only integrations a customer can connect today; don't list "coming soon" ones.
- Never name internal vendors (Twilio, Telnyx, LiveKit, Deepgram, Fish Audio, model providers) in user-facing docs. Describe capabilities, not suppliers. RingCentral is fine where the app names it (number transfers).
- **Describe what Vocal does, not what it doesn't (Bek, 2026-10-07).** Don't add "doesn't support", "not supported yet", or "can't … yet" lines; give the working path instead. The 911 notice lives only on `help/emergency-calls` and its FAQ entry; don't repeat it as a banner on other pages.
- Don't document: the `/admin` area, dev unlock codes, internal tooling, staff-only settings, pilot-only apps (mobile), or hidden settings sections (Number pools, Ring groups, API & webhooks).
- Support contact is team@vocal.solutions.

## Design — Clear Signal

White and black, generous whitespace, Inter, black pill CTAs, and one restrained blue (`#1A6EFF`, `#3D85FF` in dark mode) for links and selection. The logo is the woven orb with the "Vocal" wordmark (`logo/`). The retired lime `#E5FF2D`, Geist, and the sound-wave mark must not come back. Full rules: `SelfServe/DESIGN.md`.
