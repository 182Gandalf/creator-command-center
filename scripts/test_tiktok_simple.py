#!/usr/bin/env python3
"""Test TikTok keyword search with different params"""
import requests

api_key = os.environ.get("SOCIAVAULT_API_KEY", "your-api-key-here")

# Test various query formats
test_queries = [
    ("travel", "travel"),
    ("travel", "vacation"),
    ("beauty", "beauty"),
    ("beauty", "makeup"),
    ("gaming", "gaming"),
    ("gaming", "game"),
    ("entertainment", "movie"),
    ("entertainment", "tv"),
]

for niche, query in test_queries:
    url = "https://api.sociavault.com/v1/scrape/tiktok/search/keyword"
    
    # Try without date_posted filter
    params = {"query": query, "sort_by": "most-liked"}
    headers = {"x-api-key": api_key}
    
    r = requests.get(url, params=params, headers=headers, timeout=30)
    
    if r.status_code == 200:
        data = r.json()
        aweme_list = data.get("data", {}).get("aweme_list", {})
        post_count = len(aweme_list) if isinstance(aweme_list, dict) else len(aweme_list) if isinstance(aweme_list, list) else 0
        print(f"{niche:15} | '{query:20}' | {post_count} posts")
    else:
        print(f"{niche:15} | '{query:20}' | ERROR {r.status_code}")
