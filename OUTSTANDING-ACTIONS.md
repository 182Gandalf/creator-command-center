# FlowCast Project - Outstanding Actions & Decisions
## Prioritized by Urgency & Importance
## Last Updated: February 22, 2026

---

## 🔴 CRITICAL (Do Today)

### 1. Complete Git History Cleanup
**Status:** Started but blocked
**Issue:** Git push failed due to token authentication
**Action:** 
- [ ] Run the Git cleanup commands locally (I provided the script)
- [ ] Or provide new GitHub token for me to complete
**Why Critical:** Exposed API keys in Git history are security vulnerability
**Time:** 10 minutes

### 2. Add Gemini API Key to Railway
**Status:** Key provided but not added
**Key:** `[REDACTED - SEE GOOGLE CLOUD CONSOLE]`
**Action:**
- [ ] Go to Railway dashboard → FlowCast project → Variables
- [ ] Add: `GEMINI_API_KEY` = above key
- [ ] Redeploy service
**Why Critical:** Free/Starter tiers need this to work
**Time:** 2 minutes

### 3. Test AI Router is Working
**Status:** DeepSeek added, Gemini pending
**Action:**
- [ ] After adding Gemini key, test endpoint:
  ```
  curl https://your-app.railway.app/api/ai-content-ideas?topic=fitness
  ```
- [ ] Verify response includes `model_used` field
**Why Critical:** Confirm 85% cost savings are active
**Time:** 5 minutes

---

## 🟠 HIGH PRIORITY (This Week)

### 4. Choose & Purchase Domain Name
**Status:** Research complete, decision needed
**Top Options:**
- [ ] **flowcast.site** ($5-10/year) ⭐ RECOMMENDED
- [ ] **flowcast.cloud** ($10-15/year)
- [ ] **flowcast.eu** ($10-15/year) - if EU-focused
- [ ] **tryflowcast.com** ($10-12/year)
**Action:**
- [ ] Check availability at instantdomainsearch.com
- [ ] Purchase at Porkbun or Namecheap
- [ ] Enable auto-renew
**Why High:** Brand identity needed before launch
**Time:** 15 minutes
**Blocker:** Your decision needed

### 5. Generate Logo & Favicon Set
**Status:** Scripts created, need to run
**Action:**
- [ ] Run `python3 generate_logos.py` (needs API keys)
- [ ] OR use ChatGPT/DALL-E directly with my prompts
- [ ] Run `python3 generate_favicons.py` on chosen logo
- [ ] Upload to static/ folder
**Why High:** Visual identity needed for launch
**Time:** 30 minutes
**Blocker:** Need to decide on approach (AI vs designer)

### 6. Update YouTube API Key in Production
**Status:** New key provided, may need verification
**Key:** `AIzaSyAlaPtMIGn6tDtGbNEdF7yAJwhl-uuRfCA`
**Action:**
- [ ] Verify Railway has new key (not old exposed one)
- [ ] Test YouTube connection in app
- [ ] Monitor for any API errors
**Why High:** Core feature must work
**Time:** 5 minutes

---

## 🟡 MEDIUM PRIORITY (Next 2 Weeks)

### 7. Set Up Paddle for Payments
**Status:** Mentioned in emails, not configured
**Action:**
- [ ] Sign up at paddle.com
- [ ] Complete business verification
- [ ] Create product plans matching our pricing
- [ ] Integrate Paddle SDK into app
- [ ] Test checkout flow
**Why Medium:** Needed before accepting paying customers
**Time:** 2-3 days (mostly Paddle verification)
**Blocker:** Business verification takes time

### 8. Complete Instagram Basic Display API
**Status:** Partially implemented
**Action:**
- [ ] Finish OAuth flow
- [ ] Test media retrieval
- [ ] Add to platform list in UI
- [ ] Document limitations (read-only mostly)
**Why Medium:** Important platform for creators
**Time:** 1 day

### 9. Implement Post Scheduling Logic
**Status:** Database schema exists, logic needed
**Action:**
- [ ] Create scheduled post worker (cron job)
- [ ] Implement publishing to connected platforms
- [ ] Add error handling and retry logic
- [ ] Send notifications on success/failure
**Why Medium:** Core feature of product
**Time:** 2-3 days

### 10. Add Email Notifications
**Status:** Gmail API working, integration needed
**Action:**
- [ ] Set up email templates
- [ ] Send welcome emails
- [ ] Send post published confirmations
- [ ] Send weekly analytics summaries
**Why Medium:** User engagement & retention
**Time:** 1 day

---

## 🟢 LOW PRIORITY (Before Full Launch)

### 11. Facebook Page Posting API
**Status:** Research complete, not implemented
**Complexity:** HIGH (requires business verification + app review)
**Timeline:** 3-4 weeks
**Action:**
- [ ] Decide if worth the effort
- [ ] Submit business verification
- [ ] Create Facebook app
- [ ] Go through app review process
**Why Low:** Complex, time-consuming, not critical for MVP

