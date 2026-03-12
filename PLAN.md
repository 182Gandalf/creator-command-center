# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-12 08:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 🚀 Launch Status: **Shipping when ready**

---

## 📊 Current Status

### ✅ Completed (March 12 — Today)

- [x] **DB migration** — `alembic upgrade head` run, `trending_topics` + `calendars` tables live on Railway
- [x] **Trends tab** — wired up to real DB data (score bars, meta, empty state)
- [x] **pytrends urllib3 fix** — pinned `urllib3<2` in requirements.txt, pushed to Railway
- [x] **Scheduler improved** — delay increased to 60s + random jitter, moved to 3 AM UTC
- [x] **SerpAPI migration plan** — documented as TRENDS-001 in DASHBOARD.md (trigger: first paying users)
- [x] **Extended trends plan** — documented as TRENDS-002 in DASHBOARD.md (after TRENDS-001)

### ✅ Completed (March 11 — Full Day)

**Phase 3: Personalization — COMPLETE**
- [x] "Current Niche & Tone" panel added to header dropdown
- [x] Shows Niche, Tone, Goal, Audience (if set), Platforms with brand SVG icons
- [x] Populated from `/api/creator-profile` on load — auto-refreshes after onboarding resubmit
- [x] `/api/creator-profile` GET extended with content_goal, audience_description, content_types, content_struggle, forbidden_topics

**Phase 4: Trend Intelligence — COMPLETE** ✨
- [x] `pytrends` added to requirements.txt
- [x] `TrendingTopic` model + migration live on Railway
- [x] `services/trends.py` — async fetch, 429 handling, DB storage
- [x] Scheduler: daily trend fetch at 3:00 AM UTC, 17 niches, 60s+jitter delay
- [x] `GET /api/trends/current` endpoint — returns trends for user's niche (last 24h), supports `?limit=` param
- [x] Trend injection in idea generation — non-fatal, additive only
- [x] Dashboard trend pills — 🔥 pill bar above Generate Ideas button
- [x] Splash sees 1 pill + 🔒 upsell; Creator/Studio see all 3
- [x] Trends tab — live data from DB with score bars, timestamps, empty state

**Calendar Fixes**
- [x] 7-day blur filters by date_offset (day-based)
- [x] Splash frequency locked to 3×/week (UI + backend)
- [x] Brand SVG icons on calendar cards
- [x] Script button on all calendar cards

**Platform & Workspace Fixes**
- [x] Platform tab click persists to workspace
- [x] Workspace scoped per Clerk user ID (no cross-account leakage)
- [x] Primary platform no longer overrides idea platform

**Phase 2 + Polish (March 9–11)**
- [x] Script generation uses active hook word-for-word
- [x] Pricing page finalized across all 3 plans
- [x] Splash tier limits final: 20 ideas/month, 2 saves each, 3/5 hooks, TikTok only, 1 tweak/week
- [x] Creator save limits: 7 each
- [x] Onboarding Q6-10 blurred for Splash with upgrade overlay
- [x] Content Calendar fully built and integrated
- [x] Mobile button fixes, animated logo loading, hooks polish

---

### 🚧 Pending (No Target Date — Ship When Ready)

- [ ] **Beta Testing** — Full end-to-end test: sign up → onboard → ideas → hooks → scripts → calendar → save → export
- [ ] **Mobile QA** — Verify all sections on device
- [ ] **TikTok Secret Rotation** — Blocked on Daz (P0, security risk, day 14+ overdue)
- [ ] **FAQ page content** — `/faq` currently 404s — Daz to provide Q&As
- [ ] **Launch announcement** — What to post/send on launch day

---

## 🎯 Current Priorities

### 🔴 Needs Daz Action
1. **TikTok secret rotation** — Security risk, overdue
2. **Beta test the full flow** — Biggest pre-launch risk
3. **FAQ content** — Send Q&As when ready

### 🟡 High Priority (Dev)
4. **Mobile QA** — Full device test across all tabs
5. **Pricing page final check** — Confirm all limits accurate
6. **Marketing copy review** — Index page aligned with current features?

### 🟢 Nice to Have
7. **Launch announcement prep** — Copy for social/email

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| TikTok Secret Rotation | HIGH | 🔴 Critical | Daz action required — day 14+ overdue |
| Beta testing not done | HIGH | 🟡 Ongoing | Must complete before launch |
| FAQ page no content | MEDIUM | 🟡 Pending | Daz to provide Q&As |
| Trend pills empty on new accounts | LOW | ✅ Expected | Scheduler runs 3 AM UTC, populates overnight |

---

## 🔧 Phase Status Summary

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Paddle Billing | ✅ Complete | Full subscription lifecycle |
| Phase 2: AI Content Engine | ✅ Complete | Ideas, Hooks, Scripts, Calendar, Taste Profile |
| Phase 3: Personalization | ✅ Complete | Niche & Tone dropdown, onboarding data surfaced |
| Phase 4: Trend Intelligence | ✅ Complete | Live on Railway, scheduler running nightly at 3 AM UTC |
| Phase 5: Email Sequences | ⏳ Deferred | Post-launch |
| Phase 6: Post Scheduling | ⏳ Deferred | "Coming Soon" |

---

## 🎯 Daz's Open Action Items

1. [ ] **Beta test the full flow** — sign up, onboard, generate, save, export calendar
2. [ ] **TikTok secret rotation** — CRITICAL security risk, day 14+ overdue
3. [ ] **FAQ content** — send Q&As so the /faq page can go live

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space
- **Dashboard:** https://flowcast.space/dashboard
- **Pricing:** https://flowcast.space/pricing
- **FAQ:** https://flowcast.space/faq (⚠️ needs content)
- **GitHub:** https://github.com/182Gandalf/FlowCast
- **Railway Dashboard:** https://railway.app/dashboard

---

*Updated manually. No fixed launch date — shipping when ready.*
