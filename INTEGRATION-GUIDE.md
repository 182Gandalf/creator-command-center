# FlowCast Integration Status & Guides

**Date:** February 23, 2026  
**Status Update:** YouTube OAuth Ready for Testing, TikTok API Investigation Complete

---

## 1. YouTube OAuth - Ready for Testing ✅

### Configuration Status
- **Redirect URIs:** Added to Google Cloud Console ✓
- **Environment Variables:** Set on server ✓
- **API Key:** Configured ✓
- **Client ID/Secret:** Set ✓

### Test YouTube OAuth Flow

**Step 1: Test Auth URL Generation**
Visit this URL in your browser:
```
https://flowcast.space/api/youtube/auth
```

**Expected Result:** You should be redirected to Google OAuth consent screen asking for YouTube permissions.

**Step 2: Complete OAuth Flow**
- Select/confirm Google account
- Grant YouTube permissions
- Should redirect back to `https://flowcast.space/api/youtube/callback`

**Step 3: Verify Connection**
After callback, check if token is stored by visiting:
```
https://flowcast.space/api/youtube/channels
```

**Expected Result:** JSON response with your YouTube channel info.

### Troubleshooting

If auth fails:
1. Check browser console for errors
2. Verify `YOUTUBE_CLIENT_ID` and `YOUTUBE_CLIENT_SECRET` are set correctly in Railway
3. Confirm redirect URI `https://flowcast.space/api/youtube/callback` is in Google Cloud Console
4. Check that YouTube Data API v3 is enabled in Google Cloud Console

---

## 2. TikTok Direct Post API - Capabilities Investigation ✅

### API Overview
**Product:** TikTok Content Posting API (Direct Post)  
**Your Credentials:**
- Client Key: `awc9mhr7an8b6m9l`
- Client Secret: `EMJrQ6bzOl6ZNeNgqwCxRLxPYr6vUd8N`

### What Direct Post API Enables

✅ **Full Posting Capabilities:**
- Post videos directly to TikTok profiles
- Post photos (NEW - now supported!)
- Write captions with hashtags
- Privacy settings control (public, friends, private)
- Comment/duet/stitch controls
- Cover image selection

✅ **Content Settings:**
- Caption (max 2,200 characters)
- Hashtag support
- Privacy level: PUBLIC, FRIENDS_ONLY, SELF_ONLY
- Allow comments: true/false
- Allow duets: true/false
- Allow stitches: true/false

### Required Scopes
```
video.publish  (required for posting)
video.list     (to check post status)
user.info.basic (for user identification)
```

### Integration Flow

```
1. User clicks "Connect TikTok"
2. OAuth to TikTok → User grants video.publish permission
3. User uploads/schedules content in FlowCast
4. FlowCast calls Direct Post API
5. Content publishes directly to user's TikTok profile
```

### Important: Audit Required for Public Visibility

**⚠️ Critical:** All content posted by unaudited clients defaults to **PRIVATE viewing only**.

To enable public posting, you must:
1. Complete integration testing
2. Submit app for TikTok audit
3. Pass compliance review

**Audit Application:** https://developers.tiktok.com/application/content-posting-api

### API Endpoints You'll Use

**1. Direct Post (Video)**
```
POST https://open-api.tiktok.com/video/direct_post/
Content-Type: application/json
Authorization: Bearer {access_token}

{
  "source_info": {
    "source": "PULL_FROM_URL",
    "url": "https://flowcast.space/uploads/video123.mp4"
  },
  "title": "My awesome video #flowcast #content",
  "privacy_level": "PUBLIC",
  "disable_duet": false,
  "disable_comment": false,
  "disable_stitch": false
}
```

**2. Direct Post (Photo)**
```
POST https://open-api.tiktok.com/photo/direct_post/
Content-Type: application/json
Authorization: Bearer {access_token}

{
  "source_info": {
    "source": "PULL_FROM_URL",
    "url": "https://flowcast.space/uploads/photo123.jpg"
  },
  "title": "My photo caption #flowcast",
  "privacy_level": "PUBLIC"
}
```

### Technical Requirements
- Video formats: MP4 (H.264), MOV
- Video duration: 15 seconds to 10 minutes
- Video size: Max 500MB
- Photo: JPG/PNG, max 20MB
- Domain verification required for URL sources

### Implementation Status
✅ OAuth routes added to app.py  
⏳ Needs: Domain verification for media URLs  
⏳ Needs: Audit application for public posting  

---

## 3. Privacy & Terms URLs for TikTok Verification ✅

### Status: LIVE

**Privacy Policy:** https://flowcast.space/privacy  
**Terms of Service:** https://flowcast.space/terms

Both pages are live and accessible. TikTok requires these for app approval.

### TikTok App Configuration Checklist

**Required URLs for TikTok Developer Portal:**
- [ ] Privacy Policy URL: `https://flowcast.space/privacy`
- [ ] Terms of Service URL: `https://flowcast.space/terms`
- [ ] App Icon (1024x1024 PNG)
- [ ] App Description
- [ ] Category: Content Creation / Social Media

**Configure in TikTok Developer Portal:**
1. Go to https://developers.tiktok.com/
2. Select your app
3. Settings → Basic Information
4. Add Privacy Policy and Terms URLs
5. Save changes

---

## 4. Meta/Instagram App Review - Step-by-Step Guide

### ⚠️ IMPORTANT UPDATE (September 2024)
**Instagram Basic Display API has been DEPRECATED** as of December 4, 2024.

