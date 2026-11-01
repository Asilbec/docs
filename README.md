# Vocal help center

Customer-facing help for [Vocal](https://vocal.solutions), live at **[support.vocal.solutions](https://support.vocal.solutions)**. It's a [Mintlify](https://mintlify.com) site: every page is an `.mdx` file in this repo, and pushing to `main` publishes it.

Before writing anything, read **`AGENTS.md`**. It covers the words we use, the writing style, and what never goes in the help center.

## Set up

You need:

- **Git** and write access to `github.com/asilbec/docs`. Ask Bek.
- **Node 22.** The version is pinned in `.node-version`. Mintlify's CLI refuses to run on Node 25 or newer.

Then:

```bash
git clone https://github.com/asilbec/docs.git vocal-docs
cd vocal-docs
npm i -g mint
mint dev --port 3344
```

Open http://localhost:3344. The page reloads as you save. Port 3000 works too, but the Vocal web app usually takes it.

If `mint dev` shows something stale, run `mint update`.

## Make a change

1. Branch off `main`: `git checkout -b <your-name>/<what-you-are-changing>`.
2. Edit pages, with the preview running next to you.
3. Check it: `mint validate` and `mint broken-links`.
4. Push the branch and open a pull request. Bek reviews it.
5. Merging to `main` publishes the site in about a minute.

Typo fixes can also go through the [Mintlify web editor](https://app.mintlify.com), with no git needed. It commits to this repo for you.

## Where things live

| What | Where |
| --- | --- |
| Pages | `.mdx` files. The path is the URL: `crm/calling.mdx` → `/crm/calling` |
| Sidebar, groups, page order | `navigation` in `docs.json` |
| Site name, theme, colors, logo, navbar buttons | the top of `docs.json` |
| Link previews (the card in Slack, iMessage, Telegram) | `thumbnails` in `docs.json` |
| CSS overrides | `style.css` |
| Images | `images/`. The logo and favicon are `images/mark-black.svg` and `mark-white.svg`. The old `logo/` folder isn't used. |
| Videos | `videos/`. How they're made is in `scripts/README.md` |
| Hidden for now | `agent/` and `campaigns/`, excluded by `.mintignore` |

Each page starts with frontmatter:

```yaml
---
title: "Import and manage lead lists"
sidebarTitle: "Import leads"     # optional shorter name for the sidebar
description: "One sentence: shows under the title and in search results."
icon: "file-import"              # a Font Awesome icon name
---
```

A new page shows up only after you add it to `navigation` in `docs.json`.

## Rules that break things

- **Don't rename or delete a page without a redirect.** The Vocal app links straight to pages through `SelfServe/lib/help-links.ts` in the main repo. If you move a page, add a `redirects` entry in `docs.json` from the old path to the new one.
- **Prices live only in `billing/plans.mdx`**, plus registration fees in `numbers/sms-registration.mdx`. They mirror `SelfServe/convex/billingCatalog.ts`, so check there before changing a number.
- **Only document what customers can use today.** See `AGENTS.md` for the details.

## Look and feel

- **Theme:** `"theme": "aspen"` in `docs.json`. Mintlify's themes are `mint`, `maple`, `palm`, `willow`, `linden`, `almond`, `aspen`, `sequoia` and `luma`. Change it with `mint dev` running to try one.
- **`style.css` depends on the theme.** It turns the **Start free** button into a black pill (white in dark mode) by targeting Aspen's page structure. If you switch themes, check that button in light and dark mode, and update the selectors if it went back to blue.
- **Link previews:** Mintlify draws a card for every page from its title, description and group. The `thumbnails` block sets the style: the `headline` layout, dark, with the group label in sky blue `#4A78A8`. While `mint dev` runs, any page's card is at `http://localhost:3344/_mintlify/og/<page>.png`, for example `/_mintlify/og/crm/calling.png`. It redraws when you save `docs.json`. To render one card to a file, run `mint og crm/calling`.
- **Colors:** `colors.primary` (`#1A6EFF`) is for links and selection only. Brand rules are in `AGENTS.md` and the main repo's `SelfServe/DESIGN.md`.
