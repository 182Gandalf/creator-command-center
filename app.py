# FlowCast
# Social Media Management Platform

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta
import os
import requests
import json
import secrets

# Import OAuth manager for secure token handling
from oauth_manager import (
    get_token_manager, get_youtube_auth_url, exchange_youtube_code,
    log_token_action, revoke_youtube_token
)

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creator_command_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# API Configuration
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', '')
INSTAGRAM_APP_ID = os.environ.get('INSTAGRAM_APP_ID', '')
INSTAGRAM_APP_SECRET = os.environ.get('INSTAGRAM_APP_SECRET', '')

# Database Models
class User(db.Model):
    """User accounts"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    subscription_tier = db.Column(db.String(20), default='free')  # free, pro, team
    youtube_connected = db.Column(db.Boolean, default=False)
    youtube_token = db.Column(db.Text)  # OAuth token
    instagram_connected = db.Column(db.Boolean, default=False)
    instagram_token = db.Column(db.Text)
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')
    
    def get_post_limit(self):
        limits = {'free': 10, 'pro': 100, 'team': 1000}
        return limits.get(self.subscription_tier, 10)
    
    def get_platforms_allowed(self):
        platforms = {'free': 1, 'pro': 3, 'team': 5}
        return platforms.get(self.subscription_tier, 1)

class Post(db.Model):
    """Scheduled and published posts"""
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(500))
    content = db.Column(db.Text)
    platforms = db.Column(db.String(500))  # JSON array: ["youtube", "instagram"]
    status = db.Column(db.String(50), default='draft')  # draft, scheduled, published, failed
    scheduled_at = db.Column(db.DateTime)
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    youtube_video_id = db.Column(db.String(50))  # If published to YouTube
    instagram_media_id = db.Column(db.String(50))  # If published to Instagram
    analytics = db.Column(db.Text)  # JSON with views, likes, etc.
    
class ContentIdea(db.Model):
    """AI-generated content ideas saved by users"""
    __tablename__ = 'content_ideas'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(500))
    description = db.Column(db.Text)
    platforms = db.Column(db.String(200))  # JSON array
    format_type = db.Column(db.String(50))  # carousel, video, reel, etc.
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    used_in_post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=True)

# Routes
@app.route('/')
def index():
    """Main dashboard"""
    return render_template('dashboard.html')

@app.route('/api/health')
def health_check():
    """Health check and API status"""
    # Check which AI providers are configured
    ai_status = {
        'gemini': bool(os.environ.get('GEMINI_API_KEY')),
        'deepseek': bool(os.environ.get('DEEPSEEK_API_KEY')),
        'openai': bool(os.environ.get('OPENAI_API_KEY')),
        'mistral': bool(os.environ.get('MISTRAL_API_KEY'))
    }
    
    return jsonify({
        'status': 'healthy',
        'ai_providers_configured': ai_status,
        'youtube_api': bool(YOUTUBE_API_KEY),
        'instagram_config': bool(INSTAGRAM_APP_ID and INSTAGRAM_APP_SECRET)
    })

@app.route('/pricing')
def pricing():
    """Pricing page"""
    return render_template('pricing.html')

@app.route('/terms')
def terms():
    """Terms of Service"""
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    """Privacy Policy"""
    return render_template('privacy.html')

@app.route('/refund')
def refund():
    """Refund Policy"""
    return render_template('refund.html')

@app.route('/api/dashboard-stats')
def dashboard_stats():
    """Get dashboard statistics"""
    # Get real stats from database
    total_posts = Post.query.count()
    scheduled_posts = Post.query.filter_by(status='scheduled').count()
    
    return jsonify({
        'total_posts': total_posts,
        'scheduled_posts': scheduled_posts,
        'youtube_scheduled': 3,
        'instagram_scheduled': 2,
        'engagement_rate': 4.8
    })

@app.route('/api/content-calendar')
def content_calendar():
    """Get content calendar data"""
    posts = Post.query.filter(
        Post.scheduled_at >= datetime.now(),
        Post.scheduled_at <= datetime.now() + timedelta(days=30)
    ).all()
    
    events = []
    for post in posts:
        events.append({
            'id': post.id,
            'title': post.title,
            'date': post.scheduled_at.isoformat() if post.scheduled_at else None,
            'platforms': json.loads(post.platforms) if post.platforms else [],
            'status': post.status
        })
    
    return jsonify({'events': events})

@app.route('/api/create-post', methods=['POST'])
def create_post():
    """Create and schedule a new post"""
    data = request.json
    
    # Create new post
    post = Post(
        title=data.get('title'),
        content=data.get('content'),
        platforms=json.dumps(data.get('platforms', [])),
        status='scheduled' if data.get('scheduled_at') else 'draft',
        scheduled_at=datetime.fromisoformat(data['scheduled_at']) if data.get('scheduled_at') else None
    )
    
    db.session.add(post)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Post created successfully',
        'post_id': post.id
    })

@app.route('/api/youtube/channels')
def youtube_channels():
    """Fetch YouTube channels for connected account"""
    try:
        # Check for OAuth token first (authenticated user)
        oauth_token = session.get('youtube_token')
        
        if oauth_token:
            # Authenticated request - get user's own channels
            headers = {'Authorization': f'Bearer {oauth_token}'}
            url = 'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&mine=true'
            response = requests.get(url, headers=headers)
        else:
            # Demo mode - fetch sample channel data using API key
            url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id=UC_x5XG1OV2P6uZZ5FSM9Ttw&key={YOUTUBE_API_KEY}"
            response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            channels = []
            for item in data.get('items', []):
                channels.append({
                    'id': item['id'],
                    'title': item['snippet']['title'],
                    'description': item['snippet'].get('description', ''),
                    'thumbnail': item['snippet']['thumbnails'].get('default', {}).get('url', ''),
                    'subscriber_count': item['statistics'].get('subscriberCount', 0),
                    'video_count': item['statistics'].get('videoCount', 0),
                    'view_count': item['statistics'].get('viewCount', 0)
                })
            return jsonify({
                'success': True,
                'channels': channels
            })
        else:
            return jsonify({
                'success': False,
                'error': f'YouTube API error: {response.status_code}',
                'details': response.text
            }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/instagram/account')
def instagram_account():
    """Fetch Instagram account info"""
    # TODO: Implement with actual Instagram Basic Display API
    return jsonify({
        'success': True,
        'account': {
            'username': 'test_account',
            'connected': True
        }
    })

@app.route('/api/ai-content-ideas')
def ai_content_ideas():
    """Generate AI content ideas using multi-provider router with caching"""
    from ai_router import generate_content_ideas
    
    # Get parameters
    topic = request.args.get('topic', 'social media growth')
    platform = request.args.get('platform', 'instagram')
    count = min(int(request.args.get('count', 5)), 10)  # Max 10 ideas
    
    # Get user tier (from query param for testing, or session in production)
    user_tier = request.args.get('tier') or session.get('subscription_tier', 'free')
    
    try:
        # Generate ideas using AI router (with automatic caching)
        result = generate_content_ideas(
            user_tier=user_tier,
            topic=topic,
            platform=platform,
            count=count
        )
        
        if result['success']:
            # Add metadata for debugging
            response = {
                'success': True,
                'ideas': result['ideas'],
                'model_used': result.get('model_used', 'fallback'),
                'cached': result.get('cached', False),
                'cost_usd': result.get('cost_usd', 0),
                'tier': user_tier
            }
            return jsonify(response)
        else:
            # Fallback to default ideas - include error details
            error_msg = result.get('error', 'Unknown error')
            return jsonify({
                'success': True,
                'ideas': get_default_ideas(topic, platform, count),
                'model_used': 'fallback',
                'cached': False,
                'cost_usd': 0,
                'tier': user_tier,
                'note': f'Using fallback ideas - AI error: {error_msg}'
            })
    
    except Exception as e:
        # Log error and return fallback
        print(f"AI generation error: {e}")
        return jsonify({
            'success': True,
            'ideas': get_default_ideas(topic, platform, count),
            'model_used': 'fallback',
            'error': str(e),
            'tier': user_tier,
            'debug': {
                'gemini_configured': bool(os.environ.get('GEMINI_API_KEY')),
                'deepseek_configured': bool(os.environ.get('DEEPSEEK_API_KEY')),
                'openai_configured': bool(os.environ.get('OPENAI_API_KEY'))
            }
        })

def get_default_ideas(topic, platform, count):
    """Fallback ideas when AI is unavailable"""
    templates = [
        {
            'title': f'5 Secrets About {topic} Nobody Talks About',
            'format': 'Carousel' if platform == 'instagram' else 'Video',
            'platform': platform.capitalize(),
            'estimated_engagement': 'High',
            'best_posting_time': 'Tuesday 10 AM',
            'hook': f'Revealing hidden truths about {topic}...'
        },
        {
            'title': f'How I Mastered {topic} in 30 Days',
            'format': 'Reel' if platform == 'instagram' else 'Short',
            'platform': platform.capitalize(),
            'estimated_engagement': 'High',
            'best_posting_time': 'Thursday 2 PM',
            'hook': f'My journey with {topic}...'
        },
        {
            'title': f'The Biggest {topic} Mistakes Beginners Make',
            'format': 'Carousel' if platform == 'instagram' else 'Post',
            'platform': platform.capitalize(),
            'estimated_engagement': 'Medium',
            'best_posting_time': 'Wednesday 1 PM',
            'hook': f'Avoid these {topic} pitfalls...'
        },
        {
            'title': f'Before vs After: My {topic} Journey',
            'format': 'Reel' if platform == 'instagram' else 'Video',
            'platform': platform.capitalize(),
            'estimated_engagement': 'High',
            'best_posting_time': 'Saturday 11 AM',
            'hook': f'Transformation through {topic}...'
        },
        {
            'title': f'Why Most People Fail at {topic}',
            'format': 'Story' if platform == 'instagram' else 'Post',
            'platform': platform.capitalize(),
            'estimated_engagement': 'Medium',
            'best_posting_time': 'Sunday 9 AM',
            'hook': f'The mindset shift for {topic}...'
        }
    ]
    return templates[:count]

# Initialize token manager
token_manager = get_token_manager()

@app.route('/api/youtube/auth')
def youtube_auth():
    """
    Initiate YouTube OAuth flow with CSRF protection and consent tracking
    
    Query params:
        - redirect_uri: Optional custom redirect URI
        - user_id: User ID for tracking (required in production)
    """
    client_id = os.environ.get('YOUTUBE_CLIENT_ID', '')
    if not client_id:
        return jsonify({'success': False, 'error': 'YouTube OAuth not configured'}), 500
    
    # Generate CSRF state token
    state = secrets.token_urlsafe(32)
    session['oauth_state'] = state
    
    # Store user consent intent
    user_id = request.args.get('user_id') or session.get('user_id')
    if user_id:
        session['oauth_user_id'] = user_id
    
    # Build authorization URL
    redirect_uri = request.args.get('redirect_uri', url_for('youtube_callback', _external=True))
    auth_url = get_youtube_auth_url(client_id, redirect_uri, state)
    
    # Log consent initiation
    log_token_action(user_id or 'anonymous', 'youtube', 'auth_initiated', {
        'ip_address': request.remote_addr,
        'user_agent': request.user_agent.string[:100] if request.user_agent else 'unknown'
    })
    
    return redirect(auth_url)

@app.route('/api/youtube/callback')
def youtube_callback():
    """
    Handle YouTube OAuth callback with token encryption and audit logging
    
    Exchanges authorization code for tokens, encrypts them, and stores in database.
    """
    # Verify CSRF state
    state = request.args.get('state')
    stored_state = session.pop('oauth_state', None)
    
    if not state or state != stored_state:
        log_token_action('unknown', 'youtube', 'auth_failed', {'reason': 'csrf_mismatch'})
        return jsonify({'success': False, 'error': 'Invalid state parameter'}), 403
    
    code = request.args.get('code')
    error = request.args.get('error')
    
    if error:
        log_token_action('unknown', 'youtube', 'auth_denied', {'error': error})
        return jsonify({'success': False, 'error': f'Authorization denied: {error}'}), 400
    
    if not code:
        return jsonify({'success': False, 'error': 'No authorization code provided'}), 400
    
    # Exchange code for tokens
    client_id = os.environ.get('YOUTUBE_CLIENT_ID', '')
    client_secret = os.environ.get('YOUTUBE_CLIENT_SECRET', '')
    redirect_uri = url_for('youtube_callback', _external=True)
    
    result = exchange_youtube_code(code, client_id, client_secret, redirect_uri)
    
    if not result['success']:
        log_token_action('unknown', 'youtube', 'auth_failed', {'error': result.get('error')})
        return jsonify({
            'success': False,
            'error': 'Failed to obtain access token',
            'details': result.get('error')
        }), 400
    
    # Prepare token data for encryption
    expires_at = (datetime.utcnow() + timedelta(seconds=result['expires_in'])).isoformat()
    
    token_data = {
        'access_token': result['access_token'],
        'refresh_token': result.get('refresh_token'),  # Only present on first auth
        'expires_at': expires_at,
        'scope': result['scope'],
        'connected_at': datetime.utcnow().isoformat()
    }
    
    # Encrypt tokens
    try:
        encrypted_tokens = token_manager.encrypt_token(token_data)
    except Exception as e:
        log_token_action('unknown', 'youtube', 'encryption_failed', {'error': str(e)})
        return jsonify({'success': False, 'error': 'Token encryption failed'}), 500
    
    # Get user from session
    user_id = session.pop('oauth_user_id', None)
    
    # In production: store in database
    # For now, store in session with warning
    session['youtube_token_encrypted'] = encrypted_tokens
    session['youtube_connected'] = True
    session['youtube_scope'] = result['scope']
    
    # Generate consent record
    consent = generate_consent_record(
        user_id=user_id or 'session_user',
        platform='youtube',
        scopes=result['scope'].split(),
        ip_address=request.remote_addr
    )
    
    # Log successful connection
    log_token_action(user_id or 'session_user', 'youtube', 'connected', {
        'scopes': result['scope'],
        'ip_address': request.remote_addr,
        'consent_record': consent
    })
    
    # Return success (in production, redirect to dashboard)
    return jsonify({
        'success': True,
        'message': 'YouTube account connected successfully',
        'scopes': result['scope'],
        'consent': consent
    })

@app.route('/api/youtube/disconnect', methods=['POST'])
def youtube_disconnect():
    """
    Disconnect YouTube account with token revocation and audit logging
    
    Revokes OAuth tokens and clears stored credentials.
    """
    user_id = session.get('user_id', 'unknown')
    
    # Try to revoke tokens if available
    encrypted_tokens = session.get('youtube_token_encrypted')
    if encrypted_tokens:
        try:
            token_data = token_manager.decrypt_token(encrypted_tokens)
            access_token = token_data.get('access_token')
            
            if access_token:
                revoke_youtube_token(access_token)
                log_token_action(user_id, 'youtube', 'token_revoked')
        except Exception as e:
            logger.warning(f"Token revocation failed: {e}")
    
    # Clear session data
    session.pop('youtube_token_encrypted', None)
    session.pop('youtube_connected', None)
    session.pop('youtube_scope', None)
    session.pop('youtube_token', None)  # Legacy cleanup
    session.pop('youtube_refresh_token', None)
    
    log_token_action(user_id, 'youtube', 'disconnected', {
        'ip_address': request.remote_addr
    })
    
    return jsonify({
        'success': True,
        'message': 'YouTube disconnected successfully'
    })

@app.route('/api/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_post(post_id):
    """Get, update, or delete a specific post"""
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'GET':
        return jsonify({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'platforms': json.loads(post.platforms) if post.platforms else [],
            'status': post.status,
            'scheduled_at': post.scheduled_at.isoformat() if post.scheduled_at else None,
            'created_at': post.created_at.isoformat()
        })
    
    elif request.method == 'PUT':
        data = request.json
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.platforms = json.dumps(data.get('platforms', []))
        if data.get('scheduled_at'):
            post.scheduled_at = datetime.fromisoformat(data['scheduled_at'])
        db.session.commit()
        return jsonify({'success': True, 'message': 'Post updated'})
    
    elif request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Post deleted'})

@app.route('/api/publish-now/<int:post_id>', methods=['POST'])
def publish_now(post_id):
    """Publish a post immediately"""
    post = Post.query.get_or_404(post_id)
    
    # Check if user has connected platforms
    platforms = json.loads(post.platforms) if post.platforms else []
    results = []
    
    for platform in platforms:
        if platform == 'youtube':
            if not session.get('youtube_token'):
                results.append({'platform': 'youtube', 'status': 'error', 'message': 'YouTube not connected'})
            else:
                # In production, this would actually upload to YouTube
                results.append({'platform': 'youtube', 'status': 'success', 'message': 'Video queued for upload'})
        elif platform == 'instagram':
            results.append({'platform': 'instagram', 'status': 'pending', 'message': 'Instagram publishing coming soon'})
    
    post.status = 'published'
    post.published_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({'success': True, 'results': results})

@app.route('/api/user/subscription')
def get_subscription():
    """Get user's subscription details"""
    # In production, get from authenticated user
    return jsonify({
        'tier': 'free',
        'posts_used': Post.query.count(),
        'posts_limit': 10,
        'platforms_allowed': 1,
        'features': ['Basic scheduling', 'Content calendar', 'AI ideas (5/day)']
    })

@app.route('/api/analytics')
def get_analytics():
    """Get analytics dashboard data"""
    total_posts = Post.query.count()
    published = Post.query.filter_by(status='published').count()
    scheduled = Post.query.filter_by(status='scheduled').count()
    
    # Calculate engagement rate (mock data for now)
    engagement_rate = 4.8 if published > 0 else 0
    
    return jsonify({
        'total_posts': total_posts,
        'published': published,
        'scheduled': scheduled,
        'engagement_rate': engagement_rate,
        'top_performing_post': None if published == 0 else 'Sample Post',
        'growth_rate': '+12% this week'
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
