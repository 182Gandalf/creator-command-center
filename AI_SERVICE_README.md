# AI Service for FlowCast

## Quick Start

1. **Add your API keys to Railway:**
   ```
   # Choose which ones you want to use:
   GEMINI_API_KEY=your-google-ai-key
   MOONSHOT_API_KEY=your-moonshot-key  # For Kimi 2.5
   ANTHROPIC_API_KEY=your-anthropic-key  # For Claude
   OPENAI_API_KEY=your-openai-key  # For GPT-4
   ```

2. **Import and use in your code:**
   ```python
   from ai_service import call_ai, generate_content_ideas
   
   # Simple call
   result = call_ai('content_ideas', 'Give me YouTube video ideas about cooking')
   
   # Or use helper function
   ideas = generate_content_ideas('cooking', 'youtube', 5)
   ```

## Central Function: `call_ai(task_type, user_input, context)`

This is the ONE function that handles all AI calls.

### Parameters:
- `task_type`: What kind of AI task (content_ideas, caption_generation, etc.)
- `user_input`: The prompt or question
- `context`: Optional dict with extra info (user tier, platform, etc.)

### Returns:
```python
{
    'success': True/False,
    'response': 'AI generated text',
    'error': None or 'error message'
}
```

## Switching AI Models

To change which AI model handles a task, edit `MODEL_CONFIG` in `ai_service.py`:

```python
MODEL_CONFIG = {
    'content_ideas': {
        'provider': 'openai',      # Change from 'gemini' to 'openai'
        'model': 'gpt-4',          # Change model name
        'temperature': 0.7,
        'max_tokens': 2048
    }
}
```

Then add the API key to Railway:
```
OPENAI_API_KEY=your-openai-key
```

Redeploy: `railway up`

**Done!** All AI calls now use the new model automatically.

## Available Models

| Model | Provider | Key | Best For |
|-------|----------|-----|----------|
| **Gemini Flash** | `gemini` | `GEMINI_API_KEY` | Fast, cheap, good for most tasks |
| **Gemini Pro** | `gemini` | `GEMINI_API_KEY` | Higher quality, more tokens |
| **Kimi K2.5** | `moonshot` | `MOONSHOT_API_KEY` | Long context, great for analysis |
| **Claude Haiku** | `anthropic` | `ANTHROPIC_API_KEY` | Fast, cheap, simple tasks |
| **Claude Sonnet** | `anthropic` | `ANTHROPIC_API_KEY` | Better quality, reasoning |
| **GPT-4o Mini** | `openai` | `OPENAI_API_KEY` | Balanced performance |
| **GPT-4o** | `openai` | `OPENAI_API_KEY` | Best quality, most expensive |

### Example Configurations

**Use Kimi for everything:**
```python
'default': {
    'provider': 'moonshot',
    'model': 'kimi-k2.5',
    'temperature': 0.7,
    'max_tokens': 2048
}
```

**Use Claude Haiku for speed:**
```python
'default': {
    'provider': 'anthropic',
    'model': 'claude-3-haiku-20240307',
    'temperature': 0.7,
    'max_tokens': 2048
}
```

**Mix and match by task:**
```python
MODEL_CONFIG = {
    'default': {'provider': 'gemini', 'model': 'gemini-1.5-flash', ...},
    'premium_content': {'provider': 'anthropic', 'model': 'claude-3-sonnet-20240229', ...},
    'quick_tasks': {'provider': 'moonshot', 'model': 'kimi-k2.5', ...}
}
```

## Available Task Types

- `default` - General purpose
- `content_ideas` - Generate video/post ideas
- `caption_generation` - Write social media captions
- `hashtag_suggestions` - Suggest relevant hashtags
- `content_analysis` - Analyze post performance

## Helper Functions

### `generate_content_ideas(topic, platform, count)`
Returns list of idea dicts with title, hook, outline.

### `generate_caption(description, platform, tone)`
Returns a social media caption string.

### `suggest_hashtags(description, platform, count)`
Returns list of hashtag strings.

### `analyze_content_performance(data)`
Returns analysis dict with recommendations.

## Testing

Visit: `https://flowcast.space/api/test-ai`

Shows if AI service is configured and working.

## Adding New Task Types

1. Add entry to `MODEL_CONFIG` in `ai_service.py`:
   ```python
   'my_new_task': {
       'provider': 'gemini',
       'model': 'gemini-pro',
       'temperature': 0.5,
       'max_tokens': 1024
   }
   ```

2. Use it:
   ```python
   result = call_ai('my_new_task', 'Your prompt here')
   ```

That's it!
