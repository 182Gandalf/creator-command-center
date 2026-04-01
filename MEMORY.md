# Critical Context & Lessons Learned - Updated April 1, 2026

## April 1, 2026 — End of Day Summary (19:00 UTC)

### Activity Today
- **11:00 UTC** — Daily reminder triggered
- **~11:05 UTC** — Crypto Raven requested hero copy updates on landing page
  - Changed badge: "The Content Intelligence Engine..." → "The Personalized Content Intelligence Engine..."
  - Changed subtitle: "...scored hooks..." → "...personalized scored hooks..."
  - Commit `d570666` pushed to main
- **15:00 UTC** — Midday review completed
- **15:00–19:00 UTC** — Development work (no direct user sessions):
  - Trend data consolidated into single expandable button in Ideas tab
  - TikTok sound suggestions added to dashboard scripts
  - Daily digest system expanded with status checks and batch sending endpoints

### ✅ Completed Today
- Landing page hero copy refresh emphasizing "personalized" positioning
- Dashboard UI improvements (trend consolidation, sound suggestions)
- Backend: Daily digest infrastructure for beta period

### Key Learnings
1. **Micro-copy iterations are frictionless when scope is tight.** Small, single-purpose copy changes don't need debate — just execute.
2. **Quiet afternoons enable deep work.** No user requests between 15:00–19:00 allowed focused development on dashboard features and digest infrastructure.

### Persistent Bug Tracker (16+ Days — Critical)
1. Dashboard double "Loading trends…" render — since Mar 16 ← **16 days**
2. Pricing page closing section has no CTA button — since Mar 16 ← **16 days**
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16 ← **16 days**
4. Dashboard "Use this hook" instruction misplaced — since Mar 17 ← **15 days**
5. Creator plan lists Zapier inline as "(Creator Pro+)" in paid plan — since Mar 23 ← **9 days**

---

# Critical Context & Lessons Learned - Updated March 31, 2026

## March 31, 2026 — End of Day Summary (15:00 UTC)

### Activity Today
- **10:00 UTC** — Daily improvement suggestion sent: "Success Compounder" gated to Creator Pro in Splash but absent from Creator Pro's own feature list — broken upgrade path
- **~11:30 UTC** — Crypto Raven confirmed feature is live; fix implemented and shipped immediately
  - Added Success Compounder description to Creator Pro's Personalization section
  - Commit `dbc7851` pushed to main
- **15:00 UTC** — End-of-day review completed

### ✅ Resolved Today
- **Success Compounder pricing page gap** — feature now appears in Creator Pro's card with full description
- Upgrade path from Splash → Creator Pro for this feature is now complete and verifiable

### Today's Suggestion Quality
Fresh and valid — 3rd consecutive fresh suggestion after the Mar 28–29 stale period. Actioned within ~90 minutes of delivery — best same-day turnaround in recent memory.

### Key Learning
**Quick user confirmation + immediate execution is the ideal workflow.** The daily suggestion system works best when:
1. Suggestion is fresh and specific (not a repeat)
2. User can confirm or deny in one message ("it exists" / "not yet")
3. Fix is isolated and low-risk enough to ship without further discussion

Today's flow was exactly this. No deliberation, no back-and-forth — suggestion → confirm → fix → push.

### Persistent Bug Tracker (15+ Days — Critical)
1. Dashboard double "Loading trends…" render — since Mar 16 ← **15 days**
2. Pricing page closing section has no CTA button — since Mar 16 ← **15 days**
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16 ← **15 days**
4. Dashboard "Use this hook" instruction misplaced — since Mar 17 ← **14 days**
5. Creator plan lists Zapier inline as "(Creator Pro+)" in paid plan — since Mar 23 ← **8 days**

### Pattern Observation
Tuesday follows the Mon/Tue low-activity pattern — no direct user sessions, all activity automated. Exception today: Crypto Raven replied to a suggestion and a fix was shipped. Tuesdays are not always silent.

---

# Critical Context & Lessons Learned - Updated March 30, 2026

## March 30, 2026 — Midday Summary (11:00 UTC)

### Activity Today
- **10:00 UTC** — Daily improvement suggestion sent: Features section "30-day calendar" copy contradicts hero fix from Mar 26
- **No direct user sessions** — quiet Monday morning, all activity automated

### Key Learning
**Stale suggestion streak broken.** After two consecutive stale days (Mar 28–29), today's Mar 30 analysis correctly identified a genuinely new issue: the hero fix last week was not propagated to the features section, creating an internal page inconsistency. The analysis system is working correctly when the analysis file is up to date.

### Today's Suggestion Quality
Valid and fresh — the "30-day calendar" features block contradiction is a real issue created by the Mar 26 hero fix not being fully applied across the page. Not stale.

### End-of-Day Status (15:00 UTC)
- No direct user sessions all day — quiet Monday, consistent with weekly pattern
- Suggestion delivered, no user response received
- All persistent bugs remain unresolved

### Persistent Bug Tracker (14+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16
4. Dashboard "Use this hook" instruction misplaced — since Mar 17
5. Creator plan lists Zapier inline as "(Creator Pro+)" in paid plan — since Mar 23

### New Issues Surfaced (Mar 30 Analysis)
- Monthly pricing may now be invisible on pricing page (toggle section removed or JS-only)
- "Ten questions at signup" homepage copy still universal — Splash only gets 5
- "Success Compounder" gate tightened to Creator Pro but still unexplained anywhere on site
- "50 Early-Access Spots" static banner — 8+ days unchanged, growing credibility risk

---

# Critical Context & Lessons Learned - Updated March 29, 2026

## March 29, 2026 — End of Day Summary (15:00 UTC)

### Activity Today
- **10:00 UTC** — Daily improvement suggestion presented (hero trust micro-copy inaccuracy)
- **User context:** Fix already implemented on Mar 26 — suggestion was stale
- **15:00 UTC** — End-of-day review completed
- **No direct work sessions** — quiet Sunday, all activity automated

