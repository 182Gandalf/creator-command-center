# TikTok Content Posting API - Implementation Guide for FlowCast
## Based on https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content/

---

## 🔑 KEY REQUIREMENTS

### Prerequisites Checklist

| Requirement | Status | Notes |
|-------------|--------|-------|
| **Registered TikTok App** | ⬜ Required | Create at developers.tiktok.com |
| **Content Posting API Product** | ⬜ Add to app | Enable in app settings |
| **video.upload Scope Approval** | ⬜ Must be approved | TikTok reviews apps |
| **User Authorization** | ⬜ OAuth2 flow | User must authorize video.upload scope |
| **Access Token + Open ID** | ⬜ From OAuth | Required for all API calls |
| **Verified Domain (optional)** | ⬜ For URL uploads | Only needed for PULL_FROM_URL |

---

## 📋 API OVERVIEW

### Base URL
```
https://open.tiktokapis.com/v2/
```

### Key Endpoint
```
POST /v2/post/publish/inbox/video/init/
```

### Rate Limits
- **6 requests per minute** per user access token
- Plan accordingly for bulk uploads

---

## 🚀 UPLOAD METHODS

### Method 1: FILE_UPLOAD (Direct Upload)

**Best for:** Videos stored on your server

**Flow:**
1. Initialize upload → get `upload_url` and `publish_id`
2. PUT video file to `upload_url`
3. Check status with `publish_id`

**Request:**
```bash
curl --location 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/' \
--header 'Authorization: Bearer {USER_ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "source_info": {
    "source": "FILE_UPLOAD",
    "video_size": 30567100,
    "chunk_size": 30567100,
    "total_chunk_count": 1
  }
}'
```

**Response:**
```json
{
  "data": {
    "publish_id": "v_inbox_file~v2.123456789",
    "upload_url": "https://open-upload.tiktokapis.com/video/?upload_id=67890&upload_token=Xza123"
  },
  "error": {
    "code": "ok",
    "message": "",
    "log_id": "202210112248442CB9319E1FB30C1073F3"
  }
}
```

**Upload the file:**
```bash
curl --location --request PUT '{upload_url}' \
--header 'Content-Range: bytes 0-30567099/30567100' \
--header 'Content-Type: video/mp4' \
--data '@/path/to/video.mp4'
```

---

### Method 2: PULL_FROM_URL (URL Upload)

**Best for:** Videos hosted on your CDN/S3

**Requirements:**
- Domain must be verified with TikTok
- Video must be publicly accessible
- URL must use HTTPS

**Flow:**
1. Verify domain with TikTok (one-time)
2. Initialize with URL → get `publish_id`
3. TikTok fetches video asynchronously
4. Check status with `publish_id`

**Request:**
```bash
curl --location 'https://open.tiktokapis.com/v2/post/publish/inbox/video/init/' \
--header 'Authorization: Bearer {USER_ACCESS_TOKEN}' \
--header 'Content-Type: application/json' \
--data '{
  "source_info": {
    "source": "PULL_FROM_URL",
    "video_url": "https://cdn.yourdomain.com/videos/example.mp4"
  }
}'
```

**Response:**
```json
{
  "data": {
    "publish_id": "v_inbox_url~v2.123456789"
  },
  "error": {
    "code": "ok",
    "message": "",
    "log_id": "202210112248442CB9319E1FB30C1073F4"
  }
}
```

---

## 📱 USER WORKFLOW

### Important: User Must Complete Post in TikTok App

After successful upload:

1. **User receives inbox notification** in TikTok app
2. **User clicks notification** → opens video in TikTok editor
3. **User can add:**
   - Captions
   - Hashtags
   - Effects
   - Sounds
   - Cover image
4. **User posts** to their profile

**Your app CANNOT:**
- ❌ Auto-post directly to TikTok
- ❌ Set captions/hashtags
- ❌ Schedule posts
- ❌ Choose cover images

**Your app CAN:**
- ✅ Upload video to user's TikTok inbox
- ✅ Notify user to complete post
- ✅ Check upload status

---

## 🎥 VIDEO REQUIREMENTS

### Supported Formats
| Format | Container | Video Codec | Audio Codec |
|--------|-----------|-------------|-------------|
| MP4 | .mp4 | H.264 | AAC |
| MOV | .mov | H.264 | AAC |

### Specifications
| Requirement | Minimum | Maximum |
|-------------|---------|---------|
| **Duration** | 3 seconds | 10 minutes |
| **File Size** | - | 2 GB |
| **Resolution** | 540x960 | 1080x1920 (9:16) |
| **Frame Rate** | - | 60 fps |
| **Bitrate** | - | 25 Mbps |

