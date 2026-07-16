# AGENTS.md — universal-audio-converter

Windows tool for the full SE audio workflow. Converts WAV/OGG/MP3/etc → WAV or XWM, edits audio visually, and generates `Audio.sbc` + `SoundBlock.sbc` files for SE mods. Distributed as a packaged `.exe` via GitHub Releases.

## What this is

Windows tool for the full SE audio workflow. Converts WAV/OGG/MP3/etc → WAV or XWM, edits audio visually, and generates `Audio.sbc` + `SoundBlock.sbc` files for SE mods. Distributed as a packaged `.exe` via GitHub Releases.

## Where work lives (RULE — non-negotiable)

**Every task on this repo is a ticket on the [Personal Projects board](https://github.com/users/Godimas101/projects/2).** YOU (the agent) create the ticket BEFORE touching anything. No exceptions for "small" work.

Concrete rules — same as everywhere:

- **Starting work?** Open a ticket, add to the board, set Status = **In Progress**, then start.
- **Have an idea for later?** Ticket in **Backlog**. Not in memory, not in a README, not in NOTES.md.
- **Need Chris to check something before closing?** Move to **In QA** and comment what he needs to look at. Do NOT set to Done — that's Chris's call after review.
- **Finished + verified yourself?** Close the ticket with a closing summary (what you did / problems + solutions / anything NOT done).
- **Same-session micro-work?** Open + close in the same session — but the ticket exists.
- **Older than 30 days in Done?** The weekly cron moves it to Archived. The closed ticket persists.

Ticket body shape: see memory `[[feedback-ticket-body-shape]]` — What/Why → Acceptance → Related → Notes. Priority defaults to P2, Kind defaults to Feature.

## How to verify (before flagging In QA or closing)

- Test conversion round-trip (WAV → XWM → play in-game) with a real audio file.
- If touching the SBC generator: build a test mod with the generated SBC and load it in SE.
- Verify xWMAEncode fallback — tool must still convert to WAV even if `xWMAEncode.exe` isn't present.
- Test with mono AND stereo sources — SE Sound Blocks want mono, and the tool has a stereo→mono helper.

## MUST NOT

- Break the packaged `.exe`.
- Assume xWMAEncode is present — it's an optional dependency users provide from Mod SDK or DirectX SDK.
- Hardcode audio format assumptions in the SBC generator — users provide the source.

## Related

- Sibling tool: [`universal-image-converter`](https://github.com/Godimas101/universal-image-converter)
- Bundled by: [`space-engineers-modders-tool-kit`](https://github.com/Godimas101/space-engineers-modders-tool-kit)

---

*Part of Chris's `Godimas101` personal repos. Companion guide: `personal-docs/git-infrastructure.md` (private companion repo) covers the full infrastructure.*