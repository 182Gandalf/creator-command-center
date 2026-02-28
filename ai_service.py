# AI Service - Centralized AI Calls for FlowCast
"""
This module provides a single entry point for all AI operations.
To change which model handles a task, modify the MODEL_CONFIG dict below.
"""

import os
import json
import requests
from typing import Dict, Any, Optional, List

# ============================================================================
# MODEL CONFIGURATION - CHANGE THIS TO SWITCH AI PROVIDERS
# ============================================================================

# Available models:
# - 'gemini-flash' - Fast, cheap, good for most tasks
# - 'kimi-k2.5' - Moonshot, great for long context
# - 'claude-haiku' - Fast, cheap, good for simple tasks  
# - 'claude-sonnet' - Better quality, more expensive
# - 'gpt-4o-mini' - OpenAI, balanced
# - 'gpt-4o' - OpenAI, best quality

MODEL_CONFIG = {
    # Default model for most tasks
    'default': {
        'provider': 'gemini',
        'model': 'gemini-1.5-flash',
        'temperature': 0.7,
        'max_tokens': 2048
    },
    
    # Specific task configurations
    'content_ideas': {
        'provider': 'gemini',
        'model': 'gemini-1.5-flash',
        'temperature': 0.8,
        'max_tokens': 1024
    },
    
    'caption_generation': {
        'provider': 'gemini', 
        'model': 'gemini-1.5-flash',
        'temperature': 0.6,
        'max_tokens': 512
    },
    
    'hashtag_suggestions': {
        'provider': 'gemini',
        'model': 'gemini-1.5-flash', 
        'temperature': 0.5,
        'max_tokens': 256
    },
    
    'content_analysis': {
        'provider': 'gemini',
        'model': 'gemini-1.5-flash',
        'temperature': 0.3,
        'max_tokens': 1024
    },
    
    # Premium tasks (use better models)
    'premium_content': {
        'provider': 'gemini',
        'model': 'gemini-1.5-pro',
        'temperature': 0.7,
        'max_tokens': 4096
    },
    
    # Add more task types as needed
}

# API Keys (loaded from environment)
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
MOONSHOT_API_KEY = os.environ.get('MOONSHOT_API_KEY', '')  # For Kimi models

# ============================================================================
# CENTRAL AI SERVICE FUNCTION
# ============================================================================

def call_ai(task_type: str, user_input: str, context: Optional[Dict] = None) -> Dict[str, Any]:
    """
    Central function for all AI calls in FlowCast.
    
    Args:
        task_type: Type of AI task (content_ideas, caption_generation, etc.)
        user_input: The user's prompt/input
        context: Optional additional context (user tier, platform, etc.)
    
    Returns:
        Dict with 'success', 'response', and 'error' keys
    
    Example:
        result = call_ai('content_ideas', 'Give me YouTube video ideas about fitness')
        if result['success']:
            ideas = result['response']
    """
    # Get configuration for this task type
    config = MODEL_CONFIG.get(task_type, MODEL_CONFIG['default'])
    provider = config['provider']
    
    # Route to appropriate provider
    if provider == 'gemini':
        return _call_gemini(config, user_input, context)
    elif provider == 'openai':
        return _call_openai(config, user_input, context)
    elif provider == 'anthropic':
        return _call_anthropic(config, user_input, context)
    elif provider == 'moonshot':
        return _call_moonshot(config, user_input, context)
    else:
        return {
            'success': False,
            'response': None,
            'error': f'Unknown AI provider: {provider}'
        }

# ============================================================================
# PROVIDER-SPECIFIC IMPLEMENTATIONS
# ============================================================================

