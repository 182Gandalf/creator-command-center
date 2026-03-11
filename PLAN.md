# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-11 00:00 UTC  
**Next Update:** 2026-03-12 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 🚀 Launch Countdown: **2 days to Friday March 13**

---

## 📊 Current Status

### ✅ Completed (March 11) — UI Polish, Calendar, Bug Fixes

**Content Calendar (Phase 2 Feature 4 — COMPLETE)**
- [x] `calendars` table added to models.py (id, user_id, generated_at, entries JSON)
- [x] Migration file: `2024_03_12_calendars.py`
- [x] `routers/calendar.py` — POST /api/calendar/generate, GET /api/calendar/latest
- [x] GET /api/calendar/export/ics — Google Calendar export with VEVENT (9am–9:30am)
- [x] GET /api/calendar/export/csv — Notion CSV export with import note in UI
- [x] Calendar embedded inline in dashboard (no redirect, reuses Clerk session)
- [x] Week-by-week grid — platform emoji, date, title, hook, Copy Hook button
- [x] Tier gating: Splash sees 7 entries (blur + upgrade overlay for remainder)
- [x] Notion import note: "To import into Notion: open your database → Import → CSV"
- [x] AI prompt matches exact spec; robust parser handles date strings vs integers
- [x] `icalendar>=5.0.0` added to requirements.txt

**UI Polish**
- [x] FAQ link added to footer on all pages (dashboard, pricing, index, terms, privacy, refund)
- [x] "What's Next?" guidance card added to Hooks page (empty state + after results)
- [x] Calendar nav item restored to inline navigate('calendar') — no page redirect

**Bug Fixes**
- [x] Calendar: `date_offset` validation error — AI returned date string instead of int
- [x] Calendar: Robust `coerce_entry()` parser handles date strings, missing fields, alt field names

---

### ✅ Completed (March 10) — Taste Profile + Mobile Polish

- [x] Taste Profile System (8 items × 12.5% each):
  - Idea Evolution (7-day timer from account creation)
  - Niche Filtering (7-day timer from account creation)
  - Splash capped at 25% (items 1-2 only)
- [x] Animated logo loading on all AI generation (Ideas, Hooks, Scripts, Tweaks, Scoring)
- [x] Sidebar: 36×36px animated logo on loop
- [x] Mobile "Generate 5 New Ideas" button — final fix via addEventListener + touchend
- [x] Hooks: index-based reference for Copy Hook (no escaping bugs)
- [x] Generated hooks persist across tab navigations (localStorage cached)
- [x] Hooks: persist across nav, empty state on delete

---

### ✅ Completed (March 11 earlier) — Pricing + Script Fixes + Onboarding

- [x] Script generation now uses active hook word-for-word
- [x] Platform-specific hooks (TikTok/Reels/Shorts tailored AI guidance)
- [x] Rich idea context for script generation (full platform hooks + remix variant)
- [x] Pricing page: all 3 plans aligned — Content Ideation → Saves & Storage → Personalization → Workflow
- [x] Splash tier limits final: 20 ideas/month, 2 saves each, 3/5 hooks, TikTok only, 1 tweak/week
- [x] Onboarding: Splash sees Q1-5 only, Q6-10 blurred with "🔒 Upgrade" overlay
- [x] Onboarding: Monthly idea counter preserved when redoing onboarding
- [x] Onboarding: Tier check runs reliably on all page loads
- [x] 1-inch (96px) bottom gap on left panel and content area
- [x] Tweaks button text: "Generate 5 Fresh Ideas with Tweaks"

---

### ✅ Completed (March 9) — Save/Hooks/Scripts/Mobile

- [x] Saved Ideas: ⭐ button saves to database, counter shows Splash 1/1 limit
- [x] Saved Hooks: Save from hook generator, view in Saved section
- [x] Saved Scripts: Save from scripts tab, view in Saved section
- [x] Hook Scorer inline in dashboard (right panel of Hooks section)
- [x] Hook scoring: 1 score → 3 distinct rewrites (not duplicates)
- [x] Mobile footer: slim single-line, anchored, no content overlap
- [x] Mobile: `html { font-size: 14px }` scales whole app
- [x] Scripts context: SVG platform icons replace emojis
- [x] "Upgrade to Creator" CTA hidden for non-Splash users
- [x] `showToast()` replaces `alert()` everywhere (mobile-safe)

---

### 🚧 In Progress / Pending for Launch

