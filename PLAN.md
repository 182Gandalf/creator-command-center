# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-03-02 00:00 UTC  
**Next Update:** 2026-03-03 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (Yesterday - 2026-03-01) - MAJOR PIVOT DAY
- [x] **Brand Pivot LIVE:** Complete repositioning - "Know what to film. Before you film it."
- [x] **New Backend Structure:** FastAPI app with PostgreSQL, SQLAlchemy, Alembic
- [x] **Authentication System:** JWT-based auth with /auth/register, /auth/login, /auth/me
- [x] **Database Models:** User, CreatorProfile, ContentIdea, Trend, CalendarEntry
- [x] **GitHub Repository:** Pushed to 182Gandalf/FlowCast (private)
- [x] **Railway Deployment:** Backend live with database connection working
- [x] **Alembic Migrations:** Database migration system ready
- [x] **Environment Setup:** SECRET_KEY, DATABASE_URL configured
- [x] **Health Check Endpoints:** /health and /health/db for monitoring

### ✅ Completed (Feb 28)
- [x] **Paddle Compliance:** Provisionally approved, fixed 3 items (footer, enterprise pricing, refund policy)
- [x] **Google OAuth Fixed:** Environment variables working, login functional
- [x] **Email/Password Login:** Working after database schema fixes
- [x] **Account Settings:** Profile, preferences, billing pages created and working
- [x] **AI Service:** Centralized AI service built with multi-model support (Gemini, Kimi, Claude, GPT)

### ✅ Completed (Feb 27)
- [x] **Hero Typo Fixed:** Added space before `<br>` tag
- [x] **Daily Automation:** Daily Brief and FlowCast improvement suggestions working

### ✅ Completed (Feb 26)
- [x] **Railway Account Recovered:** Full access restored
- [x] **Domain Unlocked:** Porkbun support ticket resolved
- [x] **Cloudflare Transfer:** DNS configured, SSL active
- [x] **Pricing Currency:** All plans converted to USD ($)
- [x] **Weekend Checklist:** Created comprehensive pre-launch testing checklist

### 🚧 In Progress
- [ ] **TikTok Secret Rotation:** Deferred until backend complete - reminder set for Mar 15
- [ ] **Frontend Integration:** Connect new backend API to frontend
- [ ] **AI Service Integration:** Connect ai.py service to new backend
- [ ] **Database Migration:** Run initial migration on production DB

### ⏳ Pending
- [ ] TikTok new developer account (P0 - security)
- [ ] Paddle payment integration
- [ ] YouTube OAuth redirect URIs
- [ ] Meta/Instagram app creation
- [ ] Post scheduling system (new backend)

---

## 🎯 Today's Priorities (March 2, 2026) - BACKEND INTEGRATION DAY

### 🔴 Critical (Complete Today)
1. **Run Database Migration:** `alembic upgrade head` on Railway PostgreSQL
2. **Test Auth Endpoints:** Verify /auth/register and /auth/login work via API
3. **Frontend Connection:** Update frontend to use new backend API endpoints
4. **AI Service Hookup:** Integrate existing ai.py service with new FastAPI backend

### 🟡 High Priority (Today)
5. **Create Protected Routes:** Add JWT dependency to content generation endpoints
6. **Creator Profile API:** Build /api/profile endpoints for onboarding flow
7. **Content Ideas API:** Build /api/ideas endpoints for AI generation
8. **Environment Variables:** Ensure all API keys (OpenAI, etc.) are in Railway

### 🟢 Medium Priority (If Time)
9. **Frontend State Management:** Set up auth token storage (localStorage/cookies)
10. **Logout Functionality:** Add /auth/logout endpoint and frontend handling
11. **Error Handling:** Standardize API error responses
12. **API Documentation:** Auto-generate Swagger docs (FastAPI provides this)

### 🎯 Tuesday Goal
**Backend fully functional with frontend integration → Test complete user journey**

---

## 📅 Weekly Roadmap

