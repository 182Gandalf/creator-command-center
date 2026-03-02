# Critical Context & Lessons Learned - Updated March 2, 2026 (18:00 UTC)

## Current Status Snapshot
- **Active P0 Blockers:** 1 (SEC-001: TikTok secret rotation, 6 days, awaiting user action)
- **Review Cadence:** Validated weekly comprehensive reviews sufficient
- **Last Significant Work:** Brand pivot LIVE (March 1, 2026)
- **Today's Focus:** System validation, no new feature work

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
- Day 7: Urgent reminder
- Day 10: Follow-up
- Day 14: Final reminder

Never let user-action items age without proactive follow-up.

**Escalation Schedule:** Day 1, 3, 7, 10, 14 (not 13-day gaps)

### Self-Improvement & Subagent Results — COMPLETE SILENCE
- **NEVER share self-improvement summaries in Telegram/chat**
- **NEVER mention self-improvement work, subagents, or reviews in chat**
- **NEVER acknowledge self-improvement in responses — complete radio silence**
- Do the work in background, but keep it 100% silent
- User does not want to hear about it at all

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
| TikTok secret rotation | ⏳ Blocked (user) | P0 | Reminder Mar 15 (6 days old) |

---

## Active Operations
See `DASHBOARD.md` for single source of truth on all blockers.

**Rule:** Maximum 3 P0 items. Complete before adding more.

---

## Infrastructure Blockers
- TikTok secret rotation (P0 - user action required, 6 days old, reminder scheduled Mar 15 per escalation schedule)

---

## User Preferences
- Bullet points over walls of text
- Simple explanations with analogies
- Proactive but not pushy
- Honest about mistakes
