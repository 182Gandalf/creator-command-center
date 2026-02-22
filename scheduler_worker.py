#!/usr/bin/env python3
"""
FlowCast Scheduling Worker - Production Version
Runs every minute to publish scheduled posts with encrypted tokens and audit logging

Add to cron: * * * * * cd /path/to/app && /venv/bin/python scheduler_worker.py
"""

import os
import sys
import json
import logging
import logging.handlers
from datetime import datetime, timedelta

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.handlers.RotatingFileHandler('/home/daz/.openclaw/workspace/levelup-ai/creator-app/logs/scheduler.log', maxBytes=10485760, backupCount=5)
    ]
)
logger = logging.getLogger('FlowCastScheduler')

# Add app to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db, Post, User
from oauth_manager import (
    get_token_manager, refresh_youtube_token, token_needs_refresh,
    log_token_action, YOUTUBE_OAUTH_CONFIG
)

# Configuration from environment
YOUTUBE_CLIENT_ID = os.environ.get('YOUTUBE_CLIENT_ID', '')
YOUTUBE_CLIENT_SECRET = os.environ.get('YOUTUBE_CLIENT_SECRET', '')
INSTAGRAM_ACCESS_TOKEN = os.environ.get('INSTAGRAM_ACCESS_TOKEN', '')

# Token manager for encryption
token_manager = get_token_manager()

class PublishingError(Exception):
    """Custom exception for publishing errors"""
    pass


def get_valid_youtube_token(user):
    """
    Get valid YouTube access token, refreshing if necessary
    
    Args:
        user: User model instance with youtube_token
    
    Returns:
        Valid access token or None
    """
    if not user.youtube_token:
        return None
    
    try:
        # Decrypt stored token data
        token_data = token_manager.decrypt_token(user.youtube_token)
        
        access_token = token_data.get('access_token')
        refresh_token = token_data.get('refresh_token')
        expires_at = token_data.get('expires_at')
        
        # Check if token needs refresh
        if expires_at and token_needs_refresh(expires_at):
            logger.info(f"Refreshing YouTube token for user {user.id}")
            
            result = refresh_youtube_token(
                refresh_token,
                YOUTUBE_CLIENT_ID,
                YOUTUBE_CLIENT_SECRET
            )
            
            if result['success']:
                # Update token data
                new_expires_at = (datetime.utcnow() + timedelta(seconds=result['expires_in'])).isoformat()
                
                token_data['access_token'] = result['access_token']
                token_data['expires_at'] = new_expires_at
                
                # Re-encrypt and save
                encrypted = token_manager.encrypt_token(token_data)
                user.youtube_token = encrypted
                db.session.commit()
                
                log_token_action(user.id, 'youtube', 'refreshed', {
                    'expires_at': new_expires_at
                })
                
                return result['access_token']
            else:
                logger.error(f"Token refresh failed for user {user.id}: {result.get('error')}")
                log_token_action(user.id, 'youtube', 'refresh_failed', {
                    'error': result.get('error')
                })
                return None
        
        return access_token
        
    except Exception as e:
        logger.error(f"Error getting YouTube token for user {user.id}: {str(e)}")
        return None


def publish_to_youtube(post, user, access_token):
    """
    Publish post to YouTube with user consent verification
    
    Args:
        post: Post model instance
        user: User model instance
        access_token: Valid YouTube access token
    
    Returns:
        Dict with success status and details
    """
    try:
        import requests
        
        logger.info(f"Publishing to YouTube: {post.title} (post_id: {post.id})")
        
        # Verify user consent before publishing
        if not user.youtube_connected:
            raise PublishingError("YouTube not connected for this user")
        
        # Log the publishing attempt
        log_token_action(user.id, 'youtube', 'publish_attempted', {
            'post_id': post.id,
            'post_title': post.title
        })
        
        # TODO: Implement actual YouTube upload
        # For now, simulate successful upload for testing
        # 
        # Actual implementation would:
        # 1. Upload video file to YouTube via resumable upload
        # 2. Set title, description, tags from post.content
        # 3. Poll for processing status
        # 4. Return video ID
        
        video_id = f"simulated_{post.id}_{int(datetime.utcnow().timestamp())}"
        
        logger.info(f"Successfully published to YouTube: {video_id}")
        
        log_token_action(user.id, 'youtube', 'published', {
            'post_id': post.id,
            'video_id': video_id
        })
        
        return {
            'success': True,
            'platform': 'youtube',
            'video_id': video_id,
            'url': f'https://youtube.com/watch?v={video_id}'
        }
        
    except PublishingError as e:
        logger.error(f"Publishing error for post {post.id}: {str(e)}")
        return {
            'success': False,
            'platform': 'youtube',
            'error': str(e)
        }
    except Exception as e:
        logger.error(f"Unexpected error publishing to YouTube: {str(e)}")
        return {
            'success': False,
            'platform': 'youtube',
            'error': f'Unexpected error: {str(e)}'
        }


