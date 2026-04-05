#!/usr/bin/env python3
"""Debug combined trends for a niche to see what's being selected"""
import sys
sys.path.insert(0, '/home/daz/.openclaw/workspace/flowcast')

from services.trends import get_combined_trends_for_niche_sync
from services.reddit_trends import get_reddit_trends_for_niche_sync
from services.youtube_trends import get_youtube_trends_for_niche_sync
from services.tiktok_trends import get_tiktok_trends_for_niche_sync
from services.trends import get_trends_for_niche_sync

niche = "fitness"

print("=" * 70)
print(f"DEBUG: Trend sources for '{niche}'")
print("=" * 70)

# Check each source individually
print("\n1. GOOGLE TRENDS:")
google = get_trends_for_niche_sync(niche, limit=5)
for i, t in enumerate(google, 1):
    print(f"   {i}. {t.get('topic', 'N/A')} (score: {t.get('score', 0)})")

print("\n2. REDDIT TRENDS:")
reddit = get_reddit_trends_for_niche_sync(niche, limit=5)
for i, t in enumerate(reddit, 1):
    print(f"   {i}. {t.get('topic', 'N/A')[:50]}... (score: {t.get('score', 0)}, subreddit: {t.get('subreddit', 'N/A')})")

print("\n3. YOUTUBE TRENDS:")
youtube = get_youtube_trends_for_niche_sync(niche, limit=5)
for i, t in enumerate(youtube, 1):
    print(f"   {i}. {t.get('topic', 'N/A')[:50]}... (score: {t.get('score', 0)})")

print("\n4. TIKTOK TRENDS:")
tiktok = get_tiktok_trends_for_niche_sync(niche, limit=5)
for i, t in enumerate(tiktok, 1):
    print(f"   {i}. {t.get('topic', 'N/A')[:50]}... (score: {t.get('score', 0)}, type: {t.get('type', 'N/A')})")

print("\n" + "=" * 70)
print("COMBINED & NORMALIZED (Top 5):")
print("=" * 70)

combined = get_combined_trends_for_niche_sync(niche, limit=5)
for i, t in enumerate(combined, 1):
    source_icon = {"google_trends": "📈", "reddit": "👽", "youtube": "📺", "tiktok": "🎵"}.get(t.get("source"), "🔥")
    print(f"   {i}. {source_icon} {t.get('topic', 'N/A')[:60]}...")
    print(f"       Source: {t.get('source', 'N/A')} | Normalized: {t.get('normalized_score', 0)} | Raw: {t.get('score', 0)}")

print("\n" + "=" * 70)
print(f"Sources in top 5: {set(t.get('source') for t in combined)}")
print("=" * 70)
