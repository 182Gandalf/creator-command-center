# FlowCast TikTok Integration - Product & Scope Explanation

## App Overview

FlowCast is an AI-powered content scheduling platform designed for creators. Our application enables users to plan, create, and publish content across multiple social media platforms from a unified dashboard. With TikTok integration, creators can compose posts with captions and hashtags, set privacy controls, and publish directly to their TikTok profiles without leaving FlowCast.

## TikTok Products Used

### Content Posting API - Direct Post

FlowCast utilizes TikTok's Direct Post API to enable seamless content publishing. This integration allows creators to:

- **Upload and Publish Videos:** Users can upload video files (MP4, MOV) up to 500MB and 10 minutes in duration. The video is transferred from FlowCast's servers directly to the user's TikTok profile.
- **Publish Photos:** Support for photo posts with captions, allowing creators to share image content alongside video content.
- **Compose Captions:** Full caption editing with support for hashtags, mentions, and up to 2,200 characters of text. Our AI assistant can suggest relevant hashtags based on content type.
- **Control Privacy Settings:** Users can set visibility to PUBLIC (everyone), FRIENDS_ONLY (followers), or SELF_ONLY (private) for each post.
- **Manage Engagement Options:** Toggle comments, duets, and stitches on or off per post, giving creators full control over how their audience interacts with content.

### Login Kit (OAuth 2.0)

FlowCast uses Login Kit for secure authentication:
- Users connect their TikTok account via OAuth 2.0 flow
- One-time authorization grants FlowCast permission to post on their behalf
- Users can revoke access anytime from their FlowCast dashboard or TikTok settings

## Scopes Required & Usage

### video.publish (Required)

**Purpose:** Enables FlowCast to publish content directly to users' TikTok profiles.

**How It's Used:**
- When a user schedules or publishes content through FlowCast, this scope allows our application to transfer video/photo files and associated metadata (caption, hashtags, privacy settings) to TikTok's servers.
- The scope is only invoked when the user explicitly clicks "Publish" or when scheduled content reaches its publication time.
- FlowCast stores a draft locally; only upon user approval or scheduled trigger does the actual publishing occur.

**User Control:** Users can disable automatic publishing and use FlowCast solely for drafting, with a manual review step before each post goes live.

### video.list (Required)

**Purpose:** Allows FlowCast to check the status of published content.

**How It's Used:**
- After publishing, FlowCast queries the post status to confirm successful upload.
- Displays publishing status (pending, processing, published, failed) in the user's dashboard.
- Tracks post metrics and availability for analytics display within FlowCast.
- Enables error handling and retry mechanisms if a post fails to upload.

### user.info.basic (Required)

**Purpose:** Identifies the TikTok user account for proper content attribution.

**How It's Used:**
- Retrieves the user's unique Open ID to associate their TikTok account with their FlowCast profile.
- Displays the connected TikTok username/avatar in FlowCast's "Connected Accounts" section.
- Ensures content is posted to the correct TikTok profile when a user has multiple accounts.
- Used for session management and account verification.

## User Experience Flow

### 1. Account Connection
User clicks "Connect TikTok" in FlowCast settings. They're redirected to TikTok's OAuth screen where they review requested permissions (video.publish, video.list, user.info.basic). After granting permission, they're returned to FlowCast with their account linked.

### 2. Content Creation
User creates content within FlowCast:
- Uploads video/photo or records directly in browser
- Writes caption using our AI suggestion tool for hashtag optimization
- Sets privacy level (public, friends, private)
- Configures engagement settings (comments on/off, duets allowed, etc.)
- Schedules publication time or selects "Post Now"

### 3. Publishing Process
When publish is triggered:
- FlowCast validates media meets TikTok's requirements (format, size, duration)
- Media is uploaded to TikTok via Direct Post API
- Caption and metadata are transmitted
- User sees real-time status updates in their FlowCast dashboard
- Upon success, the post appears on their TikTok profile

### 4. Management & Revocation
Users can:
- View all scheduled and published TikTok posts in FlowCast calendar
- Edit or delete scheduled posts before publication
- Disconnect TikTok account anytime (revokes all scopes)
- View analytics on post performance

## Data Handling & Privacy

### What We Store
- **Access Tokens:** Encrypted OAuth tokens for API authentication (stored with Fernet encryption)
- **Post Metadata:** Caption text, privacy settings, scheduled times, and TikTok post IDs
- **Media Files:** Temporarily stored during upload process, then purged after successful posting

### What We Don't Store
- Raw TikTok login credentials
- User's TikTok password
- Analytics data beyond basic post status

### User Data Protection
- All OAuth tokens are encrypted at rest using industry-standard AES-256 encryption
- Users can delete their account and all associated data via FlowCast settings
- No data is shared with third parties or used for advertising
- Full compliance with GDPR and CCPA requirements

### Revocation
Users can revoke FlowCast's access at any time:
- Through FlowCast: "Disconnect TikTok" button in account settings
- Through TikTok: Settings → Security → Apps and Websites → Remove FlowCast
- Immediate revocation invalidates all access tokens

## Compliance & Safety

FlowCast is designed exclusively for content creators managing their own accounts. We do not support:
- Posting to accounts the user doesn't own
- Automated spam or bulk posting
- Content that violates TikTok's Community Guidelines
- Reselling or transferring API access

All users must agree to FlowCast's Terms of Service and Privacy Policy before connecting TikTok. Our application includes content moderation features and respects TikTok's rate limits to ensure platform stability.

## Changes in This Version (Revision Notes)

- Initial TikTok Direct Post API integration
- Support for both video and photo posting
- AI-powered caption and hashtag suggestions
- Granular privacy and engagement controls
- End-to-end encryption for OAuth tokens

---

**Contact Information:**
- Developer: FlowCast Team
- Support: customersupport@flowcast.space
- Website: https://flowcast.space
- Privacy Policy: https://flowcast.space/privacy
- Terms of Service: https://flowcast.space/terms