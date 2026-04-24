#!/usr/bin/env python3
"""Test all TikTok endpoints"""
import os
import requests

api_key = os.environ.get("SOCIAVAULT_API_KEY", "your-api-key-here")

# Test trending feed (known to work)
print("=== Trending Feed ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/trending",
    params={"region": "US"},
    headers={"x-api-key": api_key}
)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    aweme_list = data.get("data", {}).get("aweme_list", {})
    count = len(aweme_list) if isinstance(aweme_list, dict) else 0
    print(f"Posts: {count}")

# Test popular songs (known to work)
print("\n=== Popular Songs ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/music/popular",
    headers={"x-api-key": api_key}
)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    sound_list = data.get("data", {}).get("sound_list", {})
    count = len(sound_list) if isinstance(sound_list, dict) else 0
    print(f"Sounds: {count}")

# Test hashtag search
print("\n=== Hashtag Search ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/search/hashtag",
    params={"hashtag": "travel", "trim": "true"},
    headers={"x-api-key": api_key}
)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    print(f"Response keys: {data.keys() if isinstance(data, dict) else 'not dict'}")
    aweme_list = data.get("data", {}).get("aweme_list", {})
    count = len(aweme_list) if isinstance(aweme_list, dict) else 0
    print(f"Posts: {count}")

# Test keyword with full response inspection
print("\n=== Keyword Search (full response) ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/search/keyword",
    params={"query": "travel", "sort_by": "most-liked"},
    headers={"x-api-key": api_key}
)
print(f"Status: {r.status_code}")
print(f"Response (first 500 chars): {r.text[:500]}")
