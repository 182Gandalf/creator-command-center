#!/usr/bin/env python3
"""
Test SociaVault API endpoints directly to debug 400 errors
"""
import requests
import os

# Get API key from environment or prompt
api_key = os.environ.get("SOCIAVAULT_API_KEY", "")

if not api_key:
    print("ERROR: SOCIAVAULT_API_KEY not set in environment")
    print("Please set it: export SOCIAVAULT_API_KEY=your_key_here")
    exit(1)

print("=" * 70)
print("SOCIAVAULT API DIRECT TEST")
print("=" * 70)
print(f"API Key (first 10 chars): {api_key[:10]}...")
print()

# Test 1: Trending Feed (no params needed)
print("=== TEST 1: Trending Feed ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/trending")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/trending",
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Response (first 1000 chars):")
print(r.text[:1000])
print()

# Test 2: Keyword Search
print("=== TEST 2: Keyword Search ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/search/keyword?query=fitness+tips&sort_by=most-liked")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/search/keyword",
    params={"query": "fitness tips", "sort_by": "most-liked"},
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Response (first 1000 chars):")
print(r.text[:1000])
print()

# Test 3: Popular Songs
print("=== TEST 3: Popular Songs ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/music/popular")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/music/popular",
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Response (first 1000 chars):")
print(r.text[:1000])
print()

# Test 4: Credit balance
print("=== TEST 4: Credits ===")
print("URL: https://api.sociavault.com/v1/credits")
r = requests.get(
    "https://api.sociavault.com/v1/credits",
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Response (first 500 chars):")
print(r.text[:500])
print()

# Test 5: Hashtag Search
print("=== TEST 5: Hashtag Search ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/search/hashtag?hashtag=fitness&trim=true")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/search/hashtag",
    params={"hashtag": "fitness", "trim": "true"},
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Response (first 1000 chars):")
print(r.text[:1000])
print()

# Test 6: Music Details (using a dummy music ID)
print("=== TEST 6: Music Details ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/music/details?soundId=12345")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/music/details",
    params={"soundId": "12345"},
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Response (first 1000 chars):")
print(r.text[:1000])
print()

print("=" * 70)
print("TEST COMPLETE")
print("=" * 70)