**Recommended:**
- 1080x1920 (9:16 aspect ratio)
- 30-60 fps
- H.264 codec
- AAC audio

---

## 📸 PHOTO REQUIREMENTS

### For Photo Uploads
- Must use **PULL_FROM_URL** method
- Domain must be verified
- Supported: JPG, PNG, WEBP
- Max: 2 MB per photo

---

## 🔐 DOMAIN VERIFICATION (For URL Uploads)

### Steps:
1. Go to TikTok Developer Portal
2. Navigate to your app → Content Posting API
3. Add domain or URL prefix
4. Add verification file to your server OR
5. Add DNS TXT record
6. Wait for TikTok approval

**Recommended for FlowCast:**
- Verify your CDN domain (e.g., `cdn.flowcast.app`)
- Allows PULL_FROM_URL method
- Faster uploads (no file transfer)

---

## 🔧 PYTHON IMPLEMENTATION

### Step 1: OAuth2 Authorization

```python
import requests

class TikTokAPI:
    def __init__(self, client_key, client_secret):
        self.client_key = client_key
        self.client_secret = client_secret
        self.base_url = "https://open.tiktokapis.com/v2"
    
    def get_auth_url(self, redirect_uri):
        """Generate TikTok OAuth URL"""
        scope = "video.upload"  # Required scope
        auth_url = f"https://www.tiktok.com/auth/authorize/"
        params = {
            "client_key": self.client_key,
            "redirect_uri": redirect_uri,
            "scope": scope,
            "response_type": "code",
            "state": "random_state_string"  # CSRF protection
        }
        return f"{auth_url}?{urlencode(params)}"
    
    def exchange_code_for_token(self, code, redirect_uri):
        """Exchange auth code for access token"""
        url = f"{self.base_url}/oauth/token/"
        data = {
            "client_key": self.client_key,
            "client_secret": self.client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri
        }
        
        response = requests.post(url, data=data)
        return response.json()
```

### Step 2: Initialize Upload

```python
    def initialize_video_upload(self, access_token, video_size, 
                                 upload_method="FILE_UPLOAD", 
                                 video_url=None):
        """
        Initialize video upload
        
        Args:
            access_token: User's TikTok access token
            video_size: Size in bytes (for FILE_UPLOAD)
            upload_method: "FILE_UPLOAD" or "PULL_FROM_URL"
            video_url: Required if method is PULL_FROM_URL
        """
        url = f"{self.base_url}/post/publish/inbox/video/init/"
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        source_info = {"source": upload_method}
        
        if upload_method == "FILE_UPLOAD":
            source_info.update({
                "video_size": video_size,
                "chunk_size": video_size,  # Single chunk for small videos
                "total_chunk_count": 1
            })
        elif upload_method == "PULL_FROM_URL":
            source_info["video_url"] = video_url
        
        data = {"source_info": source_info}
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()
```

### Step 3: Upload Video File

```python
    def upload_video_file(self, upload_url, video_path):
        """Upload video file to TikTok servers"""
        import os
        
        file_size = os.path.getsize(video_path)
        
        headers = {
            "Content-Range": f"bytes 0-{file_size-1}/{file_size}",
            "Content-Type": "video/mp4"
        }
        
        with open(video_path, 'rb') as f:
            response = requests.put(upload_url, headers=headers, data=f)
        
        return response.status_code == 200
```

### Step 4: Check Post Status

```python
    def check_post_status(self, access_token, publish_id):
        """Check the status of a post"""
        url = f"{self.base_url}/post/publish/status/fetch/"
        
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        data = {"publish_id": publish_id}
        
        response = requests.post(url, headers=headers, json=data)
        return response.json()
```

### Complete Upload Workflow

```python
# Usage example
tiktok = TikTokAPI(
    client_key="your-client-key",
    client_secret="your-client-secret"
)

# 1. Initialize upload (FILE_UPLOAD method)
result = tiktok.initialize_video_upload(
    access_token="user-access-token",
    video_size=30567100,  # bytes
    upload_method="FILE_UPLOAD"
)

if result.get("error", {}).get("code") == "ok":
    publish_id = result["data"]["publish_id"]
    upload_url = result["data"]["upload_url"]
    
    # 2. Upload the video file
    success = tiktok.upload_video_file(upload_url, "/path/to/video.mp4")
    
    if success:
        # 3. Check status (video processing is async)
        import time
        for _ in range(10):  # Check 10 times
            time.sleep(5)
            status = tiktok.check_post_status(
                access_token="user-access-token",
                publish_id=publish_id
            )
            print(f"Status: {status}")
            
            if status.get("data", {}).get("status") == "PUBLISH_COMPLETE":
                print("Upload complete!")
                break
```

