# FlowCast Configuration Status & Setup Guide

## ✅ YouTube OAuth Configuration - COMPLETE

Your YouTube credentials are configured correctly. Here's what's needed:

**Environment Variables Required:**
```bash
export YOUTUBE_API_KEY="your-youtube-api-key"
export YOUTUBE_CLIENT_ID="your-oauth-client-id.apps.googleusercontent.com"
export YOUTUBE_CLIENT_SECRET="your-oauth-client-secret"
export TOKEN_ENCRYPTION_KEY="your-secure-encryption-key-here"
```

**Note:** Get these from your Google Cloud Console → Credentials → OAuth 2.0 Client IDs

**YouTube OAuth Redirect URI:**
Make sure this is added in your Google Cloud Console:
- `https://flowcast.space/api/youtube/callback`
- `http://localhost:5000/api/youtube/callback` (for local testing)

**Status:** ✅ Ready to test

---

## 📋 Meta/Instagram App Review Process

### Step 1: Create Meta App
1. Go to https://developers.facebook.com/
2. Create new app → Select "Other" → "Consumer"
3. Add "Instagram Basic Display" product

### Step 2: Configure Instagram Basic Display
- Add platform: Website → `https://flowcast.space`
- Valid OAuth Redirect URIs:
  - `https://flowcast.space/api/instagram/callback`
- Deauthorize Callback URL: `https://flowcast.space/api/instagram/deauth`
- Data Deletion Request URL: `https://flowcast.space/api/instagram/delete`

### Step 3: Add Test Users (Before Review)
- Add Instagram accounts as test users in Meta Dashboard
- These can use the integration immediately
- Max 5 test users during development

### Step 4: App Review Requirements
**You need to provide:**
1. **Screen Recording** showing:
   - How users connect their Instagram account
   - How content is scheduled
   - The posting flow
   
2. **Business Verification:**
   - Business license or official documents
   - Domain verification (DNS TXT record)
   - Privacy policy URL
   - Data use terms

3. **Permissions Requested:**
   - `instagram_basic` - Read basic profile info
   - `instagram_content_publish` - Publish posts (hardest to get)

### Step 5: Review Timeline
- **Submission review:** 5-7 business days
- **If rejected:** Fix issues and resubmit (another 5-7 days)
- **Common rejections:**
  - Incomplete privacy policy
  - No data deletion method
  - App doesn't clearly show permission usage

**Recommendation:** Start with test users only. Full Instagram publishing requires extensive review.

---

## 🎵 TikTok Integration - Content Posting API

### The API You Need: **TikTok Content Posting API**

**Product:** https://developers.tiktok.com/products/content-posting-api/

### How It Works (Exactly What You Want):

1. **User uploads video** in FlowCast
2. **Your app calls TikTok API** to upload as draft
3. **User receives notification** in TikTok app inbox
4. **User opens TikTok**, finds draft in inbox
5. **User edits and posts** manually on TikTok

### API Endpoints You'll Use:

**1. Video Upload (Draft Mode)**
```
POST https://open-api.tiktok.com/video/upload/
```
- Uploads video to user's TikTok inbox as draft
- User gets notification to complete the post
- Video never auto-publishes

**2. Direct Post (Alternative - skips inbox)**
```
POST https://open-api.tiktok.com/video/direct_post/
```
- Publishes immediately (requires additional permissions)

### Implementation Steps:

**Step 1: Apply for TikTok for Developers**
- https://developers.tiktok.com/
- Create app, request "Content Posting API" access
- Submit app for review (2-4 weeks)

**Step 2: Required Scopes**
```
video.upload
video.list
user.info.basic
```

**Step 3: OAuth Flow**
- Same pattern as YouTube OAuth
- Redirect to TikTok for authorization
- User grants permission to upload content
- Receive access_token

**Step 4: Upload Process**
```python
# 1. Initialize upload
POST /video/upload/
{
  "source_info": {
    "source": "PULL_FROM_URL",
    "url": "https://flowcast.space/uploads/video123.mp4"
  },
  "title": "My Video Title",
  "privacy_level": "SELF_ONLY",  # Draft mode
  "disable_duet": false,
  "disable_comment": false
}

# 2. Response includes publish_id
# 3. Query status until complete
GET /video/list/?publish_id=xxx

# 4. User gets TikTok notification when ready
```

