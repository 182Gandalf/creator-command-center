#!/usr/bin/env python3
"""
Gmail OAuth2 Setup Script for Himalaya
This script will guide you through authenticating Gmail with OAuth2
"""

import json
import urllib.parse
import urllib.request
import os
import sys

# Configuration
CLIENT_SECRETS_FILE = "/home/daz/gmail-oauth-credentials.json"
TOKEN_FILE = "/home/daz/.config/himalaya/gmail-token.json"
HIMALAYA_CONFIG = "/home/daz/.config/himalaya/config.toml"

# Gmail OAuth scopes
SCOPES = [
    "https://mail.google.com/",  # Full Gmail access
]

def print_step(step_num, text):
    print(f"\n{'='*60}")
    print(f"STEP {step_num}: {text}")
    print('='*60)

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║     Gmail OAuth2 Setup for Creator Command Center          ║
╚══════════════════════════════════════════════════════════════╝

This script will help you authenticate Gmail using OAuth2.
It's more reliable than App Passwords and is the modern standard.
""")
    
    # Step 1: Check for credentials file
    print_step(1, "Check for Google OAuth Credentials")
    
    if not os.path.exists(CLIENT_SECRETS_FILE):
        print(f"❌ Credentials file not found: {CLIENT_SECRETS_FILE}")
        print("""
You need to download your OAuth credentials from Google Cloud Console:

1. Go to: https://console.cloud.google.com/apis/credentials
2. Find your OAuth 2.0 Client ID (Desktop application)
3. Click the download icon (⬇️) to get the JSON file
4. Save it as: gmail-oauth-credentials.json in your home directory
   OR upload it to: /home/daz/gmail-oauth-credentials.json

The file should look like: client_secret_xxxx.apps.googleusercontent.com.json
""")
        return
    
    print(f"✅ Found credentials file: {CLIENT_SECRETS_FILE}")
    
    # Load credentials
    with open(CLIENT_SECRETS_FILE, 'r') as f:
        credentials = json.load(f)
    
    if 'installed' in credentials:
        client_id = credentials['installed']['client_id']
        client_secret = credentials['installed']['client_secret']
        auth_uri = credentials['installed']['auth_uri']
        token_uri = credentials['installed']['token_uri']
    else:
        print("❌ Invalid credentials file format")
        return
    
    print(f"✅ Client ID: {client_id[:20]}...")
    
    # Step 2: Generate authorization URL
    print_step(2, "Generate Authorization URL")
    
    redirect_uri = "urn:ietf:wg:oauth:2.0:oob"  # For desktop apps (manual copy-paste)
    
    auth_params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'scope': ' '.join(SCOPES),
        'response_type': 'code',
        'access_type': 'offline',  # Important: gets refresh token
        'prompt': 'consent'  # Forces consent screen to get refresh token
    }
    
    auth_url = f"{auth_uri}?{urllib.parse.urlencode(auth_params)}"
    
    print("""
🔗 Authorization URL Generated!

Please open this URL in your browser:
""")
    print(f"{auth_url}")
    print("""

