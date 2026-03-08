# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-08 00:00 UTC  
**Next Update:** 2026-03-09 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (March 7) - ONBOARDING & CREATOR PROFILES DAY
- [x] **10-Question Onboarding Quiz:** Expanded from 5 to 10 questions with AI personalization
- [x] **Enhanced CreatorProfile Model:** Added audience_description, content_types, weekly_content_hours, content_struggle, forbidden_topics
- [x] **Database Migrations:** Created migrations for new profile fields
- [x] **Onboarding Form UI:** Progress bar, section dividers, numbered questions, sliders
- [x] **Dashboard Fix:** Fixed "Authorization header missing" error
- [x] **Platforms Array Fix:** Handle both string (legacy) and ARRAY (new) formats
- [x] **All Pushed to GitHub:** Deployed to Railway

### ✅ Completed (March 6) - STABILITY & FIXES DAY
- [x] **Dashboard Auth Fix:** Removed server-side auth requirement, client-side handles it
- [x] **GitHub Push:** All changes committed and deployed

### ✅ Completed (March 5) - AI INTEGRATION DAY
- [x] **Paddle Checkout Fix:** Debugged and fixed overlay opening issue
- [x] **Creator Profile API:** /api/creator-profile endpoints working
- [x] **Onboarding Router:** Created dedicated onboarding module

### ✅ Completed (March 4) - PADDLE & AUTH PRODUCTION DAY
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
- [x] **Mobile Header CSS:** Fixed button spacing across ALL pages

### 🚧 In Progress
- [ ] **AI Content Generation:** Connect Gemini API (next priority)
- [ ] **TikTok Secret Rotation:** Still pending user action
- [ ] **Real Idea Cards:** Replace placeholders with AI-generated content

### ⏳ Pending
- [ ] TikTok NEW developer account (P0 - security)
- [ ] Meta/Instagram app creation
- [ ] Post scheduling system
- [ ] Content calendar integration

---

## 🎯 Today's Priorities (March 8, 2026) - SUNDAY FUNDAY

### 🔴 Critical (Complete Today)
1. **AI Content Generation:** Connect Gemini API to "Generate Ideas" button
2. **Real Idea Cards:** Replace placeholder ideas with AI-generated content
3. **Save Ideas:** Implement ⭐ save functionality for idea cards
4. **Regenerate:** Implement 🔄 regenerate functionality

### 🟡 High Priority (Today)
5. **Hook Generator:** Build UI and API for 10 hook variations with scoring
6. **Tone Calibration:** Ensure AI respects user's selected tone from onboarding
7. **Platform-Native Output:** Generate different versions for TikTok/Reels/Shorts

### 🟢 Medium Priority (If Time)
8. **Content Calendar:** Connect calendar to saved ideas
9. **API Rate Limiting:** Prevent abuse on free tier (20 ideas/month)
10. **User Profile Display:** Show creator profile info on dashboard

### 🎯 Sunday Goal
**AI generating real ideas + save/regenerate working + hook generator UI**

---

## 📅 Weekly Roadmap

### Week of Mar 2 - Mar 8 (COMPLETE)
- **Monday (Mar 2):** ✅ Clerk auth, dashboard UI, onboarding flow
- **Tuesday (Mar 3):** ✅ Clerk fixes, UI/UX polish, refund policy
- **Wednesday (Mar 4):** ✅ Paddle integration, Clerk production, mobile CSS fixes
- **Thursday (Mar 5):** ✅ Paddle checkout fix, creator profile API
- **Friday (Mar 6):** ✅ Dashboard auth fix, stability improvements
- **Saturday (Mar 7):** ✅ 10-question onboarding, enhanced profiles
- **Sunday (Mar 8):** 🔴 AI integration, real idea generation

