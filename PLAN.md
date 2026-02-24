# FlowCast.space - Project Plan & Roadmap

**Last Updated:** 2026-02-24 00:00 UTC  
**Next Update:** 2026-02-25 00:00 UTC

---

## 📝 Document Delivery Protocol

**Rule:** All documents requiring user review/interaction must be delivered via:
1. **Telegram** - Send as message or file attachment
2. **Email** - Send to: stgdar001@gmail.com

**Applies to:** Integration guides, review submissions, documentation, plans, reports

---

## 📊 Current Status

### ✅ Completed (Last 24h)
- [x] Landing page redesign with 6 sections (Hero, Problem, Preview, Testimonials, CTA)
- [x] Lightning bolt logo (⚡) across all pages
- [x] Comprehensive SEO optimization (meta tags, OG, structured data, sitemap)
- [x] OG image created (1200x630px) for social sharing
- [x] Bing verification file added
- [x] Sign up / Login pages created
- [x] SSL/HTTPS configuration guide (Cloudflare settings)
- [x] Free trial limits enforced (20 posts, 2 platforms, 5 AI ideas/day)
- [x] TikTok API integration (draft upload to inbox)
- [x] Contact email updated to customersupport@flowcast.space
- [x] Refund policy set to 14 days
- [x] **NEW:** Fixed all pricing buttons to say "Get Started" (was "Contact Sales" on Pro)
- [x] **NEW:** Fixed signup API network error (database schema + server-side validation)
- [x] **NEW:** Created new GitHub account (182gandalf@gmail.com) after Google ban
- [x] **NEW:** Forked repository to new GitHub account
- [x] **NEW:** Configured local git for new account (SSH keys generated)
- [x] **NEW:** Added server-side password confirmation validation (security fix)

### 🚧 In Progress
- [ ] Porkbun domain recovery (support ticket submitted)
- [ ] Railway account recovery (support ticket submitted)
- [ ] Git push to new GitHub account (SSH key needs to be added to GitHub)
- [ ] Paddle payment integration (waiting for approval)
- [ ] YouTube OAuth testing (credentials configured, needs redirect URI setup)
- [ ] Meta/Instagram app review preparation
- [ ] Git history cleanup (API keys in history)

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

## 🎯 Immediate Priorities (Next 48h)

### Critical (Blockers)
1. **Add SSH key to new GitHub account** - Required for git push (key already generated)
2. **Porkbun domain recovery** - Can't deploy without domain access
3. **Railway account recovery OR new account** - Need hosting platform
4. **Git history cleanup** - Remove exposed API keys before pushing to new repo

### High Priority
5. **Deploy current code to production** - All changes ready locally
6. **Add Gemini API key to Railway** - Required for AI features
7. **YouTube OAuth redirect URIs** - Add to Google Cloud Console

### Medium Priority
8. **Meta app creation** - Start Instagram Basic Display setup
9. **Review system** - Implement "Leave a Review" functionality
10. **Paddle integration** - Wait for approval, then implement webhooks

---

## 📅 Weekly Roadmap

### Week of Feb 23 - Mar 1
- **Monday:** Deploy, Git cleanup, Gemini key
- **Tuesday:** Mobile fixes, YouTube OAuth testing
- **Wednesday:** Meta app setup, Instagram integration
- **Thursday:** Authentication backend
- **Friday:** Review system, Paddle prep
- **Weekend:** Testing, bug fixes

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

### Security
- [ ] Git history rewrite (remove API keys)
- [ ] Environment variables audit
- [ ] SSL certificate verification

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

### 2026-02-23
- Major SEO push completed
- Sign up/login pages created
- Mobile formatting issues identified
- Ready for production deployment

### 2026-02-24
- **CRITICAL:** Google account (gandalftheclaw@gmail.com) banned - lost access to GitHub, Railway, Cloudflare
- Created new GitHub account: 182gandalf@gmail.com / Freya@06082021
- Forked repository to new account: github.com/182gandalf/creator-command-center
- Generated SSH keys for new GitHub account
- Fixed pricing buttons (all now say "Get Started")
- Fixed signup API network error (database schema issue)
- Added server-side password confirmation validation
- Submitted support tickets to Porkbun and Railway for account recovery
- App running locally on port 5000 with all fixes
- **BLOCKED:** Cannot deploy until domain/hosting access restored

---

## 🚨 Blockers & Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| Google account ban | Lost access to GitHub, Railway, Cloudflare | New accounts created, support tickets filed |
| Porkbun domain access lost | Can't manage DNS | Support ticket submitted, awaiting response |
| Railway account access lost | No hosting platform | Support ticket submitted, may need new account |
| Git push authentication | Can't deploy code | SSH key generated, needs manual add to GitHub |
| Git history cleanup delay | Security vulnerability | Use BFG Repo-Cleaner |
| Paddle approval delay | No payments | Use free tier longer |
| Meta app review delay | No Instagram | Focus on YouTube/TikTok |

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
- [ ] Affiliate program
- [ ] YouTube tutorial series
- [ ] Discord community

---

*This document is updated automatically every day at midnight UTC and reviewed at 8am UTC.*
