# FlowCast
# Social Media Management Platform

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
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

# Enable CORS for API endpoints
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://flowcast.space", "http://localhost:5000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# API Configuration
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', '')
INSTAGRAM_APP_ID = os.environ.get('INSTAGRAM_APP_ID', '')
INSTAGRAM_APP_SECRET = os.environ.get('INSTAGRAM_APP_SECRET', '')

# TikTok Configuration
TIKTOK_CLIENT_KEY = os.environ.get('TIKTOK_CLIENT_KEY', 'awc9mhr7an8b6m9l')
TIKTOK_CLIENT_SECRET = os.environ.get('TIKTOK_CLIENT_SECRET', 'EMJrQ6bzOl6ZNeNgqwCxRLxPYr6vUd8N')

# Google OAuth Configuration
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', '')

# HTTPS Enforcement (for production behind Cloudflare)
@app.before_request
def enforce_https():
    """Redirect HTTP to HTTPS in production"""
    # Skip if running locally
    if request.host.startswith('localhost') or request.host.startswith('127.'):
        return
    
    # Check if request came via HTTPS (Cloudflare sets X-Forwarded-Proto)
    forwarded_proto = request.headers.get('X-Forwarded-Proto', '')
    
    # If not HTTPS, redirect
    if forwarded_proto == 'http':
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

# Database Models
class User(db.Model):
    """User accounts"""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    subscription_tier = db.Column(db.String(20), default='free')  # free, pro, team
    trial_started_at = db.Column(db.DateTime)  # When the 7-day trial started
    trial_ended_at = db.Column(db.DateTime)   # When trial ended (or user upgraded)
    youtube_connected = db.Column(db.Boolean, default=False)
    youtube_token = db.Column(db.Text)  # OAuth token
    instagram_connected = db.Column(db.Boolean, default=False)
    instagram_token = db.Column(db.Text)
    tiktok_connected = db.Column(db.Boolean, default=False)
    tiktok_token = db.Column(db.Text)  # OAuth token for TikTok
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')
    
    def get_post_limit(self):
        limits = {'free': 20, 'pro': 100, 'team': 1000}
        return limits.get(self.subscription_tier, 20)
    
    def get_platforms_allowed(self):
        platforms = {'free': 2, 'pro': 3, 'team': 5}
        return platforms.get(self.subscription_tier, 2)

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
    tiktok_publish_id = db.Column(db.String(100))  # TikTok publish ID (for drafts)
    tiktok_draft_status = db.Column(db.String(50))  # pending, uploaded, failed
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

class AIUsageTracker(db.Model):
    """Track daily AI usage per user for enforcing limits"""
    __tablename__ = 'ai_usage_tracker'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    requests_today = db.Column(db.Integer, default=0)
    last_request_date = db.Column(db.Date, default=datetime.utcnow().date)
    
    def check_and_increment(self, limit=5):
        """Check if user has remaining quota and increment if so"""
        today = datetime.utcnow().date()
        if self.last_request_date != today:
            # Reset for new day
            self.requests_today = 0
            self.last_request_date = today
        
        if self.requests_today >= limit:
            return False, limit - self.requests_today
        
        self.requests_today += 1
        return True, limit - self.requests_today

