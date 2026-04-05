#!/usr/bin/env python3
"""
Manual trigger for TikTok trend scraping via SociaVault API
"""
import os
import sys

# Add flowcast to path
sys.path.insert(0, '/home/daz/.openclaw/workspace/flowcast')

# Set required env vars if not already set (Railway will have these)
os.environ.setdefault('DATABASE_URL', os.environ.get('DATABASE_URL', ''))
os.environ.setdefault('SOCIAVAULT_API_KEY', os.environ.get('SOCIAVAULT_API_KEY', ''))

from database import SessionLocal
from services.tiktok_trends import fetch_tiktok_trends_for_rotation_group, SOCIAVAULT_API_KEY

def main():
    print("=" * 60)
    print("TikTok Trend Scraper - Manual Trigger")
    print("=" * 60)
    
    # Check API key
    if not SOCIAVAULT_API_KEY:
        print("\n❌ ERROR: SOCIAVAULT_API_KEY not configured!")
        print("Add it to Railway environment variables.")
        sys.exit(1)
    
    print(f"\n✓ SOCIAVAULT_API_KEY configured: {SOCIAVAULT_API_KEY[:10]}...")
    
    # Get database session
    db = SessionLocal()
    
    try:
        print("\n🚀 Starting TikTok trend fetch...")
        print("-" * 60)
        
        # Run the fetch with force=True to bypass duplicate check
        result = fetch_tiktok_trends_for_rotation_group(db, force=True)
        
        print("\n" + "=" * 60)
        print("FETCH RESULTS")
        print("=" * 60)
        print(f"Status: {result.get('status', 'unknown')}")
        print(f"Credits Used: {result.get('credits_used', 0)}")
        print(f"Credits Remaining: {result.get('credits_remaining', 'N/A')}")
        print(f"Posts Stored: {result.get('posts_stored', 0)}")
        print(f"Sounds Stored: {result.get('sounds_stored', 0)}")
        print(f"Errors: {result.get('errors', 0)}")
        print(f"Rotation Group: {result.get('rotation_group', [])}")
        
        if result.get('old_posts_deleted'):
            print(f"Old Posts Deleted: {result['old_posts_deleted']}")
        if result.get('old_sounds_deleted'):
            print(f"Old Sounds Deleted: {result['old_sounds_deleted']}")
        
        if result.get('status') == 'success':
            print("\n✅ TikTok trend fetch completed successfully!")
        elif result.get('status') == 'skipped':
            print(f"\n⚠️ Fetch skipped: {result.get('message', '')}")
        else:
            print(f"\n❌ Fetch failed: {result.get('error', 'Unknown error')}")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    main()
