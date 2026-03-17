# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-17 00:00 UTC

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

### ✅ Completed (March 16)

- [x] **Generate button — size + sensitivity** — Shrunk to half size, centered, no longer full-width on mobile; touch requires ≥150ms deliberate tap (`81dc9cc`)
- [x] **Beta bar restored on landing page** — Dismiss button removed, bar always visible; mobile: shorter text, single line, dynamic height offset (`33f1d6c`, `dbf039a`)
- [x] **Hook scorer moved to own sub-tab** — Hooks tab now has ✨ Generate New Hook / 📊 Score Your Own Hook sub-tabs; generator gets full-width screen (`3374931`, `0c53f27`)
- [x] **Help guide updated** — Hooks section updated to reference new sub-tab layout
- [x] **SPF record confirmed** — `include:amazonses.com` already present in Cloudflare DNS ✅
- [x] **Scripts tab mobile header** — Confirmed fixed ✅

---

### ✅ Completed (March 15 — Full Day)

- [x] **Ghost-tap mobile fix** — Ideas no longer generate on scroll (`47b3e3c`)
- [x] **Platform heading in .txt downloads** — All script downloads start with `PLATFORM:` header (`1c5f094`)
- [x] **Per-script PDF download** — Studio only (`21041d5`, `c3d954a`)
- [x] **Daily analysis cron fixed** — Recurring nightly job at 1:00 AM UTC
- [x] **Header mobile overlap fixed** (`9021ffd`)
- [x] **Pricing & Plans link** — Added to account dropdown (`9021ffd`)
- [x] **Trust badges** — Sign-up + sign-in pages
- [x] **Hooks section overhaul** — banners, scorer buttons, copy+save
- [x] **Onboarding tones expanded** — Honest/Raw, Inspiring, Casual added
- [x] **Beta announcement bar** — Landing + pricing pages
- [x] **Admin feedback text** — Long messages now wrap

---

### ✅ Completed (March 14)

- [x] `alembic upgrade head` — video_signals table live
- [x] Paddle Creator Pro products + Railway env vars set
- [x] `ADMIN_EMAIL=182gandalf@gmail.com` set in Railway
- [x] pytrends retry hardening
- [x] Pricing cards widened
- [x] TikTok task permanently removed

---

### ✅ Completed (March 13 and Earlier)

- [x] Creator Pro tier — live
- [x] Success Compounder — live
- [x] Interactive landing page demo — live
- [x] Beta Readiness Pass — all 7 parts
- [x] Studio Features — PDFs, 90-day calendar, daily digest, workspace switcher
- [x] Phase 1–5 — Paddle billing, AI content engine, personalization, trends, email sequences

---

### 🚧 Pending — Needs Action

- [ ] **Full beta test flow** — sign up → onboard → ideas → hooks → scripts → calendar → save → export — CRITICAL before first invite
- [ ] **Mobile QA** — Real device test at 375px across all tabs
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*
- [ ] **Admin page verified** — confirm stats load correctly for admin email

---

## 🎯 Today's Priorities (March 17)

### 🔴 Must Do
1. **Full beta test flow** — end-to-end, real sign-up, every tab, every action *(#1 blocker — overdue)*

### 🟡 Should Do
2. **Mobile QA** — 375px across all pages + new hook sub-tabs
3. **Verify /admin stats** — confirm admin dashboard shows correct counts

### 🟢 Nice to Have
4. **Add `FROM_NAME` env var** in Railway
5. **Check Railway logs** — did pytrends nightly run populate all niches?

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| Beta testing not done | HIGH | 🟡 Ongoing | Must complete before inviting users |
| FROM_NAME env var | LOW | 🟡 Pending | Emails work without it |

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
| Creator Pro Tier | ✅ Complete | Live — Paddle + Railway env vars set |
| Phase 6: Post Scheduling | ⏳ Deferred | "Coming Soon" — post-launch |

---

## 📋 Before First Beta User Checklist

- [x] `alembic upgrade head` run on Railway — ✅ Mar 14
- [x] Paddle Creator Pro products created + Railway env vars set — ✅ Mar 14
- [x] `ADMIN_EMAIL` set in Railway — ✅ Mar 14
- [x] Trust badges on sign-up/sign-in — ✅ Mar 15
- [x] Beta announcement bar on landing + pricing — ✅ Mar 15/16
- [x] SPF record updated in Cloudflare — ✅ already present
- [ ] Full sign-up → onboarding → generate → save → export flow tested
- [ ] Feedback widget tested (captures user_id ✅)
- [ ] Paddle checkout tested end-to-end (Splash → Creator upgrade)
- [ ] Mobile test at 375px (ideas, hooks, calendar, onboarding)
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
