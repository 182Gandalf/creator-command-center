# FlowCast - Weekend Pre-Launch Checklist
## February 27-28, 2026
## CRITICAL: Complete Before Live Testing Begins

---

## 🔴 CRITICAL PATH (Must Complete Before Testing)

### 1. AUTHENTICATION & LOGIN SYSTEM
- [ ] Test user registration flow
- [ ] Test email verification (if enabled)
- [ ] Test login with valid credentials
- [ ] Test login with invalid credentials (error handling)
- [ ] Test password reset flow
- [ ] Test "Remember Me" functionality
- [ ] Verify session timeout works correctly
- [ ] Test logout functionality

**Testing Steps:**
```
1. Create test account at flowcast.space/signup
2. Verify email arrives (if applicable)
3. Login with new credentials
4. Check dashboard loads correctly
5. Logout and verify session cleared
6. Try password reset
```

---

### 2. DATABASE & DATA PERSISTENCE
- [ ] Verify PostgreSQL database is connected
- [ ] Test user data saves correctly
- [ ] Test scheduled posts persist in database
- [ ] Verify AI usage credits tracked properly
- [ ] Test data retrieval speed (performance check)
- [ ] Verify backup system is configured
- [ ] Test data integrity after redeploy

**Verification:**
```bash
# Check Railway logs for DB connection errors
# Verify no data loss between deployments
```

---

### 3. AI INTEGRATION
- [ ] Verify Gemini API key is in Railway environment variables
- [ ] Test AI content ideas endpoint: `/api/ai-content-ideas`
- [ ] Verify AI quota tracking works
- [ ] Test usage alerts at 80% threshold
- [ ] Test hard cap at 100% usage
- [ ] Verify bonus credits don't expire
- [ ] Test AI credits purchase flow (if Paddle ready)

**Test Commands:**
```bash
curl https://flowcast.space/api/ai-content-ideas?topic=fitness
curl https://flowcast.space/api/ai-quota-status
```

---

### 4. PAYMENT INTEGRATION (Paddle)
- [ ] Verify Paddle account is approved
- [ ] Add Paddle API keys to Railway environment
- [ ] Test Starter plan checkout ($6/month)
- [ ] Test Creator plan checkout ($15/month)
- [ ] Test Pro plan checkout ($29/month)
- [ ] Test annual billing option (20% discount)
- [ ] Test payment failure handling
- [ ] Verify webhook endpoints receive events
- [ ] Test subscription cancellation
- [ ] Test refund process

**Critical:** If Paddle not ready, disable paid tiers and offer extended free trial

---

### 5. SOCIAL PLATFORM INTEGRATIONS

#### YouTube
- [ ] Verify YouTube API key in environment variables
- [ ] Test OAuth connection flow
- [ ] Verify redirect URI: `https://flowcast.space/auth/youtube/callback`
- [ ] Test channel connection
- [ ] Test video upload (if implemented)
- [ ] Verify error handling for revoked access

#### Instagram (Basic Display API)
- [ ] Create Meta Developer app (if not done)
- [ ] Configure OAuth redirect URI
- [ ] Test Instagram connection flow
- [ ] Verify media retrieval works
- [ ] Test error handling
- [ ] Document limitations (read-only for Basic Display)

#### TikTok
- [ ] Create new TikTok developer account (not linked to old email)
- [ ] Create new FlowCast app
- [ ] Configure OAuth redirect URI
- [ ] Get new Client Key and Secret
- [ ] Add to Railway environment variables
- [ ] Test connection flow
- [ ] Document posting limitations (inbox only)

---

### 6. POST SCHEDULING SYSTEM
- [ ] Enable the disabled cron jobs:
  - FlowCast Post Scheduler (Every Minute)
  - Creator Command Center - Daily AI Content Ideas
- [ ] Test creating a scheduled post
- [ ] Verify post saves to database with correct timestamp
- [ ] Test editing a scheduled post
- [ ] Test deleting a scheduled post
- [ ] Verify posts publish at scheduled time
- [ ] Test recurring post schedules
- [ ] Verify error handling for failed posts
- [ ] Test notifications for published posts

**Files to Check:**
- Cron job configuration
- Post scheduler worker
- Database models for scheduled posts

---

### 7. EMAIL NOTIFICATIONS
- [ ] Set up billing@flowcast.space in Cloudflare Email Routing
- [ ] Configure email templates:
  - Welcome email (new signup)
  - Post published confirmation
  - Payment receipt
  - Password reset
  - Weekly analytics summary
- [ ] Test email delivery
- [ ] Verify emails not going to spam
- [ ] Test email unsubscribe

---

### 8. HOSTING & INFRASTRUCTURE

#### Railway
- [ ] Verify custom domain: flowcast.space connected
- [ ] Test www.flowcast.space redirects correctly
- [ ] Verify SSL certificates are active
- [ ] Check auto-deploy is working from GitHub
- [ ] Verify environment variables are set:
  - DATABASE_URL
  - GEMINI_API_KEY
  - PADDLE_API_KEY
  - YOUTUBE_API_KEY
  - INSTAGRAM_APP_ID
  - INSTAGRAM_APP_SECRET
  - TIKTOK_CLIENT_KEY
  - TIKTOK_CLIENT_SECRET
  - SECRET_KEY (Flask)
  - Any other API keys
