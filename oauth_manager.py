"""
Secure OAuth Token Management for FlowCast
Handles encryption, storage, and retrieval of social media OAuth tokens
"""

import os
import json
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from datetime import datetime

class TokenManager:
    """Manages encrypted OAuth tokens with audit logging"""
    
    def __init__(self, encryption_key=None):
        """
        Initialize token manager with encryption key
        
        Args:
            encryption_key: Fernet key or string to derive key from
        """
        if encryption_key is None:
            encryption_key = os.environ.get('TOKEN_ENCRYPTION_KEY')
        
        if isinstance(encryption_key, str):
            # Derive key from string using PBKDF2
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=b'flowcast_salt_v1',  # In production, use unique salt per installation
                iterations=480000,
            )
            key = base64.urlsafe_b64encode(kdf.derive(encryption_key.encode()))
            self.cipher = Fernet(key)
        else:
            self.cipher = Fernet(encryption_key)
    
    def encrypt_token(self, token_data):
        """
        Encrypt OAuth token data
        
        Args:
            token_data: Dict with 'access_token', 'refresh_token', 'expires_at', etc.
        
        Returns:
            Encrypted string
        """
        json_data = json.dumps(token_data)
        encrypted = self.cipher.encrypt(json_data.encode())
        return base64.urlsafe_b64encode(encrypted).decode()
    
    def decrypt_token(self, encrypted_data):
        """
        Decrypt OAuth token data
        
        Args:
            encrypted_data: Encrypted string from encrypt_token
        
        Returns:
            Dict with token data
        """
        encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
        decrypted = self.cipher.decrypt(encrypted_bytes)
        return json.loads(decrypted.decode())
    
    def generate_consent_record(self, user_id, platform, scopes, ip_address=None):
        """
        Generate a consent record for audit purposes
        
        Args:
            user_id: User's ID
            platform: Platform name (youtube, instagram, etc.)
            scopes: List of OAuth scopes granted
            ip_address: Optional IP for audit log
        
        Returns:
            Consent record dict
        """
        return {
            'user_id': user_id,
            'platform': platform,
            'scopes': scopes,
            'granted_at': datetime.utcnow().isoformat(),
            'ip_address': ip_address,
            'user_agent': 'FlowCast Web App',
            'purpose': 'Social media scheduling and publishing'
        }

# Global token manager instance
token_manager = None

def get_token_manager():
    """Get or create global token manager instance"""
    global token_manager
    if token_manager is None:
        token_manager = TokenManager()
    return token_manager

# YouTube OAuth Configuration
YOUTUBE_OAUTH_CONFIG = {
    'auth_uri': 'https://accounts.google.com/o/oauth2/v2/auth',
    'token_uri': 'https://oauth2.googleapis.com/token',
    'revoke_uri': 'https://oauth2.googleapis.com/revoke',
    'scopes': [
        'https://www.googleapis.com/auth/youtube.upload',
        'https://www.googleapis.com/auth/youtube.readonly'
    ]
}

# Instagram OAuth Configuration
INSTAGRAM_OAUTH_CONFIG = {
    'auth_uri': 'https://www.facebook.com/v18.0/dialog/oauth',
    'token_uri': 'https://graph.facebook.com/v18.0/oauth/access_token',
    'scopes': [
        'instagram_basic',
        'instagram_content_publish',
        'pages_read_engagement'
    ]
}

def get_youtube_auth_url(client_id, redirect_uri, state):
    """
    Generate YouTube OAuth authorization URL
    
    Args:
        client_id: Google OAuth client ID
        redirect_uri: Callback URL
        state: CSRF protection state string
    
    Returns:
        Authorization URL string
    """
    scopes = ' '.join(YOUTUBE_OAUTH_CONFIG['scopes'])
    auth_url = (
        f"{YOUTUBE_OAUTH_CONFIG['auth_uri']}?"
        f"client_id={client_id}&"
        f"redirect_uri={redirect_uri}&"
        f"scope={scopes}&"
        f"response_type=code&"
        f"access_type=offline&"
        f"prompt=consent&"
        f"state={state}"
    )
    return auth_url

def exchange_youtube_code(code, client_id, client_secret, redirect_uri):
    """
    Exchange authorization code for tokens
    
    Args:
        code: Authorization code from callback
        client_id: Google OAuth client ID
        client_secret: Google OAuth client secret
        redirect_uri: Must match the one used in auth URL
    
    Returns:
        Dict with tokens or error
    """
    import requests
    
    data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    try:
        response = requests.post(
            YOUTUBE_OAUTH_CONFIG['token_uri'],
            data=data,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        
        return {
            'success': True,
            'access_token': result.get('access_token'),
            'refresh_token': result.get('refresh_token'),
            'expires_in': result.get('expires_in'),
            'scope': result.get('scope')
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def refresh_youtube_token(refresh_token, client_id, client_secret):
    """
    Refresh expired access token
    
    Args:
        refresh_token: Stored refresh token
        client_id: Google OAuth client ID
        client_secret: Google OAuth client secret
    
    Returns:
        Dict with new tokens or error
    """
    import requests
    
    data = {
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token'
    }
    
    try:
        response = requests.post(
            YOUTUBE_OAUTH_CONFIG['token_uri'],
            data=data,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        
        return {
            'success': True,
            'access_token': result.get('access_token'),
            'expires_in': result.get('expires_in'),
            'scope': result.get('scope')
            # Note: Refresh token may not be returned again
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def revoke_youtube_token(token):
    """
    Revoke OAuth token
    
    Args:
        token: Access or refresh token to revoke
    
    Returns:
        Success boolean
    """
    import requests
    
    try:
        response = requests.post(
            YOUTUBE_OAUTH_CONFIG['revoke_uri'],
            params={'token': token},
            timeout=30
        )
        return response.status_code == 200
    except:
        return False

# Audit logging for compliance
def log_token_action(user_id, platform, action, details=None):
    """
    Log token-related actions for audit trail
    
    Args:
        user_id: User ID
        platform: Platform name
        action: Action type (granted, revoked, refreshed, used)
        details: Optional additional details
    """
    audit_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'user_id': user_id,
        'platform': platform,
        'action': action,
        'details': details or {}
    }
    
    # In production, write to secure audit log
    # For now, log to stdout (replace with proper logging)
    print(f"[AUDIT] {json.dumps(audit_entry)}")
    
    # TODO: Store in database audit_log table
    # db.session.add(AuditLog(**audit_entry))
    # db.session.commit()

# Helper function to check if token needs refresh
def token_needs_refresh(expires_at, buffer_minutes=5):
    """
    Check if access token is expired or about to expire
    
    Args:
        expires_at: ISO timestamp when token expires
        buffer_minutes: Refresh if within this many minutes of expiry
    
    Returns:
        Boolean indicating if refresh needed
    """
    from datetime import datetime, timedelta
    
    expiry = datetime.fromisoformat(expires_at)
    refresh_threshold = expiry - timedelta(minutes=buffer_minutes)
    
    return datetime.utcnow() >= refresh_threshold
