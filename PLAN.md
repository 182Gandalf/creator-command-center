# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-14 08:05 UTC

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

### ✅ Completed (March 13 — Full Day Sprint)

**Creator Pro Tier — COMPLETE**
- [x] Full implementation across 16 files: $25/mo monthly, $20/mo annual
- [x] 90-day calendar, daily digest, Zapier access
- [x] Save limit 20 (raised from sub-agent default of 15)
- [x] Paddle env vars documented (`PADDLE_PRICE_CREATOR_PRO_MONTHLY`, `PADDLE_PRICE_CREATOR_PRO_ANNUAL`)

**Success Compounder — COMPLETE**
- [x] Replaces "Niche Filtering" in taste profile
- [x] Users paste YouTube/TikTok/Instagram URLs → AI extracts content intelligence
- [x] Highest-priority signal in idea generation
- [x] DB table `video_signals` + alembic migration created
- [x] Sidebar UI with progress bar
- [x] FAQ + Help Guide updated with 3 new Q&As

**Interactive Landing Page Demo — COMPLETE**
- [x] `POST /api/demo/generate` endpoint with IP rate limit + 6hr cache
- [x] Niche + tone picker → 3 live AI idea cards
- [x] Button text evolves over 3 clicks
- [x] Conversion panel replaces cards on 3rd click
- [x] Animated logo as loading state

**pytrends & Digest Fixes — COMPLETE**
- [x] Rate limit fix: 150–200s delays, batch pauses, retry pass
- [x] Digest truncation fix: max_tokens 2000→4000, partial JSON salvage, skip placeholder emails

**Save Limits & Pricing**
- [x] Splash: 2→5 saves, Creator: 7→15 saves, Creator Pro: 20 saves
- [x] 14-day annual money-back guarantee on pricing page (both toggles + refund policy)

**UX Fixes**
- [x] Dashboard padding — all tabs + sidebar `!important` padding-bottom
- [x] Onboarding restart warning modal with taste profile reset warning
- [x] "Restart Onboarding" renamed from "Resume / Restart Onboarding"
- [x] Landing page copy: early access text + "Pending Beta Feedback" testimonials heading

**March 13 Evening — Admin & Zapier**
- [x] **Zapier webhook confirmed live** — `POST /webhooks/zapier` returns correct JSON (5 ideas + 5 scripts)
- [x] **`created_at` null fix** — `ContentIdea` model gets Python-side `default=datetime.utcnow`; Zapier route fallback added
- [x] **Admin feedback count** — per-user feedback tally column added to Last 10 Signups table
- [x] **CTA button alignment** — pricing summary section buttons now `margin-top: auto` (all 4 aligned)
- [x] **Feedback auth fix** — `submitFeedback()` now passes Clerk token so `user_id` is captured (was always NULL/anon)

---

### ✅ Completed (March 12 — Evening Sprint)

**Beta Readiness Pass — ALL 7 PARTS COMPLETE**
- [x] Loading states, error handling, input sanitization, mobile responsiveness
- [x] Admin dashboard — `/admin` + `/api/admin-ui/stats`
- [x] Feedback widget — Fixed bottom-right on 5 pages
- [x] Security audit — No hardcoded keys, all routes return 401/403 correctly

**Studio Features — ALL COMPLETE**
- [x] White-label PDF exports, 90-day calendar, daily trend digest, workspace switcher

**Content Pages**
- [x] FAQ page `/faq`, Help Guide `/help`, Zapier webhook

**Email & Deliverability**
- [x] Phase 5 email sequences — Creator weekly, Studio daily, Day 7 all live

---

### ✅ Completed (March 11 and Earlier)

- [x] Phase 1: Paddle Billing — full subscription lifecycle
- [x] Phase 2: AI Content Engine — Ideas, Hooks, Scripts, Calendar, Taste Profile
- [x] Phase 3: Personalization — Niche & Tone dropdown, onboarding data
- [x] Phase 4: Trend Intelligence — live scheduler, Trends tab, trend injection

---

### 🚧 Pending — Needs Action

- [x] **`alembic upgrade head`** — ✅ Done March 14 — `video_signals` table live
- [x] **Paddle Creator Pro products** — ✅ Done March 14 — env vars set in Railway
- [x] **Set `ADMIN_EMAIL=182gandalf@gmail.com`** — ✅ Done March 14
- [ ] **4-issue dashboard fix** — pricing grid layout, calendar nudge text, hooks button visibility, mobile hook button handlers (see details below)
- [ ] **Full beta test flow** — sign up → onboard → ideas → hooks → scripts → calendar → save → export
- [ ] **Mobile QA** — Real device test at 375px across all tabs
- [ ] **SPF record fix** — Add `include:amazonses.com` to Cloudflare DNS
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard

