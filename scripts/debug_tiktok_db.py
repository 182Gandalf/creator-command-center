#!/usr/bin/env python3
"""Debug TikTok data in database"""
import os
import sys
sys.path.insert(0, '/home/daz/.openclaw/workspace/flowcast')

os.environ.setdefault('DATABASE_URL', os.environ.get('DATABASE_URL', ''))

from database import SessionLocal
from models import TikTokTrend
from sqlalchemy import func
from datetime import datetime, timezone

db = SessionLocal()

# Get all niches with data
results = db.query(
    TikTokTrend.niche,
    func.count(TikTokTrend.id),
    func.max(TikTokTrend.fetched_at)
).group_by(TikTokTrend.niche).all()

print("TikTok Trends by Niche:")
print("-" * 60)
for niche, count, latest in sorted(results):
    age = (datetime.now(timezone.utc) - latest).total_seconds() / 3600 if latest else None
    print(f"{niche:20} | {count:4} posts | latest: {latest} ({age:.1f}h ago)")

print("\n")
print("All niches in DB:", [r[0] for r in results])

# Check for today's rotation group
from config.niche_intelligence import get_todays_tiktok_rotation_group
today = get_todays_tiktok_rotation_group()
print(f"\nToday's rotation group: {today}")

for niche in today:
    count = db.query(TikTokTrend).filter(TikTokTrend.niche == niche).count()
    print(f"  {niche}: {count} posts")

db.close()
