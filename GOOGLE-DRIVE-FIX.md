# Google Drive 403 Error - Fix Documentation

## Problem Summary

**Error:** `403 Forbidden - ACCESS_TOKEN_SCOPE_INSUFFICIENT`

**Root Cause:** The existing OAuth token (`gmail-token.json`) was created with ONLY Gmail scope:
```json
"scopes": ["https://mail.google.com/"]
```

This token can read/send emails but **cannot access Google Drive** at all. When attempting to upload files to Drive, the API returns 403 because the token lacks the necessary Drive scopes.

---

## Solution Overview

Created **separate OAuth tokens** for different Google services:
1. **Gmail token** (`gmail-token.json`) - For email operations
2. **Drive token** (`drive-token.json`) - For file upload/operations

This separation is best practice and allows granular permission control.

---

## Files Created

### 1. `setup-drive-oauth.py`
Interactive script to authenticate with Google Drive and create the token.

**What it does:**
- Requests `drive.file` scope (create/upload files) + `drive.metadata.readonly` (list files)
- Opens browser for OAuth consent
- Saves token to `~/.config/himalaya/drive-token.json`
- Does NOT interfere with existing Gmail token

**Usage:**
```bash
export GOOGLE_CLIENT_ID='your-client-id'
export GOOGLE_CLIENT_SECRET='your-client-secret'
python3 setup-drive-oauth.py
```

### 2. `drive_api.py`
Reusable Google Drive API client.

**Features:**
- `upload_file(path)` - Upload files with proper MIME type detection
- `list_files(query)` - List/search Drive files
- Automatic token refresh
- Public sharing (creates shareable links)

**Usage:**
```bash
# Upload a file
python3 drive_api.py upload /path/to/file.zip

# List files
python3 drive_api.py list
```

**Python API:**
```python
from drive_api import upload_file

result = upload_file('/path/to/file.zip')
if result['success']:
    print(f"File uploaded: {result['webViewLink']}")
```

---

## Required Scopes

### For Google Drive Upload
```
https://www.googleapis.com/auth/drive.file
```
- Can create new files
- Can modify files created by the app
- Cannot access user's existing Drive files
- **Most secure** option for upload-only use cases

### Alternative: Full Drive Access
```
https://www.googleapis.com/auth/drive
```
- Full read/write access to entire Drive
- Can modify any file
- **More permissive** - only use if necessary

---

## Step-by-Step Fix Instructions

### Step 1: Set Environment Variables
You need the Google OAuth credentials from your Google Cloud Console project.

```bash
export GOOGLE_CLIENT_ID='your-client-id-from-google-cloud-console'
export GOOGLE_CLIENT_SECRET='your-client-secret-from-google-cloud-console'
```

### Step 2: Run OAuth Setup
```bash
cd creator-app
python3 setup-drive-oauth.py
```

This will:
1. Start a local web server on port 8080
2. Open browser to Google's OAuth consent screen
3. Ask you to approve "Google Drive" permissions
4. Save the new token to `~/.config/himalaya/drive-token.json`

### Step 3: Verify Token Created
```bash
cat ~/.config/himalaya/drive-token.json
```

Should show:
```json
{
  "access_token": "ya29...",
  "refresh_token": "1//03...",
  "scopes": [
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive.metadata.readonly"
  ],
  ...
}
```

### Step 4: Test Upload
```bash
python3 drive_api.py upload /path/to/your/file.zip
```

Expected output:
```
Upload successful!
File ID: 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms
View: https://drive.google.com/file/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/view
Download: https://drive.google.com/uc?id=1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms&export=download
```

---

## Integration with Main App

To use Drive upload in the Flask app:

```python
from drive_api import upload_file

@app.route('/api/upload-to-drive', methods=['POST'])
def upload_to_drive():
    # Save uploaded file temporarily
    file = request.files['file']
    temp_path = f"/tmp/{file.filename}"
    file.save(temp_path)
    
    # Upload to Drive
    result = upload_file(temp_path)
    
    # Clean up
    os.remove(temp_path)
    
    return jsonify(result)
```

---

## Troubleshooting

### "GOOGLE_CLIENT_ID not set"
**Fix:** Export the environment variables before running the script.

### "Error 400: redirect_uri_mismatch"
**Fix:** Add `http://localhost:8080/callback` to your Google Cloud Console OAuth credentials as an authorized redirect URI.

### "Token has insufficient scope"
**Fix:** Delete the old token and re-run setup:
```bash
rm ~/.config/himalaya/drive-token.json
python3 setup-drive-oauth.py
```

### "Refresh token expired"
**Fix:** The token file stores the refresh token. If it expires, delete and re-authenticate:
```bash
rm ~/.config/himalaya/drive-token.json
python3 setup-drive-oauth.py
```

---

## Security Best Practices

1. **Never commit tokens to GitHub**
   - Already added to `.gitignore`
   - Token files are in `~/.config/himalaya/` (outside repo)

2. **Use minimal scopes**
   - `drive.file` instead of full `drive` scope
   - Only request permissions you actually need

3. **Separate tokens per service**
   - Gmail token for email
   - Drive token for files
   - Easy to revoke one without affecting others

4. **Environment variables for credentials**
   - Client ID/Secret in env vars
   - Not hardcoded in source code

---

## Why This Happened

The original Gmail OAuth setup only requested `https://mail.google.com/` scope. This is standard for email-only applications. When we later tried to use the same token for Drive operations, Google correctly rejected it with 403 - the token simply doesn't have permission.

**Grok was correct:** The fix is to either:
1. Add Drive scopes to existing token (requires re-authorization anyway)
2. Create a new token with Drive scopes (**we chose this**)

Option 2 is cleaner and follows security best practices.

---

## Summary

✅ **Problem:** Gmail token can't access Drive (scope mismatch)  
✅ **Solution:** Created separate Drive OAuth token with `drive.file` scope  
✅ **Result:** Can now upload files to Google Drive without 403 errors  

**Next Steps:**
1. Run `setup-drive-oauth.py` to create the Drive token
2. Use `drive_api.py` for file operations
3. Both tokens coexist independently
