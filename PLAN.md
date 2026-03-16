# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-16 00:00 UTC

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

### ✅ Completed (March 15 — Full Day)

- [x] **Ghost-tap mobile fix** — Ideas no longer generate on scroll; touchstart/touchend movement detection added (`47b3e3c`)
- [x] **Platform heading in .txt downloads** — All script downloads (live + saved) now start with `PLATFORM: TikTok / Reels / Shorts` header (`1c5f094`)
- [x] **Per-script PDF download** — 📄 PDF button added to each script card (live + saved); new `POST /api/export/pdf/script` endpoint (Studio only) (`21041d5`, `c3d954a`)
- [x] **PDF content fix** — Was extracting `body`/`main_content`; now correctly pulls `script_body → script → body`, plus keywords, hashtags, description, end_screen_cta, tip — matches TXT output
- [x] **Bulk PDF export** — Single bulk button stays at top of Saved Scripts; per-script buttons at bottom of each card
- [x] **Daily analysis cron fixed** — Old one-shot job (Feb 27) replaced with recurring nightly job at 1:00 AM UTC; first run triggered same day
- [x] **Header mobile overlap fixed** — Title now ellipsis-truncates, user menu is flex-shrink:0, padding reduced on mobile (`9021ffd`)
- [x] **Pricing & Plans link** — Added to account dropdown (top-right), styled in orange (`9021ffd`)
- [x] **Beta banner mobile font** — Reduced to 0.72rem on ≤640px screens for neater wrapping (`a399003`)

---

### ✅ Completed (March 15 — Overnight / Early Morning)

- [x] **Trust badges** — 🔒 SSL Secure · 💳 Paddle Payments · 🛡️ Privacy Protected added to sign-up + sign-in pages
- [x] **Hook hint texts updated** — Both hints now say "Then proceed to the Scripts tab."
- [x] **Hook generator orange banner** → replaced with plain orange text
- [x] **Hook scorer copy button fix** — data-hook-text + addEventListener
- [x] **Hooks section overhaul** — info banners, scorer buttons, copy+save on scorer results
- [x] **Onboarding tones expanded** — Added Honest/Raw, Inspiring, Casual to Q3 + whitelist fixed
- [x] **"See how it works" scroll fix** — scroll-padding-top accounts for fixed header + beta bar
- [x] **Help guide table of contents** — inline TOC with 9 hyperlinked sections
- [x] **/hooks + /calendar disabled** — both 301 → /dashboard
- [x] **Onboarding logo size** — constrained to 36×36px
- [x] **Beta announcement bar** — gradient bar on landing + pricing page (dismissable)
- [x] **Pricing summary mobile grid** — responsive 2×2 class
- [x] **Dashboard padding** — tab content + container bottom padding + scroll-padding-top
- [x] **Admin feedback text** — long messages now wrap

---

### ✅ Completed (March 14)

- [x] `alembic upgrade head` — video_signals table live
- [x] Paddle Creator Pro products + Railway env vars set
- [x] `ADMIN_EMAIL=182gandalf@gmail.com` set in Railway
- [x] pytrends retry hardening
- [x] Pricing cards widened
- [x] TikTok task permanently removed from all 27 files

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
- [ ] **SPF record fix** — Add `include:amazonses.com` to Cloudflare DNS *(5 min)*
- [ ] **`FROM_NAME` env var** — Add to Railway dashboard *(low priority — emails work)*
- [ ] **Admin page verified** — confirm stats load correctly for admin email
- [ ] **Scripts tab header missing on mobile** — header disappears when scrolling to scripts tab; under investigation

---

## 🎯 Today's Priorities (March 16)

### 🔴 Must Do
1. **Full beta test flow** — end-to-end, real sign-up, every tab, every action *(still the #1 blocker)*
2. **Fix missing header on scripts tab (mobile)** — needs investigation + fix

### 🟡 Should Do
3. **SPF record** — Add `include:amazonses.com` in Cloudflare (5 min job)
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
| Scripts tab header missing (mobile) | MEDIUM | 🔴 Active | Header disappears on scripts tab scroll |
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