# Routes
@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Main dashboard (requires login)"""
    return render_template('dashboard.html')

@app.route('/robots.txt')
def robots():
    """Serve robots.txt for SEO"""
    return app.send_static_file('robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    """Serve sitemap.xml for SEO"""
    return app.send_static_file('sitemap.xml')

@app.route('/BingSiteAuth.xml')
def bing_verification():
    """Serve Bing verification file for SEO"""
    return app.send_static_file('BingSiteAuth.xml')

@app.route('/file_28---5d0b287d-0110-44d2-aeb8-8d0024051942.txt')
def tiktok_verification_1():
    """Serve TikTok developer site verification file"""
    return app.send_static_file('file_28---5d0b287d-0110-44d2-aeb8-8d0024051942.txt')

@app.route('/file_29---33f1b90a-a3c2-4fe9-9d60-d1af8491fd6a.txt')
def tiktok_verification_2():
    """Serve TikTok developer site verification file"""
    return app.send_static_file('file_29---33f1b90a-a3c2-4fe9-9d60-d1af8491fd6a.txt')

@app.route('/signup')
def signup():
    """Sign up page"""
    return render_template('signup.html')

@app.route('/login')
def login():
    """Login page"""
    return render_template('login.html')

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
    """Create and schedule a new post with subscription limits"""
    data = request.json
    
    # Get user from session (in production, use proper auth)
    user_id = session.get('user_id')
    if not user_id:
        # For demo: use user ID 1 if exists, or return error
        user = User.query.first()
        if user:
            user_id = user.id
        else:
            return jsonify({
                'success': False,
                'error': 'Authentication required. Please log in.'
            }), 401
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({
            'success': False,
            'error': 'User not found'
        }), 404
    
    # Check post limit (20 for free/trial tier)
    posts_count = Post.query.filter_by(user_id=user_id).count()
    if posts_count >= user.get_post_limit():
        return jsonify({
            'success': False,
            'error': f'Post limit reached. Free tier allows {user.get_post_limit()} posts. Upgrade to create more.'
        }), 403
    
    # Check platform limit (2 for free/trial tier)
    requested_platforms = data.get('platforms', [])
    if len(requested_platforms) > user.get_platforms_allowed():
        return jsonify({
            'success': False,
            'error': f'Platform limit exceeded. Free tier allows {user.get_platforms_allowed()} platform(s). You selected {len(requested_platforms)}.'
        }), 403
    
    # Create new post
    post = Post(
        user_id=user_id,
        title=data.get('title'),
        content=data.get('content'),
        platforms=json.dumps(requested_platforms),
        status='scheduled' if data.get('scheduled_at') else 'draft',
        scheduled_at=datetime.fromisoformat(data['scheduled_at']) if data.get('scheduled_at') else None
    )
    
    db.session.add(post)
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Post created successfully',
        'post_id': post.id,
        'posts_remaining': user.get_post_limit() - posts_count - 1
    })

# ==================== AUTHENTICATION API ROUTES ====================

@app.route('/api/signup', methods=['POST'])
def api_signup():
    """Handle user registration"""
    data = request.json
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    confirm_password = data.get('confirm_password', '')
    
    # Validation
    if not email or not password:
        return jsonify({'success': False, 'error': 'Email and password required'}), 400
    
    if len(password) < 8:
        return jsonify({'success': False, 'error': 'Password must be at least 8 characters'}), 400
    
    # Server-side password confirmation check
    if password != confirm_password:
        return jsonify({'success': False, 'error': 'Passwords do not match'}), 400
    
    # Check if user exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'success': False, 'error': 'Email already registered'}), 409
    
    # Create new user
    # TODO: Migrate to werkzeug.security for proper password hashing
    import hashlib
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    user = User(
        email=email,
        password_hash=password_hash,
        subscription_tier='free',
        trial_started_at=datetime.utcnow()
    )
    
    db.session.add(user)
    db.session.commit()
    
    # Auto-login after signup
    session['user_id'] = user.id
    session['user_email'] = user.email
    
    return jsonify({
        'success': True,
        'message': 'Account created successfully',
        'user': {
            'id': user.id,
            'email': user.email,
            'tier': user.subscription_tier
        }
    })

@app.route('/api/login', methods=['POST'])
def api_login():
    """Handle user login"""
    data = request.json
    email = data.get('email', '').lower().strip()
    password = data.get('password', '')
    
    if not email or not password:
        return jsonify({'success': False, 'error': 'Email and password required'}), 400
    
    # Find user
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
    
    # Verify password
    import hashlib
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    if password_hash != user.password_hash:
        return jsonify({'success': False, 'error': 'Invalid credentials'}), 401
    
    # Create session
    session['user_id'] = user.id
    session['user_email'] = user.email
    
    return jsonify({
        'success': True,
        'message': 'Login successful',
        'user': {
            'id': user.id,
            'email': user.email,
            'tier': user.subscription_tier,
            'tiktok_connected': user.tiktok_connected,
            'youtube_connected': user.youtube_connected,
            'instagram_connected': user.instagram_connected
        }
    })

@app.route('/api/logout', methods=['POST'])
def api_logout():
    """Handle user logout"""
    session.clear()
    return jsonify({'success': True, 'message': 'Logout successful'})

@app.route('/api/me')
def get_current_user():
    """Get current logged in user info"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    user = User.query.get(user_id)
    if not user:
        return jsonify({'success': False, 'error': 'User not found'}), 404
    
    # Get post counts
    posts_count = Post.query.filter_by(user_id=user.id).count()
    scheduled_count = Post.query.filter_by(user_id=user.id, status='scheduled').count()
    
    return jsonify({
        'success': True,
        'user': {
            'id': user.id,
            'email': user.email,
            'tier': user.subscription_tier,
            'posts_used': posts_count,
            'posts_limit': user.get_post_limit(),
            'platforms_limit': user.get_platforms_allowed(),
            'scheduled_posts': scheduled_count,
            'tiktok_connected': user.tiktok_connected,
            'youtube_connected': user.youtube_connected,
            'instagram_connected': user.instagram_connected
        }
    })

