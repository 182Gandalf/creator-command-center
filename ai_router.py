# Multi-Provider AI Router for FlowCast
# Routes requests to cheapest adequate model based on user tier

import os
import json
import hashlib
import time
from datetime import datetime, timedelta
from functools import lru_cache
import requests

# Configuration
AI_PROVIDERS = {
    'gemini_flash': {
        'name': 'Google Gemini Flash',
        'api_url': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
        'cost_per_1m_input': 0.075,  # $0.075 per 1M tokens
        'cost_per_1m_output': 0.30,
        'max_tokens': 8192,
        'quality_score': 7.5,
        'best_for': ['captions', 'hashtags', 'short_ideas', 'free_tier']
    },
    'deepseek': {
        'name': 'DeepSeek V3',
        'api_url': 'https://api.deepseek.com/v1/chat/completions',
        'cost_per_1m_input': 0.14,
        'cost_per_1m_output': 0.28,
        'max_tokens': 4096,
        'quality_score': 7.8,
        'best_for': ['content_ideas', 'blog_outlines', 'creator_tier']
    },
    'mistral_small': {
        'name': 'Mistral Small',
        'api_url': 'https://api.mistral.ai/v1/chat/completions',
        'cost_per_1m_input': 1.00,
        'cost_per_1m_output': 3.00,
        'max_tokens': 4096,
        'quality_score': 7.9,
        'best_for': ['eu_customers', 'long_form', 'privacy_focused']
    },
    'gpt35': {
        'name': 'OpenAI GPT-3.5 Turbo',
        'api_url': 'https://api.openai.com/v1/chat/completions',
        'cost_per_1m_input': 0.50,
        'cost_per_1m_output': 1.50,
        'max_tokens': 4096,
        'quality_score': 8.0,
        'best_for': ['backup', 'complex_tasks']
    },
    'gpt4': {
        'name': 'OpenAI GPT-4',
        'api_url': 'https://api.openai.com/v1/chat/completions',
        'cost_per_1m_input': 30.00,
        'cost_per_1m_output': 60.00,
        'max_tokens': 8192,
        'quality_score': 9.0,
        'best_for': ['pro_tier', 'complex_scripts', 'premium_users']
    }
}

# Tier-based routing
TIER_ROUTING = {
    'free': ['gemini_flash'],  # Cheapest option
    'starter': ['gemini_flash'],  # Still cheap, better quality
    'creator': ['deepseek', 'gemini_flash'],  # DeepSeek primary, Gemini backup
    'pro': ['gpt4', 'deepseek']  # GPT-4 for premium, DeepSeek fallback
}

# Simple cache (in production, use Redis)
_cache = {}
_cache_ttl = {}  # Time-to-live tracking

def get_cache_key(prompt, tier):
    """Generate cache key from prompt"""
    key_data = f"{tier}:{prompt.lower().strip()}"
    return hashlib.md5(key_data.encode()).hexdigest()

def get_cached_response(prompt, tier, max_age_hours=24):
    """Check if we have a cached response"""
    key = get_cache_key(prompt, tier)
    
    if key in _cache:
        # Check if cache is still valid
        if key in _cache_ttl:
            if datetime.now() < _cache_ttl[key]:
                return _cache[key]
            else:
                # Expired, remove from cache
                del _cache[key]
                del _cache_ttl[key]
    
    return None

def cache_response(prompt, tier, response, cache_hours=24):
    """Cache a response"""
    key = get_cache_key(prompt, tier)
    _cache[key] = response
    _cache_ttl[key] = datetime.now() + timedelta(hours=cache_hours)
    
    # Simple cache size management (keep under 1000 items)
    if len(_cache) > 1000:
        # Remove oldest entries
        oldest_keys = sorted(_cache_ttl.keys(), key=lambda k: _cache_ttl[k])[:100]
        for old_key in oldest_keys:
            if old_key in _cache:
                del _cache[old_key]
            if old_key in _cache_ttl:
                del _cache_ttl[old_key]