### Week of Mar 9 - Mar 15 (LAUNCH WEEK)
- **Monday (Mar 9):** Content calendar, scheduling system
- **Tuesday (Mar 10):** Hook generator, trend intelligence
- **Wednesday (Mar 11):** Beta testing, bug fixes
- **Thursday (Mar 12):** Final polish, documentation
- **Friday (Mar 13):** 🚀 **LAUNCH DAY**
- **Weekend:** Marketing, user onboarding support

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Mitigation |
|------|--------|--------|------------|
| TikTok Secret Rotation | HIGH | 🟠 Still pending | User action required - escalated |
| AI Integration | HIGH | 🔴 Today | Priority for today |
| Paddle Checkout | MEDIUM | ✅ Fixed | Working now |
| AI API Costs | MEDIUM | 🟡 Monitoring | Track usage, set limits |

---

## 🔧 Technical Debt

### Backend
- [x] Paddle billing integration ✅
- [x] Clerk production auth ✅
- [x] Database migrations ✅
- [x] 10-question onboarding ✅
- [ ] AI content generation API (today)
- [ ] Save/regenerate endpoints (today)
- [ ] Hook generator API (today)

### Frontend
- [x] Paddle.js checkout ✅
- [x] Mobile header CSS ✅
- [x] 10-question onboarding form ✅
- [ ] AI integration (today)
- [ ] Real-time idea generation (today)
- [ ] Hook generator UI (today)

---

## 📝 Daily Notes

### 2026-03-08 - SUNDAY FUNDAY - AI INTEGRATION DAY
- **PLAN.md Updated:** March 7 progress logged, March 8 priorities set
- **Yesterday's Wins:** 10-question onboarding complete, dashboard fixed, enhanced profiles
- **Today Focus:** AI content generation, real ideas, save/regenerate, hook generator
- **Status:** Ready for AI integration - Gemini API key needed in Railway
- **Next:** Connect Gemini → Generate real ideas → Save/regenerate

### 2026-03-07 - ONBOARDING & CREATOR PROFILES DAY
- **10-Question Onboarding:** Expanded from 5 to 10 questions
- **New Questions:** Target audience, content types, weekly hours, struggle, forbidden topics
- **Database:** Added 5 new columns to creator_profiles table
- **UI Improvements:** Progress bar, section dividers, numbered questions, sliders
- **Dashboard Fix:** Fixed auth header error, platforms array handling
- **Migrations:** Created 2 new migration files

### 2026-03-06 - STABILITY & FIXES DAY
- **Dashboard Auth:** Fixed "Authorization header missing" error
- **Client-Side Auth:** Dashboard now uses client-side auth check
- **GitHub Push:** All changes deployed to Railway

### 2026-03-05 - AI INTEGRATION DAY
- **Paddle Checkout:** Fixed overlay opening issue
- **Creator Profile API:** Endpoints working for profile management
- **Onboarding Router:** Created dedicated onboarding module

### 2026-03-04 - PADDLE & AUTH PRODUCTION DAY
- **Paddle Billing:** Complete integration with checkout, webhooks
- **Clerk Production:** Migrated from dev to production
- **Mobile CSS:** Fixed header spacing across all pages

---

## 🎯 Action Items for Today (Mar 8)

### Daz - Your Tasks:
1. [ ] **Test Onboarding:** Go through new 10-question onboarding flow
2. [ ] **Verify Dashboard:** Confirm dashboard loads after onboarding
3. [ ] **Gemini API Key:** Add to Railway environment variables
4. [ ] **TikTok Rotation:** When ready, rotate the secret (still pending)

### Gandalf (Me) - My Tasks:
1. [x] **PLAN.md Updated:** Reviewed March 7, set March 8 priorities ✅
2. [ ] **AI Integration:** Connect Gemini API to "Generate Ideas" button
3. [ ] **Real Ideas:** Replace placeholders with AI-generated content
4. [ ] **Save/Regenerate:** Implement idea card functionality
5. [ ] **Hook Generator:** Build UI and API for hook variations

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