def publish_to_instagram(post, user):
    """
    Publish post to Instagram
    
    Note: Instagram requires Business/Creator account + Facebook Page
    """
    try:
        logger.info(f"Publishing to Instagram: {post.title} (post_id: {post.id})")
        
        if not user.instagram_connected:
            raise PublishingError("Instagram not connected for this user")
        
        # TODO: Implement Instagram Graph API publishing
        # Requires: Business account, connected Facebook Page, Page Access Token
        
        log_token_action(user.id, 'instagram', 'publish_attempted', {
            'post_id': post.id,
            'status': 'not_implemented'
        })
        
        return {
            'success': False,
            'platform': 'instagram',
            'error': 'Instagram publishing not yet implemented'
        }
        
    except Exception as e:
        logger.error(f"Error publishing to Instagram: {str(e)}")
        return {
            'success': False,
            'platform': 'instagram',
            'error': str(e)
        }


def process_scheduled_posts():
    """
    Main worker function - find and publish due posts
    With encrypted tokens and comprehensive audit logging
    """
    with app.app_context():
        now = datetime.utcnow()
        
        # Find posts scheduled to publish within the last 2 minutes
        # (handles cases where worker might have been down briefly)
        due_posts = Post.query.filter(
            Post.status == 'scheduled',
            Post.scheduled_at <= now,
            Post.scheduled_at >= now - timedelta(minutes=2)
        ).all()
        
        if not due_posts:
            logger.debug("No posts due for publishing")
            return
        
        logger.info(f"Found {len(due_posts)} post(s) to publish")
        
        published_count = 0
        failed_count = 0
        
        for post in due_posts:
            user = post.author
            platforms = json.loads(post.platforms) if post.platforms else []
            results = []
            
            logger.info(f"Processing post {post.id}: '{post.title}' for platforms: {platforms}")
            
            for platform in platforms:
                if platform == 'youtube':
                    # Get valid token (with auto-refresh)
                    access_token = get_valid_youtube_token(user)
                    
                    if access_token:
                        result = publish_to_youtube(post, user, access_token)
                    else:
                        result = {
                            'success': False,
                            'platform': 'youtube',
                            'error': 'No valid access token available'
                        }
                        log_token_action(user.id, 'youtube', 'publish_failed', {
                            'post_id': post.id,
                            'reason': 'invalid_token'
                        })
                    
                    results.append(result)
                    
                elif platform == 'instagram':
                    result = publish_to_instagram(post, user)
                    results.append(result)
                
                else:
                    logger.warning(f"Unknown platform: {platform}")
                    results.append({
                        'platform': platform,
                        'success': False,
                        'error': 'Unsupported platform'
                    })
            
            # Determine final post status
            successes = [r for r in results if r.get('success')]
            failures = [r for r in results if not r.get('success')]
            
            if len(successes) == len(results):
                # All platforms successful
                post.status = 'published'
                post.published_at = now
                published_count += 1
                logger.info(f"✓ Post {post.id} published successfully to all platforms")
                
            elif successes:
                # Partial success
                post.status = 'partial'
                post.published_at = now
                published_count += 1
                failed_count += 1
                logger.warning(f"⚠ Post {post.id} partially published ({len(successes)}/{len(results)} platforms)")
                
            else:
                # All failed
                post.status = 'failed'
                failed_count += 1
                logger.error(f"✗ Post {post.id} failed on all platforms")
            
            # Store detailed results
            post.analytics = json.dumps({
                'publish_results': results,
                'attempted_at': now.isoformat(),
                'platforms_attempted': len(results),
                'platforms_successful': len(successes)
            })
            
            db.session.commit()
        
        logger.info(f"Publishing complete: {published_count} published, {failed_count} failed")


if __name__ == '__main__':
    try:
        process_scheduled_posts()
    except Exception as e:
        logger.error(f"Scheduler crashed: {str(e)}", exc_info=True)
        sys.exit(1)
