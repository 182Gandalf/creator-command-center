# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-04-03 00:00 UTC

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
- [ ] **Admin signup date display** — Debug logging added; needs verification that date renders correctly
- [ ] **Cover Frame rollout** — Live for new scripts; older scripts will not show section (expected)

---

### 🚧 Pending — Needs Action

- [ ] **Verify admin signup dates** — Check browser console on /admin to confirm created_at is populated
- [ ] **Remove ENSEMBLEDATA_TOKEN from Railway** — SociaVault is live; old key is dead weight
- [ ] **Run `alembic upgrade head`** — Verify entertainment → music migration applied on Railway
- [ ] **Verify /admin stats load** — Confirm stats load correctly for admin email
- [ ] **Reach out to first user** — cooper238719831@gmail.com signed up; worth a personal welcome
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*

---

## 🎯 Next Priorities

### 🔴 Must Do
1. **Verify admin signup date rendering** — Open /admin, check browser console for "Signups data:" log, confirm created_at values present
2. **Verify entertainment → music migration ran** — Check Railway deploy logs for alembic errors
3. **Remove ENSEMBLEDATA_TOKEN from Railway** — Cleanup dead env var
4. **Fix persistent UX bugs** — Now 17–18+ days old — getting critical

### 🟡 Should Do
5. **Reach out to first beta user** — cooper238719831@gmail.com
6. **Verify Cover Frame in generated scripts** — Test that new scripts show COVER FRAME between Script Body and Caption
7. **Verify daily digest delivery** — Confirm beta users received emails

### 🟢 Nice to Have
8. **Google Trends fetch for new niches** — Will auto-run tonight at 3 AM UTC; no manual action needed
9. **Add `FROM_NAME` env var** in Railway

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| Persistent UX bugs (17-18 days) | MEDIUM | 🔴 Overdue | Pricing CTA, Studio label, Zapier gate, double loading render |
| Admin signup date not displaying | LOW | 🟡 Investigating | Debug logging added — needs verification |
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