### TikTok Limitations:
- **Video duration:** 15 seconds to 10 minutes
- **File size:** Max 500MB
- **Format:** MP4 or MOV
- **Review required** before public use
- **Quota limits:** Start with 10 uploads/day, increase after review

---

## 🔧 Missing Configuration Items

### 1. Environment Variables (Set these in production):
```bash
# Flask
export SECRET_KEY="your-random-secret-key-at-least-32-chars"

# YouTube (get from Google Cloud Console)
export YOUTUBE_API_KEY="your-youtube-api-key"
export YOUTUBE_CLIENT_ID="your-oauth-client-id"
export YOUTUBE_CLIENT_SECRET="your-oauth-client-secret"

# Encryption (CRITICAL for OAuth token security)
export TOKEN_ENCRYPTION_KEY="your-32-char-encryption-key-here!!"

# AI Providers (for content generation)
export GEMINI_API_KEY=""  # Optional, for free tier AI
export DEEPSEEK_API_KEY=""  # Optional, paid but cheap
```

### 2. Paddle Configuration (When Approved):
```bash
export PADDLE_VENDOR_ID=""
export PADDLE_API_KEY=""
export PADDLE_PUBLIC_KEY=""
export PADDLE_WEBHOOK_SECRET=""
```

### 3. Database (SQLite is fine for testing):
- Currently using SQLite: `sqlite:///creator_command_center.db`
- For production: PostgreSQL recommended
- Migrations: `flask db migrate` + `flask db upgrade`

### 4. Email Configuration:
```bash
export MAIL_SERVER="smtp.gmail.com"  # or your provider
export MAIL_PORT=587
export MAIL_USERNAME="customersupport@flowcast.space"
export MAIL_PASSWORD="your-app-password"
export MAIL_USE_TLS=true
```

---

## 🚀 Deployment Checklist

### Pre-Deployment:
- [ ] Set all environment variables
- [ ] Configure YouTube OAuth redirect URIs in Google Cloud Console
- [ ] Set up SSL certificate (Cloudflare handles this)
- [ ] Test database migrations: `flask db upgrade`
- [ ] Test YouTube OAuth flow locally

### Post-Deployment:
- [ ] Test landing page loads
- [ ] Test pricing page
- [ ] Test YouTube connection flow
- [ ] Test creating a scheduled post
- [ ] Verify email sending works
- [ ] Check subscription limits are enforced

---

## 🎯 Recommended Next Steps

### Priority 1: Test YouTube Integration (Today)
1. Deploy current code
2. Set environment variables on server
3. Test YouTube OAuth connection
4. Test video upload flow

### Priority 2: Add TikTok Support (This Week)
1. Apply for TikTok for Developers account
2. Add TikTok OAuth to app.py
3. Implement video upload to inbox
4. Test draft upload flow

### Priority 3: Instagram (Next 2 Weeks)
1. Create Meta app
2. Add test users
3. Implement Instagram Basic Display
4. Submit for app review

### Priority 4: Paddle Integration (After Approval)
1. Add Paddle SDK
2. Create checkout flows
3. Implement webhook handlers
4. Connect to subscription tiers

---

## ❓ Troubleshooting YouTube OAuth Issues

**Problem: "redirect_uri_mismatch"**
- Solution: Add exact URI to Google Cloud Console → Credentials → OAuth 2.0 → Authorized redirect URIs

**Problem: "invalid_client"**
- Solution: Check CLIENT_ID and CLIENT_SECRET are correct

**Problem: "Token encryption failed"**
- Solution: Set TOKEN_ENCRYPTION_KEY environment variable (32+ characters)

**Problem: User can connect but upload fails**
- Solution: Check YouTube API quota in Google Cloud Console (10,000 units/day default)

---

## 📞 Contact Information

All app contact points now use:
- **Support:** customersupport@flowcast.space → routes to gandalftheclaw@gmail.com

Pages updated:
- ✅ index.html
- ✅ pricing.html  
- ✅ privacy.html
- ✅ terms.html
- ✅ refund.html
