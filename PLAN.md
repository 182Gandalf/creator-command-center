# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-04-05 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 🚀 Launch Status: **Beta Ready — v0.1.0**

---

## 📊 Current Status

### ✅ Completed (April 4)

- [x] **CTA/footer gap fixed** — Removed `margin-top: 4rem` from footer and reduced CTA `padding-bottom` from 80px → 32px (`commit: landing page footer gap fix`)
- [x] **Tweak button upgraded messaging** — "Regenerate with Tweaks" button now shows "Want more ideas? Upgrade now." and redirects to `/pricing` when Splash user is at 0 tweaks; counter shows "0" in red
- [x] **Trends tab link fixed** — "Visit the Trends Tab for More →" was calling non-existent `switchIdeasTab()` — corrected to `navigate('trends')`
- [x] **Generate Ideas button upgraded messaging** — `updateIdeaCounter()` now updates button text to "💎 Want more ideas? Upgrade now." when Splash user hits 0 remaining ideas
- [x] **TXT Downloads added to all pricing tiers** — Added to Saves & Exports section for Splash, Creator, Creator Pro, and Studio
- [x] **Reddit scheduler KeyError fixed** — Scheduler was referencing `result['total_posts']`; corrected to `result['total_new']` and `result['total_updated']`
- [x] **Reddit 429 retry logic added** — Exponential backoff (5s, 10s, 20s) with 3 retries per subreddit; delay increased from 2s → 3s

### ✅ Completed (April 3)

- [x] **Admin signup dates fixed** — Clerk webhook now extracts `created_at` from payload (ms → UTC); backfill endpoint added and run — all 28 users now have correct dates
- [x] **Admin table mobile fixes** — Font size reduced, email wrapping fixed, sorting with nulls last
- [x] **Beta feedback shows user email** — Backend now looks up user email from users table when beta_feedback.email is null
- [x] **Billing page Creator Pro tier** — Added `creator_pro` to planDetails JS object (was showing Splash info for Pro users)
- [x] **"Invalid Date" fix on account page** — Scheduled cancellation message no longer uses non-existent `effective_date` field
- [x] **Welcome/upgrade email text brightened** — Feature list and tip text changed from `#94a3b8` → `#e2e8f0` for better readability on dark backgrounds
- [x] **FAQ and Help Guide major update** — Added Creator Pro tier throughout, all 4 trend sources, TikTok Sounds section, Cover Frame section, Excel export, Zapier Integrations section, Studio workspaces note
- [x] **Pricing page toggle bug fixed** — Summary section buttons were defaulting to monthly; fixed to match annual toggle default
- [x] **Landing page double bullets fixed** — Comparison section had both hardcoded `•` and CSS `::before` bullets on mobile
- [x] **Paddle checkout tax ID field** — Added `showAddTaxId: true` and `showAddDiscountCode: true` to Paddle.Initialize checkout settings
- [x] **Ideas counter turns orange at limit** — Splash users see orange counter + "Want more ideas? Upgrade now." button + explanatory message when at 20/20
- [x] **Excel export locked to Creator Pro+** — Splash and Creator users see 🔒 locked buttons with hover tooltip "Available only on Creator Pro and above"
- [x] **Pricing page: "Saves & Exports"** — Renamed from "Saves & Storage"; Excel and PDF export rows added per tier
- [x] **Pricing page: Creator tier cleanup** — Removed "All tones + custom voice input" and "Full Taste Profile"; added "Full Taste Profile Unlocked"; Hook Scorer line moved and reworded
- [x] **Pricing page: Studio Trend Intelligence** — Matched to Creator Pro exactly (removed "Enhanced" and "Daily alerts" lines)
- [x] **Pricing page: Studio Workflow** — Matched to Creator Pro; updated to "5 workspaces" and "Priority support (24h response)"
- [x] **Pricing page: Studio Personalization** — Matched to Creator Pro exactly; "Full Taste Profile Unlocked" line added
- [x] **Pricing page: Studio Workspaces section** — Renamed from "Agency Economics"; updated with workspace-focused copy
- [x] **Local backup created** — Full codebase snapshot at `backups/flowcast_backup_20260403_090218/` (522 MB)

