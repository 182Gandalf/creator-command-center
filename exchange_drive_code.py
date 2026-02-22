#!/usr/bin/env python3
"""
Exchange Google OAuth code for tokens
"""

import os
import json
import urllib.request
import urllib.parse

# Configuration - you'll need to provide these
CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', '')
TOKEN_FILE = "/home/daz/.config/himalaya/drive-token.json"

# The auth code you received from Google
def exchange_code(auth_code):
    """Exchange authorization code for access/refresh tokens"""
    
    if not CLIENT_ID or not CLIENT_SECRET:
        print("Error: GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET must be set")
        print("\nSet them with:")
        print("  export GOOGLE_CLIENT_ID='your-client-id'")
        print("  export GOOGLE_CLIENT_SECRET='your-client-secret'")
        return False
    
    token_url = 'https://oauth2.googleapis.com/token'
    redirect_uri = 'http://localhost:8080/callback'
    
    data = {
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    try:
        req = urllib.request.Request(
            token_url,
            data=urllib.parse.urlencode(data).encode(),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        
        with urllib.request.urlopen(req) as resp:
            tokens = json.loads(resp.read().decode())
            
            if 'access_token' in tokens:
                # Save tokens
                token_data = {
                    'access_token': tokens['access_token'],
                    'refresh_token': tokens.get('refresh_token'),
                    'client_id': CLIENT_ID,
                    'client_secret': CLIENT_SECRET,
                    'token_uri': 'https://oauth2.googleapis.com/token',
                    'scopes': [
                        "https://www.googleapis.com/auth/drive.file",
                        "https://www.googleapis.com/auth/drive.metadata.readonly"
                    ]
                }
                
                os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
                with open(TOKEN_FILE, 'w') as f:
                    json.dump(token_data, f, indent=2)
                
                print(f"✅ Google Drive token saved to {TOKEN_FILE}")
                print(f"   Access token: {tokens['access_token'][:20]}...")
                if tokens.get('refresh_token'):
                    print(f"   Refresh token: {tokens['refresh_token'][:20]}...")
                return True
            else:
                print(f"❌ Error: {tokens}")
                return False
                
    except Exception as e:
        print(f"❌ Error exchanging code: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 exchange_drive_code.py 'YOUR_AUTH_CODE'")
        print("\nExample:")
        print("  python3 exchange_drive_code.py '4/1AfrIepB1v-0cWP7P1DtDAmfvvDwo2NHAd__LY6Nqkhyu3f1icdzg1_4Eig8'")
        sys.exit(1)
    
    auth_code = sys.argv[1]
    success = exchange_code(auth_code)
    sys.exit(0 if success else 1)
