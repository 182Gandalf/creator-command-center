# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-05 00:00 UTC  
**Next Update:** 2026-03-06 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (Yesterday - 2026-03-04) - PADDLE & AUTH PRODUCTION DAY
- [x] **Paddle Billing Integration:** Complete subscription system with Paddle.js overlay
- [x] **Database Migration:** Added paddle_customer_id, paddle_subscription_id, subscription_ends_at
- [x] **Checkout API:** /subscribe/* endpoints for Creator/Studio monthly/annual
- [x] **Paddle Webhooks:** transaction.completed, subscription.canceled, subscription.updated handlers
- [x] **Tier Checking:** require_tier() dependency for protected routes
- [x] **Pricing Page:** Updated with Paddle.js and checkout buttons
- [x] **Clerk Production:** Switched from dev to production (accounts.flowcast.space)
- [x] **Clerk DNS:** Configured Cloudflare CNAME records for custom domain
- [x] **Google OAuth:** Fixed scopes (openid email profile)
- [x] **Auth Flow Fixed:** Sign-in/sign-out working, no more redirect loops
- [x] **Mobile Header CSS:** Fixed button spacing across ALL pages (index, pricing, dashboard, etc.)
- [x] **All Pushed to GitHub:** Deployed to Railway

### ✅ Completed (March 3) - UI/UX & AUTH FIXES DAY
- [x] **Clerk Auth Fixed:** Resolved double login window issue
- [x] **Navigation Cleanup:** Removed duplicate "Log In" links from nav menus
- [x] **Pricing CTAs Fixed:** "Start Free Trial" → "Get Started"
- [x] **Dashboard Branding:** Updated logo to match new site format
- [x] **Refund Policy:** Complete rewrite aligning with Paddle MoR terms

### ✅ Completed (March 2) - CLERK & DASHBOARD DAY
- [x] **Clerk Authentication:** Migrated from custom JWT to Clerk.com
- [x] **New Dashboard UI:** Modern app-like interface
- [x] **Onboarding Flow:** 4-step creator setup

### ✅ Completed (March 1) - MAJOR PIVOT DAY
- [x] **Brand Pivot LIVE:** "Know what to film. Before you film it."
- [x] **New Backend:** FastAPI + PostgreSQL + SQLAlchemy

### 🚧 In Progress
- [ ] **Paddle Checkout:** Overlay not opening (debugging Clerk session detection)
- [ ] **AI Content Generation:** Connect Gemini API
- [ ] **TikTok Secret Rotation:** Day 10 reminder TODAY (March 5)

### ⏳ Pending
- [ ] TikTok NEW developer account (P0 - security, reminder TODAY Mar 5)
- [ ] Meta/Instagram app creation
- [ ] Post scheduling system

---

## 🎯 Today's Priorities (March 5, 2026) - AI INTEGRATION & CHECKOUT DAY

### 🔴 Critical (Complete Today)
1. **TikTok Secret Rotation:** Day 10 reminder - MUST complete today
2. **Paddle Checkout Fix:** Debug why overlay doesn't open (Clerk session issue)
3. **AI Content Generation:** Connect Gemini API to dashboard "Generate Ideas" button
4. **Real Idea Cards:** Replace placeholder ideas with AI-generated content

### 🟡 High Priority (Today)
5. **Save Ideas:** Implement ⭐ save functionality for idea cards
6. **Regenerate:** Implement 🔄 regenerate functionality
7. **Hook Generator:** Build UI and API for 10 hook variations with scoring
8. **Tone Calibration:** Ensure AI respects user's selected tone from onboarding

### 🟢 Medium Priority (If Time)
9. **Platform-Native Output:** Generate different versions for TikTok/Reels/Shorts
10. **Content Calendar:** Connect calendar to saved ideas
11. **API Rate Limiting:** Prevent abuse on free tier (20 ideas/month)

### 🎯 Friday Goal
**Paddle checkout working + AI generating real ideas + TikTok secret rotated**

---

## 📅 Weekly Roadmap

### Week of Mar 2 - Mar 8
- **Monday (Mar 2):** ✅ Clerk auth, dashboard UI, onboarding flow
- **Tuesday (Mar 3):** ✅ Clerk fixes, UI/UX polish, refund policy
- **Wednesday (Mar 4):** ✅ Paddle integration, Clerk production, mobile CSS fixes
- **Thursday (Mar 5):** 🔴 TikTok rotation (Day 10), Paddle checkout fix, AI integration
- **Friday (Mar 6):** Hook generator, content calendar
- **Weekend:** Testing, bug fixes, beta prep

### Week of Mar 9 - Mar 15
- Full platform launch
- Marketing campaign
- User feedback collection

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Mitigation |
|------|--------|--------|------------|
| TikTok Secret Rotation | HIGH | 🔴 Day 10 TODAY | User action required |
| Paddle Checkout | HIGH | 🟡 Debugging | Clerk session detection |
| AI API Costs | MEDIUM | 🟡 Monitoring | Track usage, set limits |
| AI Integration | MEDIUM | 🔴 Not Started | Priority for today |

---

## 🔧 Technical Debt

### Backend
- [x] Paddle billing integration ✅
- [x] Clerk production auth ✅
- [x] Database migrations ✅
- [ ] AI content generation API (today)
- [ ] Paddle checkout fix (today)
- [ ] Save/regenerate endpoints

### Frontend
- [x] Paddle.js checkout ✅
- [x] Mobile header CSS ✅
- [ ] AI integration (today)
- [ ] Real-time idea generation

---

## 📝 Daily Notes

### 2026-03-05 - AI INTEGRATION & CHECKOUT DAY
- **PLAN.md Updated:** March 4 progress logged, March 5 priorities set
- **Yesterday's Wins:** Paddle integrated, Clerk production working, mobile CSS fixed
- **Today Focus:** TikTok rotation (Day 10), Paddle checkout debug, AI integration
- **Reminder CRITICAL:** TikTok rotation Day 10 reminder TODAY
- **Next:** Fix Paddle overlay → AI content generation

### 2026-03-04 - PADDLE & AUTH PRODUCTION DAY
- **Paddle Billing:** Complete integration with checkout, webhooks, tier checking
- **Clerk Production:** Migrated from dev to production, DNS configured
- **Mobile CSS:** Fixed header button spacing across all pages
- **Auth Flow:** Sign-in/sign-out working perfectly
- **Deferred:** TikTok rotation (reminder today Mar 5)

### 2026-03-03 - UI/UX & AUTH FIXES DAY
- **Clerk Loop Fixed:** Resolved navigation conflicts
- **Navigation Cleanup:** Removed duplicate login links
- **Refund Policy:** Complete rewrite for Paddle MoR

### 2026-03-02 - CLERK & DASHBOARD DAY
- **Clerk Migration:** Switched from custom JWT to Clerk.com
- **New Dashboard:** Modern app interface
- **Onboarding Flow:** 4-step creator setup

### 2026-03-01 - MAJOR PIVOT & BACKEND DAY
- **Brand Pivot LIVE:** "Know what to film. Before you film it."

---

## 🎯 Action Items for Today (Mar 5)

### Daz - Your Tasks:
1. [ ] **TikTok Secret Rotation:** Log into TikTok Developer Portal, generate new secret
2. [ ] **Test Paddle Checkout:** Try clicking upgrade on pricing page after I fix it
3. [ ] **Verify Auth Flow:** Confirm sign-in/sign-out working smoothly
4. [ ] **AI Ready:** Confirm Gemini API key is in Railway (for my work)

### Gandalf (Me) - My Tasks:
1. [x] **PLAN.md Updated:** Reviewed March 4, set March 5 priorities ✅
2. [ ] **Paddle Fix:** Debug why checkout overlay doesn't open
3. [ ] **AI Integration:** Connect Gemini API to "Generate Ideas" button
4. [ ] **TikTok Follow-up:** Send Day 10 reminder if not completed

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space
- **Onboarding:** https://flowcast.space/onboarding
- **Dashboard:** https://flowcast.space/dashboard
- **Pricing:** https://flowcast.space/pricing
- **GitHub:** https://github.com/182Gandalf/FlowCast
- **Railway Dashboard:** https://railway.app/dashboard

---

*This document is updated automatically every day at midnight UTC.*