### ✅ Completed (April 2)

- [x] **Platform logos on landing page demo cards** — Replaced emojis with actual SVG logos for TikTok, Reels, Shorts (`772e9c2`)
- [x] **Mobile: trend pills limited to 2 lines** — Each source capped with "Visit the Trends Tab for More →" link (`12a83da`)
- [x] **Bulk Excel export for Saved Ideas tab** — Matches saved hooks and saved scripts pattern (`d9e638a`)
- [x] **TikTok sound context display** — Context shown on pills (tooltip) and in Trends tab (pink text) (`ae15c51`)
- [x] **TikTok sound deduplication** — Removed duplicate sound titles, keeps highest usage_count entry (`d9f2907`)
- [x] **Niche restructure: entertainment → movies, tv, music, self_improvement** — 20 → 23 niches across all pipelines (`d20e110`)
- [x] **Alembic migration fix** — Revision ID shortened to fit varchar(32) limit (`30944cf`)
- [x] **All 23 niches in landing page demo dropdown** — Backend VALID_NICHES also updated (`cf2b07d`)
- [x] **Manual trend fetch for new niches** — Reddit, YouTube, TikTok fetched for music/movies/tv/self_improvement
- [x] **TikTok queries expanded 2 → 5 per niche** — All 23 niches now have richer search coverage (`47b750f`)
- [x] **Cover Frame feature** — AI generates one-sentence cover/thumbnail suggestion per platform in script output (`eb1264c`)
- [x] **Admin page: All Signups** — Removed 10-user limit, shows all users with signup date (`4e4a884`)
- [x] **Admin page: signup date debugging** — Explicit date formatting + console logging to diagnose display issue (`79d851c`)
- [x] **Button order fix** — Generate 5 New Ideas now appears before Excel Export

### ✅ Completed (April 1)

- [x] **Hero copy refresh** — "Personalized Content Intelligence Engine" + "personalized scored hooks" (`d570666`)
- [x] **Trend UI consolidation** — 4 trend sources merged into single expandable button in Ideas tab
- [x] **TikTok sound suggestions in scripts** — Pink-styled `sound_suggestion` field in dashboard scripts
- [x] **Daily digest endpoints** — `/digest-status`, `/send-daily-digest-to-all`, `/send-digest-to-user` added
- [x] **TikTok sound context enrichment** — `sound_context` column added to DB; AI generates 8-12 word descriptions per sound

### ✅ Completed (March 22–31)

- [x] All Phase 1–5 work, beta readiness, Paddle billing, AI engine, personalization, trend intelligence (Google + Reddit + YouTube + TikTok), email sequences, mobile fixes, Excel exports, Hook Video Direction, admin dashboard v2, Success Compounder, SociaVault TikTok migration

---

### 🚧 In Progress

- [ ] **Sound context population** — cron filling remaining sounds over next few runs
- [ ] **Excel export lock for Creator** — Button still active for Creator users despite lockExportButtons() — delayed DOMContentLoaded fix pushed, needs verification
- [ ] **Paddle tax ID field** — showAddTaxId set in Paddle.Initialize; needs verification in live checkout
- [ ] **Reddit 429 rate limiting** — Railway IP may be blocked by Reddit; retry logic added but if block is IP-level, frequency reduction or proxy needed

---

### 🚧 Pending — Needs Action

- [ ] **Remove ENSEMBLEDATA_TOKEN from Railway** — SociaVault is live; old key is dead weight
- [ ] **Run `alembic upgrade head`** — Verify entertainment → music migration applied on Railway
- [ ] **Reach out to first user** — cooper238719831@gmail.com signed up; worth a personal welcome
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*
- [ ] **Verify Excel export lock works for Creator** — Daz reported it was still active; fix pushed, needs confirmation

