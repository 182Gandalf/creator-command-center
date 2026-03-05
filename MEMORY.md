# Critical Context & Lessons Learned - Updated March 5, 2026 (12:00 UTC)

## March 5, 2026 — Daily Memory Review Summary
**Status:** Pattern validation complete, review cadence confirmed optimal, SEC-001 Day 10 reminder due tomorrow.

### Key Actions Completed
1. **Self-Improvement Review (02:03 UTC):** Automated 48-hour review validated weekly cadence, confirmed "Two Fix Rule" remains effective
2. **Security Posture:** A- maintained — no new exposures, SEC-001 tracking continues (Day 10 reminder due March 6)
3. **Review Cadence:** ✅ **FINAL VALIDATION** — 48-hour gap produced fresh insights without redundancy; weekly comprehensive + daily silent checks confirmed optimal

### Key Insights
- **Rest Day Value Confirmed:** March 4 (zero commits) was sustainable pacing after March 3's high velocity — not abandonment
- **"Two Fix Rule" Revalidated:** 8 DOM fixes failed, configuration-level fix worked (Clerk pattern)
- **No Activity ≠ Problem:** Natural work-rest cycles detected; only flag if >3 days inactive

### New Learning: The Rest Day Value
March 4 (zero commits) followed by March 5 review demonstrates the value of rest days in work cycles. No activity does not indicate abandonment — it indicates sustainable pacing. Application: Do not flag "no commits" days as concerning unless pattern persists >3 days.

---

## March 4, 2026 — Daily Memory Review Summary
**Status:** Memory system current, no new code activity today.

### Key Actions Completed
1. **Self-Improvement Review (02:03 UTC):** Automated review validated weekly cadence, confirmed "Two Fix Rule"
2. **Security Posture:** B+ maintained — no new exposures, SEC-001 tracking continues
3. **MEMORY.md Updated:** Added escalation path visualization, updated day counts

### Current State
- **SEC-001:** Day 10 reminder due March 6 (tomorrow)
- **Code Activity:** None since March 3 (rest day)
- **Memory Health:** ✅ All files current, daily logs active
- **Review Cadence:** ✅ Validated — weekly comprehensive + daily silent security checks optimal

---

# Critical Context & Lessons Learned - Updated March 3, 2026 (22:00 UTC)

## Current Status Snapshot
- **Active P0 Blockers:** 1 (SEC-001: TikTok secret rotation, 9 days old, Day 10 reminder DUE March 6, Day 14 final March 10)
- **Review Cadence:** Weekly comprehensive (Sundays) + daily silent security checks ✓ FINAL VALIDATION COMPLETE (Mar 5)
- **Last Significant Work:** Self-improvement review validated rest-day cycles and review cadence (March 5)
- **Today:** March 5, 2026 — daily review complete, MEMORY.md updated

## March 4, 2026 — Self-Improvement Review Insights

### Pattern Analysis Validated
**Review cadence confirmed optimal:** Weekly comprehensive reviews (Sundays) with daily silent security checks produces unique insights without redundancy.

### Key Finding: The "Two Fix Rule" Reconfirmed
When an issue resists 2+ fixes at the same abstraction layer, the problem exists at a **higher layer** (configuration, architecture, API). The Clerk auth issue validated this: 8 DOM fixes failed, configuration-level fix (hosted pages) worked immediately.

**Debugging Protocol Added:**
- UI/DOM issue + 2 fixes → Check component configuration/API
- Config issue + 2 fixes → Check architecture  
- Prevents wasted effort on symptoms vs root causes

### Security Posture: B+
| Check | Status |
|-------|--------|
| New hardcoded secrets | ✅ None |
| .env references | ✅ Clean |
| Memory file exposure | ✅ None |
| Git history | ⚠️ SEC-001 still exposed (historical) |

**SEC-001 Status:** 10 days old, Day 10 reminder due March 6 per escalation matrix.

