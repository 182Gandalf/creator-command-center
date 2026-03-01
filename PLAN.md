# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-01 00:00 UTC  
**Next Update:** 2026-03-02 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (Yesterday - 2026-02-28)
- [x] **Paddle Compliance:** Provisionally approved, fixed 3 items (footer, enterprise pricing, refund policy)
- [x] **Google OAuth Fixed:** Environment variables working, login functional
- [x] **Email/Password Login:** Working after database schema fixes
- [x] **Account Settings:** Profile, preferences, billing pages created and working
- [x] **Password Eye Toggle:** Added to login page for better UX
- [x] **AI Service:** Centralized AI service built with multi-model support (Gemini, Kimi, Claude, GPT)
- [x] **Instagram/Meta Reminder:** Scheduled for 9am today
- [x] **Daily Automation:** Daily Brief and FlowCast improvement suggestions working
- [x] **Security:** Removed debug logging, cleaned up app.py

### ✅ Completed (Feb 27)
- [x] **Hero Typo Fixed:** Added space before `<br>` tag to fix "aboutwhat" rendering issue
- [x] **Daily Automation:** Daily Brief and FlowCast improvement suggestions delivered successfully
- [x] **PLAN.md Review:** Daily planning session completed with priority alignment

### ✅ Completed (Feb 26)
- [x] **Railway Account Recovered:** Full access restored, connected to new GitHub repo
- [x] **Domain Unlocked:** Porkbun support ticket resolved, flowcast.space accessible
- [x] **Cloudflare Transfer:** DNS configured, SSL active, site live
- [x] **Code Repository:** All code pushed to 182gandalf/creator-command-center
- [x] **Railway Deployment:** Live deployment with all latest features
- [x] **Pricing Currency:** All plans converted from EUR (€) to USD ($)
- [x] **Refund Policy:** Updated from 30 days to 14 days across all pages
- [x] **Billing Email:** Added billing@flowcast.space to refund/contact sections
- [x] **Landing Page Copy:** Updated stats (2000+ → 1000+), added creator savings highlight
- [x] **Security Cleanup:** Removed all exposed secrets from GitHub (TOOLS.md, api-keys.md)
- [x] **Weekend Checklist:** Created comprehensive pre-launch testing checklist
- [x] **CAC Analysis:** Completed customer acquisition cost analysis (local only)
- [x] **Saturday Reminder:** Scheduled 9am weekend checklist reminder
- [x] **Daily Analysis Cron:** Set up automated daily site improvement analysis

### ✅ Completed (Feb 25)
- [x] **AI Credits System:** €1 for 10 AI ideas (all tiers except Pro)
- [x] **Usage Alerts:** Real-time warnings at 80% usage, alerts at 100%
- [x] **Annual Pricing Toggle:** Default to annual with 20% discount, toggle to monthly
- [x] **AI Quota Tracking:** Enhanced with bonus credits that don't expire
- [x] **New API Endpoints:** `/api/ai-quota-status`, `/api/ai-purchase-credits`, `/api/usage-alerts`
- [x] **Verified Gemini 1.5 Flash** for Free, Starter, and Creator tiers
- [x] **Set Reminder:** Affiliate/referral program reminder for March 15
- [x] All changes committed to GitHub
- [x] Profitability analysis recommendations implemented

### ✅ Completed (Earlier - 2026-02-24)
- [x] **MAJOR SECURITY FIX:** Implemented proper environment variable credential management
- [x] Removed hardcoded TikTok client secret from `app.py`
- [x] Updated pricing page with competitor comparison table
- [x] Updated Terms of Service with comprehensive AI Services section
- [x] Updated Refund policy (removed 48-hour exception clause)
- [x] Changed Starter plan: 2 platforms → 3 platforms

### 🚧 In Progress
- [ ] TikTok new developer account (OLD account compromised - need NEW account with fresh email)
- [ ] Git history cleanup (BFG Repo-Cleaner - waiting on TikTok NEW account setup)
- [ ] Paddle payment integration (waiting for approval)
- [ ] YouTube OAuth redirect URIs (need to add to Google Cloud Console)
- [ ] Meta/Instagram app creation (Basic Display API setup)
- [ ] Post scheduling cron jobs (disabled, need to enable for beta)
- [ ] Email notification system (billing@flowcast.space routing)

### ⏳ Pending
- [ ] Live deployment with all changes
- [ ] AI router testing with Gemini API
- [ ] User authentication backend implementation
- [ ] Review submission system
- [ ] Email notification system

---

## ⏸️ Temporarily Disabled (Pre-Beta)

The following features are disabled until beta testing begins:

| Feature | Status | Re-enable When |
|---------|--------|----------------|
| FlowCast Post Scheduler (Every Minute) | ⏸️ Disabled | Beta testing starts |
| Creator Command Center - Daily AI Content Ideas | ⏸️ Disabled | Beta testing starts |

**Note:** These are disabled to prevent automated actions during development. Re-enable before inviting beta users.

---

