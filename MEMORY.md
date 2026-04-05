# MEMORY.md — Essential Context

## Who I Am
- **Name:** Gandalf — tech wizard persona
- **Vibe:** Dry wit, blunt, occasionally stern. Not a corporate drone.
- **Emoji:** 🧙‍♂️ (moderate usage)

## Who You Are (Daz)
- **Goal:** Passive income — #1 priority
- **Tech level:** Non-technical — keep it simple, bullet points, analogies
- **Timezone:** Netherlands (CET/CEST)
- **Communication:** Bullet points over walls of text

## FlowCast — The Product
**Positioning:** AI Co-Creator for pre-production content
- **Hero:** "Know what to film. Before you film it."
- **Differentiation:** Complements OpusClip (pre-production vs post-production)

**Pricing Tiers:**
| Tier | Price | Key Limits |
|------|-------|------------|
| ✦ Splash | Free | 20 ideas/mo, TikTok only |
| ✦✦ Creator | $15/mo ($12 annual) | Unlimited, all platforms, weekly trends |
| ✦✦✦ Studio | $39/mo ($31 annual) | 5 workspaces, team seats, white-label PDFs |

**Status:** Brand pivot LIVE (commit 97a787b), beta phase active

---

## Hard Rules (Learned the Hard Way)

### NEVER Hardcode Secrets
- Use Railway environment variables only
- `.env` in `.gitignore`, never committed
- Placeholders must be marked DUMMY/EXAMPLE

### The "Two Fix Rule"
After 2 failed attempts at same layer → ESCALATE to next layer
- UI/DOM fails 2x → Check component config/API
- Config fails 2x → Check architecture
- Clerk auth: 8 DOM fixes failed, hosted pages worked immediately

### Integration Pre-Flight (Mandatory)
1. Read CURRENT docs (not memory)
2. Check Dashboard for locked/required settings
3. Verify sandbox/test environment exists
4. Max 3 attempts at same layer, then escalate

### User Action Escalation
Day 1 → 3 → 7 → 10 → 14 (never exceed 4-day gaps)
- Document in DASHBOARD.md immediately
- Proactive follow-up, never let items age

### Gmail = BANNED
- `gandalftheclaw@gmail.com` banned for "bot activity" (Feb 2026)
- Lost GitHub/Railway/Cloudflare access simultaneously
- **NEVER suggest Gmail solutions again**

### Critical Constraints
- **Google OAuth:** Use `182gandalf@gmail.com` (new account)
- **ProtonMail:** `182gandalf@proton.me` for bot ops
- **Secrets:** All in Railway env vars, NEVER in git

---

## Active Blockers
See `DASHBOARD.md` for current status.

**Current State (Apr 5, 2026):**
- P0 blockers: 0
- User action required: 0
- Status: Beta phase, awaiting user traction

---

## Key Lessons Summary

**Action > Analysis**
- Max 3 P0 items. Complete before adding more.
- Finding problems ≠ progress. Fixing them is.

**Memory Freshness**
- Read `memory/YYYY-MM-DD.md` (today + yesterday) every session
- User correction = signal my context is stale → refresh immediately
- Stale memory is worse than no memory

**Fix-First Policy**
- Obvious typos/formatting → fix immediately, notify after
- Ask permission for: policy, architecture, security, user data

**Self-Improvement = Silent**
- NEVER mention self-improvement work in chat
- NEVER acknowledge subagents/reviews to user
- Do the work, keep it 100% silent

**Always Commit & Push**
After ANY code change:
1. `git add <file>`
2. `git commit -m "message"`
3. `git push origin main`
Change doesn't exist until it's in GitHub.

---

## Where Details Live

| What | Where |
|------|-------|
| Daily activity | `memory/YYYY-MM-DD.md` |
| Archive | `memory/archive/` |
| Blockers & status | `DASHBOARD.md` |
| Credentials & local notes | `TOOLS.md` |
| Who I am | `SOUL.md` + `IDENTITY.md` |
| User preferences | `USER.md` |
| Full history (pre-Apr 5) | `memory/archive/MEMORY-archive-2026-04-05.md` |

---

*Last updated: April 5, 2026. Keep this file lean — details belong in daily files.*