def _call_gemini(config: Dict, user_input: str, context: Optional[Dict]) -> Dict[str, Any]:
    """Call Google Gemini API"""
    if not GEMINI_API_KEY:
        return {
            'success': False,
            'response': None,
            'error': 'GEMINI_API_KEY not configured'
        }
    
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{config['model']}:generateContent"
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        # Build prompt with context if provided
        prompt = user_input
        if context:
            context_str = json.dumps(context, indent=2)
            prompt = f"Context: {context_str}\n\nTask: {user_input}"
        
        data = {
            'contents': [{
                'parts': [{'text': prompt}]
            }],
            'generationConfig': {
                'temperature': config['temperature'],
                'maxOutputTokens': config['max_tokens'],
                'topP': 0.8,
                'topK': 40
            }
        }
        
        response = requests.post(
            f"{url}?key={GEMINI_API_KEY}",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if 'candidates' in result and len(result['candidates']) > 0:
                text = result['candidates'][0]['content']['parts'][0]['text']
                return {
                    'success': True,
                    'response': text,
                    'error': None
                }
            else:
                return {
                    'success': False,
                    'response': None,
                    'error': 'No response from Gemini'
                }
        else:
            return {
                'success': False,
                'response': None,
                'error': f'Gemini API error: {response.status_code} - {response.text}'
            }
    
    except Exception as e:
        return {
            'success': False,
            'response': None,
            'error': f'Exception calling Gemini: {str(e)}'
        }

def _call_openai(config: Dict, user_input: str, context: Optional[Dict]) -> Dict[str, Any]:
    """Call OpenAI API (GPT-4, GPT-3.5, etc.)"""
    if not OPENAI_API_KEY:
        return {
            'success': False,
            'response': None,
            'error': 'OPENAI_API_KEY not configured'
        }
    
    try:
        headers = {
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Build messages
        messages = []
        if context:
            context_str = json.dumps(context, indent=2)
            messages.append({
                'role': 'system',
                'content': f'Context: {context_str}'
            })
        
        messages.append({
            'role': 'user',
            'content': user_input
        })
        
        data = {
            'model': config['model'],
            'messages': messages,
            'temperature': config['temperature'],
            'max_tokens': config['max_tokens']
        }
        
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            text = result['choices'][0]['message']['content']
            return {
                'success': True,
                'response': text,
                'error': None
            }
        else:
            return {
                'success': False,
                'response': None,
                'error': f'OpenAI API error: {response.status_code} - {response.text}'
            }
    
    except Exception as e:
        return {
            'success': False,
            'response': None,
            'error': f'Exception calling OpenAI: {str(e)}'
        }

def _call_anthropic(config: Dict, user_input: str, context: Optional[Dict]) -> Dict[str, Any]:
    """Call Anthropic API (Claude)"""
    if not ANTHROPIC_API_KEY:
        return {
            'success': False,
            'response': None,
            'error': 'ANTHROPIC_API_KEY not configured'
        }
    
    try:
        headers = {
            'x-api-key': ANTHROPIC_API_KEY,
            'Content-Type': 'application/json',
            'anthropic-version': '2023-06-01'
        }
        
        # Build prompt
        prompt = user_input
        if context:
            context_str = json.dumps(context, indent=2)
            prompt = f"Context: {context_str}\n\nHuman: {user_input}\n\nAssistant:"
        else:
            prompt = f"Human: {user_input}\n\nAssistant:"
        
        data = {
            'model': config['model'],
            'prompt': prompt,
            'max_tokens_to_sample': config['max_tokens'],
            'temperature': config['temperature']
        }
        
        response = requests.post(
            'https://api.anthropic.com/v1/complete',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            text = result['completion']
            return {
                'success': True,
                'response': text,
                'error': None
            }
        else:
            return {
                'success': False,
                'response': None,
                'error': f'Anthropic API error: {response.status_code} - {response.text}'
            }
    
    except Exception as e:
        return {
            'success': False,
            'response': None,
            'error': f'Exception calling Anthropic: {str(e)}'
        }

def _call_moonshot(config: Dict, user_input: str, context: Optional[Dict]) -> Dict[str, Any]:
    """Call Moonshot AI API (Kimi models)"""
    if not MOONSHOT_API_KEY:
        return {
            'success': False,
            'response': None,
            'error': 'MOONSHOT_API_KEY not configured'
        }
    
    try:
        headers = {
            'Authorization': f'Bearer {MOONSHOT_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        # Build messages
        messages = []
        if context:
            context_str = json.dumps(context, indent=2)
            messages.append({
                'role': 'system',
                'content': f'Context: {context_str}'
            })
        
        messages.append({
            'role': 'user',
            'content': user_input
        })
        
        data = {
            'model': config['model'],
            'messages': messages,
            'temperature': config['temperature'],
            'max_tokens': config['max_tokens']
        }
        
        response = requests.post(
            'https://api.moonshot.cn/v1/chat/completions',
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            text = result['choices'][0]['message']['content']
            return {
                'success': True,
                'response': text,
                'error': None
            }
        else:
            return {
                'success': False,
                'response': None,
                'error': f'Moonshot API error: {response.status_code} - {response.text}'
            }
    
    except Exception as e:
        return {
            'success': False,
            'response': None,
            'error': f'Exception calling Moonshot: {str(e)}'
        }

# ============================================================================
# HELPER FUNCTIONS FOR COMMON TASKS
# ============================================================================

def generate_content_ideas(topic: str, platform: str = 'youtube', count: int = 5, user_tier: str = 'free') -> List[Dict]:
    """
    Generate content ideas for a specific topic and platform.
    
    Example:
        ideas = generate_content_ideas('fitness', 'youtube', 3)
        # Returns list of idea dicts with title, hook, outline
    """
    prompt = f"""Generate {count} creative content ideas for {platform} about "{topic}".
    
    For each idea, provide:
    1. A catchy title (max 60 characters)
    2. An engaging hook/opening line
    3. 3-5 bullet points for the content outline
    
    Format as JSON array like:
    [
      {{
        "title": "Title here",
        "hook": "Hook text here", 
        "outline": ["Point 1", "Point 2", "Point 3"]
      }}
    ]
    
    Return ONLY the JSON array, no other text."""
    
    result = call_ai('content_ideas', prompt, {
        'platform': platform,
        'topic': topic,
        'user_tier': user_tier
    })
    
    if result['success']:
        try:
            # Parse JSON from AI response
            ideas = json.loads(result['response'])
            return ideas if isinstance(ideas, list) else []
        except json.JSONDecodeError:
            # If AI didn't return valid JSON, return raw text as single idea
            return [{
                'title': 'AI Generated Idea',
                'hook': result['response'][:200],
                'outline': ['See full response']
            }]
    else:
        return []

def generate_caption(content_description: str, platform: str = 'instagram', tone: str = 'professional') -> str:
    """
    Generate a social media caption.
    
    Example:
        caption = generate_caption('Video about morning routines', 'instagram', 'casual')
    """
    prompt = f"""Write an engaging {platform} caption for this content:
    
    Content: {content_description}
    
    Tone: {tone}
    
    Requirements:
    - Include relevant hashtags (3-5)
    - Add a call-to-action
    - Keep it under {220 if platform == 'instagram' else 280} characters
    - Match the {tone} tone"""
    
    result = call_ai('caption_generation', prompt, {
        'platform': platform,
        'tone': tone
    })
    
    return result['response'] if result['success'] else 'Error generating caption'

def suggest_hashtags(content_description: str, platform: str = 'instagram', count: int = 10) -> List[str]:
    """
    Suggest relevant hashtags for content.
    
    Example:
        hashtags = suggest_hashtags('Video about healthy eating', 'instagram', 5)
        # Returns: ['#healthyeating', '#nutrition', '#wellness', ...]
    """
    prompt = f"""Suggest {count} relevant hashtags for this content:
    
    Content: {content_description}
    Platform: {platform}
    
    Mix of:
    - 40% broad/popular hashtags (100K+ posts)
    - 40% medium hashtags (10K-100K posts)  
    - 20% niche/specific hashtags
    
    Return as a simple comma-separated list, no other text."""
    
    result = call_ai('hashtag_suggestions', prompt, {
        'platform': platform,
        'count': count
    })
    
    if result['success']:
        # Parse comma-separated hashtags
        hashtags = [tag.strip() for tag in result['response'].split(',') if tag.strip().startswith('#')]
        return hashtags[:count]
    else:
        return []

def analyze_content_performance(content_data: Dict) -> Dict:
    """
    Analyze content performance and provide recommendations.
    
    Example:
        analysis = analyze_content_performance({
            'views': 1000,
            'likes': 50,
            'comments': 10,
            'platform': 'youtube'
        })
    """
    prompt = f"""Analyze this content performance and provide recommendations:
    
    {json.dumps(content_data, indent=2)}
    
    Provide:
    1. Engagement rate calculation
    2. What's working well
    3. 3 specific improvements
    4. Best time to post next
    
    Return as JSON with keys: engagement_rate, strengths, improvements, best_posting_time"""
    
    result = call_ai('content_analysis', prompt, content_data)
    
    if result['success']:
        try:
            return json.loads(result['response'])
        except json.JSONDecodeError:
            return {'raw_analysis': result['response']}
    else:
        return {'error': result['error']}

# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == '__main__':
    # Example usage
    print("AI Service Examples:")
    print("=" * 50)
    
    # Example 1: Generate content ideas
    print("\n1. Content Ideas:")
    ideas = generate_content_ideas('productivity tips', 'youtube', 2)
    for i, idea in enumerate(ideas, 1):
        print(f"\nIdea {i}:")
        print(f"  Title: {idea.get('title', 'N/A')}")
        print(f"  Hook: {idea.get('hook', 'N/A')[:100]}...")
    
    # Example 2: Generate caption
    print("\n2. Caption:")
    caption = generate_caption('Morning routine video', 'instagram', 'motivational')
    print(f"  {caption}")
    
    # Example 3: Hashtags
    print("\n3. Hashtags:")
    hashtags = suggest_hashtags('Healthy meal prep', 'instagram', 5)
    print(f"  {', '.join(hashtags)}")