📋 Instructions:
1. Copy the URL above
2. Open it in your browser (Chrome, Firefox, etc.)
3. Sign in with: gandaftheclaw@gmail.com
4. Click "Allow" to grant Gmail access
5. You will see an authorization code (starts with "4/xxxxx")
6. Copy that code and paste it below
""")
    
    # Step 3: Get authorization code from user
    print_step(3, "Enter Authorization Code")
    
    auth_code = input("\nPaste the authorization code here: ").strip()
    
    if not auth_code:
        print("❌ No code entered. Exiting.")
        return
    
    print(f"✅ Code received: {auth_code[:10]}...")
    
    # Step 4: Exchange code for tokens
    print_step(4, "Exchange Code for Tokens")
    
    token_data = {
        'code': auth_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    try:
        req = urllib.request.Request(
            token_uri,
            data=urllib.parse.urlencode(token_data).encode(),
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        
        with urllib.request.urlopen(req) as response:
            token_response = json.loads(response.read().decode())
        
        if 'error' in token_response:
            print(f"❌ Error: {token_response['error']}")
            print(f"Description: {token_response.get('error_description', 'Unknown error')}")
            return
        
        access_token = token_response.get('access_token')
        refresh_token = token_response.get('refresh_token')
        expires_in = token_response.get('expires_in')
        
        print("✅ Successfully obtained tokens!")
        print(f"   Access Token: {access_token[:20]}...")
        print(f"   Refresh Token: {refresh_token[:20]}...")
        print(f"   Expires in: {expires_in} seconds")
        
    except Exception as e:
        print(f"❌ Error exchanging code: {e}")
        return
    
    # Step 5: Save tokens
    print_step(5, "Save Tokens")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
    
    # Save token info
    token_info = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'token_uri': token_uri,
        'scopes': SCOPES,
        'obtained_at': str(__import__('datetime').datetime.now())
    }
    
    with open(TOKEN_FILE, 'w') as f:
        json.dump(token_info, f, indent=2)
    
    print(f"✅ Tokens saved to: {TOKEN_FILE}")
    
    # Step 6: Update Himalaya config
    print_step(6, "Update Himalaya Configuration")
    
    # Create OAuth2 config for himalaya
    oauth2_config = f"""
# Gmail OAuth2 Configuration for Himalaya
# Generated automatically by setup script

[accounts.gmail]
email = "gandaftheclaw@gmail.com"
display-name = "Gandalf the Claw"
default = true

backend.type = "imap"
backend.host = "imap.gmail.com"
backend.port = 993
backend.encryption.type = "tls"
backend.login = "gandaftheclaw@gmail.com"
backend.auth.type = "oauth2"
backend.auth.method = "xoauth2"
backend.auth.client-id = "{client_id}"
backend.auth.client-secret = "{client_secret}"
backend.auth.access-token = "{access_token}"
backend.auth.refresh-token = "{refresh_token}"

message.send.backend.type = "smtp"
message.send.backend.host = "smtp.gmail.com"
message.send.backend.port = 587
message.send.backend.encryption.type = "start-tls"
message.send.backend.login = "gandaftheclaw@gmail.com"
message.send.backend.auth.type = "oauth2"
message.send.backend.auth.method = "xoauth2"
message.send.backend.auth.client-id = "{client_id}"
message.send.backend.auth.client-secret = "{client_secret}"
message.send.backend.auth.access-token = "{access_token}"
message.send.backend.auth.refresh-token = "{refresh_token}"
"""
    
    # Backup old config
    if os.path.exists(HIMALAYA_CONFIG):
        backup_file = HIMALAYA_CONFIG + ".backup"
        os.rename(HIMALAYA_CONFIG, backup_file)
        print(f"✅ Backed up old config to: {backup_file}")
    
    # Write new config
    with open(HIMALAYA_CONFIG, 'w') as f:
        f.write(oauth2_config)
    
    print(f"✅ Himalaya config updated: {HIMALAYA_CONFIG}")
    
    # Step 7: Test connection
    print_step(7, "Test Connection")
    print("""
Testing Gmail connection with OAuth2...

Run this command to test:
    export PATH="$HOME/.local/bin:$PATH"
    himalaya folder list

If you see a list of folders (INBOX, Sent, etc.), it's working!

If you see an error, the OAuth2 token may need to be refreshed.
The refresh happens automatically.
""")
    
    # Summary
    print_step("COMPLETE", "Setup Summary")
    print(f"""
✅ Gmail OAuth2 setup complete!

Files created:
  • Token file: {TOKEN_FILE}
  • Config file: {HIMALAYA_CONFIG}
  • Backup: {HIMALAYA_CONFIG}.backup (if existed)

Next steps:
  1. Test with: himalaya folder list
  2. Send test email: himalaya message send --to your-email@test.com
  3. The token will auto-refresh when needed

Important:
  • Keep {TOKEN_FILE} secure (contains sensitive tokens)
  • Do not commit to git
  • Tokens expire but refresh automatically

🎉 You're ready to use Gmail with Himalaya!
""")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)
