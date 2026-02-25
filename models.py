# Database Models for Creator Command Center

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User accounts"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Subscription
    subscription_tier = db.Column(db.String(50), default='free')
    trial_started_at = db.Column(db.DateTime)
    trial_ended_at = db.Column(db.DateTime)

    # Social platform connections
    youtube_connected = db.Column(db.Boolean, default=False)
    youtube_token = db.Column(db.Text)
    instagram_connected = db.Column(db.Boolean, default=False)
    instagram_token = db.Column(db.Text)
    tiktok_connected = db.Column(db.Boolean, default=False)
    tiktok_token = db.Column(db.Text)

    # Relationships
    posts = db.relationship('Post', backref='author', lazy=True)
    platforms = db.relationship('PlatformConnection', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def get_post_limit(self):
        """Get monthly post limit based on subscription tier"""
        limits = {
            'free': 20,
            'starter': 50,
            'creator': float('inf'),
            'pro': float('inf')
        }
        return limits.get(self.subscription_tier, 20)

class PlatformConnection(db.Model):
    """Connected social media platforms"""
    __tablename__ = 'platform_connections'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    platform = db.Column(db.String(50), nullable=False)  # youtube, instagram, etc.
    access_token = db.Column(db.Text)
    refresh_token = db.Column(db.Text)
    token_expires_at = db.Column(db.DateTime)
    channel_id = db.Column(db.String(100))  # YouTube channel or Instagram user ID
    channel_name = db.Column(db.String(200))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<PlatformConnection {self.platform} - {self.channel_name}>'

class Post(db.Model):
    """Scheduled and published posts"""
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Content
    title = db.Column(db.String(500))
    content = db.Column(db.Text)
    media_urls = db.Column(db.Text)  # JSON array of media file URLs
    
    # Platform targeting
    platforms = db.Column(db.String(500))  # JSON array: ["youtube", "instagram"]
    
    # Scheduling
    status = db.Column(db.String(50), default='draft')  # draft, scheduled, published, failed
    scheduled_at = db.Column(db.DateTime)
    published_at = db.Column(db.DateTime)
    
    # Platform-specific IDs after publishing
    youtube_video_id = db.Column(db.String(100))
    instagram_media_id = db.Column(db.String(100))
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Post {self.id} - {self.title[:50]}...>'

class ContentIdea(db.Model):
    """AI-generated content ideas saved by user"""
    __tablename__ = 'content_ideas'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    title = db.Column(db.String(500))
    description = db.Column(db.Text)
    suggested_platforms = db.Column(db.String(500))  # JSON array
    suggested_format = db.Column(db.String(100))  # carousel, video, etc.
    
    # AI metadata
    ai_generated = db.Column(db.Boolean, default=True)
    ai_prompt_used = db.Column(db.Text)
    
    # User actions
    is_saved = db.Column(db.Boolean, default=False)
    converted_to_post = db.Column(db.Boolean, default=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=True)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ContentIdea {self.title[:50]}...>'

class AnalyticsCache(db.Model):
    """Cached analytics data from platforms"""
    __tablename__ = 'analytics_cache'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    
    # Metrics
    total_posts = db.Column(db.Integer, default=0)
    total_views = db.Column(db.Integer, default=0)
    total_likes = db.Column(db.Integer, default=0)
    total_comments = db.Column(db.Integer, default=0)
    engagement_rate = db.Column(db.Float, default=0.0)
    
    # Raw data (JSON)
    raw_data = db.Column(db.Text)
    
    # Cache timestamp
    cached_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AnalyticsCache {self.platform} - {self.cached_at}>'

class ScheduledJob(db.Model):
    """Background jobs for posting"""
    __tablename__ = 'scheduled_jobs'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    
    job_type = db.Column(db.String(50))  # publish_post, refresh_analytics
    status = db.Column(db.String(50), default='pending')  # pending, running, completed, failed
    
    scheduled_for = db.Column(db.DateTime, nullable=False)
    executed_at = db.Column(db.DateTime)
    error_message = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<ScheduledJob {self.job_type} - {self.status}>'
