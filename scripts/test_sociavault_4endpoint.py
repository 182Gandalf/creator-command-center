#!/usr/bin/env python3
"""
SociaVault 4-Endpoint Test Script
Paste the output of this script.
"""
import requests
import os

api_key = os.environ.get("SOCIAVAULT_API_KEY", "")
if not api_key:
    print("ERROR: Set SOCIAVAULT_API_KEY environment variable")
    exit(1)

print("=" * 70)
print("SOCIAVAULT 4-ENDPOINT TEST")
print("=" * 70)

# Test 1: Trending Feed (no params)
print("\n=== TEST 1: Trending Feed ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/trending",
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:800]}")

# Test 2: Keyword Search
print("\n=== TEST 2: Keyword Search ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/search/keyword",
    params={"query": "fitness tips", "sort_by": "most-liked"},
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:800]}")

# Test 3: Popular Songs
print("\n=== TEST 3: Popular Songs ===")
r = requests.get(
    "https://api.sociavault.com/v1/scrape/tiktok/music/popular",
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:800]}")

# Test 4: Credits
print("\n=== TEST 4: Credits ===")
r = requests.get(
    "https://api.sociavault.com/v1/credits",
    headers={"x-api-key": api_key},
    timeout=30
)
print(f"Status: {r.status_code}")
print(f"Body: {r.text[:500]}")

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