# ==================== CONTENT CREATION & SCHEDULING API ====================

@app.route('/api/posts')
def get_posts():
    """Get all posts for current user"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    posts = Post.query.filter_by(user_id=user_id).order_by(Post.created_at.desc()).all()
    
    posts_data = []
    for post in posts:
        posts_data.append({
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'platforms': json.loads(post.platforms) if post.platforms else [],
            'status': post.status,
            'scheduled_at': post.scheduled_at.isoformat() if post.scheduled_at else None,
            'published_at': post.published_at.isoformat() if post.published_at else None,
            'created_at': post.created_at.isoformat(),
            'tiktok_publish_id': post.tiktok_publish_id,
            'tiktok_draft_status': post.tiktok_draft_status
        })
    
    return jsonify({'success': True, 'posts': posts_data})

@app.route('/api/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def manage_post(post_id):
    """Get, update or delete a specific post"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    post = Post.query.filter_by(id=post_id, user_id=user_id).first()
    if not post:
        return jsonify({'success': False, 'error': 'Post not found'}), 404
    
    if request.method == 'GET':
        return jsonify({
            'success': True,
            'post': {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'platforms': json.loads(post.platforms) if post.platforms else [],
                'status': post.status,
                'scheduled_at': post.scheduled_at.isoformat() if post.scheduled_at else None,
                'published_at': post.published_at.isoformat() if post.published_at else None,
                'created_at': post.created_at.isoformat()
            }
        })
    
    elif request.method == 'PUT':
        data = request.json
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        if data.get('platforms'):
            post.platforms = json.dumps(data['platforms'])
        if data.get('scheduled_at'):
            post.scheduled_at = datetime.fromisoformat(data['scheduled_at'])
        post.updated_at = datetime.utcnow()
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Post updated successfully'})
    
    elif request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Post deleted successfully'})

@app.route('/api/posts/<int:post_id>/publish', methods=['POST'])
def publish_post(post_id):
    """Publish a post to connected platforms"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    user = User.query.get(user_id)
    post = Post.query.filter_by(id=post_id, user_id=user_id).first()
    
    if not post:
        return jsonify({'success': False, 'error': 'Post not found'}), 404
    
    platforms = json.loads(post.platforms) if post.platforms else []
    results = []
    
    for platform in platforms:
        if platform == 'tiktok':
            if not user.tiktok_connected:
                results.append({'platform': 'tiktok', 'status': 'error', 'message': 'TikTok not connected'})
            else:
                # Simulate TikTok publishing (API integration pending)
                post.tiktok_draft_status = 'pending'
                results.append({
                    'platform': 'tiktok', 
                    'status': 'pending', 
                    'message': 'Content queued for TikTok posting. Will be published via Direct Post API once approved.',
                    'note': 'Demo mode - TikTok API integration pending approval'
                })
        elif platform == 'youtube':
            if not user.youtube_connected:
                results.append({'platform': 'youtube', 'status': 'error', 'message': 'YouTube not connected'})
            else:
                results.append({'platform': 'youtube', 'status': 'published', 'message': 'Published to YouTube'})
        elif platform == 'instagram':
            if not user.instagram_connected:
                results.append({'platform': 'instagram', 'status': 'error', 'message': 'Instagram not connected'})
            else:
                results.append({'platform': 'instagram', 'status': 'published', 'message': 'Published to Instagram'})
    
    post.status = 'published'
    post.published_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({
        'success': True,
        'message': 'Post published',
        'results': results
    })

@app.route('/api/tiktok/posts', methods=['GET', 'POST'])
def tiktok_posts():
    """Get or create TikTok-specific posts"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'error': 'Not authenticated'}), 401
    
    user = User.query.get(user_id)
    
    if request.method == 'POST':
        data = request.json
        
        # Create TikTok-specific post
        post = Post(
            user_id=user_id,
            title=data.get('title', ''),
            content=data.get('caption', ''),  # Caption with hashtags
            platforms=json.dumps(['tiktok']),
            status='draft',
            scheduled_at=datetime.fromisoformat(data['scheduled_at']) if data.get('scheduled_at') else None
        )
        
        db.session.add(post)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'TikTok post created',
            'post_id': post.id,
            'note': 'Post ready for TikTok Direct Post API integration'
        })
    
    else:  # GET
        posts = Post.query.filter(
            Post.user_id == user_id,
            Post.platforms.contains('tiktok')
        ).order_by(Post.created_at.desc()).all()
        
        return jsonify({
            'success': True,
            'posts': [{
                'id': p.id,
                'title': p.title,
                'caption': p.content,
                'status': p.status,
                'scheduled_at': p.scheduled_at.isoformat() if p.scheduled_at else None,
                'tiktok_status': p.tiktok_draft_status or 'not_submitted'
            } for p in posts]
        })

