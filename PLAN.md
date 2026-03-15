# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-15 00:00 UTC

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

### ✅ Completed (March 15 — Overnight / Early Morning)

- [x] **Trust badges** — 🔒 SSL Secure · 💳 Paddle Payments · 🛡️ Privacy Protected added to sign-up + sign-in pages
- [x] **Hook hint texts updated** — Both hints now say "Then proceed to the Scripts tab."
- [x] **Hook generator orange banner** → replaced with plain orange text (matches scorer style)
- [x] **Hook scorer copy button fix** — data-hook-text + addEventListener (no more raw JS in button)
- [x] **Hooks section overhaul** — info banners, scorer buttons match generator style, copy+save on scorer results
- [x] **Onboarding tones expanded** — Added Honest/Raw, Inspiring, Casual to Q3 + whitelist fixed
- [x] **"See how it works" scroll fix** — scroll-padding-top accounts for fixed header + beta bar
- [x] **Help guide table of contents** — inline TOC with 9 hyperlinked sections
- [x] **/hooks + /calendar disabled** — both 301 → /dashboard
- [x] **Onboarding logo size** — constrained to 36×36px (was expanding full width)
- [x] **PADDLE_CLIENT_TOKEN** — confirmed server-injected, never hardcoded
- [x] **Beta announcement bar** — gradient bar on landing page + callout card on pricing page (dismissable, localStorage)
- [x] **Pricing summary mobile grid** — replaced inline `repeat(4,1fr)` with responsive 2×2 class
- [x] **Dashboard padding** — tab content + container bottom padding + scroll-padding-top
- [x] **Admin feedback text** — long messages now wrap instead of truncating

---

### ✅ Completed (March 14 — Full Day Sprint)

**Blockers Cleared by Daz ✅**
- [x] `alembic upgrade head` — video_signals table live, Success Compounder works
- [x] Paddle Creator Pro products created + Railway env vars set
- [x] `ADMIN_EMAIL=182gandalf@gmail.com` set in Railway

**Shipped**
- [x] pytrends retry hardening — delays 200–280s, 20min batch pause, 45min + 60min retry passes, randomised niche order
- [x] Pricing cards widened — container 1400px, gap 2rem, breakpoint 1480px
- [x] TikTok task permanently removed from all 27 files

---

### ✅ Completed (March 13 — Full Day Sprint)

- [x] Creator Pro tier — $25/mo / $20/mo annual, 90-day calendar, Zapier, 20 saves
- [x] Success Compounder — video URL → AI content intelligence → top signal in idea gen
- [x] Interactive landing page demo — niche/tone picker → 3 live ideas → conversion panel
- [x] Admin feedback count, CTA alignment, feedback auth fix
- [x] Zapier webhook confirmed live

---

### ✅ Completed (March 12 and Earlier)

- [x] Beta Readiness Pass — all 7 parts (loading states, error handling, mobile, admin, security)
- [x] Studio Features — PDFs, 90-day calendar, daily digest, workspace switcher
- [x] Phase 1–5 — Paddle billing, AI content engine, personalization, trends, email sequences

---

### 🚧 Pending — Needs Action

- [ ] **Full beta test flow** — sign up → onboard → ideas → hooks → scripts → calendar → save → export — CRITICAL before first invite
- [ ] **Mobile QA** — Real device test at 375px across all tabs
- [ ] **SPF record fix** — Add `include:amazonses.com` to Cloudflare DNS *(5 min)*
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*
- [ ] **Daily analysis cron** — Midnight scan stale since Feb 27, not auto-updating — needs fix
- [ ] **Admin page verified** — confirm stats load correctly for admin email

---

## 🎯 Today's Priorities (March 15)

### 🔴 Must Do
1. **Full beta test flow** — end-to-end, real sign-up, every tab, every action
2. **Fix daily midnight analysis cron** — stale since Feb 27

### 🟡 Should Do
3. **SPF record** — Add `include:amazonses.com` in Cloudflare (5 min)
4. **Mobile QA** — 375px across all pages
5. **Verify /admin stats** — confirm admin dashboard shows correct counts

### 🟢 Nice to Have
6. **Add `FROM_NAME` env var** in Railway
7. **Check Railway logs** — did pytrends nightly run populate all niches?

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| Beta testing not done | HIGH | 🟡 Ongoing | Must complete before inviting users |
| Daily analysis cron stale | MEDIUM | 🔴 Broken | Last ran Feb 27 — midnight job not auto-updating |
| SPF record missing Resend | MEDIUM | 🟡 Pending | Add `include:amazonses.com` in Cloudflare |
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
- [x] Beta announcement bar on landing + pricing — ✅ Mar 15
- [ ] Full sign-up → onboarding → generate → save → export flow tested
- [ ] Feedback widget tested (captures user_id ✅)
- [ ] Paddle checkout tested end-to-end (Splash → Creator upgrade)
- [ ] Mobile test at 375px (ideas, hooks, calendar, onboarding)
- [ ] Railway deploy logs checked for migration errors
- [ ] SPF record updated in Cloudflare
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