---

## 🌐 INTEGRATION WITH FLOWCAST

### Database Schema Addition

```python
class TikTokAccount(db.Model):
    """TikTok OAuth credentials for users"""
    __tablename__ = 'tiktok_accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    open_id = db.Column(db.String(100), unique=True)  # TikTok user ID
    access_token = db.Column(db.Text)  # OAuth access token
    refresh_token = db.Column(db.Text)  # OAuth refresh token
    expires_at = db.Column(db.DateTime)  # Token expiration
    connected_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
```

### API Routes to Add

```python
@app.route('/api/tiktok/connect')
def tiktok_connect():
    """Initiate TikTok OAuth flow"""
    # Redirect user to TikTok authorization
    pass

@app.route('/api/tiktok/callback')
def tiktok_callback():
    """Handle TikTok OAuth callback"""
    # Exchange code for tokens
    pass

@app.route('/api/tiktok/upload', methods=['POST'])
def tiktok_upload():
    """Upload video to TikTok inbox"""
    # Initialize upload
    # Upload file or provide URL
    # Return publish_id
    pass

@app.route('/api/tiktok/status/<publish_id>')
def tiktok_status(publish_id):
    """Check upload status"""
    pass
```

---

## ⚠️ LIMITATIONS & CONSIDERATIONS

### Major Limitations
1. **No Auto-Posting** - User must complete post in TikTok app
2. **No Scheduling** - TikTok API doesn't support scheduled posts
3. **Rate Limits** - 6 requests/minute per user
4. **No Caption/Hashtag API** - Can't pre-fill captions
5. **Approval Required** - TikTok must approve your app

### Workarounds for FlowCast

| Limitation | Workaround |
|------------|------------|
| No scheduling | Store in FlowCast DB, notify user at scheduled time |
| No auto-post | Send push notification: "Your video is ready to post!" |
| No captions | Store caption suggestions, user copies in TikTok app |
| Rate limits | Queue uploads, process 6/minute per user |

---

## 📊 COST COMPARISON

| Feature | TikTok API | Instagram API | YouTube API |
|---------|-----------|---------------|-------------|
| **Price** | Free | Free | Free |
| **Auto-post** | ❌ No | ✅ Yes | ✅ Yes |
| **Scheduling** | ❌ No | ❌ No | ✅ Yes |
| **Captions API** | ❌ No | ❌ No | ✅ Yes |
| **Rate Limits** | 6/min | 200/hour | 10,000/day |

---

## ✅ IMPLEMENTATION CHECKLIST

### Phase 1: Setup (Week 1)
- [ ] Register TikTok developer account
- [ ] Create app at developers.tiktok.com
- [ ] Apply for video.upload scope
- [ ] Wait for TikTok approval (can take days/weeks)

### Phase 2: OAuth Integration (Week 2)
- [ ] Implement OAuth2 flow
- [ ] Store access/refresh tokens
- [ ] Handle token refresh
- [ ] Test with sandbox user

### Phase 3: Upload Feature (Week 3)
- [ ] Implement initialize upload
- [ ] Implement file upload (FILE_UPLOAD)
- [ ] Implement URL upload (PULL_FROM_URL) - optional
- [ ] Add status checking
- [ ] Handle errors gracefully

### Phase 4: UI Integration (Week 4)
- [ ] Add "Connect TikTok" button
- [ ] Add TikTok to platform list
- [ ] Show upload status
- [ ] Notify user to complete post in app

---

## 🔗 USEFUL LINKS

- **TikTok for Developers:** https://developers.tiktok.com
- **Content Posting API Docs:** https://developers.tiktok.com/doc/content-posting-api-get-started-upload-content/
- **OAuth Guide:** https://developers.tiktok.com/doc/login-kit-web/
- **API Reference:** https://developers.tiktok.com/doc/content-posting-api-reference-upload-video/
- **Scopes:** https://developers.tiktok.com/doc/scopes-overview/

---

## 📝 SUMMARY

**TikTok API is useful BUT limited:**

✅ **Pros:**
- Free to use
- Direct video upload
- Good for creator workflow

❌ **Cons:**
- Cannot auto-post (user must complete in app)
- Cannot schedule
- Cannot set captions/hashtags
- Requires app approval
- Rate limited (6/min)

**Recommendation:**
Implement TikTok as a "Draft Upload" feature - user gets notification to complete post in TikTok app. This is still valuable (saves download/upload steps) but different from YouTube/Instagram auto-posting.

**Priority:** Medium - Add after YouTube and Instagram are stable.