### Week of Mar 2 - Mar 8
- **Monday (Mar 2):** 🔴 Backend integration, database migrations, auth testing
- **Tuesday (Mar 3):** Frontend API connection, AI service hookup
- **Wednesday (Mar 4):** Content generation API, creator profiles
- **Thursday (Mar 5):** TikTok API (new account), post scheduling
- **Friday (Mar 6):** Testing, bug fixes, beta prep
- **Weekend:** Beta user onboarding

### Week of Mar 9 - Mar 15
- Paddle payment integration
- Full platform launch
- Marketing campaign
- User feedback collection

---

## 🚨 Blockers & Risks

| Risk | Impact | Status | Mitigation |
|------|--------|--------|------------|
| TikTok NEW account needed | HIGH | ⏸️ Deferred | Reminder set Mar 15, focus on backend first |
| Frontend-Backend Integration | HIGH | 🟡 In Progress | Today's priority |
| Database Migration | MEDIUM | 🟡 Pending | Run today on Railway |
| AI API Keys in Railway | MEDIUM | 🟡 Pending | Add OpenAI/Gemini keys today |
| Paddle approval | MEDIUM | ⏳ Waiting | Follow up if not approved by Wed |

---

## 🔧 Technical Debt

### Backend (New - Priority)
- [ ] Run initial Alembic migration
- [ ] Test all auth endpoints
- [ ] Build content generation API
- [ ] Build creator profile API
- [ ] Build calendar/scheduling API
- [ ] Integrate existing AI service

### Security
- [ ] TikTok client secret rotation (Mar 15)
- [ ] Git history rewrite (after TikTok)
- [ ] API key rotation for new backend

---

## 📝 Daily Notes

### 2026-03-02 - BACKEND INTEGRATION DAY
- **PLAN.md Updated:** March 1 progress logged, March 2 priorities set
- **Yesterday's Wins:** Brand pivot complete, new FastAPI backend live, auth working, database connected
- **Today Focus:** Database migrations, frontend API connection, AI service integration
- **Reminder Active:** TikTok rotation set for March 15
- **Next:** Complete backend-frontend integration → Test user journey

### 2026-03-01 - MAJOR PIVOT & BACKEND DAY
- **Brand Pivot LIVE:** "Know what to film. Before you film it." - new positioning deployed
- **New Backend:** FastAPI + PostgreSQL + SQLAlchemy + Alembic structure created
- **Authentication:** JWT auth system with register/login/me endpoints
- **Database Models:** User, CreatorProfile, ContentIdea, Trend, CalendarEntry
- **GitHub:** Pushed to 182Gandalf/FlowCast (private repo)
- **Railway:** Backend deployed, database connection verified
- **Deferred:** TikTok secret rotation (reminder set for 2 weeks)

### 2026-02-28 - MAJOR FIXES & FEATURES
- **Paddle Compliance:** Provisionally approved, fixed 3 items
- **Google OAuth:** Fixed environment variables, login working
- **Email Login:** Fixed after database schema changes
- **Account Settings:** Profile, preferences, billing pages created
- **AI Service:** Built centralized AI service (Gemini, Kimi, Claude, GPT)

---

## 🎯 Action Items for Today (Mar 2)

### Daz - Your Tasks:
1. [ ] **Database Migration:** Run `alembic upgrade head` in Railway console
2. [ ] **Test Auth:** Try registering and logging in via API
3. [ ] **API Keys:** Add OpenAI/Gemini keys to Railway environment variables
4. [ ] **Frontend:** Update frontend code to call new backend endpoints
5. [ ] **Integration Test:** Complete user journey (register → login → generate idea)

### Gandalf (Me) - My Tasks:
1. [x] **PLAN.md Updated:** Reviewed March 1, set March 2 priorities
2. [ ] **API Documentation:** Ensure Swagger UI is accessible (/docs)
3. [ ] **Error Handling:** Review and standardize error responses
4. [ ] **Testing Support:** Help debug any integration issues

---

## 🔗 Important Links

- **Live Site:** https://flowcast.space
- **GitHub (Backend):** https://github.com/182Gandalf/FlowCast
- **Railway Dashboard:** https://railway.app/dashboard
- **API Docs (Swagger):** https://your-app.railway.app/docs
- **API Health Check:** https://your-app.railway.app/health/db

---

*This document is updated automatically every day at midnight UTC.*
