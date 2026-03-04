# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-04 00:00 UTC  
**Next Update:** 2026-03-05 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (Yesterday - 2026-03-03) - UI/UX & AUTH FIXES DAY
- [x] **Clerk Auth Fixed:** Resolved double login window issue (removed conflicting signUpUrl/signInUrl)
- [x] **Navigation Cleanup:** Removed duplicate "Log In" links from nav menus
- [x] **Old Auth Pages:** Disabled old login/signup with redirects to Clerk versions
- [x] **Pricing CTAs Fixed:** "Start Free Trial" → "Get Started" (no free trial exists)
- [x] **Dashboard Branding:** Updated logo to match new site format
- [x] **Refund Policy:** Complete rewrite aligning with Paddle MoR terms
- [x] **Refund Route:** Added missing /refund route to main.py
- [x] **SOUL.md Updated:** Added continuous improvement section
- [x] **All Pushed to GitHub:** Deployed to Railway

### ✅ Completed (March 2) - CLERK & DASHBOARD DAY
- [x] **Clerk Authentication:** Migrated from custom JWT to Clerk.com (more reliable)
- [x] **Auth Fixed:** Resolved passlib and router import errors
- [x] **User Database:** Migrated to Clerk schema (clerk_user_id, subscription_tier)
- [x] **Webhook Integration:** Clerk user.created webhook auto-creates users
- [x] **Dynamic Navigation:** Header shows "Log Out" when logged in, "Log In/Sign Up" when not
- [x] **New Dashboard UI:** Modern app-like interface with sidebar, quick actions, content grid
- [x] **Onboarding Flow:** 4-step creator setup (niche, platforms, tone, frequency)
- [x] **Taste Profile:** Progress bar starting at 25%, visible in header
- [x] **Platform Tabs:** TikTok active, Reels/Shorts locked for free tier
- [x] **Trending Section:** Top trends with growth indicators
- [x] **Calendar Preview:** Weekly content calendar view
- [x] **Creator Profile API:** POST/GET endpoints for onboarding data
- [x] **All Pushed to GitHub:** Latest code deployed to Railway

### ✅ Completed (March 1) - MAJOR PIVOT DAY
- [x] **Brand Pivot LIVE:** Complete repositioning - "Know what to film. Before you film it."
- [x] **New Backend Structure:** FastAPI app with PostgreSQL, SQLAlchemy, Alembic
- [x] **GitHub Repository:** Pushed to 182Gandalf/FlowCast (private)
- [x] **Railway Deployment:** Backend live with database connection working

### 🚧 In Progress
- [ ] **AI Content Generation:** Connect Gemini API to generate real ideas
- [ ] **Save/Regenerate Ideas:** Implement idea favoriting and regeneration
- [ ] **Clerk Auth Verification:** User testing the sign-in/sign-up flow

### ⏳ Pending
- [ ] TikTok new developer account (P0 - security, reminder Mar 6)
- [ ] Paddle payment integration
- [ ] Meta/Instagram app creation
- [ ] Post scheduling system

---

## 🎯 Today's Priorities (March 4, 2026) - AI INTEGRATION DAY

### 🔴 Critical (Complete Today)
1. **AI Content Generation:** Connect Gemini API to dashboard "Generate Ideas" button
2. **Real Idea Cards:** Replace placeholder ideas with AI-generated content
3. **Save Ideas:** Implement ⭐ save functionality for idea cards
4. **Regenerate:** Implement 🔄 regenerate functionality

### 🟡 High Priority (Today)
5. **Hook Generator:** Build UI and API for 10 hook variations with scoring
6. **Tone Calibration:** Ensure AI respects user's selected tone from onboarding
7. **Platform-Native Output:** Generate different versions for TikTok/Reels/Shorts
8. **Feedback System:** Thumbs up/down on ideas to improve Taste Profile

### 🟢 Medium Priority (If Time)
9. **Content Calendar:** Connect calendar to saved ideas
10. **Trend Integration:** Use trending topics in AI prompts
11. **API Rate Limiting:** Prevent abuse on free tier (20 ideas/month)
12. **Error Handling:** Graceful failures when AI is unavailable

### 🎯 Wednesday Goal
**AI content generation fully working → Users can generate, save, and regenerate ideas**

---

## 📅 Weekly Roadmap