## 🎯 Today's Priorities (March 1, 2026) - SUNDAY SETUP DAY

### 🔴 Critical (Complete Today)
1. **Instagram/Meta API Application** - 9am reminder set, apply for Basic Display API
2. **AI API Keys Setup** - Get keys for: Gemini, Kimi 2.5, Claude Haiku/Sonnet
3. **Test Full Login Flow** - Verify Google OAuth and email login both working
4. **Paddle Final Review** - Check if approval complete after identity verification

### 🟡 High Priority (Today)
5. **YouTube OAuth** - Configure redirect URIs in Google Cloud Console
6. **Account Settings Test** - Verify profile, billing, password change all work
7. **AI Service Test** - Generate test content ideas with new service
8. **TikTok NEW Account** - Create fresh developer account (old compromised)

### 🟢 Medium Priority (If Time)
9. **Post Scheduling** - Enable cron jobs, test scheduling functionality
10. **Email System** - Set up billing@flowcast.space in Cloudflare Email Routing
11. **Analytics Setup** - Google Analytics 4 configuration
12. **Performance Check** - Page load speed, mobile responsiveness

### 🎯 Sunday Goal
**Complete API applications and AI setup → Ready for beta testing Monday**

---

## 📅 Weekly Roadmap

### Week of Feb 23 - Mar 1
- **Monday (Feb 24):** ✅ Security fixes, credential management, pricing updates, terms update
- **Tuesday (Feb 25):** ✅ AI credits, usage alerts, annual pricing toggle, Gemini Flash verification
- **Wednesday (Feb 26):** ✅ Railway/domain recovery, USD pricing, billing email, weekend checklist
- **Thursday (Feb 27):** ✅ Hero typo fix, daily automation confirmed working
- **Friday (Feb 28):** 🔴 Weekend pre-launch sprint: auth, AI, database, security testing
- **Weekend:** 🧪 Live testing, bug fixes, final polish → BETA READY

### Week of Mar 2 - Mar 8
- Paddle payment integration
- TikTok API approval process
- Beta user onboarding
- Analytics setup

### Week of Mar 9 - Mar 15
- Full platform launch
- Marketing campaign
- User feedback collection
- Iteration based on feedback

---

## 📈 Key Metrics to Track

| Metric | Current | Target |
|--------|---------|--------|
| Sign ups | 0 | 100 (Week 1) |
| Active users | 0 | 50 (Week 1) |
| Posts scheduled | 0 | 500 (Week 1) |
| Conversion rate | N/A | 5% |
| Churn rate | N/A | <10% |

---

## 🔧 Technical Debt

### Security (In Progress)
- [x] Hardcoded secrets removed from `app.py`
- [x] Environment variables implemented
- [ ] TikTok client secret rotation (PENDING - DAZ ACTION REQUIRED)
- [ ] Git history rewrite (remove API keys)
- [ ] Railway token rotation
- [ ] Password manager migration

### Performance
- [ ] Image optimization
- [ ] CSS minification
- [ ] Database indexing

### Code Quality
- [ ] Test coverage for AI router
- [ ] Error handling improvements
- [ ] Logging standardization

---

## 📝 Daily Notes

### 2026-03-01 - SUNDAY SETUP DAY
- **PLAN.md Updated:** Reviewed Feb 28 progress, set Mar 1 priorities
- **Yesterday's Wins:** Google OAuth working, email login fixed, AI service built, account settings pages created
- **Today Focus:** Instagram/Meta API application (9am), AI API keys setup, final testing
- **Reminder Set:** 9am for Instagram/Meta API application
- **Next:** Complete API applications → Beta testing Monday

### 2026-02-28 - MAJOR FIXES & FEATURES
- **Paddle Compliance:** Provisionally approved, fixed 3 items, enterprise pricing created
- **Google OAuth:** Fixed environment variable loading on Railway, login now working
- **Email Login:** Fixed after removing incompatible User model fields
- **Account Settings:** Complete profile, preferences, billing pages with working forms
- **Password Toggle:** Eye button added to login for better UX
- **AI Service:** Built centralized AI service supporting Gemini, Kimi, Claude, GPT
- **Instagram Reminder:** Scheduled for 9am Sunday (today)
- **Security:** Cleaned up debug logging, removed test code

### 2026-02-27 - TYPO FIX & AUTOMATION
- **Hero Headline:** Fixed "aboutwhat" typo by adding space before `<br>` tag
- **Daily Automation:** Daily Brief and FlowCast improvement analysis working correctly
- **Self-Improvement:** Multiple subagent reviews completed for pattern analysis
- **Next:** Weekend pre-launch sprint begins - focus on critical path items

