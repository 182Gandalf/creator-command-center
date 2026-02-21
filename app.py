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
    youtube_connected = db.Column(db.Boolean, default=False)
    instagram_connected = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    """Scheduled and published posts"""
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(500))
    content = db.Column(db.Text)
    platforms = db.Column(db.String(500))
    status = db.Column(db.String(50), default='draft')
    scheduled_at = db.Column(db.DateTime)
    published_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

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
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true&key={YOUTUBE_API_KEY}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                'success': True,
                'channels': data.get('items', [])
            })
        else:
            return jsonify({
                'success': False,
                'error': f'YouTube API error: {response.status_code}'
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
    """Generate AI content ideas"""
    ideas = [
        {
            'title': '5 AI Tools That Save Me 10 Hours/Week',
            'format': 'Carousel (5 slides)',
            'platform': 'Instagram'
        },
        {
            'title': 'How I Batch Create Content',
            'format': 'YouTube Short',
            'platform': 'YouTube'
        },
        {
            'title': 'Before vs After: My Workflow',
            'format': 'Reel/TikTok',
            'platform': 'Instagram'
        }
    ]
    return jsonify({'ideas': ideas})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