---

## 🎯 Next Priorities (April 5)

### 🔴 Must Do
1. **Investigate Reddit IP block** — Confirm if Railway's IP is permanently blocked or temporary throttle; consider reducing fetch frequency from 4x → 1x daily
2. **Verify Excel export locked for Creator** — Confirm 🔒 tooltip shows and export is blocked
3. **Verify Paddle tax ID field visible** — Confirm "Add tax number" field shows in checkout
4. **Fix persistent UX bugs** — Now 20+ days old — critical

### 🟡 Should Do
5. **Remove ENSEMBLEDATA_TOKEN from Railway** — Cleanup dead env var
6. **Reach out to first beta user** — cooper238719831@gmail.com
7. **Verify entertainment → music migration ran** — Check Railway deploy logs for alembic errors

### 🟢 Nice to Have
8. **Add `FROM_NAME` env var** in Railway

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| Persistent UX bugs (20+ days) | MEDIUM | 🔴 Overdue | Pricing CTA, Studio label, double loading render |
| Reddit 429 rate limiting | MEDIUM | 🔴 Active | Railway IP may be blocked; sports/politics/DIY data stale |
| Excel export not locking for Creator | LOW | 🟡 Investigating | Fix pushed with delayed DOM load — needs verification |
| Paddle tax field not visible | LOW | 🟡 Investigating | showAddTaxId added to Initialize — needs live test |
| Entertainment migration not verified | MEDIUM | 🟡 Monitor | Check Railway deploy logs |
| FROM_NAME env var | LOW | 🟢 Backlog | Emails work without it |

---

## 🔧 Phase Status Summary

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Paddle Billing | ✅ Complete | Full subscription lifecycle |
| Phase 2: AI Content Engine | ✅ Complete | Ideas, Hooks, Scripts, Calendar, Taste Profile |
| Phase 3: Personalization | ✅ Complete | Niche & Tone, onboarding, Success Compounder |
| Phase 4: Trend Intelligence v1 | ✅ Complete | Google Trends live, nightly at 3 AM UTC |
| Phase 4b: Trend Intelligence v2 | ✅ Complete | Reddit + YouTube + TikTok signals, trend_source tracking |
| Phase 4c: TikTok Sound Intelligence | ✅ Complete | SociaVault, 6K credits, music fetch, sound context AI |
| Phase 5: Email Sequences | ✅ Complete | Creator weekly, Studio daily, Day 7 onboarding |
| Beta Readiness (v0.1.0) | ✅ Complete | All 7 parts done and pushed |
| Creator Pro Tier | ✅ Complete | Live — Paddle + Railway env vars set |
| Niche Expansion | ✅ Complete | 20 → 23 niches; entertainment replaced by movies/tv/music/self_improvement |
| Cover Frame Feature | ✅ Complete | Per-platform cover/thumbnail suggestions in all script outputs |
| Phase 6: Post Scheduling | ⏳ Deferred | "Coming Soon" — post-launch |

---

## 📋 Before First Beta User Checklist

- [x] Full sign-up → onboarding → generate → save → export flow tested ✅
- [x] Paddle checkout tested end-to-end ✅
- [x] Mobile test at 375px ✅
- [x] Admin email notification on signup ✅
- [x] YOUTUBE_API_KEY added to Railway ✅
- [ ] Railway deploy logs checked for migration errors
- [ ] /admin verified (stats load + signup dates show)

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space
- **Dashboard:** https://flowcast.space/dashboard
- **Admin:** https://flowcast.space/admin
- **Pricing:** https://flowcast.space/pricing
- **FAQ:** https://flowcast.space/faq
- **Help:** https://flowcast.space/help
- **GitHub:** https://github.com/182Gandalf/FlowCast
- **Railway Dashboard:** https://railway.app/dashboard

---

*No fixed launch date — shipping when ready.*