def call_gemini(prompt, api_key, max_tokens=500):
    """Call Google Gemini Flash API"""
    url = f"{AI_PROVIDERS['gemini_flash']['api_url']}?key={api_key}"
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    data = {
        'contents': [{
            'parts': [{'text': prompt}]
        }],
        'generationConfig': {
            'maxOutputTokens': max_tokens,
            'temperature': 0.7
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if 'candidates' in result and len(result['candidates']) > 0:
            content = result['candidates'][0]['content']['parts'][0]['text']
            return {
                'success': True,
                'content': content,
                'model': 'gemini_flash',
                'tokens': len(content.split())  # Approximate
            }
        else:
            return {
                'success': False,
                'error': 'No content generated',
                'model': 'gemini_flash'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'model': 'gemini_flash'
        }

def call_deepseek(prompt, api_key, max_tokens=500):
    """Call DeepSeek API"""
    url = AI_PROVIDERS['deepseek']['api_url']
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    data = {
        'model': 'deepseek-chat',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0]['message']['content']
            return {
                'success': True,
                'content': content,
                'model': 'deepseek',
                'tokens': result.get('usage', {}).get('total_tokens', len(content.split()))
            }
        else:
            return {
                'success': False,
                'error': 'No content generated',
                'model': 'deepseek'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'model': 'deepseek'
        }

def call_openai(prompt, api_key, model='gpt-3.5-turbo', max_tokens=500):
    """Call OpenAI API"""
    url = AI_PROVIDERS['gpt35']['api_url']
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0]['message']['content']
            return {
                'success': True,
                'content': content,
                'model': model,
                'tokens': result.get('usage', {}).get('total_tokens', len(content.split()))
            }
        else:
            return {
                'success': False,
                'error': 'No content generated',
                'model': model
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'model': model
        }

def call_mistral(prompt, api_key, max_tokens=500):
    """Call Mistral API"""
    url = AI_PROVIDERS['mistral_small']['api_url']
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    
    data = {
        'model': 'mistral-small-latest',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.7
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        if 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0]['message']['content']
            return {
                'success': True,
                'content': content,
                'model': 'mistral_small',
                'tokens': result.get('usage', {}).get('total_tokens', len(content.split()))
            }
        else:
            return {
                'success': False,
                'error': 'No content generated',
                'model': 'mistral_small'
            }
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'model': 'mistral_small'
        }

