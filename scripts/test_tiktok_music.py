#!/usr/bin/env python3
"""
Test TikTok music endpoints from SociaVault
"""
import requests
import os

api_key = os.environ.get("SOCIAVAULT_API_KEY", "your-api-key-here")
headers = {"x-api-key": api_key}

# Test 1: Popular Songs
print("=== TEST 1: Popular Songs ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/music/popular")
r = requests.get("https://api.sociavault.com/v1/scrape/tiktok/music/popular", headers=headers, timeout=30)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    print(f"Response keys: {list(data.keys()) if isinstance(data, dict) else 'not dict'}")
    if isinstance(data, dict) and 'data' in data:
        sounds = data['data'].get('sound_list', {})
        if sounds:
            if isinstance(sounds, dict):
                first_sound = list(sounds.values())[0] if sounds else None
            else:
                first_sound = sounds[0] if sounds else None
            if first_sound:
                print(f"First sound keys: {list(first_sound.keys())}")
                print(f"Sample: {first_sound}")
print()

# Test 2: Search Music
print("=== TEST 2: Search Music (fitness) ===")
print("URL: https://api.sociavault.com/v1/scrape/tiktok/search/music?query=fitness")
r = requests.get("https://api.sociavault.com/v1/scrape/tiktok/search/music", params={"query": "fitness"}, headers=headers, timeout=30)
print(f"Status: {r.status_code}")
if r.status_code == 200:
    data = r.json()
    print(f"Response keys: {list(data.keys()) if isinstance(data, dict) else 'not dict'}")
    print(f"Body (first 800 chars): {r.text[:800]}")
print()

# Test 3: Song Details
print("=== TEST 3: Song Details ===")
print("Need music_id from previous results...")
print("Skipping - no music_id available yet")