### Code Velocity (March 3)
- 10 commits, 9 files modified
- 0 syntax errors introduced
- Quality maintained at high velocity

---

## March 4, 2026 — Clerk Auth Resolution & Lessons Learned

### What Happened
**The Problem:** Clerk double login window (modal + embedded form appearing simultaneously)
**Time Wasted:** 8+ code attempts over multiple hours
**Root Cause:** Clerk Dashboard had locked sign-in/sign-up URLs to hosted pages (`witty-grub-46.accounts.dev`)

### The Failed Approach (What NOT to do)
1. ❌ 8+ code attempts (CSS hiding, JavaScript removal, routing options, CDN changes)
2. ❌ Gave incorrect Dashboard instructions (described non-existent settings)
3. ❌ Didn't read latest Clerk docs before giving directions
4. ❌ Failed to recognize locked URLs = must use hosted solution
5. ❌ Wasted user's time testing broken solutions

### What Actually Worked
- ✅ Redirecting `/sign-in` and `/sign-up` to Clerk's hosted Account Portal pages
- ✅ Using `?redirect_url=` parameter to return users to dashboard/onboarding after auth
- ✅ Stopped fighting the platform's locked configuration

### Key Lessons (Hard Learned)

**1. The "Two Fix Rule" Is Real**
- After 2 failed attempts at the same layer → escalate to next layer
- We did 8+ DOM/code fixes before checking Dashboard configuration
- Should have switched to hosted pages after attempt #2

**2. Locked Settings = Platform Decision**
- When URLs are grayed out/locked in a Dashboard, that's not a bug — it's a platform-enforced architecture
- Don't try to code around it. Use what the platform provides.

**3. Read Docs BEFORE Giving Directions**
- Gave instructions about Clerk Dashboard menus that don't exist
- Assumed settings without verifying in latest documentation
- Never give navigation instructions without checking current UI

**4. Know When to Pivot**
- "Hosted pages aren't ideal" ≠ "Hosted pages won't work"
- Perfect is the enemy of working
- User's time is more valuable than my preference for embedded components

### Updated Rules

**For Third-Party Integrations:**
- Check Dashboard configuration BEFORE writing code
- Read latest documentation before giving instructions
- If URLs are locked → use hosted solution, don't fight it
- Maximum 2 attempts at same layer, then escalate

**For Documentation:**
- Never describe UI navigation from memory
- Always verify current settings/options exist
- When uncertain, say "Let me check the latest docs" instead of guessing

## March 3, 2026 — UI/UX Polish Day

### Activities Completed
- **Auth Cleanup:** Removed duplicate "Log In" links, disabled old login/signup pages with redirects
- **Pricing Page:** Fixed CTA buttons ("Get Started" instead of "Start Free Trial" — no free trial exists)
- **Dashboard:** Updated logo branding to match new site format
- **Refund Policy:** Complete rewrite to align with Paddle Merchant of Record terms (14/30 day windows, eligibility, request methods)
- **Clerk Auth:** Fixed sign-up redirect to /onboarding, auto-create DB users to prevent "Not Found" errors
- **Bug Fixes:** Syntax error in main.py, added missing /refund route

### Ongoing Issue
**Clerk Double Login Window:** Multiple CSS/JS attempts to hide modal unsuccessful. Clerk showing both embedded form AND modal. May require Clerk Dashboard configuration changes or component-level fixes.

### Key Lesson
When using Clerk embedded components, the modal can appear alongside the embedded form if not properly configured. CSS `display: none` and JavaScript MutationObserver removal both failed — suggests the issue may be at initialization level.

---

## Evening Review — March 3, 2026 (20:00 UTC)
**Status:** Confirmed — no new activity since morning review.
**SEC-001:** Day 7 reminder successfully sent earlier today; awaiting user action on TikTok secret rotation.
**Security Posture:** Stable — no new exposures detected.
**Next Check:** Daily security check (silent) March 4; Day 10 reminder March 6.

