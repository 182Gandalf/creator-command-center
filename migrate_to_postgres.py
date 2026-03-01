#!/usr/bin/env python3
"""
SQLite to PostgreSQL Migration Script for FlowCast

This script exports all data from the SQLite database to JSON format,
which can then be imported into PostgreSQL.

Usage:
    python migrate_to_postgres.py --export
    python migrate_to_postgres.py --import --db-url "postgresql://..."
"""

import json
import os
import sys
from datetime import datetime

# Add the parent directory to path to import app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def export_sqlite_data():
    """Export all data from SQLite to JSON files"""
    print("🔄 Exporting SQLite data...")
    
    # Import here to avoid database connection issues
    from app import app, db
    from app import User, Post, ContentIdea, AIUsageTracker
    
    with app.app_context():
        data = {
            'users': [],
            'posts': [],
            'content_ideas': [],
            'ai_usage_trackers': [],
            'exported_at': datetime.utcnow().isoformat()
        }
        
        # Export Users
        print("  📦 Exporting users...")
        users = User.query.all()
        for user in users:
            data['users'].append({
                'id': user.id,
                'email': user.email,
                'password_hash': user.password_hash,
                'created_at': user.created_at.isoformat() if user.created_at else None,
                'subscription_tier': user.subscription_tier,
                'trial_started_at': user.trial_started_at.isoformat() if user.trial_started_at else None,
                'trial_ended_at': user.trial_ended_at.isoformat() if user.trial_ended_at else None,
                'youtube_connected': user.youtube_connected,
                'youtube_token': user.youtube_token,
                'instagram_connected': user.instagram_connected,
                'instagram_token': user.instagram_token,
                'tiktok_connected': user.tiktok_connected,
                'tiktok_token': user.tiktok_token
            })
        
        # Export Posts
        print("  📦 Exporting posts...")
        posts = Post.query.all()
        for post in posts:
            data['posts'].append({
                'id': post.id,
                'user_id': post.user_id,
                'title': post.title,
                'content': post.content,
                'platforms': post.platforms,
                'status': post.status,
                'scheduled_at': post.scheduled_at.isoformat() if post.scheduled_at else None,
                'published_at': post.published_at.isoformat() if post.published_at else None,
                'created_at': post.created_at.isoformat() if post.created_at else None,
                'updated_at': post.updated_at.isoformat() if post.updated_at else None,
                'youtube_video_id': post.youtube_video_id,
                'instagram_media_id': post.instagram_media_id,
                'tiktok_publish_id': post.tiktok_publish_id,
                'tiktok_draft_status': post.tiktok_draft_status,
                'analytics': post.analytics
            })
        
        # Export Content Ideas
        print("  📦 Exporting content ideas...")
        ideas = ContentIdea.query.all()
        for idea in ideas:
            data['content_ideas'].append({
                'id': idea.id,
                'user_id': idea.user_id,
                'title': idea.title,
                'description': idea.description,
                'platforms': idea.platforms,
                'format_type': idea.format_type,
                'created_at': idea.created_at.isoformat() if idea.created_at else None,
                'used_in_post_id': idea.used_in_post_id
            })
        
        # Export AI Usage Trackers
        print("  📦 Exporting AI usage trackers...")
        trackers = AIUsageTracker.query.all()
        for tracker in trackers:
            data['ai_usage_trackers'].append({
                'id': tracker.id,
                'user_id': tracker.user_id,
                'requests_today': tracker.requests_today,
                'last_request_date': tracker.last_request_date.isoformat() if tracker.last_request_date else None,
                'bonus_credits': tracker.bonus_credits
            })
        
        # Save to file
        export_file = 'migration_data.json'
        with open(export_file, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\n✅ Export complete!")
        print(f"   Users: {len(data['users'])}")
        print(f"   Posts: {len(data['posts'])}")
        print(f"   Content Ideas: {len(data['content_ideas'])}")
        print(f"   AI Usage Trackers: {len(data['ai_usage_trackers'])}")
        print(f"\n📁 Data saved to: {export_file}")
        
        return export_file

def import_to_postgres(db_url, data_file='migration_data.json'):
    """Import data from JSON to PostgreSQL"""
    print(f"🔄 Importing data to PostgreSQL...")
    print(f"   Database: {db_url[:50]}...")
    
    # Set the DATABASE_URL environment variable
    os.environ['DATABASE_URL'] = db_url
    
    # Import after setting env var
    from app import app, db
    from app import User, Post, ContentIdea, AIUsageTracker
    
    # Load data
    with open(data_file, 'r') as f:
        data = json.load(f)
    
    with app.app_context():
        # Create all tables
        print("  📦 Creating tables...")
        db.create_all()
        
        # Import Users
        print("  📦 Importing users...")
        for user_data in data['users']:
            user = User(
                id=user_data['id'],
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                subscription_tier=user_data['subscription_tier'],
                youtube_connected=user_data['youtube_connected'],
                youtube_token=user_data['youtube_token'],
                instagram_connected=user_data['instagram_connected'],
                instagram_token=user_data['instagram_token'],
                tiktok_connected=user_data['tiktok_connected'],
                tiktok_token=user_data['tiktok_token']
            )
            if user_data['created_at']:
                user.created_at = datetime.fromisoformat(user_data['created_at'])
            if user_data['trial_started_at']:
                user.trial_started_at = datetime.fromisoformat(user_data['trial_started_at'])
            if user_data['trial_ended_at']:
                user.trial_ended_at = datetime.fromisoformat(user_data['trial_ended_at'])
            db.session.add(user)
        
        # Import Posts
        print("  📦 Importing posts...")
        for post_data in data['posts']:
            post = Post(
                id=post_data['id'],
                user_id=post_data['user_id'],
                title=post_data['title'],
                content=post_data['content'],
                platforms=post_data['platforms'],
                status=post_data['status'],
                youtube_video_id=post_data['youtube_video_id'],
                instagram_media_id=post_data['instagram_media_id'],
                tiktok_publish_id=post_data['tiktok_publish_id'],
                tiktok_draft_status=post_data['tiktok_draft_status'],
                analytics=post_data['analytics']
            )
            if post_data['scheduled_at']:
                post.scheduled_at = datetime.fromisoformat(post_data['scheduled_at'])
            if post_data['published_at']:
                post.published_at = datetime.fromisoformat(post_data['published_at'])
            if post_data['created_at']:
                post.created_at = datetime.fromisoformat(post_data['created_at'])
            if post_data['updated_at']:
                post.updated_at = datetime.fromisoformat(post_data['updated_at'])
            db.session.add(post)
        
        # Import Content Ideas
        print("  📦 Importing content ideas...")
        for idea_data in data['content_ideas']:
            idea = ContentIdea(
                id=idea_data['id'],
                user_id=idea_data['user_id'],
                title=idea_data['title'],
                description=idea_data['description'],
                platforms=idea_data['platforms'],
                format_type=idea_data['format_type'],
                used_in_post_id=idea_data['used_in_post_id']
            )
            if idea_data['created_at']:
                idea.created_at = datetime.fromisoformat(idea_data['created_at'])
            db.session.add(idea)
        
        # Import AI Usage Trackers
        print("  📦 Importing AI usage trackers...")
        for tracker_data in data['ai_usage_trackers']:
            tracker = AIUsageTracker(
                id=tracker_data['id'],
                user_id=tracker_data['user_id'],
                requests_today=tracker_data['requests_today'],
                bonus_credits=tracker_data['bonus_credits']
            )
            if tracker_data['last_request_date']:
                tracker.last_request_date = datetime.fromisoformat(tracker_data['last_request_date']).date()
            db.session.add(tracker)
        
        # Commit all changes
        print("  💾 Committing changes...")
        db.session.commit()
        
        print(f"\n✅ Import complete!")
        print(f"   Users: {len(data['users'])}")
        print(f"   Posts: {len(data['posts'])}")
        print(f"   Content Ideas: {len(data['content_ideas'])}")
        print(f"   AI Usage Trackers: {len(data['ai_usage_trackers'])}")

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python migrate_to_postgres.py --export")
        print("  python migrate_to_postgres.py --import --db-url 'postgresql://...'")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == '--export':
        export_sqlite_data()
    elif command == '--import':
        if '--db-url' not in sys.argv:
            print("Error: --db-url required for import")
            print("Example: python migrate_to_postgres.py --import --db-url 'postgresql://user:pass@host/db'")
            sys.exit(1)
        
        db_url_index = sys.argv.index('--db-url') + 1
        if db_url_index >= len(sys.argv):
            print("Error: Database URL required after --db-url")
            sys.exit(1)
        
        db_url = sys.argv[db_url_index]
        import_to_postgres(db_url)
    else:
        print(f"Unknown command: {command}")
        print("Use --export or --import")
        sys.exit(1)

if __name__ == '__main__':
    main()