- [ ] Test site loads without errors
- [ ] Check logs for any startup errors

#### Cloudflare
- [ ] Verify SSL/TLS set to "Full (Strict)"
- [ ] Enable "Always Use HTTPS"
- [ ] Enable Bot Fight Mode
- [ ] Set Security Level to Medium
- [ ] Verify DNS records:
  - CNAME @ → Railway
  - CNAME www → Railway
- [ ] Test global CDN is caching assets

---

### 9. SECURITY CHECKLIST
- [ ] Verify no secrets in code (run git-secrets or similar)
- [ ] Ensure .env file is in .gitignore
- [ ] Verify DEBUG=False in production
- [ ] Test for SQL injection vulnerabilities
- [ ] Test for XSS vulnerabilities
- [ ] Verify rate limiting is enabled
- [ ] Check CORS settings are correct
- [ ] Verify session security (HttpOnly, Secure flags)
- [ ] Run security scan (if available)

---

### 10. MONITORING & LOGGING
- [ ] Set up error tracking (Sentry or similar)
- [ ] Configure application logs
- [ ] Set up uptime monitoring
- [ ] Configure alerts for:
  - Site down
  - High error rates
  - Database connection failures
  - Payment failures
- [ ] Test log rotation (to prevent disk full)

---

## 🟡 HIGH PRIORITY (Complete Before Public Beta)

### 11. USER ONBOARDING
- [ ] Test first-time user experience
- [ ] Verify onboarding tutorial works
- [ ] Test "Connect Your First Platform" flow
- [ ] Verify empty state messages
- [ ] Test help tooltips

### 12. ANALYTICS & TRACKING
- [ ] Set up Google Analytics 4
- [ ] Configure conversion tracking
- [ ] Verify UTM parameter handling
- [ ] Set up privacy-compliant tracking

### 13. LEGAL & COMPLIANCE
- [ ] Verify Terms of Service is current
- [ ] Verify Privacy Policy is current
- [ ] Verify Refund Policy is current
- [ ] Test cookie consent banner (if required)
- [ ] Verify GDPR compliance (data export, deletion)

### 14. PERFORMANCE
- [ ] Test page load speed (target < 3 seconds)
- [ ] Optimize images
- [ ] Verify lazy loading works
- [ ] Test mobile responsiveness
- [ ] Check for broken links

---

## 🟢 NICE TO HAVE (Can Add After Initial Testing)

### 15. ADDITIONAL FEATURES
- [ ] Review submission system
- [ ] Win-back email campaigns
- [ ] Advanced analytics dashboard
- [ ] Team collaboration features
- [ ] Content templates library

---

## 🧪 TESTING SCENARIOS

### End-to-End Test 1: New User Journey
1. Visit flowcast.space
2. Click "Get Started"
3. Create account
4. Verify email (if applicable)
5. Login
6. Connect YouTube account
7. Generate AI content ideas
8. Schedule a post
9. Verify post appears in calendar
10. Wait for scheduled time, verify post publishes
11. Check email confirmation received

### End-to-End Test 2: Paid Conversion
1. Create free trial account
2. Use up AI credits
3. Click "Upgrade"
4. Select Creator plan
5. Complete Paddle checkout
6. Verify subscription active
7. Verify credits replenished
8. Test subscription management (cancel/upgrade)

### End-to-End Test 3: Error Handling
1. Try to login with wrong password (should fail gracefully)
2. Disconnect internet during post creation (should save draft)
3. Try to upload oversized image (should show error)
4. Try to schedule post in past (should prevent)
5. Revoke OAuth access, try to post (should handle error)

---

## 📋 PRE-LAUNCH SIGN-OFF

Before going live, verify:

- [ ] All critical path items complete
- [ ] No console errors in browser
- [ ] All integrations tested
- [ ] Payment flow working
- [ ] Database backed up
- [ ] Rollback plan ready
- [ ] Support email (billing@flowcast.space) monitored
- [ ] Team (you + me) on standby for issues

---

## 🚨 EMERGENCY CONTACTS

| Issue | Action |
|-------|--------|
| Site down | Check Railway dashboard → restart if needed |
| Database errors | Check Railway logs → restore from backup |
| Payment failures | Check Paddle dashboard → verify webhooks |
| Security breach | Rotate ALL API keys immediately |
| High traffic | Scale Railway instances |

---

## 📅 WEEKEND TIMELINE

### Saturday Morning (9 AM)
- [ ] Receive reminder notification
- [ ] Review this checklist
- [ ] Start with authentication testing

### Saturday Afternoon
- [ ] Complete payment integration testing
- [ ] Test all social platform connections

### Sunday
- [ ] End-to-end testing
- [ ] Security audit
- [ ] Performance check
- [ ] Final bug fixes

### Sunday Evening
- [ ] Final sign-off
- [ ] Prepare for beta launch Monday

---

## 📝 NOTES

**Created:** February 26, 2026  
**Last Updated:** February 26, 2026  
**Status:** Ready for weekend execution  
**Blockers:** None identified

**Remember:** It's better to launch with fewer features that work perfectly than many features that are buggy. Focus on the core: login → connect platforms → schedule posts → AI ideas. Everything else is bonus.

---

*Good luck this weekend! 🚀*