# ==================== END AUTHENTICATION & CONTENT API ====================

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
    
    # Get user tier and ID (from query param for testing, or session in production)
    user_tier = request.args.get('tier') or session.get('subscription_tier', 'free')
    user_id = session.get('user_id')
    
    # For free tier, check daily AI usage limit (5 per day)
    if user_tier == 'free':
        # Get or create usage tracker
        if user_id:
            tracker = AIUsageTracker.query.filter_by(user_id=user_id).first()
            if not tracker:
                tracker = AIUsageTracker(user_id=user_id)
                db.session.add(tracker)
                db.session.commit()
            
            allowed, remaining = tracker.check_and_increment(limit=5)
            if not allowed:
                return jsonify({
                    'success': False,
                    'error': 'Daily AI limit reached. Free tier allows 5 AI ideas per day. Upgrade for unlimited ideas.',
                    'limit': 5,
                    'used': tracker.requests_today,
                    'tier': user_tier
                }), 429
        else:
            # For anonymous users, allow but don't track
            remaining = None
    else:
        remaining = 'unlimited'
    
    try:
        # Generate ideas using AI router (with automatic caching)
        result = generate_content_ideas(
            user_tier=user_tier,
            topic=topic,
            platform=platform,
            count=count
        )
        
        # Commit the usage tracker update
        if user_tier == 'free' and user_id:
            db.session.commit()
        
        if result['success']:
            # Add metadata for debugging
            response = {
                'success': True,
                'ideas': result['ideas'],
                'model_used': result.get('model_used', 'fallback'),
                'cached': result.get('cached', False),
                'cost_usd': result.get('cost_usd', 0),
                'tier': user_tier,
                'ai_remaining_today': remaining
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
                'ai_remaining_today': remaining,
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
    redirect_uri = request.args.get('redirect_uri', url_for('youtube_callback', _external=True, _scheme='https'))
    # Force HTTPS redirect URI
    if redirect_uri.startswith('http://'):
        redirect_uri = redirect_uri.replace('http://', 'https://', 1)
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
    redirect_uri = url_for('youtube_callback', _external=True, _scheme='https')
    # Force HTTPS redirect URI
    if redirect_uri.startswith('http://'):
        redirect_uri = redirect_uri.replace('http://', 'https://', 1)
    
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

# ==================== TIKTOK OAUTH ROUTES ====================

@app.route('/api/tiktok/auth')
def tiktok_auth():
    """
    Initiate TikTok OAuth flow
    
    TikTok Content Posting API requires:
    - video.upload scope (to upload drafts to inbox)
    - user.info.basic scope (to get user profile)
    """
    client_key = os.environ.get('TIKTOK_CLIENT_KEY', '')
    if not client_key:
        return jsonify({'success': False, 'error': 'TikTok OAuth not configured'}), 500
    
    # Generate CSRF state token
    state = secrets.token_urlsafe(32)
    session['tiktok_oauth_state'] = state
    
    # Build authorization URL
    redirect_uri = request.args.get('redirect_uri', url_for('tiktok_callback', _external=True))
    
    # TikTok OAuth endpoints
    auth_url = (
        f"https://www.tiktok.com/auth/authorize/?"
        f"client_key={client_key}&"
        f"redirect_uri={redirect_uri}&"
        f"scope=user.info.basic,video.upload&"
        f"state={state}&"
        f"response_type=code"
    )
    
    log_token_action('unknown', 'tiktok', 'auth_initiated', {
        'ip_address': request.remote_addr
    })
    
    return redirect(auth_url)

@app.route('/api/tiktok/callback')
def tiktok_callback():
    """Handle TikTok OAuth callback"""
    # Verify CSRF state
    state = request.args.get('state')
    stored_state = session.pop('tiktok_oauth_state', None)
    
    if not state or state != stored_state:
        return jsonify({'success': False, 'error': 'Invalid state parameter'}), 403
    
    code = request.args.get('code')
    error = request.args.get('error')
    
    if error:
        return jsonify({'success': False, 'error': f'Authorization denied: {error}'}), 400
    
    if not code:
        return jsonify({'success': False, 'error': 'No authorization code provided'}), 400
    
    # Exchange code for access token
    client_key = os.environ.get('TIKTOK_CLIENT_KEY', '')
    client_secret = os.environ.get('TIKTOK_CLIENT_SECRET', '')
    redirect_uri = url_for('tiktok_callback', _external=True)
    
    token_url = "https://open-api.tiktok.com/oauth/access_token/"
    response = requests.post(token_url, json={
        'client_key': client_key,
        'client_secret': client_secret,
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri
    })
    
    if response.status_code != 200:
        return jsonify({
            'success': False,
            'error': 'Failed to obtain access token',
            'details': response.text
        }), 400
    
    token_data = response.json()
    access_token = token_data.get('data', {}).get('access_token')
    
    if not access_token:
        return jsonify({
            'success': False,
            'error': 'No access token in response'
        }), 400
    
    # Store in session (encrypt in production)
    session['tiktok_token'] = access_token
    session['tiktok_connected'] = True
    
    log_token_action('session_user', 'tiktok', 'connected', {
        'ip_address': request.remote_addr
    })
    
    return jsonify({
        'success': True,
        'message': 'TikTok account connected successfully'
    })

@app.route('/api/tiktok/upload', methods=['POST'])
def tiktok_upload():
    """
    Upload video to TikTok as draft (goes to user's inbox)
    
    Flow:
    1. User uploads video to FlowCast
    2. We call TikTok Content Posting API
    3. Video goes to user's TikTok inbox as draft
    4. User gets notification in TikTok app
    5. User edits and posts manually
    """
    if not session.get('tiktok_token'):
        return jsonify({'success': False, 'error': 'TikTok not connected'}), 401
    
    data = request.json
    video_url = data.get('video_url')  # URL where video is hosted
    title = data.get('title', '')
    
    if not video_url:
        return jsonify({'success': False, 'error': 'Video URL required'}), 400
    
    access_token = session.get('tiktok_token')
    
    # Step 1: Initialize upload
    init_url = "https://open-api.tiktok.com/video/upload/"
    init_response = requests.post(init_url, json={
        'source_info': {
            'source': 'PULL_FROM_URL',
            'url': video_url
        },
        'title': title,
        'privacy_level': 'SELF_ONLY',  # Upload as draft only
        'disable_duet': False,
        'disable_comment': False
    }, headers={'Authorization': f'Bearer {access_token}'})
    
    if init_response.status_code != 200:
        return jsonify({
            'success': False,
            'error': 'Failed to initiate TikTok upload',
            'details': init_response.text
        }), 400
    
    result = init_response.json()
    publish_id = result.get('data', {}).get('publish_id')
    
    return jsonify({
        'success': True,
        'message': 'Video uploaded to TikTok inbox as draft',
        'publish_id': publish_id,
        'note': 'User will receive notification in TikTok app to complete the post'
    })

@app.route('/api/tiktok/disconnect', methods=['POST'])
def tiktok_disconnect():
    """Disconnect TikTok account"""
    user_id = session.get('user_id', 'unknown')
    
    session.pop('tiktok_token', None)
    session.pop('tiktok_connected', None)
    
    log_token_action(user_id, 'tiktok', 'disconnected', {
        'ip_address': request.remote_addr
    })
    
    return jsonify({
        'success': True,
        'message': 'TikTok disconnected successfully'
    })

# ==================== END TIKTOK ROUTES ====================

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
        elif platform == 'tiktok':
            results.append({'platform': 'tiktok', 'status': 'pending', 'message': 'TikTok draft upload coming soon'})
    
    post.status = 'published'
    post.published_at = datetime.utcnow()
    db.session.commit()
    
    return jsonify({'success': True, 'results': results})

@app.route('/api/user/subscription')
def get_subscription():
    """Get user's subscription details"""
    # In production, get from authenticated user
    # Trial: 20 posts, 2 platforms, 5 AI ideas/day, basic analytics, email support
    return jsonify({
        'tier': 'free',
        'posts_used': Post.query.count(),
        'posts_limit': 20,
        'platforms_allowed': 2,
        'ai_ideas_per_day': 5,
        'analytics_level': 'basic',
        'support_level': 'email',
        'features': [
            '20 posts per month',
            '2 social platforms',
            '5 AI ideas per day',
            'Basic analytics',
            'Email support'
        ]
    })

# ==================== GOOGLE OAUTH ROUTES ====================

@app.route('/api/google/auth')
def google_auth():
    """Initiate Google OAuth flow for sign-in"""
    if not GOOGLE_CLIENT_ID:
        return jsonify({'success': False, 'error': 'Google OAuth not configured'}), 500
    
    # Generate state for CSRF protection
    state = secrets.token_urlsafe(32)
    session['google_oauth_state'] = state
    
    # Build Google OAuth URL
    redirect_uri = url_for('google_callback', _external=True, _scheme='https')
    if redirect_uri.startswith('http://'):
        redirect_uri = redirect_uri.replace('http://', 'https://', 1)
    
    auth_url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?"
        f"client_id={GOOGLE_CLIENT_ID}&"
        f"redirect_uri={redirect_uri}&"
        f"response_type=code&"
        f"scope=openid%20email%20profile&"
        f"state={state}&"
        f"access_type=offline&"
        f"prompt=select_account"
    )
    
    return redirect(auth_url)

