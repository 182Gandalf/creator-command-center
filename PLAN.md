# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-31 00:00 UTC

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

### ✅ Completed (March 31)

- [x] **Admin Dashboard v2** — Reddit and YouTube trends now visible in admin panel; user signups and beta feedback moved to top for priority visibility (`6d919ea`)
- [x] **Reddit + YouTube Trend Intelligence (Phase 2)** — AI prompts now include Reddit/YouTube trend context; `trend_source` field tracks which intelligence source inspired each idea (google_trends, reddit, youtube, seed, tweak, ai_generated) (`88b1832`)
- [x] **YOUTUBE_API_KEY added to Railway** — YouTube trend intelligence now fully operational

### ✅ Completed (March 30)

- [x] **Mobile onboarding header spacing fixed** — Padding, logo size, category chip grid all fixed for <640px (`846cf15`)
- [x] **Excel Bulk Export (Creator+ tiers)** — Ideas, Hooks, Scripts — exports freshly generated session content, not saved; locked for Splash (`cb3946f`, `eb7ec28`)
- [x] **Beta feedback widget captures user email** — Clerk JWT email extracted and stored; admin console shows email instead of user_id (`2f6ee3c`, `f5846c0`)
- [x] **Hook Video Direction feature** — AI generates 1-2 sentence visual direction for first 3 seconds; expandable on hook cards (▸/▾); appears between HOOK and SCRIPT BODY in script output; hook type alignment rules in prompt (`727bc1a`, `f4b6b58`, `4475ce7`)
- [x] **Reddit + YouTube Trend Intelligence (Phase 1)** — Unified NICHE_CONFIG (20 niches × subreddits + YouTube queries), new DB tables (reddit_trends, youtube_trends), Reddit public .json fetch (no API key), YouTube Data API v3, trend aggregation service, scheduler updated (Reddit 02:00+14:00, YouTube 03:00)

### ✅ Completed (March 29)

- [x] **Default tier changed from Splash → Creator** — All user creation paths updated
- [x] **Pricing page — collapsible feature categories accordion** — Synced across all 4 tiers
- [x] **"Creator+" renamed to "Creator Pro" site-wide**
- [x] **Admin email notification for new signups**
- [x] **First real user signed up** — cooper238719831@gmail.com

### ✅ Completed (March 26–28)

- [x] **Site recovered from HTTP 500 outage**
- [x] **Discord links added to footer**
- [x] **Hero trust micro-copy fixed** — "30-day calendar" → "7-day calendar on Splash"

### ✅ Completed (March 22 and Earlier)

- [x] All Phase 1–5 work, beta readiness, Paddle billing, AI engine, personalization, trend intelligence v1, email sequences

---

### 🚧 In Progress

Nothing currently in progress.

---

### 🚧 Pending — Needs Action

- [ ] **Admin page verified** — confirm stats load correctly for admin email
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*
- [ ] **Railway deploy logs** — Check for migration errors post-deploy
- [ ] **Run `alembic upgrade head`** — Apply new migrations (reddit_trends, youtube_trends, trend_source)
- [ ] **Reach out to first user** — cooper238719831@gmail.com signed up; worth a personal welcome

---

## 🎯 Next Priorities

### 🔴 Must Do
1. **Run `alembic upgrade head`** on Railway — Apply pending migrations
2. **Verify /admin stats** — confirm stats load correctly for admin email
3. **Check Railway deploy logs** — Verify no migration errors post-deploy

### 🟡 Should Do
4. **Reach out to first beta user** — cooper238719831@gmail.com
5. **Verify YouTube trend fetch** — confirm daily fetch at 03:00 UTC works with new API key

### 🟢 Nice to Have
6. **Add `FROM_NAME` env var** in Railway

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| alembic upgrade head not run | MEDIUM | 🔴 Pending | New tables (reddit_trends, youtube_trends, trend_source) won't exist until migration runs |
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
| Phase 4b: Trend Intelligence v2 | ✅ Complete | Reddit + YouTube signals, trend_source tracking |
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
- [ ] Railway deploy logs checked for migration errors
- [ ] /admin verified (stats load for admin email)
- [ ] YOUTUBE_API_KEY added to Railway

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
