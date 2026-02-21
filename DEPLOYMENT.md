# Deployment Guide - FlowCast

## Recommended Hosting: Railway (Best Free Option)

### Why Railway:
- ✅ $5/month free credit (enough for small app)
- ✅ No credit card required to start
- ✅ Automatic HTTPS
- ✅ GitHub integration
- ✅ PostgreSQL included
- ✅ Custom domains
- ✅ 24/7 uptime

### Alternative Options:

| Platform | Free Tier | Best For | Limitations |
|----------|-----------|----------|-------------|
| **Railway** | $5 credit/month | Production SaaS | Credit runs out |
| **Render** | Always free | Side projects | Sleeps after 15min idle |
| **Fly.io** | $5 credit/month | Global edge | Complex setup |
| **Vercel** | Always free | Frontend only | No backend support |
| **PythonAnywhere** | Limited | Python only | Very limited free tier |

### Railway Setup Steps:

1. **Sign up:** https://railway.app (use GitHub)
2. **Create new project**
3. **Connect GitHub repo** (or upload code)
4. **Add PostgreSQL plugin** (for database)
5. **Set environment variables:**
   - YOUTUBE_API_KEY
   - STRIPE_SECRET_KEY (when ready)
   - DATABASE_URL (auto-generated)
6. **Deploy!**

### Environment Variables for Railway:

```bash
YOUTUBE_API_KEY=your_youtube_api_key_here
INSTAGRAM_APP_ID=your_instagram_app_id
INSTAGRAM_APP_SECRET=your_instagram_app_secret
STRIPE_PUBLISHABLE_KEY=pk_test_51T2yT2CqgkDJXcQzq2epuWvXqs50cUdGEYNYCmc4fGX8e51llMXhbWjED7tJ1wvVxcUIrPt72PTssDmVAZ7Lrsy900dgwP05Xv
PADDLE_API_KEY=your_paddle_key
DATABASE_URL=${{Postgres.DATABASE_URL}}
```

### Custom Domain (Free):
- Get free domain from: Freenom (dot.tk)
- Or use: DuckDNS (free subdomains)
- Railway provides: yourapp.railway.app (free)

---

## Current Server Status

**Problem:** Port 8080 blocked by firewall
**Solution:** Deploy to Railway for immediate public access
**Timeline:** 10 minutes to deploy

---

## Files Ready for Deployment

✅ `app_simple.py` - Main application
✅ `requirements.txt` - Dependencies  
✅ `templates/dashboard-new.html` - Modern UI
✅ `stripe_integration.py` - Payments
✅ `models.py` - Database models
✅ All API integrations configured

---

## Next Steps

1. **Create GitHub repo** (or I can create one)
2. **Push code to GitHub**
3. **Connect Railway to GitHub**
4. **Deploy automatically**
5. **Get custom domain**
6. **SSL certificate** (auto-provided)

**Want me to proceed with Railway deployment?**
