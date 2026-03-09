# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-09 00:00 UTC  
**Next Update:** 2026-03-10 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (March 8) - AI INTEGRATION DAY - HUGE PROGRESS!
- [x] **Multi-Provider AI Service:** Built services/ai.py supporting Anthropic, OpenAI, Gemini, Moonshot
- [x] **Moonshot Integration:** Set as default provider with Kimi K2.5 model
- [x] **AI Idea Generation:** POST /generate/ideas endpoint working with real AI responses
- [x] **5 Ideas Per Generation:** Always returns exactly 5 ideas with auto-padding if AI returns fewer
- [x] **Platform-Native Output:** Each idea includes TikTok, Reels, and Shorts versions
- [x] **Dashboard UI:** New dashboard-new.html with modern AI Co-Creator design
- [x] **Tier Gating:** Splash users see TikTok only; Reels/Shorts blurred with upgrade CTA
- [x] **Copy Functionality:** Copy buttons for each platform's content
- [x] **Bold Remix Section:** Shows alternative angle for each idea
- [x] **Idea Counter:** Shows "Unlimited" for paid users, countdown (20→0) for Splash
- [x] **Next Steps Card:** Appears after generation with guidance text
- [x] **Example Ideas:** Updated to match generated format with platform tabs
- [x] **Error Handling:** Better JSON parsing, AI provider fallback, detailed logging
- [x] **3-Column Layout:** Widened dashboard to fit 3 idea cards per row
- [x] **Brand Icons:** Replaced emojis with SVG icons for TikTok, Reels, Shorts
- [x] **Loading States:** "This may take a minute" message during generation

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
- [ ] **Save Ideas:** ⭐ button functionality to save ideas to database
- [ ] **Regenerate Ideas:** 🔄 button to regenerate individual ideas
- [ ] **TikTok Secret Rotation:** Still pending user action
- [ ] **Hook Generator:** Build 10-hook generator with scoring UI

### ⏳ Pending
- [ ] TikTok NEW developer account (P0 - security)
- [ ] Meta/Instagram app creation
- [ ] Post scheduling system
- [ ] Content calendar integration

---

## 🎯 Today's Priorities (March 9, 2026) - MONDAY MOMENTUM

### 🔴 Critical (Complete Today)
1. **Save Ideas:** Implement ⭐ button to save ideas to user's profile
2. **Regenerate Ideas:** Implement 🔄 button to regenerate individual ideas
3. **Saved Ideas Page:** Create page to view all saved ideas
4. **Idea Feedback:** Thumbs up/down to improve AI personalization

### 🟡 High Priority (Today)
5. **Hook Generator:** Build UI for 10 hook variations with 1-10 scoring
6. **Content Calendar:** Connect saved ideas to calendar view
7. **Taste Profile:** Display and update taste profile percentage based on feedback

### 🟢 Medium Priority (If Time)
8. **Trending Intelligence:** Show what's trending in user's niche
9. **Quick Actions:** Generate Hooks, Plan Content buttons functional
10. **Beta Testing Prep:** Final polish before launch week

### 🎯 Monday Goal
**Save/regenerate working + hook generator functional + content calendar connected**

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

### 2026-03-09 - MONDAY MOMENTUM - SAVE & REGENERATE DAY
- **PLAN.md Updated:** March 8 AI integration logged, March 9 priorities set
- **Yesterday's Wins:** AI idea generation LIVE! 5 ideas per click, platform-native output, tier gating working
- **Today Focus:** Save ideas (⭐), regenerate (🔄), hook generator, content calendar
- **Status:** Core AI feature working - now building user interaction features
- **Next:** Save/regenerate → Hook generator → Content calendar → LAUNCH WEEK

### 2026-03-08 - SUNDAY FUNDAY - AI INTEGRATION DAY - MASSIVE SUCCESS!
- **AI Service:** Multi-provider support (Moonshot, Anthropic, Gemini, OpenAI)
- **Idea Generation:** Working end-to-end with real AI responses
- **Dashboard:** New modern UI with 3-column layout
- **Tier Gating:** Splash users see TikTok only, Creator/Studio see all platforms
- **Always 5 Ideas:** Auto-padding if AI returns fewer than 5
- **User Testing:** Daz beta testing live, feedback incorporated
- **Polish:** Brand icons, loading states, idea counter, next steps card

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

## 🎯 Action Items for Today (Mar 9)

### Daz - Your Tasks:
1. [ ] **Beta Test Save Ideas:** Click ⭐ on generated ideas, verify they save
2. [ ] **Test Regenerate:** Click 🔄 on an idea, verify it regenerates
3. [ ] **Check Saved Ideas Page:** Verify saved ideas appear in new page
4. [ ] **Provide Feedback:** Tell me what features need polish for launch
5. [ ] **TikTok Rotation:** When ready, rotate the secret (still pending)

### Gandalf (Me) - My Tasks:
1. [x] **PLAN.md Updated:** Reviewed March 8, set March 9 priorities ✅
2. [ ] **Save Ideas:** POST /ideas/{id}/save endpoint + database storage
3. [ ] **Regenerate Ideas:** POST /ideas/{id}/regenerate with AI call
4. [ ] **Saved Ideas Page:** Create /saved-ideas page with all saved content
5. [ ] **Hook Generator:** Build UI for 10 hooks + API endpoint
6. [ ] **Content Calendar:** Connect calendar to saved ideas

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
