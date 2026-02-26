# Open Topics Summary - 2026-02-23

**Prepared for conversation reset**

---

## FlowCast.space - Active Issues & Status

### 1. Deployment (CRITICAL)
- **Status:** Fixed crash (duplicate route), ready to redeploy
- **Pending:** User needs to `git pull` and restart on Railway

### 2. SSL/HTTPS "Not Secure" Warning (HIGH)
- **Issue:** TLS 1.0/1.1 still enabled, HSTS missing
- **Fix Required in Cloudflare:**
  - Set Minimum TLS to 1.2
  - Enable HSTS (6 months, include subdomains, preload)
  - SSL/TLS mode: Full (Strict)
- **Guide:** `SSL-FIXES-PRIORITY.md` in repo

### 3. DNS/Email Errors (MEDIUM)
- **Issues:** Missing DMARC record, SMTP open relay, SOA config
- **Fix:** Add DMARC TXT record, check Cloudflare Email Routing
- **Guide:** `DNS-EMAIL-FIXES.md` in repo

### 4. YouTube OAuth (READY FOR TEST)
- **Status:** Fixed redirect_uri_mismatch error (forced HTTPS)
- **Test URL:** `https://flowcast.space/api/youtube/auth`
- **Needs:** Redeploy first, then test

### 5. Google OAuth (JUST ADDED)
- **Status:** Routes created, needs configuration
- **Needs:** GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET env vars
- **Redirect URI:** `https://flowcast.space/api/google/callback`

### 6. TikTok API (WAITING APPROVAL)
- **Status:** App review submission ready, verification files uploaded
- **Document:** `TIKTOK-APP-REVIEW-SUBMISSION.md` (893 chars)
- **Next:** Submit to TikTok developer portal

### 7. Authentication System (FIXED)
- **Status:** Signup/login working (CORS issue resolved)
- **Note:** "Create account" network error fixed with flask-cors

### 8. Logo (UPDATED)
- **Status:** New logo deployed to all pages
- **File:** `/static/logo-new.jpg`

---

## Immediate Actions for User

1. **Redeploy app** - `git pull origin main` on Railway
2. **Fix SSL in Cloudflare** - Follow `SSL-FIXES-PRIORITY.md`
3. **Add DMARC record** - Follow `DNS-EMAIL-FIXES.md`
4. **Configure Google OAuth** - Add Client ID/Secret to Railway env vars
5. **Submit TikTok app** - Copy text from `TIKTOK-APP-REVIEW-SUBMISSION.md`

---

## Key Files in Repo

- `SSL-FIXES-PRIORITY.md` - SSL configuration steps
- `DNS-EMAIL-FIXES.md` - DNS and email fixes
- `TIKTOK-APP-REVIEW-SUBMISSION.md` - TikTok app review text
- `INTEGRATION-GUIDE.md` - YouTube/TikTok/Meta setup guides
- `DEMO-VIDEO-GUIDE.md` - Demo video script and features

---

## Self-Sufficiency Rule (Committed to SOUL.md)

Before asking user anything, ask: "How can I remove this bottleneck?"

---

*Conversation reset requested - all topics captured*