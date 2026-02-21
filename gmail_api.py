# Simple Gmail API Client (No Himalaya needed)
import json
import urllib.request
import urllib.parse
import base64
from email.mime.text import MIMEText
import os

TOKEN_FILE = "/home/daz/.config/himalaya/gmail-token.json"

def get_access_token():
    with open(TOKEN_FILE, 'r') as f:
        tokens = json.load(f)
    
    data = {
        'refresh_token': tokens['refresh_token'],
        'client_id': tokens['client_id'],
        'client_secret': tokens['client_secret'],
        'grant_type': 'refresh_token'
    }
    
    req = urllib.request.Request(
        'https://oauth2.googleapis.com/token',
        data=urllib.parse.urlencode(data).encode(),
        headers={'Content-Type': 'application/x-www-form-urlencoded'}
    )
    
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())['access_token']

def send_email(to, subject, body, access_token=None):
    if not access_token:
        access_token = get_access_token()
    
    msg = MIMEText(body)
    msg['to'] = to
    msg['from'] = 'gandaftheclaw@gmail.com'
    msg['subject'] = subject
    
    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    
    req = urllib.request.Request(
        'https://www.googleapis.com/gmail/v1/users/me/messages/send',
        data=json.dumps({'raw': raw}).encode(),
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
    )
    
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def list_emails(max_results=10, access_token=None):
    if not access_token:
        access_token = get_access_token()
    
    req = urllib.request.Request(
        f'https://www.googleapis.com/gmail/v1/users/me/messages?maxResults={max_results}',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

# CLI interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 gmail_api.py list")
        print("  python3 gmail_api.py send 'to@example.com' 'Subject' 'Body'")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == 'list':
        emails = list_emails()
        print(f"Found {len(emails.get('messages', []))} emails")
    elif cmd == 'send':
        if len(sys.argv) < 5:
            print("Usage: python3 gmail_api.py send 'to' 'subject' 'body'")
            sys.exit(1)
        result = send_email(sys.argv[2], sys.argv[3], sys.argv[4])
        print(f"Email sent! ID: {result['id']}")