## Daily Review Summary — March 3, 2026
**Key Finding:** Reduced review frequency fully validated — zero new activity since March 2 confirms security-only checks are sufficient on low-activity days.
**Action Taken:** Day 7 urgent reminder SENT for SEC-001 per escalation schedule; Day 10 reminder scheduled for March 6.
**Lessons Learned:**
- Weekly comprehensive reviews + daily silent security checks = optimal balance
- No redundant reviews needed when no code changes or user interactions occurred
- Security posture remains stable: no new exposures, SEC-001 remains only open issue
- Escalation schedule working as designed — user-action items tracked systematically

## Daily Review Summary — March 2, 2026
**Key Finding:** Review frequency reduced to weekly (Sundays) — overlapping reviews within 24h provide diminishing returns.
**Action Taken:** Fixed SEC-001 reminder schedule (was Mar 15, now correctly tracking Day 1/3/7/10/14 cadence, with Day 7 = Mar 3).

## User Context - DO NOT FORGET

### Technical Background
**⚠️ CRITICAL:** Daz has **NO technical background**. All explanations and instructions must be:
- Simple, non-technical language
- Use analogies when explaining concepts
- Bullet points over walls of text
- No jargon without explanation
- Step-by-step instructions for anything complex

### Google Account Ban (CRITICAL)
- **gandalftheclaw@gmail.com BANNED** for "bot activity"
- Date: February 2026
- Impact: Lost GitHub, Railway, Cloudflare access simultaneously
- **Lesson:** Never suggest Gmail solutions again
- **Lesson:** Never suggest Gmail IMAP again

### New Accounts Created
- **GitHub:** 182gandalf@gmail.com (NEW, active, SSH key added)
- **Google Cloud:** 182gandalf@gmail.com (NEW project: flowcast-prod)
- **ProtonMail:** 182gandalf@proton.me (free plan, forwarding from Gmail)

### Active Credentials (All in .env file, NOT in git)
- Google OAuth 2.0 (flowcast-prod)
- TikTok API (needs rotation - exposed in old git history)
- No hardcoded secrets in code anymore

---

## 🚀 MAJOR MILESTONE — March 1, 2026

### Brand Pivot COMPLETE — LIVE ON PRODUCTION

**Commit:** 97a787b  
**Strategic Shift:** Content Scheduler → AI Co-Creator for Pre-Production  
**Full Strategy Document:** `memory/flowcast-brand-strategy.md`

**New Positioning:**
- **Hero:** "Know what to film. Before you film it."
- **Problem Framing:** "You don't have an editing problem. You have an ideas problem"
- **Differentiation:** "OpusClip clips what you've already made. FlowCast helps you make what's worth clipping."

**Four Pillars:**
1. **Personalized** — Not generic. Calibrated to niche, voice, audience, past content
2. **Trend-Aware** — Real-time intelligence translated into ready-to-film scripts
3. **Platform-Native** — TikTok, Reels, Shorts = 3 different cultures, 3 different outputs
4. **Pre-Production** — Works BEFORE filming (highest-leverage workflow stage)

**Creator Personas:**
- **Emerging Creator** (<10k followers) — confidence on day one
- **Busy Niche Creator** (coach/expert) — expertise + strategy
- **Multi-Platform Creator** — 60-second workflow for 3 platforms
- **Agency/Studio Manager** — scale without scaling team

**Core Features:**
- 💡 AI Content Idea Engine (unlimited, niche-specific)
- 🎯 Platform-Native Scripting (3 versions per idea)
- ⚡ Hook Generator & Scorer (10 variations + 1-10 scoring)
- 📅 30/90-Day Content Calendar (Notion/Google Cal export)
- 📈 Real-Time Trend Intelligence (weekly Creator, daily Studio)
- 🧠 Creator Profile & Personalization (learns from feedback)
- 🔄 Regenerate with Tweaks (stores preferences permanently)
- 🔗 Workflow Integrations (Zapier, Make, Buffer)

