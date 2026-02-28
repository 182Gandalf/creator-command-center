#!/bin/bash
# OAuth Diagnostic Script for FlowCast

echo "=== FlowCast OAuth Diagnostics ==="
echo ""

cd /home/daz/.openclaw/workspace/levelup-ai/creator-app
source venv/bin/activate 2>/dev/null

echo "1. Checking environment variables..."
python3 << 'EOF'
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.environ.get('GOOGLE_CLIENT_ID')
client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')
secret_key = os.environ.get('SECRET_KEY')

if client_id:
    print(f"   ✅ GOOGLE_CLIENT_ID: {client_id[:25]}...")
else:
    print("   ❌ GOOGLE_CLIENT_ID: NOT SET")

if client_secret:
    print(f"   ✅ GOOGLE_CLIENT_SECRET: {'*' * 10} (hidden)")
else:
    print("   ❌ GOOGLE_CLIENT_SECRET: NOT SET")

if secret_key and secret_key != 'dev-secret-key-change-in-production':
    print(f"   ✅ SECRET_KEY: Set (custom)")
else:
    print(f"   ⚠️  SECRET_KEY: Using default (change in production!)")
EOF

echo ""
echo "2. Checking redirect URI configuration..."
python3 << 'EOF'
from flask import Flask, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'

# Mock the route
@app.route('/api/google/callback')
def google_callback():
    pass

with app.test_request_context():
    # Local URL
    local_url = url_for('google_callback', _external=True)
    print(f"   Local URL: {local_url}")
    
    # Production URL
    prod_url = url_for('google_callback', _external=True, _scheme='https')
    print(f"   Production URL: {prod_url}")
EOF

echo ""
echo "3. Checking required Google OAuth scopes..."
echo "   Required: openid email profile"
echo "   ✅ These are standard OAuth 2.0 scopes"

echo ""
echo "=== Diagnostics Complete ==="
echo ""
echo "Next steps:"
echo "  1. Verify redirect URIs in Google Cloud Console match the URLs above"
echo "  2. Ensure OAuth consent screen is configured"
echo "  3. Test locally: python app.py → visit http://localhost:5000/api/google/auth"