### 2026-02-26 - MAJOR RECOVERIES & SETUP
- **Railway Account:** Fully recovered! Support ticket worked, deployment live
- **Domain Access:** Porkbun domain unlocked, Cloudflare transfer complete
- **Site Live:** https://flowcast.space now working with SSL
- **GitHub Repo:** All code pushed to 182gandalf/creator-command-center
- **Pricing Update:** All plans converted from EUR to USD ($6/$15/$29)
- **Refund Policy:** Updated to 14 days, billing@flowcast.space added
- **Landing Page:** Stats updated (1000+ creators), added savings highlight
- **Security:** Removed all exposed secrets from GitHub
- **Weekend Prep:** Created comprehensive pre-launch checklist
- **CAC Analysis:** Completed (saved locally, not on GitHub)
- **Reminders:** Saturday 9am reminder + daily improvement analysis cron jobs set up
- **Next:** Weekend testing begins - focus on critical path items

### 2026-02-25
- **AI Credits System:** Implemented €1 for 10 AI ideas (all tiers except Pro)
- **Usage Alerts:** Real-time warnings at 80%, alerts at 100% usage
- **Annual Pricing Toggle:** Default to annual with monthly toggle option
- **New API Endpoints:** /api/ai-quota-status, /api/ai-purchase-credits, /api/usage-alerts
- **Verified Gemini 1.5 Flash** is active for Free, Starter, Creator tiers
- **Set reminder** for affiliate/referral program (March 15)
- All code changes committed and pushed
- Profitability improvements implemented (caching, tier optimization)

### 2026-02-24
- **CRITICAL:** Google account (gandalftheclaw@gmail.com) banned - lost access to GitHub, Railway, Cloudflare
- Created new GitHub account: 182gandalf@gmail.com
- **SECURITY:** Implemented proper .env credential management
- **SECURITY:** Removed hardcoded TikTok secret from app.py
- Updated pricing page with annual billing and competitor comparison
- Updated Terms of Service with AI Services section
- Submitted support tickets to Porkbun and Railway for account recovery

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Mitigation |
|------|--------|--------|------------|
| TikTok NEW account needed | HIGH | 🔴 PENDING | Old account linked to banned email - create fresh account |
| Git history cleanup | MEDIUM | 🟡 WAITING | BFG Repo-Cleaner ready - waiting on NEW TikTok credentials |
| Paddle approval | MEDIUM | 🟡 IN PROGRESS | Identity check complete, awaiting final approval |
| YouTube OAuth setup | MEDIUM | 🟡 IN PROGRESS | Need to add redirect URIs to Google Cloud |
| Post scheduling disabled | MEDIUM | 🔴 PENDING | Enable cron jobs before beta testing |
| Meta app creation | MEDIUM | ⏳ SCHEDULED | 9am reminder set - apply today |
| AI API keys | LOW | ⏳ SCHEDULED | Set up today (Gemini, Kimi, Claude) |

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space ✅ LIVE WITH SSL
- **GitHub (NEW):** https://github.com/182gandalf/creator-command-center
- **Railway Dashboard:** https://railway.app/dashboard (RESTORED)
- **Porkbun Domain:** https://porkbun.com (UNLOCKED)
- **Google Cloud Console:** https://console.cloud.google.com/apis/credentials (YouTube OAuth)
- **Meta Developers:** https://developers.facebook.com/ (for Instagram)
- **TikTok Developers:** https://developers.tiktok.com/ (NEED NEW ACCOUNT)
- **Paddle Dashboard:** https://sandbox-vendors.paddle.com/ (awaiting approval)
- **Cloudflare:** https://dash.cloudflare.com (ACTIVE)
- **Weekend Checklist:** PRE-LAUNCH-CHECKLIST-WEEKEND.md

---

## 🎯 Action Items for Today (Mar 1)

### Daz - Your Tasks:
1. [ ] **Instagram/Meta API (9am):** Apply at https://developers.facebook.com/ for Basic Display API
2. [ ] **AI API Keys:** Get keys for Gemini, Kimi 2.5, Claude (Haiku + Sonnet)
3. [ ] **Test Login:** Verify both Google OAuth and email login work end-to-end
4. [ ] **Paddle Status:** Check if final review approved after identity verification
5. [ ] **Account Settings:** Test profile, billing, and password change pages
6. [ ] **TikTok NEW Account:** Create fresh developer account (avoid old email)
7. [ ] **YouTube OAuth:** Add redirect URIs to Google Cloud Console

### Gandalf (Me) - My Tasks:
1. [x] **PLAN.md Updated:** Reviewed yesterday's progress, set today's priorities
2. [ ] **AI Service Test:** Verify multi-model service works when keys added
3. [ ] **Login Debugging:** Remove debug logging if login stable
4. [ ] **Documentation:** Create API setup guides for Instagram, YouTube, TikTok

---

## 💡 Ideas & Backlog

### Future Features
- [ ] Analytics dashboard
- [ ] Team collaboration
- [ ] Content templates
- [ ] Bulk scheduling
- [ ] RSS feed import
- [ ] AI content generation (beyond ideas)

### Marketing Ideas
- [ ] Creator testimonials video
- [ ] Comparison page vs competitors
- [ ] Affiliate program (reminder set for March 15)
- [ ] YouTube tutorial series
- [ ] Discord community

---

*This document is updated automatically every day at midnight UTC and reviewed at 8am UTC.*