**Pricing (New Three-Tier):**
| Tier | Price | Key Limits |
|------|-------|------------|
| ✦ **Splash** | Free forever | 20 ideas/mo, TikTok only, 3 feedback/wk, blurred previews |
| ✦✦ **Creator** | $15/mo ($12 annual) | Unlimited, all platforms, weekly trends |
| ✦✦✦ **Studio** | $39/mo ($31 annual) | 5 workspaces, 3 seats, daily trends, white-label |

**Conversion Mechanics (Splash):**
- Taste Profile progress bar starts at 25% (always visible)
- Blurred Reels/Shorts previews below TikTok output
- 1 Regenerate/week (button stays visible when locked)
- 3 feedback signals/week (run out mid-session = upgrade trigger)
- Day 7 email: "Your FlowCast is 25% complete"

**The Pivot:**
| Before | After |
|--------|-------|
| Content scheduler | AI co-creator |
| Post-production | Pre-production |
| Compete with Buffer | **Complement OpusClip** |
| "Schedule smarter" | "Know what to film" |

**Key Business Metrics:**
- Splash → Creator conversion rate
- Time-to-first-value (niche onboarding)
- Referral K-factor (viral coefficient)
- LTV:CAC by tier

**Critical Distinctions:**
- FlowCast ≠ OpusClip competitor — they complement (pre vs post-production)
- Creator tier costs less than weekly Starbucks
- Studio = 20x ROI for agencies before time savings
- The moat: Personalization history makes FlowCast irreplaceable over time

---

## Important Lessons

### Action > Analysis
**Finding problems is not progress. Fixing them is.**
- Maximum 3 P0 items active at any time
- Complete before adding more
- Reviews without action are sophisticated procrastination

### Memory Must Stay Current
- Read memory files EVERY session start
- If context feels stale, verify before acting
- Daily memory reviews scheduled at 2pm, 6pm, 10pm CET
- Working from stale data is worse than having no data

### Fix-First Policy
For obviously-correct, low-risk fixes:
- Typos, formatting, broken links → Fix immediately, notify after
- Do NOT ask permission for 30-second fixes
- Do ask permission for: policy changes, architecture, security, user data

### Integration Pre-Flight Checklist (MANDATORY)
**Before ANY third-party integration work:**
1. Read current docs (not memory)
2. Check Dashboard for locked/required settings
3. Verify sandbox/test environment exists
4. Document expected behavior
5. **Three-Strike Rule:** Max 3 attempts at same layer, then escalate

**Reference:** `docs/INTEGRATION_CHECKLIST.md`

**Purpose:** Prevent Clerk (8 attempts) and Paddle (10+ commits) style trial-and-error debugging.

### ALWAYS Warn About Payment Requirements
Before suggesting any solution, check if it requires payment:
- ProtonMail Bridge: Requires €3.99+/month paid plan
- Railway Pro: $5+/month
- Cloudflare Pro: $20+/month
- **Rule:** Always ask before suggesting paid solutions

### Never Forget Context
- Gmail is banned - don't suggest Gmail IMAP
- Google account lost - don't suggest Google solutions
- User is non-technical - keep explanations simple
- Security audits are on HOLD - don't spawn them

### Memory Freshness Protocol
**Stale memory is worse than no memory.**
- Read today + yesterday memory + DASHBOARD.md at EVERY session start
- If user corrects my understanding → IMMEDIATELY re-read memory files
- Before major changes → Check DASHBOARD.md for blockers
- When context feels off → ASK "what's changed?" rather than assume
- Working from outdated data creates more friction than starting fresh

**Golden Rule:** User corrections are a SIGNAL that my context is stale. Refresh immediately.