**New Solution:** Instagram Graph API + Instagram Business Login

### Prerequisites for Instagram Graph API

1. **Facebook Business Account**
2. **Instagram Business Account** (or Creator Account)
3. **Facebook Page** connected to Instagram account
4. **Meta Business Portfolio** (formerly Business Manager)

### Step-by-Step Setup

#### Step 1: Convert Instagram to Business Account
1. Open Instagram app
2. Go to Settings → Account
3. Select "Switch to Professional Account"
4. Choose "Business" (not Creator)
5. Complete setup wizard

#### Step 2: Create Facebook Page
1. Go to https://www.facebook.com/pages/create
2. Select category (e.g., "Software Company")
3. Name: "FlowCast"
4. Complete page setup

#### Step 3: Connect Instagram to Facebook Page
1. Go to Facebook Page → Settings
2. Click "Linked Accounts"
3. Select "Instagram"
4. Click "Connect Account"
5. Login with Instagram credentials
6. Grant permissions

#### Step 4: Create Meta App
1. Go to https://developers.facebook.com/
2. Click "My Apps" → "Create App"
3. Select "Business" app type
4. App Name: "FlowCast"
5. App Contact Email: your email
6. Business Portfolio: Select or create new

#### Step 5: Add Instagram Graph API Product
1. In App Dashboard, click "Add Product"
2. Find "Instagram Graph API"
3. Click "Set Up"

#### Step 6: Configure Instagram Business Login
1. Go to Products → Instagram Graph API → Settings
2. Add "Instagram Business Login" product
3. Configure OAuth redirect URI:
   - `https://flowcast.space/api/instagram/callback`

#### Step 7: Request Required Permissions
In App Review → Permissions and Features, request:

**Required Permissions:**
- `instagram_basic` - Read profile info
- `instagram_content_publish` - Publish posts
- `pages_read_engagement` - Read page engagement

**Usage Description Examples:**
```
instagram_basic: "We use this permission to display the user's Instagram profile information and connected accounts in our content scheduling dashboard."

instagram_content_publish: "We use this permission to allow users to schedule and publish content directly to their Instagram business accounts through our platform."

pages_read_engagement: "We use this permission to verify the connection between the Facebook Page and Instagram Business account."
```

#### Step 8: Business Verification (CRITICAL)
Before app review, you must complete Business Verification:

1. Go to Settings → Basic
2. Scroll to "Business Verification"
3. Click "Start Verification"
4. Provide:
   - Business legal name
   - Business address
   - Business phone
   - Business website (flowcast.space)
   - Verification document (business license, tax doc, etc.)

**Verification takes 3-5 business days.**

#### Step 9: Add Test Users (Before Review)
1. Go to Roles → Test Users
2. Click "Add Test Users"
3. Add Instagram Business accounts
4. These can test immediately without review

#### Step 10: Submit for App Review
1. Go to App Review → Requests
2. Click "Add to Submission"
3. Select permissions: instagram_basic, instagram_content_publish
4. Complete video screencast showing:
   - User login flow
   - How permission is used
   - Data handling
5. Submit review

**Review Timeline:** 5-10 business days

#### Step 11: Configure Webhooks (Optional but Recommended)
For real-time updates on post status:
1. Go to Products → Instagram Graph API → Webhooks
2. Subscribe to fields: mentions, story_insights
3. Callback URL: `https://flowcast.space/api/instagram/webhook`
4. Verify token: Set in environment variables

### Meta App Review Requirements

**Video Screencast Must Show:**
1. User authenticating with Instagram
2. Granting requested permissions
3. Using the integration (scheduling/posting)
4. Logout/disconnect option

**Privacy Requirements:**
- [ ] Valid Privacy Policy URL
- [ ] Valid Terms of Service URL
- [ ] Data deletion instructions
- [ ] User data handling explanation

**Common Rejection Reasons:**
- Missing Business Verification
- Vague permission use descriptions
- No screencast or poor quality
- Test users not configured
- Broken functionality

### Implementation Code

**OAuth URL:**
```
https://www.facebook.com/v18.0/dialog/oauth?
  client_id={app_id}
  &redirect_uri=https://flowcast.space/api/instagram/callback
  &scope=instagram_basic,instagram_content_publish,pages_read_engagement
  &response_type=code
```

**Exchange Code for Token:**
```
POST https://graph.facebook.com/v18.0/oauth/access_token
  ?client_id={app_id}
  &client_secret={app_secret}
  &redirect_uri=https://flowcast.space/api/instagram/callback
  &code={code}
```

**Publish Post:**
```
POST https://graph.facebook.com/v18.0/{instagram_business_account_id}/media
  ?image_url={image_url}
  &caption={caption}
  &access_token={access_token}
```

### Current Status
❌ Not started - Awaiting your go-ahead  
⏳ Pending: Facebook Business Account setup  
⏳ Pending: Instagram Business conversion  
⏳ Pending: Meta app creation  

---

## Summary: Next Actions

### Immediate (Today)
1. **Test YouTube OAuth** - Visit `/api/youtube/auth`
2. **Verify TikTok URLs work** - Check privacy/terms pages load
3. **Apply for TikTok audit** - After testing direct post

### This Week
1. **Set up Facebook Business Account**
2. **Convert Instagram to Business account**
3. **Create Meta app** and add Instagram Graph API
4. **Complete Business Verification** (takes 3-5 days)

### Next Week
1. **Submit Meta app for review**
2. **TikTok audit application**
3. **Test all three platforms**

---

*Questions or issues with any step? Let me know!*