- [ ] **Beta Testing** — Full end-to-end test on all features before Friday launch
- [ ] **TikTok Secret Rotation** — Still blocked on user action (P0, Day 14+ old)
- [ ] **Post Scheduling / Publishing** — Post Coming Soon (deferred to Phase 3)
- [ ] **Trend Intelligence** — Placeholder showing (deferred to Phase 3)

---

## 🎯 Today's Priorities (March 11 → 12, 2026)

### 🔴 Critical (Launch Prep — 2 Days Left)
1. **Beta Testing** — Full flow test: sign up → onboard → generate ideas → hooks → scripts → calendar
2. **Mobile QA** — Test all critical paths on mobile (known issues were fixed but need verification)
3. **Fix any regressions** — Calendar generation working? All 3 tiers rendering correctly?
4. **Export testing** — Verify .ics opens in Google Calendar, .csv imports into Notion

### 🟡 High Priority
5. **FAQ page** — Populate /faq with common questions (link is live but page returns 404)
6. **Error states** — Ensure all errors are user-friendly (no raw stack traces shown)
7. **Onboarding edge cases** — What happens if user skips fields?

### 🟢 Nice to Have (If Time)
8. **Marketing copy review** — Index page copy aligned with current feature set?
9. **Pricing page final check** — All plan descriptions accurate?
10. **Launch announcement** — Prepare what to post/send on Friday

---

## 📅 Weekly Roadmap

### Week of Mar 9 - Mar 15 (LAUNCH WEEK)
- **Monday (Mar 9):** ✅ Save features, hook scorer inline, mobile fixes
- **Tuesday (Mar 10):** ✅ Taste profile, animated logo, mobile button fixes
- **Wednesday (Mar 11):** ✅ Pricing polish, script fixes, onboarding, Content Calendar
- **Thursday (Mar 12):** 🔴 Beta testing, bug fixes, launch prep, FAQ page
- **Friday (Mar 13):** 🚀 **LAUNCH DAY**
- **Weekend:** Marketing, user onboarding support

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| TikTok Secret Rotation | HIGH | 🔴 Overdue | Day 14+ — user action required |
| FAQ page missing content | MEDIUM | 🟡 Today | Link is live, page is blank |
| Beta testing not done | HIGH | 🔴 Today | Must test before Friday launch |
| Calendar AI generation | MEDIUM | ✅ Fixed | Date-string parsing bug resolved |

---

## 🔧 Phase 2 Feature Status

| Feature | Status | Notes |
|---------|--------|-------|
| 1. Save Ideas / Hooks / Scripts | ✅ Complete | Splash: 2 saves each |
| 2. Hook Generator + Scorer | ✅ Complete | Inline in dashboard |
| 3. Script Generator | ✅ Complete | Platform-specific, uses active hook |
| 4. Content Calendar | ✅ Complete | AI-generated, ICS + CSV export |
| 5. Taste Profile | ✅ Complete | 8 items, unlocks over time |
| 6. Trend Intelligence | ⏳ Deferred | Placeholder only (Phase 3) |
| 7. Post Scheduling | ⏳ Deferred | "Coming Soon" (Phase 3) |

---

## 📝 Daily Notes

### 2026-03-11 (Midnight) — PLAN.md Update
- 2 days to launch — all Phase 2 features complete except deferred ones
- Content Calendar built and integrated into dashboard
- Calendar generation bug fixed (AI returning date strings)
- Notion import note added to UI per spec
- Tomorrow: beta testing is the priority, then FAQ page content

### 2026-03-10
- Taste profile, animated logo, mobile button war resolved
- Hooks persist across navigation
- All major UX issues addressed

### 2026-03-09
- Huge output day: save features, hook scorer, scripts, mobile fixes
- 20+ commits

---

## 🎯 Daz's Action Items (Before Friday)

1. [ ] **Beta test the full flow** — sign up, onboard, generate, save, export calendar
2. [ ] **TikTok secret rotation** — please do this ASAP (security risk)
3. [ ] **FAQ content** — send me the Q&As to populate the FAQ page
4. [ ] **Approve launch** — green light on Friday or push to next week?

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space
- **Dashboard:** https://flowcast.space/dashboard
- **Calendar:** https://flowcast.space/dashboard (Calendar tab)
- **Pricing:** https://flowcast.space/pricing
- **FAQ:** https://flowcast.space/faq (⚠️ needs content)
- **GitHub:** https://github.com/182Gandalf/FlowCast
- **Railway Dashboard:** https://railway.app/dashboard

---

*Updated automatically at midnight UTC. Next update: March 12, 2026.*