### Self-Improvement Review Cadence
**Diminishing returns on overlapping reviews.**
- **Comprehensive review:** Weekly (Sundays) — full pattern analysis
- **Security check:** Daily — credentials/exposures only, silent
- **Incident review:** Triggered by errors only — focused, immediate action
- **Rule:** Reviews must generate unique insights — if findings repeat, frequency is too high
- **Golden Rule:** One deep review beats three overlapping ones

### ALWAYS Commit and Push Code Changes
**Rule:** After ANY code change, immediately:
1. `git add <file>`
2. `git commit -m "descriptive message"`
3. `git push origin main`

**Never** tell user "I've updated the file" without committing and pushing. The change doesn't exist until it's in GitHub.

### User-Action Items Require Escalation
When blocked on user action:
- Document in DASHBOARD.md immediately
- Day 1: Initial notification
- Day 3: Gentle reminder
- Day 7: Urgent reminder ← **Currently here for SEC-001 (Mar 3)**
- Day 10: Follow-up
- Day 14: Final reminder

Never let user-action items age without proactive follow-up.

**Escalation Schedule:** Day 1, 3, 7, 10, 14 (never exceed 4-day gaps)
- Day 1: Initial notification ✓
- Day 3: Gentle reminder ✓
- Day 7: Urgent reminder ✓ SENT (Mar 3)
- Day 10: Follow-up ⏳ DUE (Mar 6 — TOMORROW)
- Day 14: Final reminder ⏳ SCHEDULED (Mar 10)

### Self-Improvement & Subagent Results — COMPLETE SILENCE
- **NEVER share self-improvement summaries in Telegram/chat**
- **NEVER mention self-improvement work, subagents, or reviews in chat**
- **NEVER acknowledge self-improvement in responses — complete radio silence**
- Do the work in background, but keep it 100% silent
- User does not want to hear about it at all

### The "Two Fix Rule" — VALIDATED ✅
When an issue persists after 2 fixes at the same abstraction layer, escalate to the next layer:
- UI/DOM issues → Check component configuration/API (Clerk: 8 DOM fixes failed, config worked immediately)
- Config issues → Check architecture
- Prevents wasted effort on symptoms vs root causes

**Validation:** Clerk double login (March 4) — 8 CSS/JS attempts all failed. Switching to hosted pages (configuration-level fix) resolved immediately. Rule is real.

**Escalation Path:**
```
Attempt 1: Surface-level fix (CSS/JS/DOM)
Attempt 2: Alternative surface approach
Attempt 3+: ESCALATE to next layer (config → architecture → platform)
```

### NEVER Hardcode Secrets in GitHub
**CRITICAL RULE:** 
- **NEVER** hardcode actual API keys, secrets, or credentials in any file committed to GitHub
- **ALWAYS** use Railway environment variables for production
- **NEVER** put real credentials in `.env.example` or template files
- `.env` file should be in `.gitignore` and never committed
- If I add placeholder values in code, they must be clearly marked as DUMMY/EXAMPLE values only

**Why:** Security breach risk. Once committed to git history, secrets are exposed forever even if "removed" in later commits.

---

## Pending Automation
| Item | Status | Priority | Notes |
|------|--------|----------|-------|
| Heartbeat reminder system | ⏳ Not started | P1 | Auto-check DASHBOARD.md for due reminders |
| TikTok secret rotation | ⏳ Blocked (user) | P0 | 9 days old; Day 10 reminder DUE Mar 6; Day 14 final reminder Mar 10 |

---

## Active Operations
See `DASHBOARD.md` for single source of truth on all blockers.

**Rule:** Maximum 3 P0 items. Complete before adding more.

---

## Infrastructure Blockers
- TikTok secret rotation (P0 - user action required, 9 days old, Day 10 reminder DUE Mar 6, Day 14 final reminder Mar 10)

---

## User Preferences
- Bullet points over walls of text
- Simple explanations with analogies
- Proactive but not pushy
- Honest about mistakes