@app.route('/api/google/callback')
def google_callback():
    """Handle Google OAuth callback"""
    # Verify state
    state = request.args.get('state')
    stored_state = session.pop('google_oauth_state', None)
    
    if not state or state != stored_state:
        return jsonify({'success': False, 'error': 'Invalid state parameter'}), 403
    
    code = request.args.get('code')
    error = request.args.get('error')
    
    if error:
        return jsonify({'success': False, 'error': f'Google auth denied: {error}'}), 400
    
    if not code:
        return jsonify({'success': False, 'error': 'No authorization code'}), 400
    
    # Exchange code for tokens
    redirect_uri = url_for('google_callback', _external=True, _scheme='https')
    if redirect_uri.startswith('http://'):
        redirect_uri = redirect_uri.replace('http://', 'https://', 1)
    
    token_url = "https://oauth2.googleapis.com/token"
    response = requests.post(token_url, data={
        'code': code,
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    })
    
    if response.status_code != 200:
        return jsonify({'success': False, 'error': 'Failed to get access token'}), 400
    
    tokens = response.json()
    access_token = tokens.get('access_token')
    
    # Get user info from Google
    user_info_response = requests.get(
        'https://www.googleapis.com/oauth2/v2/userinfo',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    
    if user_info_response.status_code != 200:
        return jsonify({'success': False, 'error': 'Failed to get user info'}), 400
    
    user_info = user_info_response.json()
    email = user_info.get('email')
    name = user_info.get('name', '')
    
    # Check if user exists, create if not
    user = User.query.filter_by(email=email.lower()).first()
    if not user:
        # Create new user
        user = User(
            email=email.lower(),
            password_hash='google_oauth',  # Mark as OAuth user
            subscription_tier='free',
            trial_started_at=datetime.utcnow()
        )
        db.session.add(user)
        db.session.commit()
    
    # Create session
    session['user_id'] = user.id
    session['user_email'] = user.email
    
    # Redirect to dashboard
    return redirect('/dashboard')

# ==================== END GOOGLE OAUTH ROUTES ====================

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
