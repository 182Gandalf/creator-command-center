# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-13 00:00 UTC

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

### ✅ Completed (March 12 — Evening Sprint)

**Beta Readiness Pass — ALL 7 PARTS COMPLETE**
- [x] **Loading states** — All AI buttons show niche-personalised loading messages, disable on click, re-enable on response
- [x] **Error handling** — `AIServiceException` caught across all routes; global `showBanner()` (red/amber, dismissible); no tracebacks ever shown
- [x] **Input sanitization** — `services/sanitize.py` created; HTML escape, 500-char max, 6 injection phrases blocked
- [x] **Mobile responsiveness** — Media queries at 480px + 375px across dashboard, onboarding, pricing; 44px tap targets; iOS zoom fix
- [x] **Admin dashboard** — `/admin` + `/api/admin-ui/stats` (403 for non-admins); shows user counts by tier, ideas today, last 10 signups, all feedback
- [x] **Feedback widget** — Fixed bottom-right on 5 pages; `POST /feedback` → `beta_feedback` table; Alembic migration created
- [x] **Security audit** — No hardcoded keys, all routes return 401/403 correctly, Paddle keys env-var only, `.env` not in git

**Studio Features — ALL COMPLETE**
- [x] **White-label PDF exports** — Scripts, hooks, content-pack, calendar; brand settings modal in sidebar (Studio only)
- [x] **90-day calendar** — Backend confirmed; lock banner shown to non-Studio users
- [x] **Daily trend digest email** — Scheduler running at 07:00 UTC
- [x] **Workspace switcher** — UI complete; greyed out + "In development" notice added; backend isolation documented in FUTURE-FEATURES.md

**Content Pages**
- [x] **FAQ page** — `/faq` live; 35 questions, 8 sections, live search, accordion
- [x] **Help Guide** — `/help` live; 9 sections, sticky TOC, mobile header collision fixed
- [x] **Zapier webhook** — `POST /webhooks/zapier`; API key management in Settings > Integrations

**Email & Deliverability**
- [x] **Phase 5 email sequences** — Creator weekly digest, Studio daily digest, Day 7 email all live
- [x] **Deliverability hardened** — Plain-text versions, List-Unsubscribe headers, personal Day 7 email
- [x] **OG image** — Updated to 1200×630 from brand reference JPG (`?v=3` cache busted)

**Bug Fixes**
- [x] Ideas counter bug fixed — was reading `User.splash_ideas_used_this_month` (never written); now reads `CreatorProfile.splash_ideas_used_this_month`
- [x] Animated logos — all 13 templates use `<video autoplay loop muted playsinline>` (no more static `logo.jpg`)

---

### ✅ Completed (March 12 — Morning)

- [x] Trends tab wired to real DB data
- [x] pytrends urllib3 fix
- [x] Scheduler improved (60s + jitter, 3 AM UTC)
- [x] Phase 5 email sequences built and tested

### ✅ Completed (March 11 and Earlier)

- [x] Phase 1: Paddle Billing — full subscription lifecycle
- [x] Phase 2: AI Content Engine — Ideas, Hooks, Scripts, Calendar, Taste Profile
- [x] Phase 3: Personalization — Niche & Tone dropdown, onboarding data
- [x] Phase 4: Trend Intelligence — live scheduler, Trends tab, trend injection

---

### 🚧 Pending — Needs Action Before First Beta User

- [ ] **`alembic upgrade head`** — Run on Railway to create `beta_feedback` table *(BLOCKING)*
- [ ] **Set `ADMIN_EMAIL` in Railway** — Without this, `/admin` returns 403 for everyone *(BLOCKING)*
- [ ] **Full beta test flow** — sign up → onboard → ideas → hooks → scripts → calendar → save → export
- [ ] **Mobile QA** — Real device test at 375px across all tabs
- [ ] **SPF record fix** — Add `include:amazonses.com` to Cloudflare DNS (TXT) for email deliverability
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard
- [ ] **TikTok Secret Rotation** — Security risk, overdue

---

## 🎯 Today's Priorities (March 13)

### 🔴 Must Do (Blocking First Beta User)
1. **Run `alembic upgrade head`** on Railway — creates `beta_feedback` table
2. **Set `ADMIN_EMAIL=182gandalf@gmail.com`** in Railway env vars
3. **Full end-to-end beta test** — go through the entire user journey yourself
4. **Mobile QA** — test on real device or Chrome DevTools at 375px

### 🟡 Should Do
5. **SPF record** — Add `include:amazonses.com` in Cloudflare (small, 5 minutes)
6. **Add `FROM_NAME` env var** in Railway dashboard
7. **Verify admin page** loads at flowcast.space/admin after signing in
8. **Test feedback widget** submits from dashboard, pricing, help pages

### 🟢 Nice to Have
9. **pytrends check** — Railway logs for 03:00 UTC run — did all 17 niches populate?
10. **TikTok secret rotation** — Still technically overdue

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| `beta_feedback` migration not run | HIGH | 🔴 Blocking | Run `alembic upgrade head` on Railway |
| `ADMIN_EMAIL` not set | MEDIUM | 🔴 Action needed | Add to Railway env vars |
| SPF record missing Resend | MEDIUM | 🟡 Pending | Add `include:amazonses.com` in Cloudflare |
| Beta testing not done | HIGH | 🟡 Ongoing | Must complete before inviting users |
| TikTok Secret Rotation | HIGH | 🔴 Overdue | Security risk — day 14+ |

---

## 🔧 Phase Status Summary

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 1: Paddle Billing | ✅ Complete | Full subscription lifecycle |
| Phase 2: AI Content Engine | ✅ Complete | Ideas, Hooks, Scripts, Calendar, Taste Profile |
| Phase 3: Personalization | ✅ Complete | Niche & Tone dropdown, onboarding data surfaced |
| Phase 4: Trend Intelligence | ✅ Complete | Live on Railway, scheduler running nightly 3 AM UTC |
| Phase 5: Email Sequences | ✅ Complete | Creator weekly, Studio daily, Day 7 onboarding |
| Beta Readiness (v0.1.0) | ✅ Complete | All 7 parts done and pushed |
| Phase 6: Post Scheduling | ⏳ Deferred | "Coming Soon" — post-launch |
| Real Workspace Isolation | ⏳ Deferred | Documented in FUTURE-FEATURES.md — on demand |

---

## 🎯 Daz's Open Action Items

1. [ ] **`alembic upgrade head`** on Railway — creates beta_feedback table *(TODAY)*
2. [ ] **Set `ADMIN_EMAIL`** in Railway env vars *(TODAY)*
3. [ ] **Beta test the full flow** — critical before first invite *(TODAY)*
4. [ ] **SPF record** — Cloudflare → add `include:amazonses.com` *(TODAY — 5 min)*
5. [ ] **TikTok secret rotation** — CRITICAL security risk, seriously overdue

---

## 📋 Before First Beta User Checklist

- [ ] `alembic upgrade head` run on Railway
- [ ] `ADMIN_EMAIL` set in Railway
- [ ] `/admin` page verified (stats load for admin email)
- [ ] Full sign-up → onboarding → generate → save → export flow tested
- [ ] Feedback widget tested on dashboard + pricing
- [ ] Paddle checkout tested end-to-end
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