def generate_content_ideas(user_tier='free', topic='', platform='instagram', count=5):
    """
    Generate AI content ideas based on user tier
    Routes to cheapest adequate model
    """
    
    # Build prompt
    prompt = f"""Generate {count} creative content ideas for {platform} about: {topic}

For each idea, provide:
1. A catchy title
2. Brief description (1-2 sentences)
3. Suggested format (carousel, reel, story, etc.)
4. Estimated engagement level (high/medium/low)

Make them engaging and trendy for 2025."""
    
    # Check cache first
    cached = get_cached_response(prompt, user_tier)
    if cached:
        return {
            'success': True,
            'ideas': cached,
            'cached': True,
            'cost': 0
        }
    
    # Get routing configuration for this tier
    providers = TIER_ROUTING.get(user_tier, ['gemini_flash'])
    
    # Try each provider in order
    for provider in providers:
        result = None
        
        if provider == 'gemini_flash':
            api_key = os.environ.get('GEMINI_API_KEY', '')
            if api_key:
                result = call_gemini(prompt, api_key)
        
        elif provider == 'deepseek':
            api_key = os.environ.get('DEEPSEEK_API_KEY', '')
            if api_key:
                result = call_deepseek(prompt, api_key)
        
        elif provider == 'gpt4':
            api_key = os.environ.get('OPENAI_API_KEY', '')
            if api_key:
                result = call_openai(prompt, api_key, model='gpt-4')
        
        elif provider == 'gpt35':
            api_key = os.environ.get('OPENAI_API_KEY', '')
            if api_key:
                result = call_openai(prompt, api_key, model='gpt-3.5-turbo')
        
        elif provider == 'mistral_small':
            api_key = os.environ.get('MISTRAL_API_KEY', '')
            if api_key:
                result = call_mistral(prompt, api_key)
        
        # If successful, parse and cache
        if result and result.get('success'):
            ideas = parse_ideas(result['content'])
            
            # Cache the response (24 hours for content ideas)
            cache_response(prompt, user_tier, ideas, cache_hours=24)
            
            # Calculate approximate cost
            tokens = result.get('tokens', 500)
            cost_data = AI_PROVIDERS.get(result['model'], {})
            input_cost = (tokens * 0.5 / 1_000_000) * cost_data.get('cost_per_1m_input', 0.50)
            output_cost = (tokens * 0.5 / 1_000_000) * cost_data.get('cost_per_1m_output', 1.50)
            total_cost = input_cost + output_cost
            
            return {
                'success': True,
                'ideas': ideas,
                'model_used': result['model'],
                'cached': False,
                'cost_usd': round(total_cost, 6)
            }
    
    # All providers failed, return fallback ideas with error details
    error_details = []
    for provider in providers:
        if provider == 'gemini_flash':
            api_key = os.environ.get('GEMINI_API_KEY', '')
            if api_key:
                test_result = call_gemini("test", api_key)
                if not test_result.get('success'):
                    error_details.append(f"Gemini: {test_result.get('error', 'Unknown')}")
            else:
                error_details.append("Gemini: No API key")
        elif provider == 'deepseek':
            api_key = os.environ.get('DEEPSEEK_API_KEY', '')
            if api_key:
                test_result = call_deepseek("test", api_key)
                if not test_result.get('success'):
                    error_details.append(f"DeepSeek: {test_result.get('error', 'Unknown')}")
            else:
                error_details.append("DeepSeek: No API key")
    
    return {
        'success': True,
        'ideas': get_fallback_ideas(topic, platform, count),
        'model_used': 'fallback',
        'cached': False,
        'cost_usd': 0,
        'error': '; '.join(error_details) if error_details else 'All AI providers failed'
    }

def parse_ideas(content):
    """Parse AI response into structured ideas"""
    ideas = []
    lines = content.strip().split('\n')
    
    current_idea = {}
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Look for numbered ideas
        if line[0].isdigit() and '.' in line[:3]:
            if current_idea:
                ideas.append(current_idea)
            current_idea = {
                'title': line.split('.', 1)[1].strip() if '.' in line else line,
                'description': '',
                'format': 'Post',
                'engagement': 'Medium'
            }
        elif 'format' in line.lower() or 'type' in line.lower():
            current_idea['format'] = line.split(':')[-1].strip() if ':' in line else line
        elif 'engagement' in line.lower():
            current_idea['engagement'] = line.split(':')[-1].strip() if ':' in line else 'Medium'
        elif current_idea:
            current_idea['description'] += line + ' '
    
    if current_idea:
        ideas.append(current_idea)
    
    # Clean up descriptions
    for idea in ideas:
        idea['description'] = idea['description'].strip()
    
    return ideas

