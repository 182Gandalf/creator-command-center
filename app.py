# Creator Command Center
# Flask Backend Application

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta
import os
import requests
import json

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///creator_command_center.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# API Configuration
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', '[REDACTED_YOUTUBE_KEY]')
INSTAGRAM_APP_ID = os.environ.get('INSTAGRAM_APP_ID', '[REDACTED_INSTAGRAM_ID]')
INSTAGRAM_APP_SECRET = os.environ.get('INSTAGRAM_APP_SECRET', '[REDACTED_INSTAGRAM_SECRET]')

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
    """Generate AI content ideas based on user's content history"""
    # Get user's recent posts to personalize suggestions
    recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
    
    # AI-generated ideas (in production, this would call OpenAI/Claude API)
    ideas = [
        {
            'id': 1,
            'title': '5 AI Tools That Save Me 10 Hours/Week',
            'format': 'Carousel (5 slides)',
            'platform': 'Instagram',
            'estimated_engagement': 'High',
            'best_posting_time': 'Tuesday 10 AM',
            'hook': 'Stop wasting time on manual tasks...'
        },
        {
            'id': 2,
            'title': 'How I Batch Create Content',
            'format': 'YouTube Short',
            'platform': 'YouTube',
            'estimated_engagement': 'Medium',
            'best_posting_time': 'Thursday 2 PM',
            'hook': 'I create a week of content in 2 hours...'
        },
        {
            'id': 3,
            'title': 'Before vs After: My Workflow',
            'format': 'Reel/TikTok',
            'platform': 'Instagram',
            'estimated_engagement': 'High',
            'best_posting_time': 'Saturday 11 AM',
            'hook': 'This changed everything for me...'
        },
        {
            'id': 4,
            'title': 'The Truth About Going Viral',
            'format': 'Long-form Video',
            'platform': 'YouTube',
            'estimated_engagement': 'Very High',
            'best_posting_time': 'Sunday 9 AM',
            'hook': 'Everyone gets this wrong...'
        },
        {
            'id': 5,
            'title': '3 Mistakes Killing Your Engagement',
            'format': 'Carousel',
            'platform': 'Instagram',
            'estimated_engagement': 'High',
            'best_posting_time': 'Wednesday 1 PM',
            'hook': 'I made all of these...'
        }
    ]
    return jsonify({'success': True, 'ideas': ideas})

@app.route('/api/youtube/auth')
def youtube_auth():
    """Initiate YouTube OAuth flow"""
    # Google OAuth2 configuration
    client_id = os.environ.get('GOOGLE_CLIENT_ID', '')
    redirect_uri = request.args.get('redirect_uri', url_for('youtube_callback', _external=True))
    
    auth_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    scope = 'https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/youtube.upload'
    
    params = {
        'client_id': client_id,
        'redirect_uri': redirect_uri,
        'response_type': 'code',
        'scope': scope,
        'access_type': 'offline',
        'prompt': 'consent'
    }
    
    auth_request_url = f"{auth_url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return redirect(auth_request_url)

@app.route('/api/youtube/callback')
def youtube_callback():
    """Handle YouTube OAuth callback"""
    code = request.args.get('code')
    if not code:
        return jsonify({'success': False, 'error': 'No authorization code provided'}), 400
    
    # Exchange code for tokens
    token_url = 'https://oauth2.googleapis.com/token'
    client_id = os.environ.get('GOOGLE_CLIENT_ID', '')
    client_secret = os.environ.get('GOOGLE_CLIENT_SECRET', '')
    redirect_uri = url_for('youtube_callback', _external=True)
    
    data = {
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    
    try:
        response = requests.post(token_url, data=data)
        tokens = response.json()
        
        if 'access_token' in tokens:
            # Store token in session (in production, store in database)
            session['youtube_token'] = tokens['access_token']
            if 'refresh_token' in tokens:
                session['youtube_refresh_token'] = tokens['refresh_token']
            
            return jsonify({
                'success': True,
                'message': 'YouTube account connected successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to obtain access token',
                'details': tokens
            }), 400
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/youtube/disconnect', methods=['POST'])
def youtube_disconnect():
    """Disconnect YouTube account"""
    session.pop('youtube_token', None)
    session.pop('youtube_refresh_token', None)
    return jsonify({'success': True, 'message': 'YouTube disconnected'})

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