### Key Learning
**Stale analysis is now a confirmed pattern.**
Two consecutive days (Mar 28 and Mar 29) of presenting the same stale suggestion confirms this isn't a one-off. The daily improvement system pulls from `flowcast-daily-improvements.md`, which was last updated on 2026-03-26. When fixes are implemented, the analysis file doesn't automatically refresh. The system needs either: (a) a way to mark suggestions as resolved, or (b) more frequent re-analysis to ensure suggestions reflect current site state.

### Pattern Observation
- Weekends remain predictably quiet — no user sessions
- Persistent UX bugs continue unresolved (now 13+ days for the oldest issues)
- No new issues introduced today

### Persistent Bug Tracker (13+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16
4. Dashboard "Use this hook" instruction misplaced — since Mar 17

---

## March 29, 2026 — Midday Summary (11:00 UTC)

### Activity Today
- **10:00 UTC** — Daily improvement suggestion presented (hero trust micro-copy inaccuracy)
- **User context:** Fix already implemented on Mar 26 — suggestion was stale
- **No direct work sessions** — quiet Sunday morning, all activity automated

### Key Learning
**Stale analysis persists as a systemic issue.**
The daily improvement suggestion presented today was based on 2026-03-26 analysis data, but the fix had already been implemented on March 26. This is the second consecutive day of stale suggestions. The root cause: the analysis log isn't being updated to mark items as resolved when fixes are deployed. The system needs a mechanism to invalidate or refresh suggestions once confirmed resolved.

### Pattern Observation
Weekend Sundays remain predictably quiet — no user sessions, only automated crons. This is consistent and acceptable.

### Persistent Bug Tracker (13+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16
4. Dashboard "Use this hook" instruction misplaced — since Mar 17

---

## March 28, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion presented (hero trust micro-copy inaccuracy)
- **User response:** Fix already implemented — suggestion was stale
- **16:00 UTC** — Midday memory review completed
- **20:00 UTC** — Final end-of-day review — no new activity since 16:00 UTC
- **No direct work sessions** — quiet Saturday

### Key Learning
**Analysis file lag creates stale suggestions.**
The daily improvement suggestion was based on 2026-03-26 analysis, but the fix had already been implemented. When the user confirms a fix is done, the analysis file may be behind reality. Consider noting resolved items more promptly in the analysis log to avoid repeat suggestions.

### Pattern Observation
Weekends (Saturday/Sunday) consistently show minimal activity — this is predictable and acceptable. No action needed.

---

# Critical Context & Lessons Learned - Updated March 27, 2026

## March 27, 2026 — End of Day Summary (16:00 UTC)

### Activity Today
- **11:35 UTC** — Daily improvement suggestion presented (from 2026-03-26 analysis: hero trust micro-copy inaccuracy)
- **11:35–13:52 UTC** — Cron misfired repeatedly (5+ triggers within ~2 hours)
- **No direct user sessions** — quiet Friday, all activity automated

### Key Learning
When cron jobs misfire repeatedly, the schedule configuration is likely incorrect (e.g., `*/8 * * * *` instead of `0 12 * * *`). The user should be alerted to check and fix the cron schedule to prevent notification fatigue.

### Cron Issue
- **Daily suggestion job** fired 5+ times between 11:35 and 13:52 UTC
- **End-of-day review** fired twice (13:44 and 16:00 UTC)
- **Action needed:** Verify cron expression is `0 12 * * *` (daily at noon), not `*/8 * * * *` (every 8 minutes)

### Site Status
✅ **Operational** — No outages reported

### Persistent Bug Tracker (11+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16
4. Dashboard "Use this hook" instruction misplaced — since Mar 17

---

## March 26, 2026 — End of Day Summary (16:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion presented: Hero trust micro-copy inaccuracy (30-day vs 7-day calendar)
- **~11:00 UTC** — Crypto Raven requested Discord link in footer; added to pricing.html, faq.html, help.html
- **~12:00 UTC** — Crypto Raven requested implementation of today's improvement; fixed hero copy
- **16:00 UTC** — End-of-day review completed
- **Commits:** `fe9cbca` (Discord links), `2157c30` (calendar copy fix)

### Key Learning
User-requested fixes via Telegram can be executed immediately when they're isolated copy/UX changes. The daily improvement system and direct user requests can work in parallel — no need to wait for end-of-day to implement clear, low-risk fixes.

### Site Status
✅ **Recovered** — Site fully operational after March 25 HTTP 500 outage

### Persistent Bug Tracker (10+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16
4. Dashboard "Use this hook" instruction misplaced — since Mar 17

---

## March 25, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion presented: Site-wide HTTP 500 outage (CRITICAL)
- **16:00 UTC** — End-of-day memory review completed
- **20:00 UTC** — Final review: No new activity since 16:00 UTC
- **No direct user sessions** — activity limited to automated crons

### Key Learning
An outage of the entire production site is a "stop everything" event. All marketing optimizations, UX fixes, and feature work are irrelevant when visitors see error pages. Infrastructure stability is prerequisite to everything else.

### New Critical Issue
- **flowcast.space completely down** — HTTP 500 on all routes
- **Error:** `unhashable type: 'dict'` — Python regression
- **Action needed:** Railway rollback + root cause fix
- **No uptime monitoring** — outage duration unknown

### Persistent Bug Tracker (9+ Days) — Unverifiable Due to Outage
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16