### 12. TikTok Content Posting API
**Status:** Research complete
**Limitation:** Cannot auto-post (inbox only)
**Action:**
- [ ] Decide if "inbox upload" feature is valuable
- [ ] If yes, implement upload to inbox
- [ ] Add notification system
**Why Low:** Limited functionality, complex approval

### 13. Mobile App
**Status:** Not started
**Action:**
- [ ] Decide: native app vs PWA vs skip
- [ ] If PWA: add service worker
- [ ] If native: choose React Native vs Flutter
**Why Low:** Web app sufficient for MVP

### 14. Advanced Analytics Dashboard
**Status:** Basic stats exist
**Action:**
- [ ] Add engagement tracking
- [ ] Create charts/graphs
- [ ] Add comparison metrics
**Why Low:** Nice-to-have, not critical

---

## 📋 DECISIONS NEEDED FROM YOU

### Decision 1: Domain Name
**Options:**
- A) flowcast.site ($5-10) - Cheap, professional
- B) flowcast.cloud ($10-15) - SaaS-focused
- C) flowcast.eu ($10-15) - EU market
- D) Something else
**Need:** Your choice
**Impact:** Brand identity

### Decision 2: Logo Approach
**Options:**
- A) AI generate now (fast, cheap, $0-5)
- B) Hire designer on Fiverr ($50-200, better quality)
- C) Use Canva templates (free, DIY)
**Need:** Your preference
**Impact:** Visual brand

### Decision 3: Facebook Integration
**Options:**
- A) Yes, invest 3-4 weeks for full integration
- B) No, skip for now (focus on YouTube/Instagram)
- C) Maybe later (after initial launch)
**Need:** Your call
**Impact:** Feature set, timeline

### Decision 4: TikTok Integration
**Options:**
- A) Yes, implement "upload to inbox" feature
- B) No, skip (limited value)
- C) Wait and see user demand
**Need:** Your decision
**Impact:** Platform support

### Decision 5: Launch Timeline
**Options:**
- A) Soft launch ASAP (current state + bug fixes)
- B) Polish first (add missing features)
- C) Full feature complete (all platforms)
**Need:** Your target date
**Impact:** Development priority

### Decision 6: Pricing Tier Focus
**Options:**
- A) Push Free tier hard (user acquisition)
- B) Focus on paid conversions immediately
- C) Beta testing with select users first
**Need:** Go-to-market strategy
**Impact:** Revenue, growth

---

## 📊 SUMMARY MATRIX

| Task | Urgency | Importance | Effort | Blocker |
|------|---------|------------|--------|---------|
| Git cleanup | 🔴 High | 🔴 Critical | Low | Token/auth |
| Add Gemini key | 🔴 High | 🔴 Critical | Low | Your action |
| Test AI router | 🔴 High | 🔴 Critical | Low | Above tasks |
| Choose domain | 🟠 Med | 🔴 Critical | Low | Your decision |
| Generate logo | 🟠 Med | 🔴 Critical | Med | Your decision |
| Verify YouTube key | 🟠 Med | 🔴 Critical | Low | None |
| Set up Paddle | 🟡 Low | 🟠 High | High | Verification time |
| Instagram API | 🟡 Low | 🟠 High | Med | None |
| Post scheduling | 🟡 Low | 🔴 Critical | High | None |
| Email notifications | 🟡 Low | 🟡 Med | Low | None |
| Facebook API | 🟢 Low | 🟡 Med | Very High | Your decision |
| TikTok API | 🟢 Low | 🟢 Low | High | Your decision |
| Mobile app | 🟢 Low | 🟢 Low | Very High | Your decision |
| Analytics | 🟢 Low | 🟢 Low | Med | None |

---

## 🎯 RECOMMENDED ACTION PLAN

### Today (30 minutes)
1. Complete Git cleanup
2. Add Gemini key to Railway
3. Test AI router
4. Choose domain name

### This Week (2-3 hours)
5. Purchase domain
6. Generate logo
7. Verify YouTube integration
8. Set up Paddle account

### Next 2 Weeks (1 week work)
9. Complete Instagram API
10. Implement post scheduling
11. Add email notifications
12. Soft launch to beta users

### Before Full Launch (1 month)
13. Polish based on feedback
14. Decide on Facebook/TikTok
15. Scale infrastructure
16. Marketing push

---

## ❓ IMMEDIATE QUESTIONS FOR YOU

1. **Can you complete the Git cleanup** (I can provide exact commands) or **provide a new GitHub token** for me to finish?

2. **Which domain** do you want to buy? (I recommend flowcast.site)

3. **Logo approach:** AI generate now or hire designer?

4. **Facebook/TikTok:** Skip for MVP or invest time?

5. **Target launch date:** This month or next?

**Ready to tackle the critical items?** Let's start with Git cleanup and domain decision! 🚀
