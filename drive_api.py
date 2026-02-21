#!/usr/bin/env python3
"""
Google Drive API Client with Proper Scopes
Uses drive.file scope - can create/upload files, read metadata
"""

import json
import urllib.request
import urllib.parse
import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# Token file for Drive (separate from Gmail)
TOKEN_FILE = "/home/daz/.config/himalaya/drive-token.json"

# Configuration from environment
CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', '')

def get_access_token():
    """Get valid access token (refresh if needed)"""
    with open(TOKEN_FILE, 'r') as f:
        tokens = json.load(f)
    
    # Refresh if needed
    refresh_token = tokens.get('refresh_token')
    if refresh_token:
        data = {
            'refresh_token': refresh_token,
            'client_id': CLIENT_ID or tokens.get('client_id', ''),
            'client_secret': CLIENT_SECRET or tokens.get('client_secret', ''),
            'grant_type': 'refresh_token'
        }
        
        req = urllib.request.Request(
            'https://oauth2.googleapis.com/token',
            data=urllib.parse.urlencode(data).encode(),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        
        try:
            with urllib.request.urlopen(req) as resp:
                new_tokens = json.loads(resp.read().decode())
                tokens['access_token'] = new_tokens['access_token']
                
                # Update file with new access token
                with open(TOKEN_FILE, 'w') as f:
                    json.dump(tokens, f, indent=2)
                
                return tokens['access_token']
        except Exception as e:
            print(f"Warning: Failed to refresh token: {e}")
            # Return existing token as fallback
            return tokens['access_token']
    
    return tokens['access_token']

def upload_file(file_path, folder_id=None, make_public=True):
    """
    Upload a file to Google Drive
    
    Args:
        file_path: Path to file to upload
        folder_id: Optional Drive folder ID to upload into
        make_public: Whether to make file publicly readable
    
    Returns:
        dict with 'id', 'name', 'webViewLink', 'webContentLink'
    """
    if not os.path.exists(TOKEN_FILE):
        return {
            'success': False,
            'error': 'No Drive token found. Run: python3 setup-drive-oauth.py'
        }
    
    access_token = get_access_token()
    filename = os.path.basename(file_path)
    mime_type = 'application/octet-stream'  # Generic binary
    
    # Determine MIME type from extension
    ext = os.path.splitext(filename)[1].lower()
    mime_types = {
        '.txt': 'text/plain',
        '.pdf': 'application/pdf',
        '.zip': 'application/zip',
        '.tar.gz': 'application/gzip',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.mp4': 'video/mp4',
        '.json': 'application/json',
        '.py': 'text/x-python',
        '.js': 'application/javascript',
        '.html': 'text/html',
        '.css': 'text/css'
    }
    if ext in mime_types:
        mime_type = mime_types[ext]
    
    # Read file content
    with open(file_path, 'rb') as f:
        file_content = f.read()
    
    # Build multipart request
    boundary = '---BOUNDARY_xyz789---'
    
    # Metadata
    metadata = {'name': filename}
    if folder_id:
        metadata['parents'] = [folder_id]
    
    body = []
    body.append(f'--{boundary}'.encode())
    body.append(b'Content-Type: application/json; charset=UTF-8')
    body.append(b'')
    body.append(json.dumps(metadata).encode())
    body.append(f'--{boundary}'.encode())
    body.append(f'Content-Type: {mime_type}'.encode())
    body.append(b'')
    body.append(file_content)
    body.append(f'--{boundary}--'.encode())
    
    full_body = b'\r\n'.join(body)
    
    # Upload request
    req = urllib.request.Request(
        'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart',
        data=full_body,
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': f'multipart/related; boundary={boundary}'
        }
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read().decode())
            file_id = result.get('id')
            
            # Make file publicly readable if requested
            if make_public and file_id:
                permission_req = urllib.request.Request(
                    f'https://www.googleapis.com/drive/v3/files/{file_id}/permissions',
                    data=json.dumps({
                        'role': 'reader',
                        'type': 'anyone'
                    }).encode(),
                    headers={
                        'Authorization': f'Bearer {access_token}',
                        'Content-Type': 'application/json'
                    }
                )
                
                with urllib.request.urlopen(permission_req) as perm_resp:
                    perm_resp.read()
            
            return {
                'success': True,
                'id': file_id,
                'name': result.get('name'),
                'webViewLink': f'https://drive.google.com/file/d/{file_id}/view',
                'webContentLink': f'https://drive.google.com/uc?id={file_id}&export=download'
            }
            
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        return {
            'success': False,
            'error': f'HTTP {e.code}',
            'details': error_body
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def list_files(query=None, page_size=10):
    """List files in Google Drive"""
    access_token = get_access_token()
    
    url = f'https://www.googleapis.com/drive/v3/files?pageSize={page_size}'
    if query:
        url += f'&q={urllib.parse.quote(query)}'
    
    req = urllib.request.Request(
        url,
        headers={'Authorization': f'Bearer {access_token}'}
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {'error': str(e)}

# CLI interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 drive_api.py upload /path/to/file")
        print("  python3 drive_api.py list")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == 'upload':
        if len(sys.argv) < 3:
            print("Usage: python3 drive_api.py upload /path/to/file")
            sys.exit(1)
        
        result = upload_file(sys.argv[2])
        
        if result['success']:
            print(f"✅ Upload successful!")
            print(f"📁 File ID: {result['id']}")
            print(f"🔗 View: {result['webViewLink']}")
            print(f"⬇️  Download: {result['webContentLink']}")
        else:
            print(f"❌ Upload failed: {result['error']}")
            if 'details' in result:
                print(f"Details: {result['details']}")
    
    elif cmd == 'list':
        files = list_files()
        if 'files' in files:
            print(f"Found {len(files['files'])} files:")
            for f in files['files']:
                print(f"  - {f['name']} ({f['mimeType']})")
        else:
            print(f"Error: {files.get('error', 'Unknown error')}")
    
    else:
        print(f"Unknown command: {cmd}")