### Week of Mar 2 - Mar 8
- **Monday (Mar 2):** ✅ Clerk auth, dashboard UI, onboarding flow
- **Tuesday (Mar 3):** ✅ Clerk fixes, UI/UX polish, refund policy
- **Wednesday (Mar 4):** 🔴 AI content generation, save/regenerate ideas
- **Thursday (Mar 5):** Hook generator, content calendar
- **Friday (Mar 6):** TikTok API (new account), Day 10 reminder for SEC-001
- **Weekend:** Testing, bug fixes, beta prep

### Week of Mar 9 - Mar 15
- Paddle payment integration
- Full platform launch
- Marketing campaign
- User feedback collection

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Mitigation |
|------|--------|--------|------------|
| AI API Costs | MEDIUM | 🟡 Monitoring | Track usage, set limits |
| TikTok NEW account needed | HIGH | ⏸️ Deferred | Day 10 reminder Mar 6 |
| Clerk Auth Loop | HIGH | 🟡 Fixed | Awaiting user verification |
| AI Integration | MEDIUM | 🔴 Not Started | Priority for today |

---

## 🔧 Technical Debt

### Backend
- [x] Clerk authentication ✅
- [x] Database migrations ✅
- [x] Creator profile API ✅
- [ ] AI content generation API (today)
- [ ] Save/regenerate endpoints (today)
- [ ] Hook generator API (today)
- [ ] Content calendar API

### Frontend
- [x] Dynamic navigation ✅
- [x] Onboarding flow ✅
- [x] Dashboard UI ✅
- [ ] AI integration (today)
- [ ] Real-time idea generation
- [ ] Loading states

---

## 📝 Daily Notes

### 2026-03-04 - AI INTEGRATION DAY
- **PLAN.md Updated:** March 3 progress logged, March 4 priorities set
- **Yesterday's Wins:** Clerk auth loop fixed, UI/UX polished, refund policy complete
- **Today Focus:** AI content generation, real ideas instead of placeholders
- **Reminder Active:** TikTok rotation Day 10 reminder on March 6
- **Next:** Connect Gemini API → Generate real content ideas

### 2026-03-03 - UI/UX & AUTH FIXES DAY
- **Clerk Loop Fixed:** Removed signUpUrl/signInUrl that caused navigation conflicts
- **Navigation Cleanup:** Removed duplicate login links
- **Pricing Fixed:** CTAs now say "Get Started" not "Start Free Trial"
- **Refund Policy:** Complete rewrite to align with Paddle Merchant of Record
- **SOUL.md Updated:** Added continuous improvement principles
- **Deferred:** TikTok rotation (reminder set Mar 6)

### 2026-03-02 - CLERK & DASHBOARD DAY
- **Clerk Migration:** Switched from custom JWT to Clerk.com - much more reliable
- **New Dashboard:** Modern app interface with sidebar, quick actions, trending
- **Onboarding Flow:** 4-step creator setup (niche, platforms, tone, frequency)
- **Taste Profile:** Progress bar starting at 25%, refines with user feedback
- **Platform Locking:** Free tier = TikTok only, Creator = all platforms
- **Dynamic Nav:** Shows "Log Out" when logged in
- **Fixed:** Multiple deployment issues (passlib, routers, CORS)

### 2026-03-01 - MAJOR PIVOT & BACKEND DAY
- **Brand Pivot LIVE:** "Know what to film. Before you film it."
- **New Backend:** FastAPI + PostgreSQL + SQLAlchemy + Alembic
- **Deferred:** TikTok secret rotation (reminder set for 2 weeks)

---

## 🎯 Action Items for Today (Mar 4)

### Daz - Your Tasks:
1. [ ] **Test Clerk Auth:** Verify sign-in and sign-up work without looping
2. [ ] **Test Onboarding:** Go through /onboarding flow if not done
3. [ ] **Test Dashboard:** Check new dashboard loads correctly
4. [ ] **Verify UI:** Check if flows match brand pivot vision
5. [ ] **AI Ready:** Confirm Gemini API key is in Railway (for my work)

### Gandalf (Me) - My Tasks:
1. [x] **PLAN.md Updated:** Reviewed March 3, set March 4 priorities ✅
2. [ ] **AI Integration:** Connect Gemini API to "Generate Ideas" button
3. [ ] **Real Ideas:** Replace placeholders with AI-generated content
4. [ ] **Save/Regenerate:** Implement idea card actions
5. [ ] **Hook Generator:** Build UI and API for hook generation

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space
- **Onboarding:** https://flowcast.space/onboarding
- **Dashboard:** https://flowcast.space/dashboard
- **GitHub:** https://github.com/182Gandalf/FlowCast
- **Railway Dashboard:** https://railway.app/dashboard

---

*This document is updated automatically every day at midnight UTC.*