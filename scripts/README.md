# CRM walkthrough renders

Recorded with Recordly on October 7, 2026, using fictional data in Vocal's local CRM preview. No customer account, phone call, or message was used. Captions and trims are rendered locally with ffmpeg and Pillow.

| Clip | Length | Guide |
| --- | --- | --- |
| `today` | 19 seconds | CRM → Start here |
| `callback` | 25.4 seconds | CRM → Follow-ups |
| `manager` | 18 seconds | CRM → Access and stopping contact |

The Manager preview represents CRM Owner/Admin access. Ordinary group management does not grant those tools. These clips demonstrate the shared Today/Replied, callback, and Team View as interactions, not every feature of the older fixture preview.

## Re-render this capture

Requires Python with Pillow, ffmpeg with libx264, and Inter. From this repository:

```sh
python3 scripts/render-crm-videos.py \
  --recording "$HOME/Library/Application Support/Recordly/recordings/recording-1791359950444.mp4" \
  --background ../SelfServe/public/images/brand/social-meadow.webp \
  --font "$HOME/Library/Fonts/Inter-Variable.ttf"
```

The saved editing project is `~/Library/Application Support/Recordly/recordings/Projects/Vocal CRM support walkthroughs.recordly`. Raw recordings stay outside Git. The script's cut times and 2648 × 1880 source crop belong to this capture; adjust them when recording again.

Outputs are MP4, JPG poster, and VTT under `videos/crm/`. MP4s include visible captions, a small Example data label, no audio, and the existing Vocal meadow artwork outside the product viewport. The crop removes Safari chrome and Recordly's capture HUD. The three MP4s together are under 2 MiB.

Guides use native video controls without autoplay. Captions are burned into the video and the steps are also written in the guide. The current Mintlify renderer strips nested `track` tags; VTT files remain available for reuse in other players.

## Record another take

Start SelfServe's dev server and open `/preview/leads/leads`. The floating Preview controls switch between Recruiter and Manager, reset fictional data, and hide for recording. Restore hidden controls with Option/Alt+Shift+P or Profile → Leads preview → Show preview controls. Switching roles preserves edits; Reset restores the fixture data and keeps the current role. Role changes and Reset are disabled while a simulated call or its wrap-up is active.

The `app/preview/` tree is intentionally ignored by SelfServe Git and unavailable in production. Keep changes there local unless deliberately promoting the preview later.
