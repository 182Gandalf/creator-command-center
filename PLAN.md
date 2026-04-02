# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-04-02 00:00 UTC

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

### ✅ Completed (April 1)

- [x] **Hero copy refresh** — "Personalized Content Intelligence Engine" + "personalized scored hooks" (`d570666`)
- [x] **Trend UI consolidation** — 4 trend sources merged into single expandable button in Ideas tab
- [x] **Blur effect for Splash users** — Reddit/YouTube/TikTok trends blurred; Google Trends stays clear
- [x] **TikTok sound suggestions in scripts** — Pink-styled `sound_suggestion` field in dashboard scripts
- [x] **Daily digest endpoints** — `/digest-status`, `/send-daily-digest-to-all`, `/send-digest-to-user` added
- [x] **TikTok sound context enrichment** — `sound_context` column added to DB; AI generates 8-12 word descriptions per sound
- [x] **Async fix for sound context generation** — Functions made async; AI calls now properly awaited
- [x] **TikTok cron Phase 5** — Context generation runs automatically after each fetch cycle
- [x] **Discord links in footer** — Added to pricing, faq, help pages (`fe9cbca`)
- [x] **Hero calendar copy fix** — "30-day calendar" → "7-day calendar on Splash" (`2157c30`)
- [x] **Landing page demo enhanced** — Engagement predictions, viral probability, hook scores, content angles
- [x] **Demo fallback mock data** — Demo always works even if AI parsing fails
- [x] **Demo switched to Anthropic** — Higher quality output for landing page

### ✅ Completed (March 31)

- [x] **TikTok migrated from EnsembleData → SociaVault** — New API, x-api-key auth, dict-to-list aweme_list handling, /music/popular + /trending endpoints, credit tracking, 402 failsafe (`783cd6a`)
- [x] **Success Compounder added to Creator Pro pricing card** — Upgrade path from Splash → Creator Pro now complete (`dbc7851`)

### ✅ Completed (March 22–30)

- [x] All Phase 1–5 work, beta readiness, Paddle billing, AI engine, personalization, trend intelligence (Google + Reddit + YouTube + TikTok), email sequences, mobile fixes, Excel exports, Hook Video Direction, admin dashboard v2

---

### 🚧 In Progress

- [ ] **Sound context population** — 7/96 sounds have AI contexts; cron will fill remaining over next few runs
- [ ] **Verify daily digest delivery** — 26 eligible beta users; confirm emails received

---

### 🚧 Pending — Needs Action

- [ ] **Remove ENSEMBLEDATA_TOKEN from Railway** — SociaVault is live; old key is dead weight
- [ ] **Admin page verified** — confirm stats load correctly for admin email
- [ ] **Run `alembic upgrade head`** — Verify migration applied on Railway (`sound_context` column)
- [ ] **Reach out to first user** — cooper238719831@gmail.com signed up; worth a personal welcome
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*

---

## 🎯 Next Priorities

### 🔴 Must Do
1. **Verify sound suggestion format in generated scripts** — Test that `sound_suggestion` now shows in TikTok scripts with correct format: `🎵 "Sound Name" by @artist (245K videos) — specific direction`
2. **Verify daily digest delivery** — Confirm all 26 beta users received emails; trigger again if needed
3. **Remove ENSEMBLEDATA_TOKEN from Railway** — Cleanup dead env var
4. **Verify /admin stats** — confirm stats load correctly for admin email

### 🟡 Should Do
5. **Reach out to first beta user** — cooper238719831@gmail.com
6. **Fix persistent UX bugs** — 5 bugs open 15–16+ days (see MEMORY.md bug tracker)
   - Dashboard double "Loading trends…" render
   - Pricing page closing section — no CTA button
   - Studio plan "Everything in Creator, plus:" → should say "Creator Pro"
   - Dashboard "Use this hook" instruction misplaced
   - Creator plan lists Zapier as "(Creator Pro+)" in paid plan

### 🟢 Nice to Have
7. **Add `FROM_NAME` env var** in Railway
8. **Daily auto-fetch for all niches** — Digest emails need sounds for all niches, not just rotation group

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| 5 persistent UX bugs (15–16 days) | MEDIUM | 🔴 Overdue | See MEMORY.md bug tracker |
| alembic upgrade head not verified | MEDIUM | 🟡 Monitor | sound_context column — run-migration endpoint returned success |
| Idea generation reliability | MEDIUM | 🟡 Monitor | Fallback chain fixed, needs production verification |
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
| Phase 6: Post Scheduling | ⏳ Deferred | "Coming Soon" — post-launch |

---

## 📋 Before First Beta User Checklist

- [x] Full sign-up → onboarding → generate → save → export flow tested ✅
- [x] Paddle checkout tested end-to-end ✅
- [x] Mobile test at 375px ✅
- [x] Admin email notification on signup ✅
- [x] YOUTUBE_API_KEY added to Railway ✅
- [ ] Railway deploy logs checked for migration errors
- [ ] /admin verified (stats load for admin email)

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
