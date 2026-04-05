#!/usr/bin/env python3
"""
Check digest email status for all users
"""
import os
import sys

# Try to get DB URL from Railway or local env
db_url = os.environ.get('DATABASE_URL', '')

if not db_url:
    print("ERROR: DATABASE_URL not set")
    print("Please run: railway run python3 check_digests.py")
    sys.exit(1)

os.environ['DATABASE_URL'] = db_url

sys.path.insert(0, '/home/daz/.openclaw/workspace/flowcast')

from database import SessionLocal
from models import User, CreatorProfile

db = SessionLocal()

print("=" * 60)
print("DIGEST EMAIL STATUS CHECK")
print("=" * 60)

# Get all users
users = db.query(User).all()
print(f"\nTotal users in database: {len(users)}")

# Check by tier
print("\n--- Users by Tier ---")
for tier in ['splash', 'creator', 'creator_pro', 'studio', 'admin']:
    count = db.query(User).filter(User.subscription_tier == tier).count()
    print(f"  {tier}: {count}")

# Check users with valid emails
print("\n--- Email Status ---")
valid_emails = 0
placeholder_emails = 0
missing_emails = 0

for user in users:
    if not user.email:
        missing_emails += 1
    elif 'placeholder' in user.email.lower():
        placeholder_emails += 1
    else:
        valid_emails += 1

print(f"  Valid emails: {valid_emails}")
print(f"  Placeholder emails: {placeholder_emails}")
print(f"  Missing emails: {missing_emails}")

# Check profiles
print("\n--- Profile Status ---")
users_with_profile = db.query(User).join(CreatorProfile).count()
users_without_profile = len(users) - users_with_profile
print(f"  Users with profile: {users_with_profile}")
print(f"  Users without profile: {users_without_profile}")

# Eligible users (valid email + has profile)
print("\n--- Eligible for Digest ---")
eligible = db.query(User, CreatorProfile).join(CreatorProfile).filter(
    User.email.isnot(None),
    ~User.email.contains('placeholder')
).all()

print(f"  Total eligible users: {len(eligible)}")

print("\n--- Sample Eligible Users (first 10) ---")
for user, profile in eligible[:10]:
    print(f"  {user.email} ({user.subscription_tier}) - {profile.niche}")

print("\n" + "=" * 60)
print(f"SUMMARY: {len(eligible)} users should have received the digest")
print("=" * 60)

db.close()
