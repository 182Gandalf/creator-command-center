# AI Service Integration Examples for FlowCast
"""
This file shows how to use the centralized AI service in your Flask routes.
Copy these examples into your app.py or use them as reference.
"""

# ============================================================================
# OPTION 1: Simple Import and Use
# ============================================================================

from ai_service import call_ai, generate_content_ideas, generate_caption, suggest_hashtags

# In your Flask route:
@app.route('/api/generate-ideas', methods=['POST'])
def generate_ideas():
    data = request.get_json()
    topic = data.get('topic', '')
    platform = data.get('platform', 'youtube')
    
    # Use the helper function
    ideas = generate_content_ideas(topic, platform, count=5)
    
    return jsonify({
        'success': True,
        'ideas': ideas
    })

# ============================================================================
# OPTION 2: Direct Call with Task Type
# ============================================================================

@app.route('/api/ai-chat', methods=['POST'])
def ai_chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # Use the central function directly
    result = call_ai(
        task_type='default',
        user_input=user_message,
        context={'user_id': session.get('user_id')}
    )
    
    if result['success']:
        return jsonify({
            'success': True,
            'response': result['response']
        })
    else:
        return jsonify({
            'success': False,
            'error': result['error']
        }), 500

# ============================================================================
# OPTION 3: Custom Prompt with Specific Task Type
# ============================================================================

@app.route('/api/analyze-post', methods=['POST'])
def analyze_post():
    data = request.get_json()
    post_content = data.get('content', '')
    
    # Build custom prompt
    prompt = f"""Analyze this social media post and suggest improvements:
    
    Post Content:
    {post_content}
    
    Provide:
    1. Hook strength (1-10)
    2. Engagement prediction
    3. 3 specific improvements
    4. Better hashtag suggestions"""
    
    # Call with custom task type
    result = call_ai(
        task_type='content_analysis',
        user_input=prompt,
        context={'post_length': len(post_content)}
    )
    
    return jsonify(result)

# ============================================================================
# HOW TO SWITCH AI MODELS
# ============================================================================

"""
To switch from Gemini to OpenAI:

1. Edit ai_service.py MODEL_CONFIG:

MODEL_CONFIG = {
    'default': {
        'provider': 'openai',  # <-- Change this
        'model': 'gpt-4',      # <-- Change this
        'temperature': 0.7,
        'max_tokens': 2048
    },
    # ... rest of config
}

2. Add OpenAI API key to Railway:
   OPENAI_API_KEY=your-key-here

3. Redeploy:
   railway up

That's it! All AI calls now use GPT-4 instead of Gemini.
"""

# ============================================================================
# ERROR HANDLING BEST PRACTICES
# ============================================================================

@app.route('/api/safe-ai-call', methods=['POST'])
def safe_ai_call():
    """Example with proper error handling"""
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        
        result = call_ai('default', prompt)
        
        if not result['success']:
            # Log error for debugging
            print(f"AI Service Error: {result['error']}")
            
            # Return user-friendly error
            return jsonify({
                'success': False,
                'error': 'AI service temporarily unavailable. Please try again.',
                'details': result['error']  # Optional: remove in production
            }), 503
        
        return jsonify({
            'success': True,
            'response': result['response']
        })
        
    except Exception as e:
        print(f"Unexpected error in AI route: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'An unexpected error occurred'
        }), 500

# ============================================================================
# TESTING THE SERVICE
# ============================================================================

@app.route('/api/test-ai', methods=['GET'])
def test_ai_service():
    """Quick test endpoint to verify AI service is working"""
    result = call_ai('default', 'Say "AI service is working!" and nothing else.')
    
    return jsonify({
        'service_status': 'working' if result['success'] else 'error',
        'response': result.get('response'),
        'error': result.get('error'),
        'config': {
            'gemini_configured': bool(os.environ.get('GEMINI_API_KEY')),
            'openai_configured': bool(os.environ.get('OPENAI_API_KEY')),
            'anthropic_configured': bool(os.environ.get('ANTHROPIC_API_KEY'))
        }
    })