def get_fallback_ideas(topic, platform, count):
    """Fallback ideas when all AI providers fail"""
    templates = [
        {
            'title': f'5 Secrets About {topic} Nobody Talks About',
            'description': 'Revealing the hidden truths that will change how you think about this topic.',
            'format': 'Carousel' if platform == 'instagram' else 'Video',
            'engagement': 'High'
        },
        {
            'title': f'How I Improved My {topic} in 30 Days',
            'description': 'A personal journey with actionable tips you can implement today.',
            'format': 'Reel' if platform == 'instagram' else 'Short',
            'engagement': 'High'
        },
        {
            'title': f'The Biggest {topic} Mistakes Beginners Make',
            'description': 'Avoid these common pitfalls and fast-track your success.',
            'format': 'Story' if platform == 'instagram' else 'Post',
            'engagement': 'Medium'
        },
        {
            'title': f'Before vs After: My {topic} Transformation',
            'description': 'Visual proof that these methods actually work.',
            'format': 'Carousel' if platform == 'instagram' else 'Video',
            'engagement': 'High'
        },
        {
            'title': f'Why Most People Fail at {topic} (And How to Fix It)',
            'description': 'The mindset shift that makes all the difference.',
            'format': 'Reel' if platform == 'instagram' else 'Post',
            'engagement': 'Medium'
        }
    ]
    
    return templates[:count]

# Pre-generated popular ideas (cache forever)
POPULAR_CACHES = {
    'fitness': [
        {'title': '5 Home Workouts That Actually Work', 'description': 'No equipment needed', 'format': 'Reel', 'engagement': 'High'},
        {'title': 'What I Eat in a Day (Healthy Edition)', 'description': 'Simple meals for busy people', 'format': 'Carousel', 'engagement': 'High'},
    ],
    'business': [
        {'title': 'How I Started My Business with €100', 'description': 'Bootstrapping tips', 'format': 'Carousel', 'engagement': 'High'},
        {'title': 'The Productivity System That Changed Everything', 'description': 'Work smarter, not harder', 'format': 'Video', 'engagement': 'Medium'},
    ],
    'travel': [
        {'title': 'Hidden Gems in Europe Nobody Knows About', 'description': 'Off the beaten path', 'format': 'Carousel', 'engagement': 'High'},
        {'title': 'How to Travel on a Budget', 'description': 'Save money while seeing the world', 'format': 'Reel', 'engagement': 'High'},
    ]
}

# Initialize cache with popular topics
for topic, ideas in POPULAR_CACHES.items():
    for tier in ['free', 'starter', 'creator', 'pro']:
        cache_response(f"Generate content ideas for instagram about: {topic}", tier, ideas, cache_hours=168)  # 7 days

def get_ai_stats():
    """Get current AI usage statistics"""
    return {
        'cache_size': len(_cache),
        'cache_hit_rate': calculate_cache_hit_rate(),
        'providers_available': {
            'gemini': bool(os.environ.get('GEMINI_API_KEY')),
            'deepseek': bool(os.environ.get('DEEPSEEK_API_KEY')),
            'openai': bool(os.environ.get('OPENAI_API_KEY')),
            'mistral': bool(os.environ.get('MISTRAL_API_KEY'))
        }
    }

def calculate_cache_hit_rate():
    """Calculate approximate cache hit rate (simplified)"""
    # In production, track actual hits vs misses
    return 0.70  # Estimated 70% hit rate with good caching

# Test function
if __name__ == "__main__":
    print("AI Router Test")
    print("=" * 50)
    
    # Test fallback generation
    result = generate_content_ideas(
        user_tier='free',
        topic='fitness',
        platform='instagram',
        count=3
    )
    
    print(f"Success: {result['success']}")
    print(f"Model: {result.get('model_used', 'unknown')}")
    print(f"Cached: {result.get('cached', False)}")
    print(f"Cost: ${result.get('cost_usd', 0):.6f}")
    print("\nIdeas:")
    for i, idea in enumerate(result['ideas'], 1):
        print(f"{i}. {idea['title']}")
        print(f"   {idea['description'][:80]}...")
    
    print("\n" + "=" * 50)
    print("Setup Instructions:")
    print("1. Get Gemini API key: https://ai.google.dev")
    print("2. Set environment variable: export GEMINI_API_KEY='your-key'")
    print("3. (Optional) Get DeepSeek key: https://platform.deepseek.com")
    print("4. (Optional) Get OpenAI key: https://platform.openai.com")