### Open Items Status
- Site outage is now **P0 emergency** — blocks all other work
- Full beta test flow remains **CRITICAL and overdue** — no progress
- All persistent UX bugs still unresolved
- Telegram group: Crypto Raven asked about Discord bot access — declined (I'm private, not public)

---

## March 24, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: Creator Pro "Most Value" badge lacks ROI math
- **~12:00 UTC** — User declined suggestion (Crypto Raven), marked in file
- **16:00 UTC** — End-of-day memory review completed
- **No direct user sessions** — activity limited to Telegram group

### Key Learning
When suggestions are declined, mark immediately and move on. The system surfaces fresh alternatives next cycle — no need to revisit rejected ideas.

### Persistent Bug Tracker (8+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All other open items unchanged

---

## March 23, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: Money-back guarantee is invisible in main plan card section (HIGH priority, LOW effort)
- **16:00 UTC** — End-of-day memory review completed
- **No direct user interaction** — quiet Monday, all activity automated crons

### Key Insight
Three UX bugs have now persisted for **7+ consecutive days** without resolution. After a full week of flagging, the pattern is clear: these items are documented sufficiently but need implementation. The daily analysis system continues to surface fresh, high-value suggestions (today's money-back guarantee placement is a good example), so the system itself remains valuable — but the persistent bugs should no longer be the headline finding each day.

### Pattern Observation
Monday = consistently low-activity day (similar to Sunday). No user sessions, only automated crons. This is predictable — no action needed.

### Persistent Bug Tracker (7+ Days)
1. Dashboard double "Loading trends…" render — since Mar 16
2. Pricing page closing section has no CTA button — since Mar 16
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" — since Mar 16

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All other open items unchanged

---

## March 22, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: "50 Early-Access Spots" scarcity claim is static and potentially misleading (HIGH priority, LOW effort)
- **16:00 UTC** — End-of-day memory review completed
- **No direct user interaction** — quiet Sunday, all activity automated crons

### Key Insight
Three UX bugs have now persisted for 6+ consecutive days of analysis without resolution: (1) Dashboard double "Loading trends…" render, (2) Pricing page closing section has no CTA button, (3) Studio plan reads "Everything in Creator, plus:" instead of "Creator Pro." These are documented sufficiently — they need implementation, not further documentation. The pattern suggests either: (a) Daz is prioritizing other work, (b) the fixes are harder than they appear, or (c) they haven't been seen/reviewed. After 6 days, additional flagging is noise.

### Pattern Observation
Sunday = consistently lowest activity day. No user sessions, only automated crons firing. This is predictable and acceptable — no action needed.

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All three persistent UX bugs still unresolved (6+ days flagged)
- All other open items unchanged

## March 22, 2026 — Midday Review (12:00 UTC)

### Activity So Far
- **11:00 UTC** — Daily improvement suggestion sent: "50 Early-Access Spots" scarcity claim is static and potentially misleading (HIGH priority, LOW effort)
- **No direct user interaction yet** — quiet Sunday morning, all activity automated crons

### Persistent Issues Requiring Action
Three bugs have been flagged for 6+ consecutive days without resolution:
1. Dashboard double "Loading trends…" render (since Mar 16)
2. Pricing page closing section has no CTA button (since Mar 16)
3. Studio plan reads "Everything in Creator, plus:" — should be "Creator Pro" (since Mar 16)

These are documented sufficiently — they need implementation, not further analysis.

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All other open items unchanged

---

## March 22, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: "50 Early-Access Spots" scarcity claim is static and potentially misleading (HIGH priority, LOW effort)
- **16:00 UTC** — End-of-day memory review completed
- **No direct user interaction** — quiet Sunday, all activity automated crons

### Key Insight
Three UX bugs have now persisted for 6+ consecutive days of analysis without resolution: (1) Dashboard double "Loading trends…" render, (2) Pricing page closing section has no CTA button, (3) Studio plan reads "Everything in Creator, plus:" instead of "Creator Pro." These are documented sufficiently — they need implementation, not further documentation. The pattern suggests either: (a) Daz is prioritizing other work, (b) the fixes are harder than they appear, or (c) they haven't been seen/reviewed. After 6 days, additional flagging is noise.

### Pattern Observation
Sunday = consistently lowest activity day. No user sessions, only automated crons firing. This is predictable and acceptable — no action needed.

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All three persistent UX bugs still unresolved (6+ days flagged)
- All other open items unchanged

---

# Critical Context & Lessons Learned - Updated March 21, 2026

## March 21, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: Monthly prices are JavaScript-only — not visible to Google crawlers or no-JS users (SEO/trust liability)
- **16:00 UTC** — End-of-day memory review completed
- **No direct user interaction** — quiet day, all activity automated crons

### Key Insight
Two consecutive days of pricing-page-related suggestions (buried toggle on Mar 20, invisible monthly prices on Mar 21) indicate this area needs attention. The pricing page has multiple UX and SEO issues that compound each other.

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All other open items unchanged (see list below)

---

## March 21, 2026 — Midday Review (12:00 UTC)

### Activity So Far
- **11:00 UTC** — Daily improvement suggestion sent: Monthly prices are JavaScript-only — not visible to Google crawlers or no-JS users (SEO/trust liability)
- **No direct user interaction yet** — quiet morning, all activity automated crons

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress
- All other open items unchanged
- Two consecutive days of pricing-page-related suggestions (buried toggle on Mar 20, invisible monthly prices on Mar 21) indicate this area needs attention

### Daily Analysis Cron — Status
- `flowcast-daily-improvements.md` properly updated with 2026-03-21 analysis — cron is working
- Suggestion quality remains high (SEO and conversion-critical issues being surfaced)

---

# Critical Context & Lessons Learned - Updated March 20, 2026

## March 20, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: Pricing page monthly/annual toggle buried at bottom (high impact, low effort)
- **16:00 UTC** — End-of-day memory review completed
- **No direct user interaction** — quiet day, all activity automated crons

### Key Insight
Consistent automated analysis continues to surface conversion-critical UX issues. Today's suggestion (buried billing toggle) is another example of a small UX friction point that likely costs conversions. The pattern of daily suggestions showing "high impact / low effort" fixes validates the value of the automated analysis system.

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All other open items unchanged (see list below)

---

## March 20, 2026 — Midday Review (12:00 UTC)

### Activity So Far
- **11:00 UTC** — Daily improvement suggestion sent: Pricing page monthly/annual toggle buried at bottom (high impact, low effort)
- **No direct user interaction yet** — quiet morning, all activity automated crons

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress
- All other open items unchanged

### Daily Analysis Cron — Status
- `flowcast-daily-improvements.md` properly updated with 2026-03-20 analysis — cron is working
- Suggestion quality remains high (conversion-critical UX issues being surfaced)

---

# Critical Context & Lessons Learned - Updated March 19, 2026

## March 19, 2026 — End of Day Summary (20:00 UTC)

### Activity Today
- **11:00 UTC** — Daily improvement suggestion sent: Hero CTA hierarchy issue (two CTAs competing without visual hierarchy)
- **Afternoon** — CTA fix implemented via Telegram group request (Crypto Raven)
  - Changed hero secondary CTA from button to text link
  - Commit `fa67510` deployed to production
- **Feedback loop validated:** Suggestion surfaced → Daz saw it → implemented same day (~4 hour turnaround)

### Key Insight
The daily improvement system is working as designed. Even small UX fixes (low effort, high clarity) compound when they can go from identification → implementation in hours rather than days. This justifies continuing the automated analysis despite the initial setup friction.

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today (now significantly behind schedule)
- All other open items unchanged (see list below)

---

## March 18, 2026 — Session Summary

### Activity Today
- **04:01 UTC** — Daz confirmed Railway completions: `alembic upgrade head` (niche_category live) and `AI_PROVIDER=anthropic` set
- **11:00 UTC** — Daily improvement suggestion sent (Telegram msg 190): Hero CTA hierarchy issue — two CTAs competing without visual hierarchy
- **No direct user sessions** — quiet infrastructure day, no code changes

### Open Items Status
- Full beta test flow remains **CRITICAL and overdue** — no progress today
- All other open items unchanged (see list below)

### Note on Daily Analysis Cron
- `flowcast-daily-improvements.md` has 2026-03-18 analysis section — cron appears to be working
- File has been auto-updating since March 17, contradicting earlier "broken" status
- Cron status should be considered **resolved** unless evidence of failure emerges

---

## March 17, 2026 — Session Summary

### Shipped Today
- **Trends Scraper panel on `/admin`** (`a910302`) — shows all 18 niches with health status (✅/⚠️/🔴/⬜), last fetched time, top 5 topics + scores, summary bar. New backend endpoint: `GET /api/admin-ui/trends` (Clerk auth gated to admin email). Own refresh button.
- **Fixed "family and home" niche** (`8bd5b26`) — replaced with `"parenting"` + `"home decor"`. Now 18 niches (was 17). "Family and home" consistently returned 0 results from pytrends — too vague.
- **Success Compounder locked for Splash** (`6a6f65e`) — confirmed locked, Taste Profile capped at 25% for Splash. Updated:
  - `pricing.html` — added "Success Compounder (Creator+)" as disabled item under Splash personalization
  - `faq.html` — 3 edits: Taste Profile answer, Success Compounder answer (⚠️ Creator+ only), stuck-at-25% answer rewritten (25% = permanent Splash cap)
  - `help.html` — 3 edits: Success Compounder in signal list tagged Creator+, section header red badge, percentage breakdown notes Splash cap

### Lesson Learned — Confirmed
- Daz said "I think it should be [locked]" re: Success Compounder — I treated it as an instruction and unlocked it, then had to revert. It was a question/concern, not a directive.
- **Rule added to MEMORY.md:** If instructions are ambiguous or unclear — ask for clarification before acting.

### Open Items Carrying Forward
- [ ] Full beta test flow (CRITICAL — overdue)
- [ ] Mobile QA at 375px
- [ ] SPF record: `include:amazonses.com` in Cloudflare
- [ ] FROM_NAME env var in Railway (low priority)
- [ ] /admin stats verification
- [ ] Pricing page monthly/annual toggle
- [ ] Beta banner / paid pricing mixed signals
- [ ] Creator Pro monthly price on pricing page
- [ ] Fix daily midnight analysis cron (status unclear — see note below)
- [ ] Trends scraper: verify "parenting" + "home decor" pull data on next 03:00 UTC run

### March 18 Completions (confirmed by Daz)
- ✅ `alembic upgrade head` on Railway — `niche_category` column live, onboarding saves unblocked
- ✅ `AI_PROVIDER=anthropic` set on Railway — Anthropic fallback chain active

### 11:00–12:00 UTC Automated Activity
- Daily improvement suggestion sent to Daz (Telegram msg 179): "Upgrade" CTA copy wrong for first-time visitors — quick fix, high impact
- **Note on midnight analysis cron:** `flowcast-daily-improvements.md` now has a `2026-03-17` analysis section present — this suggests the cron may have run successfully last night (contradicts "confirmed still broken" status). Status should be verified — may be partially or fully working now.

---

# Critical Context & Lessons Learned - Updated March 16, 2026 (16:00 UTC)

## March 16, 2026 — End of Day

### Full Day Summary
- **No direct user interaction today** — all activity was automated crons
- **11:00 UTC** — Daily improvement cron fired. Fetched live site, surfaced Creator Pro pricing gap, sent to Daz via Telegram (message 175). No response received.
- **16:00 UTC** — End-of-day memory review (this entry)

### Daily Analysis Cron — STILL BROKEN (Correction from March 15)
- `flowcast-daily-improvements.md` has NOT auto-updated since Feb 27, 2026
- March 15 MEMORY.md entry said "RESOLVED ✅" — that was **incorrect**; the file was manually updated that day, not by the automated cron
- **Confirmed ongoing issue:** Midnight analysis cron is either not firing or not writing to the file
- Current workaround: manually fetch live site at presentation time
- **Priority fix needed — and false "RESOLVED" flag in memory has been corrected here**

### Suggestions Sent This Week (No Response Yet)
- Mar 15: Trust badges on signup page (low effort)
- Mar 16: Creator Pro monthly price missing (low effort, 30 min)
- Both sent via Telegram — awaiting Daz confirmation

### Open Items Carrying Into March 17
- [ ] Full beta test flow (CRITICAL — overdue)
- [ ] Mobile QA at 375px
- [ ] SPF record: `include:amazonses.com` in Cloudflare
- [ ] FROM_NAME env var in Railway (low priority)
- [ ] /admin stats verification
- [ ] Pricing page monthly/annual toggle
- [ ] Beta banner / paid pricing mixed signals
- [ ] Creator Pro monthly price on pricing page
- [ ] Fix daily midnight analysis cron (confirmed still broken)

---

## March 16, 2026 — Midday Check-in

### Activity So Far
- **11:00 UTC** — Daily improvement cron fired. `flowcast-daily-improvements.md` still stale (file not auto-updating despite March 15 "resolved" note). Fetched live site manually, identified fresh suggestion: Creator Pro pricing page missing monthly price (`$25/mo`). Sent to Daz via Telegram.
- No direct user interaction yet today.

### New Finding — Creator Pro Pricing Gap
- `/pricing` shows Creator Pro at `$20/mo` annual only — no monthly price displayed
- All other plans show monthly price clearly
- Recommendation sent: add `$25/mo` monthly, "Save 20%" badge, 1-line differentiator ("For creators who post daily")
- Effort: Low (30 min)

### Note on Daily Analysis Cron
- `flowcast-daily-improvements.md` is NOT auto-updating despite March 15 claim it was resolved
- File still shows Feb 27 as last real analysis
- Workaround: manually fetch live site at cron time and derive fresh suggestions
- **TODO:** Properly fix the midnight analysis cron job

### Open Items Carrying Forward
- [ ] Full beta test flow (CRITICAL)
- [ ] Mobile QA at 375px
- [ ] SPF record: `include:amazonses.com` in Cloudflare
- [ ] FROM_NAME env var in Railway (low priority)
- [ ] /admin stats verification
- [ ] Pricing page monthly/annual toggle
- [ ] Beta banner / paid pricing mixed signals
- [ ] Creator Pro monthly price on pricing page (new)
- [ ] Fix daily midnight analysis cron (still not auto-updating)

---

# Critical Context & Lessons Learned - Updated March 15, 2026 (12:00 UTC)

## March 15, 2026 — End of Day

### Shipped Today
- **Commit `90d0a58`** — trust/copy fixes (Daz approved via Telegram):
  - Testimonials heading: "— Pending Beta Feedback" removed from index.html ✅
  - Homepage footer pricing: "Creator from $12/mo. Studio from $31/mo." ✅
  - Pricing page meta descriptions: all three updated to current prices ✅

### Daily Analysis Cron — RESOLVED ✅
`flowcast-daily-improvements.md` updated with fresh 2026-03-15 analysis. "Stale since Feb 27" issue cleared.

### Affiliate/Referral Programs — DEFERRED
Reminder fired 08:00 UTC. Prerequisites not met (no active users). Parked until post-beta-launch.

### Open Items Carrying Into March 16
- [ ] Full beta test flow (CRITICAL — not done)
- [ ] Mobile QA at 375px
- [ ] SPF record: `include:amazonses.com` in Cloudflare
- [ ] FROM_NAME env var in Railway (low priority)
- [ ] /admin stats verification
- [ ] Pricing page monthly/annual toggle
- [ ] Beta banner / paid pricing mixed signals

---

# Critical Context & Lessons Learned - Updated March 14, 2026 (20:00 UTC)

## March 14, 2026 — End of Day Summary

### All Blockers Cleared ✅
- `alembic upgrade head` — run on Railway (video_signals table live, Success Compounder works)
- Paddle Creator Pro products created + Railway env vars set (Creator Pro checkout live)
- `ADMIN_EMAIL=182gandalf@gmail.com` set in Railway (admin dashboard stats working)

### Fixes Shipped
- **pytrends retry hardening** (`69fc13e`): delays 200–280s, 20min batch pause, 45min retry-1, 60min retry-2, randomised niche order
- **Pricing cards widened** (`73aa766`): container 1400px, gap 2rem, breakpoint 1480px
- **TikTok task purged** (`50cc182`): scrubbed from 27 files — permanently deleted, never re-add

### Midday — Trust Badge Suggestion Surfaced
Sent to Daz: add 🔒 SSL / 💳 Paddle / 🛡️ Privacy badges to signup page. LOW effort. Awaiting response.

### Stale Analysis Cron — KNOWN ISSUE
`flowcast-daily-improvements.md` not updated since 2026-02-27. Midnight analysis job broken. Needs fix.

### Open Items Carrying Into March 15
- [ ] SPF record: add `include:amazonses.com` in Cloudflare (5 min job)
- [ ] FROM_NAME env var in Railway (low priority — emails already work)
- [ ] 4-issue dashboard fix (diagnosed, not yet committed)
- [ ] Full beta test flow (critical before first invite)
- [ ] Mobile QA at 375px
- [ ] Fix stale daily analysis cron (midnight job)

---

# Critical Context & Lessons Learned - Updated March 13, 2026 (21:00 UTC)

## March 13, 2026 — Full Sprint Day (Evening Update)

### Key Completions (afternoon/evening session)
- **Creator Pro tier** live: $25/mo / $20/mo annual — 90-day calendar, daily digest, Zapier access, 20 saves
  - Paddle env vars still needed: `PADDLE_PRICE_CREATOR_PRO_MONTHLY`, `PADDLE_PRICE_CREATOR_PRO_ANNUAL`
- **Success Compounder** built: replaces Niche Filtering in taste profile — users paste video links → AI extracts content intelligence → highest-priority signal in idea generation
  - Needs `alembic upgrade head` on Railway
- **Interactive landing page demo** live: niche/tone picker → 3 live AI ideas → conversion panel
- **pytrends rate limit fix**: delays 150-200s, batch pauses, retry pass
- **Digest fix**: max_tokens 2000→4000, partial JSON salvage, skip placeholder emails
- **Save limits**: Splash 5, Creator 15, Creator Pro 20
- **Annual 14-day guarantee** on pricing page (both toggles + refund policy)
- Multiple dashboard UX fixes: nav reorder, padding, button alignment, calendar nudge text, hooks button visible, mobile hook fix (position:relative on hook-card)

### Active Pending Items (as of March 13 end-of-day — see March 14 section above for updates)
- [x] Paddle: Creator Pro product + Railway env vars — ✅ Done March 14
- [x] Railway: `alembic upgrade head` — ✅ Done March 14
- [ ] SPF record: add `include:amazonses.com` to Cloudflare
- [ ] Railway: add `FROM_NAME` env var (low priority)
- [ ] Fix stale daily midnight analysis cron

## March 13, 2026 — Launch Day (End of Day)

### Day Summary
- Quiet day — no direct user interaction; automated crons ran as scheduled
- **FlowCast improvement cron** (11:00 UTC): surfaced hero headline typo ("aboutwhat" → "about what") to Daz via Telegram
- **Daily analysis cron is stale** — `flowcast-daily-improvements.md` last updated 2026-02-27; midnight analysis job appears broken/never auto-updating — needs investigation
- No confirmation received from Daz on typo fix or Railway logs

### Carried-Forward Blockers (from March 12 + today)
- [ ] Hero headline typo fix — confirm deployed to flowcast.space
- [ ] Railway logs: did pytrends nightly scheduler populate all 17 niches?
- [ ] SPF record: add `include:amazonses.com` to Cloudflare DNS
- [ ] Railway env var: `FROM_NAME` still needs adding in Railway dashboard
- [ ] Fix/investigate daily midnight FlowCast analysis cron (stale since 2026-02-27)

---

## March 12, 2026 — Evening Sprint Complete

### Latest Commit: `db0caed` | All features live on Railway

### Features Shipped Today (Full Day — 27+ commits)

**Studio Plan — All features confirmed:**
- ✅ 90-day calendar (backend `_get_tier_days("studio")=(90,90)` + visible lock banner for non-Studio)
- ✅ Daily trend digest email (studio_daily_digest scheduler 07:00 UTC)
- ✅ Workspace switcher: 5 slots Studio / 1 others, localStorage, add/rename/delete, locked slots visible with 🔒
- ✅ White-label PDF exports: scripts, hooks, content-pack, calendar (reportlab, brand settings on CreatorProfile)
- ✅ Zapier webhook: `POST /webhooks/zapier` → returns `{scripts:[...5], ideas:[...5]}`

**New DB tables (auto-migrated on Railway deploy):**
- `api_keys` (id, user_id UNIQUE, api_key 32-char, created_at) — for Zapier auth
- `creator_profiles` new cols: brand_name, brand_color, brand_logo_url

**New routes:**
- `GET/POST /api/export/branding` — brand settings
- `GET /api/export/pdf/{scripts,hooks,content-pack}` — Studio PDF exports
- `GET /api/calendar/export/pdf` — Studio branded calendar PDF
- `GET/POST /api/settings/api-key`, `/api/settings/generate-api-key`
- `POST /webhooks/zapier`
- `GET /faq`, `GET /help`

**New pages:**
- `/faq` — 35 questions, 8 sections, live search, accordion
- `/help` — full tutorial, sticky TOC, 9 sections (onboarding → taste profile)

**Bug fixed:** Ideas counter always showed 20 — was reading `User.splash_ideas_used_this_month` (never written); fixed to read `CreatorProfile.splash_ideas_used_this_month`

**Product knowledge correction:** "Tweaks" = regenerates ALL 5 ideas with fresh angles. NOT a single idea. FAQ + help guide corrected.

**Content updates:**
- Day 7 splash email: added retention paragraph after "Creator-tier FlowCast learns all of that."
- All 13 templates: static logo.jpg → `<video autoplay loop muted playsinline>` animated logo
- Dashboard dropdown: Help Guide + FAQ + Email Support links

**Settings page (`/settings`):** Integrations section — generate/regenerate API key, 30s full-key display, double-click confirm for regen, Zapier instructions

### Reminder Active
- Tomorrow 9AM NL (8AM UTC): check Railway logs for pytrends nightly scheduler — did all 17 niches populate?

---

## March 12, 2026 — Phase 5 Complete: Email Sequences + Trend Intelligence

### Summary
**19+ commits** — Trends tab live, email digest system built, OG image updated, deliverability hardened, onboarding Splash fix.

### Key Completions

**Phase 5: Email Sequences — COMPLETE ✅**
- `services/email.py` — Resend SDK wrapper, FROM display name, plain-text + headers
- `services/digests.py` — `generate_digest_scripts()` (Gemini), `generate_and_send_trend_digest()`, Day 7 email
- `services/scheduler.py` — Creator weekly digest (Mon 07:00), Studio daily digest (07:00), Day 7 hourly check
- Admin endpoints: `/api/admin/test/send-digest`, `/api/admin/test/send-day7-email`
- Both test emails confirmed delivered ✅ (Fitness niche, Creator + Splash tiers)

**Trends Tab — LIVE ✅**
- `/api/trends/current` returns 10 topics with score bars + `fetched_at` timestamp
- Splash gating: topic #1 visible, #2–10 blurred + "Upgrade to Creator" overlay
- Pricing page updated: "Trend Intelligence" section added to all 3 plans
- pytrends `urllib3<2` pinned — scheduler runs at 03:00 UTC with 60s+jitter between fetches

**Email Deliverability Hardened:**
- Day 7 email is plain/personal (no HTML template) — targets Primary inbox
- All emails have plain-text versions + `List-Unsubscribe` headers
- FROM: `Daz from FlowCast <hello@flowcast.space>`
- DMARC `p=quarantine` ✅, DKIM ✅, SPF gap: needs `include:amazonses.com` in Cloudflare
- `FROM_NAME` env var needed in Railway

**OG Image Updated:**
- Was: square 1024×1024 logo-only
- Now: 1200×630 cropped from Daz's brand reference JPG
- Cache-busted with `?v=3` in index.html + pricing.html

**Onboarding Splash Fix:**
- Splash users were blocked from submitting onboarding (Q7 blank validation check)
- Fix: frontend skips disabled inputs; backend Q6–10 made Optional in Pydantic model

**Key Decisions:**
- **No fixed launch date** — ship when ready (Daz, March 12)
- SerpAPI ($25/mo) planned as pytrends replacement at first paying user milestone
- Day 7 email deliberately plain — Primary inbox > marketing template
- Gemini key (DIGEST_API_KEY) was suspended initially — replaced by Daz mid-session, now working

### Known Gap
- **SPF record** missing Resend: add `include:amazonses.com` to Cloudflare DNS (TXT record)
- **FROM_NAME** env var needs adding in Railway dashboard

### Commits Today
`f43f7a5` `a208db3` `0fcc86c` `6edc7b0` `6faff41` `9cb10c1` `1fdee53` `35d8686` `604863d` `b06e260` `4138896` `4f2f05c` `f7c6b92` `148bcaf` `4791e40`

---

# Critical Context & Lessons Learned - Updated March 11, 2026 (22:00 UTC)

## March 11, 2026 — Major Polish & Bug Fixes Day

### Summary
**21+ commits** — All pricing constraints finalized, onboarding tier-gating, script generation fixes, UI polish.

### Key Accomplishments

**Script Generation Fixed:**
- Active hook now properly flows into generated scripts
- Platform-specific hooks (TikTok/Reels/Shorts tailored)
- Rich idea context (not just title) for better script variety

**Pricing Page Finalized:**
- All 3 plans aligned: Content Ideation → Saves & Storage → Personalization → Workflow
- Splash: 5-question onboarding (Q6-10 locked), 2 saves each, unlimited feedback
- Creator: 10-question onboarding highlighted
- Studio: Same sections as Creator + Agency Economics

**Splash Tier Limits (Final):**
| Feature | Limit |
|---------|-------|
| Ideas/month | 20 |
| Saves (ideas/hooks/scripts) | 2 each |
| Hooks visible | 3/5 |
| Platforms | TikTok only |
| Tweaks/week | 1 |
| Feedback signals | Unlimited |

**Onboarding Changes:**
- Splash sees Q1-5 only, Q6-10 blurred with "🔒 Upgrade" overlay
- Monthly idea counter PRESERVED when redoing onboarding
- Tier check runs reliably on all page loads (DOMContentLoaded + retry logic)

**UI Polish:**
- Animated logo loading on all AI operations
- 1-inch bottom gap on left panel and content area
- Hooks page clarifies "not platform specific"
- "Generate 5 Fresh Ideas with Tweaks" button text

### Bugs Fixed
1. Script generation ignoring active hook when idea_id passed
2. Saved counter showing 2/1 instead of 2/2 for Splash
3. Onboarding resetting monthly idea tally
4. Onboarding tier check not running when accessed via settings
5. Pricing sections misaligned across plans

### Current State
- **Launch target:** Friday March 13 (2 days)
- **Active blockers:** None
- **Next:** Beta testing, Content Calendar (Phase 2 Feature 4)

---

# Critical Context & Lessons Learned - Updated March 10, 2026 (20:00 UTC)

## March 10, 2026 — Taste Profile Polish + Mobile Battle

### Key Features Built / Fixed Today
**17 commits to FlowCast**

**Taste Profile System (8 items × 12.5%):**
- Added Idea Evolution (7-day timer from account creation)
- Added Niche Filtering (7-day timer from account creation)
- Splash users capped at 25% (items 1-2 only)
- No visible countdown — described as "proprietary algorithm"
- Onboarding now properly resets AI learning data (liked_topics, tone_prefs)

**Animated Logo Loading:**
- Replaces CSS spinner on all AI generation
- Dark navy background (#050d1c) with no mix-blend-mode issues
- Also loops in sidebar (36×36px video)

**Mobile Button War:**
- "Generate 5 New Ideas" button unresponsive on mobile
- Final fix: removed onclick attr, bound via addEventListener('click') + touchend at script end
- touch-action: manipulation + z-index:2 + :active state
- Show loading state BEFORE async work (immediate feedback)

**Hooks Polish:**
- Use Hook: index-based reference (not inline text) to avoid escaping bugs
- Generated hooks persist across tab navigations (localStorage cached)
- Persist across nav, empty state on delete

### Technical Lessons Learned
- `onclick="func('${text}')"` is ALWAYS risky for AI-generated text — use index + stored array
- Mobile unclickable buttons: try touch-action:manipulation FIRST
- addEventListener('touchend', preventDefault) + click at script END is most reliable
- `mix-blend-mode: screen` requires truly transparent backgrounds
- MP4 with `loop autoplay muted playsinline` > GIF for animations

### Current State
- **Active:** Testing mobile button fix (deployed, awaiting confirmation)
- **Launch:** Friday March 13 deadline approaching

---

# Critical Context & Lessons Learned - Updated March 9, 2026 (22:30 UTC)

## March 9, 2026 — Full Day Build: Dashboard Polish + Mobile UX

### Status: Phase 2 Features 1–3 COMPLETE + Major Mobile Polish

**Commits today:** 20+ commits, all pushed to `github.com/182Gandalf/FlowCast`
**Full log:** `memory/2026-03-09.md` (evening section)

### Key Completions
- Orange "✦ Selected" state works on saved hooks AND ideas (not just generated)
- Download .txt button on scripts (live + saved) — pure JS, no backend
- Hook scorer: 1 rewrite → 3 distinct rewrites (`improved_versions: List[str]`)
- Hook generation: 10 → 5 per batch; Splash sees 2, last 3 blurred; unique on regenerate (history in localStorage)
- Scripts context: SVG platform icons replace emojis; platform icon dynamic
- "Upgrade to Creator" CTA hidden for non-Splash users
- Saved ideas counter: Splash limited to 1 with pill counter
- Mobile footer: slim single-line, properly anchored, no content overlap
- Mobile: `html { font-size: 14px }` scales whole app; section headers stack; 160px bottom padding per section
- Generate Scripts: `alert()` → `showToast()` (mobile browsers block alert); Clerk null check added

### Current State
- **Next session priority:** Phase 2 Feature 4 (Content Calendar) OR beta testing polish before Friday March 13 launch
- **Migration head:** `2024_03_08_ideas_platform`

### Technical Lessons Learned Today
- `JSON.stringify` in HTML `onclick=""` breaks when text contains double quotes → use stored JS object + index reference
- `padding-bottom` on `flex:1 overflow-y:auto` containers is unreliable → use real DOM spacer element
- CSS media query overridden by later base styles → `!important` or restructure CSS order
- `alert()` silently blocked on mobile browsers → always use `showToast()` instead
- `position:static` removes containing block for `position:absolute` children → lock overlays escape their container

---

# Critical Context & Lessons Learned - Updated March 7, 2026 (20:00 UTC)

## March 7, 2026 — Phase 1 Complete: Paddle Foundation
**Status:** ✅ **PHASE 1 COMPLETE** — All subscription infrastructure built and tested

### Major Milestone: Payment System Production-Ready
**Commit Range:** `33fc2df` through `72b657d`
**Duration:** 2 days intensive work
**Result:** Full subscription lifecycle from subscribe → upgrade → downgrade → cancel

### Phase 1 Deliverables Completed:
1. **Paddle Billing Integration:** Complete checkout, webhooks, tier management
2. **Subscription Database:** All migration files committed, schema stable
3. **User-Facing Features:**
   - Upgrade via Paddle checkout (4 plans)
   - Downgrade button with reason collection
   - Cancel button with feedback
   - Auto-downgrade on expiration
   - Email notifications to admin
4. **Admin Tools:**
   - Process expired subscriptions endpoint
   - Test webhooks for cancellation/downgrade
   - Subscription change logging
5. **Technical:**
   - FastAPI patterns applied (CORS, DB pooling, async httpx)
   - Webhook handlers for all Paddle events
   - Auto-downgrade on login (no manual intervention)

### Key Technical Decisions:
- **Manual downgrade/cancel:** Admin applies in Paddle Dashboard (safer than automation)
- **Graceful expiration:** Users keep access until period end, then auto-downgrade
- **Email logging:** Simple file-based + SMTP notifications (no complex queue)
- **Testing:** Dedicated admin endpoints for simulating webhooks

### Documents Created:
- `PHASE1-COMPLETE.md` — Full Phase 1 documentation
- `PHASE2-PLAN.md` — AI Content Engine roadmap
- `LIVECHECKLIST.md` — Pre-launch verification items

### Next: Phase 2 — AI Content Engine
**Focus:** Gemini API integration, hook generator, content calendar
**See:** `PHASE2-PLAN.md` for detailed timeline

---

## March 5, 2026 (12:00 UTC)

## March 6, 2026 — Self-Improvement Review Findings
**Status:** Hourly review cron producing redundant work; validated weekly cadence contradicts current automation.

### Key Finding: Cron Job Misalignment
**Problem:** Hourly self-improvement reviews directly contradict validated optimal cadence (weekly comprehensive + daily silent security checks).

**Impact:**
- 80% redundant analysis between 24-hour reviews
- Token waste on overlapping findings
- Diminishing analytical returns

**Action Required:**
- Disable hourly review cron (cron job 37621ee6-7a3e-4d37-becf-b6da1777cadd)
- Maintain: Weekly comprehensive reviews (Sundays)
- Maintain: Daily silent security checks
- Add: Incident-triggered reviews only (when errors occur)


---

## March 5, 2026 — Daily Memory Review Summary
**Status:** Pattern validation complete, review cadence confirmed optimal.

### Key Actions Completed
1. **Self-Improvement Review (02:03 UTC):** Automated 48-hour review validated weekly cadence, confirmed "Two Fix Rule" remains effective
2. **Security Posture:** A- maintained — no new exposures
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
2. **Security Posture:** B+ maintained — no new exposures
3. **MEMORY.md Updated:** Added escalation path visualization, updated day counts

### Current State
- **Code Activity:** None since March 3 (rest day)
- **Memory Health:** ✅ All files current, daily logs active
- **Review Cadence:** ✅ Validated — weekly comprehensive + daily silent security checks optimal

---

# Critical Context & Lessons Learned - Updated March 3, 2026 (22:00 UTC)

## Current Status Snapshot
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
**Security Posture:** Stable — no new exposures detected.
**Next Check:** Daily security check (silent) March 4; Day 10 reminder March 6.

## Daily Review Summary — March 3, 2026
**Key Finding:** Reduced review frequency fully validated — zero new activity since March 2 confirms security-only checks are sufficient on low-activity days.
**Lessons Learned:**
- Weekly comprehensive reviews + daily silent security checks = optimal balance
- No redundant reviews needed when no code changes or user interactions occurred
- Escalation schedule working as designed — user-action items tracked systematically

## Daily Review Summary — March 2, 2026
**Key Finding:** Review frequency reduced to weekly (Sundays) — overlapping reviews within 24h provide diminishing returns.

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
- Day 7: Urgent reminder
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

---

## Active Operations
See `DASHBOARD.md` for single source of truth on all blockers.

**Rule:** Maximum 3 P0 items. Complete before adding more.

---

## Infrastructure Blockers

---

## User Preferences
- Bullet points over walls of text
- Simple explanations with analogies
- Proactive but not pushy
- Honest about mistakes
- **If instructions are ambiguous or unclear — ask for clarification or confirmation before acting. Do not assume and execute. One wrong action wastes more time than one clarifying question.**
