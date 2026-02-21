#!/usr/bin/env python3
"""
Google Drive OAuth Setup
Creates a separate token for Drive operations (doesn't interfere with Gmail)
"""

import os
import json
import urllib.request
import urllib.parse
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Configuration
CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', '')
REDIRECT_URI = "http://localhost:8080/callback"
TOKEN_FILE = "/home/daz/.config/himalaya/drive-token.json"

# Google Drive scopes we need
SCOPES = [
    "https://www.googleapis.com/auth/drive.file",  # Create/upload files only
    "https://www.googleapis.com/auth/drive.metadata.readonly"  # Read metadata
]

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if '/callback' in self.path:
            # Extract authorization code
            code = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query).get('code', [None])[0]
            
            if code:
                # Exchange code for tokens
                success = exchange_code_for_tokens(code)
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                
                if success:
                    self.wfile.write(b"""
                        <h1>Google Drive Connected!</h1>
                        <p>You can close this window and return to the terminal.</p>
                        <script>window.close();</script>
                    """)
                else:
                    self.wfile.write(b"""
                        <h1>Connection Failed</h1>
                        <p>Check the terminal for error details.</p>
                    """)
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"<h1>Error: No authorization code received</h1>")
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass  # Suppress log output

def exchange_code_for_tokens(code):
    """Exchange authorization code for access/refresh tokens"""
    data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }
    
    req = urllib.request.Request(
        'https://oauth2.googleapis.com/token',
        data=urllib.parse.urlencode(data).encode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            tokens = json.loads(resp.read().decode())
            
            # Save tokens with scopes
            token_data = {
                'access_token': tokens['access_token'],
                'refresh_token': tokens.get('refresh_token'),
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
                'token_uri': 'https://oauth2.googleapis.com/token',
                'scopes': SCOPES,
                'obtained_at': str(datetime.now())
            }
            
            os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
            with open(TOKEN_FILE, 'w') as f:
                json.dump(token_data, f, indent=2)
            
            print(f"Google Drive token saved to {TOKEN_FILE}")
            return True
    except Exception as e:
        print(f"Error exchanging code: {e}")
        return False

def start_oauth_flow():
    """Start the OAuth flow"""
    from datetime import datetime
    
    # Validate configuration
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Error: GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET environment variables must be set")
        print("\nSet them with:")
        print("  export GOOGLE_CLIENT_ID='your-client-id'")
        print("  export GOOGLE_CLIENT_SECRET='your-client-secret'")
        return False
    
    # Build authorization URL
    auth_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    params = {
        'client_id': CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'scope': ' '.join(SCOPES),
        'access_type': 'offline',
        'prompt': 'consent'
    }
    
    full_url = f"{auth_url}?{urllib.parse.urlencode(params)}"
    
    print("=" * 60)
    print("Google Drive OAuth Setup")
    print("=" * 60)
    print("\n1. Opening browser for authorization...")
    print("2. Log in with your Google account")
    print("3. Approve Drive permissions when prompted")
    print("\nWaiting for authorization...")
    
    # Start local server to receive callback
    server = HTTPServer(('localhost', 8080), OAuthHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Open browser
    webbrowser.open(full_url)
    
    # Wait for callback (with timeout)
    import time
    timeout = 120  # 2 minutes
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'r') as f:
                data = json.load(f)
                if data.get('scopes') == SCOPES:
                    server.shutdown()
                    print("\n✅ Setup complete! Google Drive token created.")
                    print(f"📁 Token saved to: {TOKEN_FILE}")
                    return True
        time.sleep(1)
    
    server.shutdown()
    print("\n❌ Timeout waiting for authorization")
    return False

if __name__ == "__main__":
    # Check if token already exists
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            existing = json.load(f)
        if existing.get('scopes') and 'drive' in str(existing.get('scopes')):
            print("✅ Google Drive token already exists with correct scopes!")
            print(f"📁 Location: {TOKEN_FILE}")
            print("\nScopes granted:")
            for scope in existing['scopes']:
                print(f"  - {scope}")
            exit(0)
    
    success = start_oauth_flow()
    exit(0 if success else 1)
