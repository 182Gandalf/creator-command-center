#!/usr/bin/env python3
"""Test TikTok keyword search for today's niches"""
import requests
import os

api_key = os.environ.get("SOCIAVAULT_API_KEY", "your-api-key-here")

queries = {
    "travel": ["travel hack", "hidden gem travel"],
    "beauty": ["skincare routine", "makeup tutorial"],
    "gaming": ["gaming setup", "new game"],
    "entertainment": ["movie review", "binge watch"]
}

for niche, niche_queries in queries.items():
    print(f"\n=== Testing {niche} ===")
    for query in niche_queries:
        url = "https://api.sociavault.com/v1/scrape/tiktok/search/keyword"
        params = {"query": query, "date_posted": "this-week", "sort_by": "most-liked"}
        headers = {"x-api-key": api_key}
        
        r = requests.get(url, params=params, headers=headers, timeout=30)
        print(f"  Query: '{query}' -> Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            aweme_list = data.get("data", {}).get("aweme_list", {})
            post_count = len(aweme_list) if isinstance(aweme_list, dict) else len(aweme_list) if isinstance(aweme_list, list) else 0
            print(f"    Posts returned: {post_count}")
        else:
            print(f"    Error: {r.text[:200]}")
