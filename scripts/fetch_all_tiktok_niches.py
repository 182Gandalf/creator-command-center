#!/usr/bin/env python3
"""
FORCE FETCH: All TikTok niches for admin dashboard update
Bypasses rotation group - fetches every niche immediately
"""
import os
import sys

# Add flowcast to path
sys.path.insert(0, '/home/daz/.openclaw/workspace/flowcast')

os.environ.setdefault('DATABASE_URL', os.environ.get('DATABASE_URL', ''))
os.environ.setdefault('SOCIAVAULT_API_KEY', os.environ.get('SOCIAVAULT_API_KEY', ''))

from database import SessionLocal, engine
from services.tiktok_trends import fetch_tiktok_trends_for_rotation_group, SOCIAVAULT_API_KEY
from config.niche_intelligence import get_all_tracked_niches

def main():
    print("=" * 70)
    print("FORCE FETCH: ALL TikTok Niches")
    print("=" * 70)
    
    if not SOCIAVAULT_API_KEY:
        print("\n❌ ERROR: SOCIAVAULT_API_KEY not configured!")
        sys.exit(1)
    
    # Get ALL niches (23 total)
    all_niches = get_all_tracked_niches()
    print(f"\n📊 Total niches to fetch: {len(all_niches)}")
    print(f"Niches: {', '.join(all_niches)}")
    
    db = SessionLocal()
    
    total_credits = 0
    total_posts = 0
    total_sounds = 0
    total_errors = 0
    
    try:
        # Fetch ALL niches in one batch
        print("\n🚀 Starting FULL fetch for all niches...")
        print("-" * 70)
        
        result = fetch_tiktok_trends_for_rotation_group(
            db, 
            force=True,
            override_niches=all_niches
        )
        
        print("\n" + "=" * 70)
        print("FETCH RESULTS - ALL NICHES")
        print("=" * 70)
        print(f"Status: {result.get('status', 'unknown')}")
        print(f"Credits Used: {result.get('credits_used', 0)}")
        print(f"Credits Remaining: {result.get('credits_remaining', 'N/A')}")
        print(f"Posts Stored: {result.get('posts_stored', 0)}")
        print(f"Sounds Stored: {result.get('sounds_stored', 0)}")
        print(f"Errors: {result.get('errors', 0)}")
        print(f"Niches Processed: {len(all_niches)}")
        
        if result.get('old_posts_deleted'):
            print(f"Old Posts Deleted: {result['old_posts_deleted']}")
        if result.get('old_sounds_deleted'):
            print(f"Old Sounds Deleted: {result['old_sounds_deleted']}")
        
        if result.get('status') == 'success':
            print("\n✅ All niches fetched successfully!")
            print("📊 Admin dashboard data is now updated with fresh TikTok trends.")
        elif result.get('status') == 'partial':
            print(f"\n⚠️ Partial success - some niches may have failed")
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
        print("\n" + "=" * 70)
        print("Admin Dashboard Update Complete")
        print("=" * 70)

if __name__ == "__main__":
    main()
