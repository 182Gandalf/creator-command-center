# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-21 00:00 UTC

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

### ✅ Completed (March 20)

- [x] **Dual hook selection bug fixed** — Generator + saved/scorer hooks could both show active simultaneously; fixed via `selected_hook_source` tracking in workspace state (`8147659`)
- [x] **Scripts failing from scorer hook fixed** — Scripts failed to generate when using a scored hook without an active idea; hook text now used as topic fallback (`8147659`)
- [x] **Onboarding content_types validation removed** — Q7 (talking head / voiceover checkboxes) was silently blocking form submission; made optional (`344c591`)
- [x] **Onboarding prefill completely broken — fixed** — `prefillExistingProfile()` was calling `/api/onboarding` (non-existent endpoint, silent 404); now calls `/api/creator-profile` and restores all 10 questions for returning users (`344c591`)
- [x] **`niche_category` added to `/api/creator-profile` response** — Was missing, required for prefill (`344c591`)
- [x] **Idea generation 500 error fixed** — AI occasionally returns invalid JSON (unescaped quotes in creative niches like "Teleportation", or truncation); added `json-repair` library as final fallback across ideas, hooks, scripts (`9a7f800`)
- [x] **`content_ideas` + `tweak_ideas` max tokens increased** — 2500 → 4000; prevents mid-JSON truncation for 5 full ideas (`9a7f800`)

---

### ✅ Completed (March 17)

- [x] **Full beta test flow** — Daz tested end-to-end ✅
- [x] **Trends Scraper panel on /admin** — 18 niches, health status, last fetched, top topics (`a910302`)
- [x] **"family and home" niche replaced** — split into `"parenting"` + `"home decor"` — now 18 niches (`8bd5b26`)
- [x] **Success Compounder locked for Splash** — 25% Taste Profile cap enforced; pricing, FAQ, help guide all updated (`6a6f65e`)
- [x] **Per-row delete on admin feedback table** — 🗑 button per row, instant removal without reload (`907a7c6`)
- [x] **Two-part onboarding Q1** — category picker (18 chips) + specific niche text (`7fc27d3`)
- [x] **AI fallback chain** — Anthropic primary → Kimi K2.5 → moonshot-v1-8k inner safety net (`9f0a76a`)
- [x] **Ideas tab full-width on desktop** (`b634bf2`)
- [x] **YouTube "Coming Soon"** — Connected Accounts page updated (`1668e9e`)

---

### ✅ Completed (March 16)

- [x] **Generate button — size + sensitivity** (`81dc9cc`)
- [x] **Beta bar restored on landing page** (`33f1d6c`, `dbf039a`)
- [x] **Hook scorer moved to own sub-tab** — Generate / Score sub-tabs (`3374931`, `0c53f27`)
- [x] **Help guide updated** — Hooks section
- [x] **SPF record confirmed** — `include:amazonses.com` already present ✅
- [x] **Scripts tab mobile header** — Confirmed fixed ✅

---

### ✅ Completed (March 15 and Earlier)

- [x] Ghost-tap mobile fix, platform headings in downloads, per-script PDF, daily analysis cron, header mobile fix, pricing link, trust badges, hooks overhaul, onboarding tones, beta bar, pytrends hardening, Paddle Creator Pro, all phases 1–5

---

### 🚧 Pending — Needs Action

- [ ] **Mobile QA** — Real device test at 375px across all tabs *(still not done — blocking first beta invite)*
- [ ] **Paddle checkout tested** — Splash → Creator upgrade end-to-end
- [ ] **Admin page verified** — confirm stats load correctly for admin email
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*
- [ ] **Railway deploy logs** — Check for migration errors post-deploy

---

## 🎯 Today's Priorities (March 21)

### 🔴 Must Do
1. **Mobile QA at 375px** — This is the last thing standing between now and sending beta invites. Test: ideas, hooks (both sub-tabs), scripts, onboarding (new prefill + category chips), calendar
2. **Verify Railway deploy** — Confirm `json-repair` installed correctly (check deploy logs)

### 🟡 Should Do
3. **Paddle checkout test** — Splash → Creator upgrade end-to-end
4. **Verify /admin stats** — confirm stats load for admin email

### 🟢 Nice to Have
5. **Add `FROM_NAME` env var** in Railway
6. **Send first beta invite** — if Mobile QA passes 🎉

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Notes |
|------|--------|--------|-------|
| Mobile QA not done | HIGH | 🔴 Blocking | Last item before beta invites |
| json-repair Railway install | MEDIUM | 🟡 Verify | Check deploy logs after next push |
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
- [x] Full sign-up → onboarding → generate → save → export flow tested — ✅ March 17
- [ ] Feedback widget tested (captures user_id ✅)
- [ ] Paddle checkout tested end-to-end (Splash → Creator upgrade)
- [ ] **Mobile test at 375px** (ideas, hooks, calendar, onboarding) ← **LAST BLOCKER**
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
