# Gmail API with Attachment Support
import json
import urllib.request
import urllib.parse
import base64
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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

def send_email_with_attachment(to, subject, body, file_path, access_token=None):
    if not access_token:
        access_token = get_access_token()
    
    msg = MIMEMultipart()
    msg['to'] = to
    msg['from'] = 'gandalftheclaw@gmail.com'
    msg['subject'] = subject
    
    # Attach body
    msg.attach(MIMEText(body))
    
    # Attach file
    filename = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(f.read())
    
    encoders.encode_base64(attachment)
    attachment.add_header(
        'Content-Disposition',
        f'attachment; filename= {filename}'
    )
    msg.attach(attachment)
    
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

def upload_to_drive(file_path, access_token=None):
    if not access_token:
        access_token = get_access_token()
    
    filename = os.path.basename(file_path)
    
    # First, get the file metadata and upload URL
    metadata = {
        'name': filename,
        'mimeType': 'application/gzip'
    }
    
    # Read file content
    with open(file_path, 'rb') as f:
        file_content = f.read()
    
    # Create multipart body manually
    boundary = '---BOUNDARY---'
    
    body = []
    body.append(f'--{boundary}'.encode())
    body.append(b'Content-Type: application/json; charset=UTF-8')
    body.append(b'')
    body.append(json.dumps(metadata).encode())
    body.append(f'--{boundary}'.encode())
    body.append(b'Content-Type: application/gzip')
    body.append(b'')
    body.append(file_content)
    body.append(f'--{boundary}--'.encode())
    
    full_body = b'\r\n'.join(body)
    
    req = urllib.request.Request(
        'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart',
        data=full_body,
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': f'multipart/related; boundary={boundary}'
        }
    )
    
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode())
        file_id = result.get('id')
        
        # Make it publicly readable
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
        
        return f"https://drive.google.com/file/d/{file_id}/view"

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 gmail_with_attach.py email 'to@example.com' 'Subject' 'Body' '/path/to/file'")
        print("  python3 gmail_with_attach.py drive '/path/to/file'")
        sys.exit(1)
    
    cmd = sys.argv[1]
    
    if cmd == 'email':
        if len(sys.argv) < 6:
            print("Usage: python3 gmail_with_attach.py email 'to' 'subject' 'body' '/path/to/file'")
            sys.exit(1)
        result = send_email_with_attachment(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        print(f"Email sent! ID: {result['id']}")
    elif cmd == 'drive':
        if len(sys.argv) < 3:
            print("Usage: python3 gmail_with_attach.py drive '/path/to/file'")
            sys.exit(1)
        link = upload_to_drive(sys.argv[2])
        print(f"File uploaded! Link: {link}")
    else:
        print(f"Unknown command: {cmd}")
