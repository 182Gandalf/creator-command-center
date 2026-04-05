#!/usr/bin/env python3
"""
Test script to send digest emails to 182gandalf@gmail.com
Tests both weekly and daily digest formats with all 4 trend sources.
"""
import asyncio
import os
import sys

sys.path.insert(0, '/home/daz/.openclaw/workspace/flowcast')

# Set up minimal env
os.environ.setdefault('DATABASE_URL', os.environ.get('DATABASE_URL', ''))
os.environ.setdefault('FROM_EMAIL', os.environ.get('FROM_EMAIL', 'hello@flowcast.space'))
os.environ.setdefault('RESEND_API_KEY', os.environ.get('RESEND_API_KEY', ''))

from database import SessionLocal
from models import User, UserProfile
from services.digests import generate_and_send_trend_digest, send_day7_onboarding_email
from services.trends import get_combined_trends_for_niche_sync

TEST_EMAIL = "182gandalf@gmail.com"

async def test_weekly_digest():
    """Send a weekly digest test email."""
    print("=" * 60)
    print("TEST 1: Weekly Digest")
    print("=" * 60)
    
    # Create a mock user and profile
    class MockUser:
        email = TEST_EMAIL
        subscription_tier = "creator"
        clerk_user_id = "test_clerk_id"
    
    class MockProfile:
        niche = "fitness"
        niche_category = "fitness"
        tone = "energetic"
    
    user = MockUser()
    profile = MockProfile()
    
    # Show what trends would be included
    print(f"\nFetching combined trends for '{profile.niche}'...")
    trends = get_combined_trends_for_niche_sync(profile.niche, limit=5)
    print(f"Found {len(trends)} trends:")
    for i, t in enumerate(trends, 1):
        source_icon = {"google_trends": "📈", "reddit": "👽", "youtube": "📺", "tiktok": "🎵"}.get(t.get("source"), "🔥")
        print(f"  {i}. {source_icon} {t['topic']} ({t.get('source', 'unknown')})")
    
    # Send the digest
    print(f"\nSending weekly digest to {TEST_EMAIL}...")
    result = await generate_and_send_trend_digest(user, profile, frequency="weekly")
    
    if result:
        print("✅ Weekly digest sent successfully!")
    else:
        print("❌ Failed to send weekly digest")
    
    return result


async def test_daily_digest():
    """Send a daily digest test email."""
    print("\n" + "=" * 60)
    print("TEST 2: Daily Digest")
    print("=" * 60)
    
    class MockUser:
        email = TEST_EMAIL
        subscription_tier = "studio"
        clerk_user_id = "test_clerk_id"
    
    class MockProfile:
        niche = "technology"
        niche_category = "technology"
        tone = "professional"
    
    user = MockUser()
    profile = MockProfile()
    
    print(f"\nFetching combined trends for '{profile.niche}'...")
    trends = get_combined_trends_for_niche_sync(profile.niche, limit=5)
    print(f"Found {len(trends)} trends:")
    for i, t in enumerate(trends, 1):
        source_icon = {"google_trends": "📈", "reddit": "👽", "youtube": "📺", "tiktok": "🎵"}.get(t.get("source"), "🔥")
        print(f"  {i}. {source_icon} {t['topic']} ({t.get('source', 'unknown')})")
    
    print(f"\nSending daily digest to {TEST_EMAIL}...")
    result = await generate_and_send_trend_digest(user, profile, frequency="daily")
    
    if result:
        print("✅ Daily digest sent successfully!")
    else:
        print("❌ Failed to send daily digest")
    
    return result


async def test_day7_email():
    """Send a Day 7 onboarding email."""
    print("\n" + "=" * 60)
    print("TEST 3: Day 7 Onboarding Email")
    print("=" * 60)
    
    class MockUser:
        email = TEST_EMAIL
        subscription_tier = "splash"
        clerk_user_id = "test_clerk_id"
    
    class MockProfile:
        niche = "gaming"
        tone = "casual"
    
    user = MockUser()
    profile = MockProfile()
    
    print(f"\nSending Day 7 onboarding email to {TEST_EMAIL}...")
    print(f"Niche: {profile.niche}, Tone: {profile.tone}")
    
    result = await send_day7_onboarding_email(user, profile)
    
    if result:
        print("✅ Day 7 onboarding email sent successfully!")
    else:
        print("❌ Failed to send Day 7 email")
    
    return result


async def main():
    print("\n🚀 FlowCast Digest Email Test Suite")
    print("Sending test emails to:", TEST_EMAIL)
    print()
    
    # Run all tests
    weekly_ok = await test_weekly_digest()
    daily_ok = await test_daily_digest()
    day7_ok = await test_day7_email()
    
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Weekly Digest:  {'✅ PASS' if weekly_ok else '❌ FAIL'}")
    print(f"Daily Digest:   {'✅ PASS' if daily_ok else '❌ FAIL'}")
    print(f"Day 7 Email:    {'✅ PASS' if day7_ok else '❌ FAIL'}")
    print()
    
    if weekly_ok and daily_ok and day7_ok:
        print("🎉 All tests passed! Check your inbox at", TEST_EMAIL)
    else:
        print("⚠️  Some tests failed. Check the logs above.")


if __name__ == "__main__":
    asyncio.run(main())