---

### 📋 4-Issue Dashboard Fix (Diagnosed, Not Yet Committed)

1. **Pricing grid 4-column layout** — `repeat(auto-fit, minmax(200px, 1fr))` → `repeat(4, 1fr)` at line ~423 of `pricing.html`
2. **Calendar nudge text** — Splash message: "Splash users have a 7-day calendar, upgrade to Creator to unlock up to 30 days. Upgrade to Creator →" (lines 3718-3720 of `dashboard-new.html`)
3. **Generate hook button missing on desktop** — `#hooks-initial-generate-btn` is inside `#hooks-idea-banner` which is `display:none`; needs to be exposed on desktop
4. **Mobile hook buttons not responding on 1st generated hook** — click handlers around lines 5808-5908 of `dashboard-new.html` need investigation

---

## 🎯 Today's Priorities (March 14)

### ✅ Blocking Items — ALL CLEARED (March 14 morning)
1. ~~**Run `alembic upgrade head`**~~ — ✅ Done
2. ~~**Create Creator Pro products in Paddle**~~ — ✅ Done
3. ~~**Set `ADMIN_EMAIL`**~~ — ✅ Done

### 🟡 Should Do
4. **Complete the 4-issue dashboard fix** — commit the diagnosed changes
5. **SPF record** — Add `include:amazonses.com` in Cloudflare (5 min job)
6. **Add `FROM_NAME` env var** in Railway
7. **Full beta test flow** — end-to-end user journey

### 🟢 Nice to Have
8. **Mobile QA** — 375px device or DevTools
9. **Check Railway logs** — pytrends nightly run (3 AM UTC) — did all 17 niches populate?

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| `alembic upgrade head` not run | HIGH | ✅ Done Mar 14 | Success Compounder live |
| Paddle Creator Pro products missing | HIGH | ✅ Done Mar 14 | Creator Pro checkout live |
| `ADMIN_EMAIL` not set | MEDIUM | ✅ Done Mar 14 | Admin dashboard stats live |
| SPF record missing Resend | MEDIUM | 🟡 Pending | Add `include:amazonses.com` in Cloudflare |
| Beta testing not done | HIGH | 🟡 Ongoing | Must complete before inviting users |

---

## 🔧 Phase Status Summary

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Paddle Billing | ✅ Complete | Full subscription lifecycle |
| Phase 2: AI Content Engine | ✅ Complete | Ideas, Hooks, Scripts, Calendar, Taste Profile |
| Phase 3: Personalization | ✅ Complete | Niche & Tone, onboarding, Success Compounder |
| Phase 4: Trend Intelligence | ✅ Complete | Live on Railway, scheduler running nightly 3 AM UTC |
| Phase 5: Email Sequences | ✅ Complete | Creator weekly, Studio daily, Day 7 onboarding |
| Beta Readiness (v0.1.0) | ✅ Complete | All 7 parts done and pushed |
| Creator Pro Tier | ✅ Complete | Pending Paddle product creation + Railway env vars |
| Phase 6: Post Scheduling | ⏳ Deferred | "Coming Soon" — post-launch |
| Real Workspace Isolation | ⏳ Deferred | Documented in FUTURE-FEATURES.md — on demand |

---

## 🎯 Daz's Open Action Items

1. [x] **`alembic upgrade head`** on Railway — ✅ Done March 14
2. [x] **Create Creator Pro products in Paddle** — ✅ Done March 14
3. [x] **Set `ADMIN_EMAIL=182gandalf@gmail.com`** in Railway — ✅ Done March 14
4. [ ] **SPF record** — Cloudflare → add `include:amazonses.com` *(5 min)*
5. [ ] **Add `FROM_NAME` env var** in Railway dashboard
7. [ ] **Beta test the full flow** — critical before first invite

---

## 📋 Before First Beta User Checklist

- [x] `alembic upgrade head` run on Railway (video_signals table) — ✅ Mar 14
- [x] Paddle Creator Pro products created + Railway env vars set — ✅ Mar 14
- [x] `ADMIN_EMAIL` set in Railway — ✅ Mar 14
- [ ] `/admin` page verified (stats load for admin email)
- [ ] Full sign-up → onboarding → generate → save → export flow tested
- [ ] Feedback widget tested on dashboard + pricing (now captures user_id ✅)
- [ ] Paddle checkout tested end-to-end (Splash → Creator upgrade)
- [ ] Monthly limit banner verified (shows correct reset date)
- [ ] Mobile test at 375px (ideas, hooks, calendar, onboarding)
- [ ] Railway deploy logs checked for migration errors
- [ ] SPF record updated in Cloudflare

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
