# FlowCast AI Setup Guide
## Getting Your API Keys

---

## 1. Google Gemini API (FREE TIER - RECOMMENDED)

**Why Gemini?**
- 90% cheaper than GPT-3.5
- 1,500 free requests/day
- Excellent for social media content

### Step-by-Step:

1. **Go to Google AI Studio**
   - Visit: https://ai.google.dev
   - Sign in with your Google account

2. **Get API Key**
   - Click "Get API Key"
   - Click "Create API Key"
   - Select "Create API key in new project" (or existing)
   - Copy your key (starts with `AIzaSy...`)

3. **Set Environment Variable**
   ```bash
   export GEMINI_API_KEY='your-key-here'
   ```

4. **Verify it works**
   ```bash
   python3 -c "import os; print('Gemini:', 'Set' if os.getenv('GEMINI_API_KEY') else 'Missing')"
   ```

**Free Tier Limits:**
- 1,500 requests/day
- 1,000,000 tokens/day (generous!)
- Perfect for Free and Starter tiers

---

## 2. DeepSeek API (CHEAP & GOOD)

**Why DeepSeek?**
- 85% cheaper than GPT-3.5
- High quality (7.8/10)
- Good for Creator tier

### Step-by-Step:

1. **Create Account**
   - Visit: https://platform.deepseek.com
   - Sign up with email
   - Verify your account

2. **Get API Key**
   - Go to "API Keys" section
   - Click "Create new key"
   - Copy the key (starts with `sk-...`)

3. **Add Credit (Optional but recommended)**
   - DeepSeek gives some free credits initially
   - Add $5-10 for testing (lasts a long time)
   - Much cheaper than OpenAI

4. **Set Environment Variable**
   ```bash
   export DEEPSEEK_API_KEY='your-key-here'
   ```

**Pricing:**
- $0.14 per 1M input tokens
- $0.28 per 1M output tokens
- Example: 1,000 requests = ~$0.50

---

## 3. OpenAI API (OPTIONAL - PRO TIER)

**Why OpenAI?**
- Best quality (GPT-4)
- Use only for Pro tier
- Most expensive

### Step-by-Step:

1. **Create Account**
   - Visit: https://platform.openai.com
   - Sign up / Sign in

2. **Add Payment Method**
   - Go to "Billing"
   - Add credit card
   - Set usage limits (recommended: $50/month max)

3. **Get API Key**
   - Go to "API Keys"
   - Click "Create new secret key"
   - Copy immediately (can't see again!)

4. **Set Environment Variable**
   ```bash
   export OPENAI_API_KEY='your-key-here'
   ```

**Pricing:**
- GPT-3.5: $0.50 per 1M tokens (input)
- GPT-4: $30 per 1M tokens (input)
- Use sparingly!

---

## 4. Mistral API (OPTIONAL - EU FRIENDLY)

**Why Mistral?**
- European company (GDPR friendly)
- Good quality
- Alternative option

### Step-by-Step:

1. **Create Account**
   - Visit: https://console.mistral.ai
   - Sign up with email

2. **Get API Key**
   - Go to "API Keys"
   - Create new key
   - Copy the key

3. **Set Environment Variable**
   ```bash
   export MISTRAL_API_KEY='your-key-here'
   ```

---

## Quick Setup Script

Save this as `setup-ai-keys.sh`:

```bash
#!/bin/bash

echo "FlowCast AI API Key Setup"
echo "=========================="
echo ""

# Gemini (REQUIRED - Free tier)
read -p "Enter Gemini API Key (from https://ai.google.dev): " gemini_key
export GEMINI_API_KEY="$gemini_key"

# DeepSeek (OPTIONAL but recommended)
read -p "Enter DeepSeek API Key (or press Enter to skip): " deepseek_key
if [ ! -z "$deepseek_key" ]; then
    export DEEPSEEK_API_KEY="$deepseek_key"
fi

# OpenAI (OPTIONAL - for Pro tier)
read -p "Enter OpenAI API Key (or press Enter to skip): " openai_key
if [ ! -z "$openai_key" ]; then
    export OPENAI_API_KEY="$openai_key"
fi

echo ""
echo "Keys set for this session!"
echo "To make permanent, add these lines to ~/.bashrc or ~/.zshrc:"
echo ""
echo "export GEMINI_API_KEY='$gemini_key'"
if [ ! -z "$deepseek_key" ]; then
    echo "export DEEPSEEK_API_KEY='$deepseek_key'"
fi
if [ ! -z "$openai_key" ]; then
    echo "export OPENAI_API_KEY='$openai_key'"
fi
```

Make it executable:
```bash
chmod +x setup-ai-keys.sh
./setup-ai-keys.sh
```

---

## Testing Your Setup

Run this test script:

```bash
python3 ai_router.py
```

You should see output like:
```
AI Router Test
==================================================
Success: True
Model: fallback
Cached: False
Cost: $0.000000

Ideas:
1. 5 Secrets About fitness Nobody Talks About
   Revealing the hidden truths that will change...
2. How I Improved My fitness in 30 Days
   A personal journey with actionable tips...
3. The Biggest fitness Mistakes Beginners Make
   Avoid these common pitfalls and fast-track...

==================================================
Setup Instructions:
1. Get Gemini API key: https://ai.google.dev
2. Set environment variable: export GEMINI_API_KEY='your-key'
3. (Optional) Get DeepSeek key: https://platform.deepseek.com
4. (Optional) Get OpenAI key: https://platform.openai.com
```

---

## Cost Comparison at 1,000 Users

| Provider | Cost/Month | Use For |
|----------|-----------|---------|
| **Gemini** | $50 | Free + Starter tiers |
| **DeepSeek** | $100 | Creator tier |
| **OpenAI** | $500 | Pro tier only |
| **Total** | **$650** | vs $5,000 (pure OpenAI) |

**You save: $4,350/month (87%)**

---

## Railway Environment Variables

Add these in your Railway dashboard:

1. Go to: https://railway.app/dashboard
2. Select your FlowCast project
3. Click "Variables" tab
4. Add:
   - `GEMINI_API_KEY` = your-key
   - `DEEPSEEK_API_KEY` = your-key (optional)
   - `OPENAI_API_KEY` = your-key (optional)
5. Redeploy

---

## Troubleshooting

### "No API keys found"
- Make sure you set environment variables
- Run: `echo $GEMINI_API_KEY` to verify

### "API rate limit exceeded"
- Gemini: Wait 24 hours (free tier resets daily)
- DeepSeek: Add payment method for higher limits

### "Invalid API key"
- Double-check you copied the full key
- Regenerate if needed

### "Module not found"
- Install dependencies: `pip install requests`

---

## Security Best Practices

✅ DO:
- Store keys in environment variables
- Rotate keys every 90 days
- Set usage limits (especially OpenAI)
- Monitor API usage regularly

❌ DON'T:
- Never commit keys to Git
- Don't share keys in emails
- Don't hardcode keys in source code
- Don't expose keys in client-side code

---

## Next Steps

1. ✅ Get Gemini API key (free, 5 minutes)
2. ✅ Set environment variable
3. ✅ Test with `python3 ai_router.py`
4. ✅ (Optional) Get DeepSeek key for Creator tier
5. ✅ Add to Railway environment variables
6. ✅ Deploy and enjoy 90% cost savings!

---

**Questions?** Check the ai_router.py comments or ask for help!
