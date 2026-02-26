# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-02-26 00:00 UTC  
**Next Update:** 2026-02-27 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (Yesterday - 2026-02-25)
- [x] **AI Credits System:** €1 for 10 AI ideas (all tiers except Pro)
- [x] **Usage Alerts:** Real-time warnings at 80% usage, alerts at 100%
- [x] **Annual Pricing Toggle:** Default to annual with 20% discount, toggle to monthly
- [x] **AI Quota Tracking:** Enhanced with bonus credits that don't expire
- [x] **New API Endpoints:** `/api/ai-quota-status`, `/api/ai-purchase-credits`, `/api/usage-alerts`
- [x] **Verified Gemini 1.5 Flash** for Free, Starter, and Creator tiers
- [x] **Set Reminder:** Affiliate/referral program reminder for March 15
- [x] All changes committed to GitHub (commit: e8ea41a)
- [x] Profitability analysis recommendations implemented

### ✅ Completed (Earlier - 2026-02-24)
- [x] **MAJOR SECURITY FIX:** Implemented proper environment variable credential management
- [x] Removed hardcoded TikTok client secret from `app.py`
- [x] Updated pricing page with competitor comparison table
- [x] Updated Terms of Service with comprehensive AI Services section
- [x] Updated Refund policy (removed 48-hour exception clause)
- [x] Changed Starter plan: 2 platforms → 3 platforms

### 🚧 In Progress
- [ ] Porkbun domain recovery (support ticket submitted - awaiting response)
- [ ] Railway account recovery (support ticket submitted - awaiting response)
- [ ] TikTok client secret rotation (CRITICAL - exposed in git history)
- [ ] Git history cleanup (remove exposed API keys before new repo push)
- [ ] Paddle payment integration (waiting for approval)
- [ ] YouTube OAuth testing (credentials configured, needs redirect URI setup)
- [ ] Meta/Instagram app review preparation

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

## 🎯 Today's Priorities (February 26, 2026)

### 🔴 Critical (Must Do Today)
1. **TikTok client secret rotation** - STILL PENDING - Log into TikTok Developer Portal and regenerate
2. **Check support ticket status** - Porkbun and Railway account recovery updates
3. **Git history cleanup** - Use BFG Repo-Cleaner to remove exposed secrets

### 🟡 High Priority
4. **YouTube OAuth redirect URIs** - Add to Google Cloud Console
5. **Meta app creation** - Start Instagram Basic Display setup
6. **Paddle integration follow-up** - Check approval status, prepare webhooks
7. **Test AI credits flow** - Verify purchase and usage works correctly

### 🟢 Medium Priority
8. **Password manager migration** - Move credentials from `TOOLS.md` to secure storage
9. **Review system planning** - Design "Leave a Review" functionality
10. **Win-back offer emails** - Draft copy for inactive users

---

## 📅 Weekly Roadmap

### Week of Feb 23 - Mar 1
- **Monday (Feb 24):** ✅ Security fixes, credential management, pricing updates, terms update
- **Tuesday (Feb 25):** ✅ AI credits, usage alerts, annual pricing toggle, Gemini Flash verification
- **Wednesday (Feb 26):** TikTok rotation, support ticket checks, git cleanup, YouTube OAuth, Meta setup
- **Thursday (Feb 27):** Authentication backend, deployment if hosting restored
- **Friday (Feb 28):** Review system, testing, bug fixes
- **Weekend:** Documentation, final testing

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
| TikTok secret exposed | CRITICAL | 🔴 PENDING | **DAZ ACTION REQUIRED** - Rotate secret in TikTok Developer Portal |
| Porkbun domain access | HIGH | 🟡 WAITING | Support ticket submitted - check email |
| Railway account access | HIGH | 🟡 WAITING | Support ticket submitted - check email |
| Git history cleanup | HIGH | 🔴 PENDING | Use BFG Repo-Cleaner - waiting on TikTok rotation |
| Paddle approval delay | MEDIUM | ⏳ PENDING | Use free tier longer |
| Meta app review delay | MEDIUM | ⏳ PENDING | Focus on YouTube/TikTok first |

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space (DOWN - awaiting domain recovery)
- **GitHub (NEW):** https://github.com/182gandalf/creator-command-center
- **GitHub (OLD - LOCKED):** https://github.com/gandalftheclaw-alt/creator-command-center
- **Railway Dashboard:** UNAVAILABLE (account recovery in progress)
- **Porkbun Domain:** UNAVAILABLE (account recovery in progress)
- **Google Cloud Console:** YouTube OAuth settings
- **Meta Developers:** https://developers.facebook.com/ (for Instagram)
- **TikTok Developers:** https://developers.tiktok.com/ (application pending)
- **Paddle Dashboard:** https://sandbox-vendors.paddle.com/ (awaiting approval)

---

## 🎯 Action Items for Today

### Daz - Your Tasks:
1. [ ] **URGENT:** Log into TikTok Developer Portal → rotate client secret
2. [ ] Check email for Porkbun/Railway support ticket responses
3. [ ] Confirm you're okay with BFG Repo-Cleaner for git history cleanup
4. [ ] Test the new AI credits feature on the site

### Gandalf (Me) - My Tasks:
1. [ ] Prepare BFG Repo-Cleaner commands for git history cleanup
2. [ ] Set up Meta Developer app for Instagram integration
3. [ ] Document YouTube OAuth redirect URI setup steps
4. [ ] Draft win-back email templates

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
