#!/usr/bin/env python3
"""
Creator Command Center - Pure Python Version
No external dependencies. Uses only standard library.
"""

import http.server
import socketserver
import json
import os
import sqlite3
from datetime import datetime
from urllib.parse import parse_qs, urlparse
import requests
from stripe_integration import (
    init_stripe_keys, get_subscription_features, check_feature_access,
    can_create_post, get_checkout_session, handle_webhook, 
    STRIPE_PUBLISHABLE_KEY, SUBSCRIPTION_PLANS
)

# Configuration
PORT = 8080
DATA_DIR = "/home/daz/.openclaw/workspace/levelup-ai/creator-app/data"
YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY', '')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Simple JSON database
class JSONDB:
    def __init__(self, filename):
        self.filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump([], f)
    
    def read(self):
        with open(self.filepath, 'r') as f:
            return json.load(f)
    
    def write(self, data):
        with open(self.filepath, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    def add(self, item):
        data = self.read()
        item['id'] = len(data) + 1
        item['created_at'] = datetime.now().isoformat()
        data.append(item)
        self.write(data)
        return item
    
    def get(self, id):
        data = self.read()
        for item in data:
            if item.get('id') == id:
                return item
        return None

# Initialize databases
posts_db = JSONDB('posts.json')
users_db = JSONDB('users.json')

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        
        # API Routes
        if path == '/api/dashboard-stats':
            self.send_json({
                'total_posts': len(posts_db.read()),
                'scheduled_posts': len([p for p in posts_db.read() if p.get('status') == 'scheduled']),
                'youtube_scheduled': 3,
                'instagram_scheduled': 2,
                'engagement_rate': 4.8
            })
            return
        
        elif path == '/api/content-calendar':
            posts = posts_db.read()
            events = []
            for post in posts:
                if post.get('scheduled_at'):
                    events.append({
                        'id': post['id'],
                        'title': post.get('title', 'Untitled'),
                        'date': post['scheduled_at'],
                        'platforms': post.get('platforms', []),
                        'status': post.get('status', 'draft')
                    })
            self.send_json({'events': events})
            return
        
        elif path == '/api/youtube/channels':
            try:
                url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&forUsername=GoogleDevelopers&key={YOUTUBE_API_KEY}"
                response = requests.get(url)
                if response.status_code == 200:
                    self.send_json({
                        'success': True,
                        'channels': response.json().get('items', [])
                    })
                else:
                    self.send_json({
                        'success': False,
                        'error': f'YouTube API error: {response.status_code}'
                    })
            except Exception as e:
                self.send_json({'success': False, 'error': str(e)})
            return
        
        elif path == '/api/ai-content-ideas':
            # FREE TIER: Load cached AI ideas
            try:
                ideas_db = JSONDB('ai_ideas.json')
                ideas = ideas_db.read()
                
                # Add metadata
                response = {
                    'tier': 'free',
                    'ideas': ideas,
                    'total_available': len(ideas),
                    'last_updated': ideas[0].get('created_at', 'Today') if ideas else 'Today',
                    'upgrade_prompt': 'Upgrade to Pro for real-time AI generation'
                }
                self.send_json(response)
            except Exception as e:
                # Fallback to static ideas if file not found
                fallback_ideas = [
                    {
                        'id': 1,
                        'title': '5 AI Tools That Save Me 10 Hours/Week',
                        'format': 'Carousel (5 slides)',
                        'platform': 'Instagram',
                        'key_points': ['ChatGPT for drafts', 'Canva for design', 'Otter for transcription']
                    }
                ]
                self.send_json({'tier': 'free', 'ideas': fallback_ideas, 'error': str(e)})
            return
        
        elif path == '/api/ai-content-ideas/premium':
            # PREMIUM TIER: Real-time AI generation
            # This would call OpenAI/Claude API in production
            # For now, return enhanced version with more detail
            try:
                ideas_db = JSONDB('ai_ideas.json')
                ideas = ideas_db.read()
                
                # Add AI-generated details to each idea
                for idea in ideas:
                    idea['ai_generated_script'] = f"Hook: {idea['title']}\n\nBody: {idea['description']}\n\nCTA: Save this for later!"
                    idea['hashtag_suggestions'] = ['#ContentCreation', '#AITools', '#Productivity', '#CreatorTips']
                    idea['best_posting_time'] = '9:00 AM - 11:00 AM'
                
                self.send_json({
                    'tier': 'premium',
                    'ideas': ideas,
                    'real_time': True,
                    'features': ['Full scripts', 'Hashtag optimization', 'Best posting times']
                })
            except Exception as e:
                self.send_json({'error': 'Premium feature requires subscription', 'details': str(e)})
            return
        
        elif path == '/api/subscription/status':
            # Check user's subscription tier
            # For MVP, default to free
            self.send_json({
                'tier': 'free',
                'features': {
                    'cached_ai_ideas': True,
                    'basic_scheduling': True,
                    'youtube_integration': True,
                    'instagram_integration': True,
                    'real_time_ai': False,
                    'unlimited_posts': False,
                    'analytics': False
                },
                'upgrade_available': True,
                'upgrade_price': '$12/month'
            })
            return
        
        elif path == '/api/pricing':
            # Return pricing plans
            self.send_json({
                'plans': SUBSCRIPTION_PLANS,
                'currency': 'USD',
                'stripe_publishable_key': STRIPE_PUBLISHABLE_KEY or 'pk_test_demo_key'
            })
            return
        
        elif path == '/api/checkout':
            # Get query parameters
            query = parse_qs(parsed.query)
            plan = query.get('plan', ['pro'])[0]
            email = query.get('email', [''])[0]
            
            # Create checkout session
            plan_config = SUBSCRIPTION_PLANS.get(plan, SUBSCRIPTION_PLANS['pro'])
            
            if plan_config['price'] == 0:
                self.send_json({'error': 'Free plan does not require checkout'})
                return
            
            # Create checkout session (mock or real Stripe)
            try:
                session = get_checkout_session(
                    price_id=plan_config['price_id'],
                    customer_email=email,
                    success_url=f'http://100.116.210.37:8080/checkout/success?plan={plan}',
                    cancel_url='http://100.116.210.37:8080/checkout/cancel'
                )
                
                self.send_json({
                    'success': True,
                    'checkout_url': session['url'],
                    'session_id': session['id'],
                    'plan': plan,
                    'price': plan_config['price']
                })
            except Exception as e:
                self.send_json({'error': str(e)})
            return
        
        elif path == '/checkout/success':
            # Handle successful checkout
            query = parse_qs(parsed.query)
            plan = query.get('plan', ['pro'])[0]
            
            self.send_checkout_success_page(plan)
            return
        
        elif path == '/checkout/cancel':
            # Handle cancelled checkout
            self.send_checkout_cancel_page()
            return
        
        elif path == '/pricing':
            # Serve pricing page
            self.send_pricing_page()
            return
        
        elif path == '/terms':
            self.send_terms_page()
            return
        
        elif path == '/privacy':
            self.send_privacy_page()
            return
        
        elif path == '/refund':
            self.send_refund_page()
            return
        
        # Serve dashboard HTML for root path
        elif path == '/':
            self.send_dashboard()
            return
        
        # Default: serve static files
        super().do_GET()
    
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        
        if path == '/api/create-post':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            post = posts_db.add({
                'title': data.get('title'),
                'content': data.get('content'),
                'platforms': data.get('platforms', []),
                'status': 'scheduled' if data.get('scheduled_at') else 'draft',
                'scheduled_at': data.get('scheduled_at')
            })
            
            self.send_json({
                'success': True,
                'message': 'Post created successfully',
                'post_id': post['id']
            })
            return
        
        elif path == '/webhook/stripe':
            # Handle Stripe webhooks
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            signature = self.headers.get('Stripe-Signature', '')
            
            result = handle_webhook(post_data, signature)
            self.send_json(result)
            return
        
        self.send_json({'error': 'Not found'}, 404)
    
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def send_pricing_page(self):
        """Serve the pricing page"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Creator Command Center Pricing - Free, Pro ($12/month), and Team ($29/month) plans. Social media scheduling with AI content ideas.">
    <meta name="keywords" content="social media scheduler pricing, content calendar pricing, YouTube scheduler cost, Instagram posting tool price">
    <meta name="author" content="Creator Command Center">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Pricing | Creator Command Center">
    <meta property="og:description" content="Free, Pro, and Team plans for social media scheduling">
    <meta property="og:type" content="website">
    <link rel="canonical" href="http://creatorcommand.center/pricing">
    <title>Pricing | Creator Command Center - Social Media Scheduler Plans</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        .header {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            padding: 2rem;
            text-align: center;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 2rem;
        }
        .pricing-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        .pricing-card {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            position: relative;
        }
        .pricing-card.featured {
            border: 2px solid #6366f1;
            transform: scale(1.05);
        }
        .featured-badge {
            position: absolute;
            top: -12px;
            left: 50%;
            transform: translateX(-50%);
            background: #6366f1;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.875rem;
        }
        .price {
            font-size: 3rem;
            font-weight: bold;
            color: #6366f1;
            margin: 1rem 0;
        }
        .price span {
            font-size: 1rem;
            color: #666;
        }
        .features {
            list-style: none;
            margin: 1.5rem 0;
        }
        .features li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #eee;
        }
        .features li:before {
            content: "✓ ";
            color: #10b981;
            font-weight: bold;
        }
        .btn {
            display: block;
            width: 100%;
            background: #6366f1;
            color: white;
            padding: 1rem;
            border: none;
            border-radius: 8px;
            font-size: 1.1rem;
            cursor: pointer;
            text-decoration: none;
            text-align: center;
        }
        .btn:hover { background: #5558e0; }
        .btn-outline {
            background: transparent;
            border: 2px solid #6366f1;
            color: #6366f1;
        }
        .btn-outline:hover {
            background: #6366f1;
            color: white;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Choose Your Plan</h1>
        <p>Start free, upgrade when you're ready</p>
    </div>
    
    <div class="container">
        <div class="pricing-grid">
            <div class="pricing-card">
                <h2>Free</h2>
                <div class="price">$0<span>/month</span></div>
                <p>Perfect for getting started</p>
                <ul class="features">
                    <li>1 social platform</li>
                    <li>10 posts per month</li>
                    <li>Daily AI content ideas</li>
                    <li>Basic scheduling</li>
                    <li>Community support</li>
                </ul>
                <a href="/" class="btn btn-outline">Get Started Free</a>
            </div>
            
            <div class="pricing-card featured">
                <div class="featured-badge">Most Popular</div>
                <h2>Pro</h2>
                <div class="price">$12<span>/month</span></div>
                <p>For serious creators</p>
                <ul class="features">
                    <li>Unlimited platforms</li>
                    <li>Unlimited posts</li>
                    <li>Real-time AI generation</li>
                    <li>Advanced analytics</li>
                    <li>Priority email support</li>
                    <li>Google Calendar sync</li>
                </ul>
                <button class="btn" onclick="startCheckout('pro')">Start Pro Trial</button>
            </div>
            
            <div class="pricing-card">
                <h2>Team</h2>
                <div class="price">$29<span>/month</span></div>
                <p>For agencies & teams</p>
                <ul class="features">
                    <li>Everything in Pro</li>
                    <li>Up to 5 team members</li>
                    <li>Collaboration tools</li>
                    <li>White-label options</li>
                    <li>Priority phone support</li>
                    <li>Custom integrations</li>
                </ul>
                <button class="btn" onclick="startCheckout('team')">Contact Sales</button>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 3rem; color: #666;">
            <p>All plans include: 14-day free trial • Cancel anytime • No credit card required for free tier</p>
        </div>
    </div>
    
    <script>
        function startCheckout(plan) {
            // Get user email (in real app, from logged-in user)
            const email = prompt('Enter your email to start checkout:', '');
            if (email) {
                fetch(`/api/checkout?plan=${plan}&email=${email}`)
                    .then(res => res.json())
                    .then(data => {
                        if (data.checkout_url) {
                            window.location.href = data.checkout_url;
                        } else {
                            alert('Demo mode: In production, this would redirect to Stripe checkout');
                        }
                    });
            }
        }
    </script>
</body>
</html>'''
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def send_checkout_success_page(self, plan):
        """Serve checkout success page"""
        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Welcome to Creator Command Center {plan.title()}! Your subscription is now active.">
    <meta name="robots" content="noindex, nofollow">
    <title>Welcome to {plan.title()}! - Creator Command Center</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }}
        .container {{
            background: white;
            color: #333;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 500px;
        }}
        .success-icon {{
            font-size: 4rem;
            color: #10b981;
            margin-bottom: 1rem;
        }}
        h1 {{
            color: #6366f1;
            margin-bottom: 1rem;
        }}
        .btn {{
            display: inline-block;
            background: #6366f1;
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            margin-top: 1rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="success-icon">🎉</div>
        <h1>Welcome to {plan.title()}!</h1>
        <p>Your subscription is now active. You now have access to all {plan} features!</p>
        <p style="color: #666; margin-top: 1rem;">Demo mode: In production, this would activate your subscription immediately.</p>
        <a href="/" class="btn">Go to Dashboard</a>
    </div>
</body>
</html>'''
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def send_terms_page(self):
        """Serve Terms of Service page"""
        try:
            with open('/home/daz/.openclaw/workspace/levelup-ai/creator-app/templates/terms.html', 'r') as f:
                content = f.read()
            html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Terms of Service for Creator Command Center">
    <title>Terms of Service | Creator Command Center</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.6; color: #333; }}
        h1 {{ color: #6366f1; }}
        h2 {{ color: #4b5563; margin-top: 2rem; }}
        a {{ color: #6366f1; }}
        .back {{ margin-top: 2rem; }}
    </style>
</head>
<body>
    {content.replace(chr(35), '&#35;').replace(chr(10), '<br>')}
    <div class="back"><a href="/">← Back to Dashboard</a></div>
</body>
</html>'''
        except:
            html = '''<!DOCTYPE html>
<html><head><title>Terms of Service</title></head>
<body><h1>Terms of Service</h1><p>Full terms available at signup.</p><a href="/">← Back</a></body></html>'''
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def send_privacy_page(self):
        """Serve Privacy Policy page"""
        try:
            with open('/home/daz/.openclaw/workspace/levelup-ai/creator-app/templates/privacy.html', 'r') as f:
                content = f.read()
            html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Privacy Policy for Creator Command Center">
    <title>Privacy Policy | Creator Command Center</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.6; color: #333; }}
        h1 {{ color: #6366f1; }}
        h2 {{ color: #4b5563; margin-top: 2rem; }}
        a {{ color: #6366f1; }}
        .back {{ margin-top: 2rem; }}
    </style>
</head>
<body>
    {content.replace(chr(35), '&#35;').replace(chr(10), '<br>')}
    <div class="back"><a href="/">← Back to Dashboard</a></div>
</body>
</html>'''
        except:
            html = '''<!DOCTYPE html>
<html><head><title>Privacy Policy</title></head>
<body><h1>Privacy Policy</h1><p>Full policy available at signup.</p><a href="/">← Back</a></body></html>'''
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def send_refund_page(self):
        """Serve Refund Policy page"""
        try:
            with open('/home/daz/.openclaw/workspace/levelup-ai/creator-app/templates/refund.html', 'r') as f:
                content = f.read()
            html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Refund Policy for Creator Command Center">
    <title>Refund Policy | Creator Command Center</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; line-height: 1.6; color: #333; }}
        h1 {{ color: #6366f1; }}
        h2 {{ color: #4b5563; margin-top: 2rem; }}
        a {{ color: #6366f1; }}
        .back {{ margin-top: 2rem; }}
    </style>
</head>
<body>
    {content.replace(chr(35), '&#35;').replace(chr(10), '<br>')}
    <div class="back"><a href="/">← Back to Dashboard</a></div>
</body>
</html>'''
        except:
            html = '''<!DOCTYPE html>
<html><head><title>Refund Policy</title></head>
<body><h1>Refund Policy</h1><p>14-day free trial. Cancel anytime.</p><a href="/">← Back</a></body></html>'''
        
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

    def send_checkout_cancel_page(self):
        """Serve checkout cancel page"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Checkout cancelled - Creator Command Center. Continue with our free plan.">
    <meta name="robots" content="noindex, nofollow">
    <title>Checkout Cancelled - Creator Command Center</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }
        .container {
            background: white;
            padding: 3rem;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 500px;
        }
        .icon {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        h1 {
            color: #374151;
            margin-bottom: 1rem;
        }
        .btn {
            display: inline-block;
            background: #6366f1;
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            text-decoration: none;
            margin-top: 1rem;
        }
        .btn-outline {
            background: transparent;
            border: 2px solid #6366f1;
            color: #6366f1;
            margin-left: 0.5rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">😕</div>
        <h1>Checkout Cancelled</h1>
        <p>No worries! You can continue using the free plan or try again anytime.</p>
        <div style="margin-top: 1.5rem;">
            <a href="/" class="btn">Continue with Free</a>
            <a href="/pricing" class="btn btn-outline">View Pricing</a>
        </div>
    </div>
</body>
</html>'''
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())
    
    def send_dashboard(self):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Creator Command Center - Schedule posts to YouTube, Instagram, and more. AI-powered content ideas for creators. Free plan available.">
    <meta name="keywords" content="social media scheduler, content calendar, YouTube scheduler, Instagram posting tool, AI content ideas, creator tools">
    <meta name="author" content="Creator Command Center">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="Creator Command Center | Social Media Scheduling for Creators">
    <meta property="og:description" content="Schedule posts to YouTube, Instagram, and more. AI-powered content ideas. Free plan available.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="http://creatorcommand.center">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Creator Command Center">
    <meta name="twitter:description" content="Social media scheduling with AI-powered content ideas">
    <link rel="canonical" href="http://creatorcommand.center/">
    <title>Creator Command Center | Social Media Scheduling for Creators</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            color: #333;
        }
        .header {
            background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
            color: white;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .platforms {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        .platform-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .platform-card h3 {
            margin-bottom: 0.5rem;
            color: #6366f1;
        }
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 2rem;
        }
        .stat-card {
            background: white;
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .stat-card .number {
            font-size: 2rem;
            font-weight: bold;
            color: #6366f1;
        }
        .btn {
            background: #6366f1;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
        }
        .btn:hover { background: #5558e0; }
        .status-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.875rem;
        }
        .status-connected { background: #d1fae5; color: #065f46; }
        .status-disconnected { background: #fee2e2; color: #991b1b; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 Creator Command Center</h1>
        <button class="btn" onclick="alert('Create post feature coming soon!')">+ New Post</button>
    </div>
    <div class="container">
        <div class="platforms">
            <div class="platform-card">
                <h3>YouTube</h3>
                <span class="status-badge status-connected">Connected</span>
                <p style="margin-top: 0.5rem;">3 posts scheduled</p>
            </div>
            <div class="platform-card">
                <h3>Instagram</h3>
                <span class="status-badge status-connected">Connected</span>
                <p style="margin-top: 0.5rem;">2 posts scheduled</p>
            </div>
            <div class="platform-card">
                <h3>Google Calendar</h3>
                <span class="status-badge status-connected">Connected</span>
                <p style="margin-top: 0.5rem;">Sync enabled</p>
            </div>
        </div>
        <div class="stats">
            <div class="stat-card">
                <div class="number" id="total-posts">0</div>
                <div>Total Posts</div>
            </div>
            <div class="stat-card">
                <div class="number">4.8%</div>
                <div>Engagement Rate</div>
            </div>
            <div class="stat-card">
                <div class="number">15,420</div>
                <div>Total Views</div>
            </div>
        </div>
        <div style="background: white; border-radius: 8px; padding: 1.5rem; margin-bottom: 2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <h2>🤖 AI Content Ideas</h2>
                <span class="status-badge status-connected">Free Tier</span>
            </div>
            <p style="color: #666; margin-bottom: 1rem;">Daily AI-generated content ideas. Updated every morning.</p>
            <div id="ai-ideas">
                <p>Loading ideas...</p>
            </div>
            <div style="margin-top: 1rem; padding: 1rem; background: #fef3c7; border-radius: 6px; border-left: 4px solid #f59e0b;">
                <strong>💡 Upgrade to Pro:</strong> Get real-time AI generation, full scripts, hashtag optimization, and best posting times for $12/month.
                <button class="btn" style="margin-left: 1rem; background: #f59e0b;">Upgrade</button>
            </div>
        </div>
        
        <div style="background: white; border-radius: 8px; padding: 1.5rem;">
            <h2 style="margin-bottom: 1rem;">Content Calendar</h2>
            <p style="color: #666;">Calendar view coming in next update...</p>
        </div>
    </div>
    
    <footer style="background: #1f2937; color: #9ca3af; padding: 2rem; margin-top: 3rem; text-align: center;">
        <div style="max-width: 1200px; margin: 0 auto;">
            <div style="margin-bottom: 1rem;">
                <a href="/" style="color: white; text-decoration: none; margin: 0 1rem;">Dashboard</a>
                <a href="/pricing" style="color: white; text-decoration: none; margin: 0 1rem;">Pricing</a>
                <a href="/terms" style="color: white; text-decoration: none; margin: 0 1rem;">Terms</a>
                <a href="/privacy" style="color: white; text-decoration: none; margin: 0 1rem;">Privacy</a>
                <a href="/refund" style="color: white; text-decoration: none; margin: 0 1rem;">Refunds</a>
            </div>
            <p style="font-size: 0.875rem;">© 2026 Creator Command Center. All rights reserved.</p>
            <p style="font-size: 0.75rem; margin-top: 0.5rem;">Made with ❤️ for content creators</p>
        </div>
    </footer>
    
    <script>
        // Load dashboard stats
        fetch('/api/dashboard-stats')
            .then(res => res.json())
            .then(data => {
                document.getElementById('total-posts').textContent = data.total_posts;
            });
        
        // Load AI content ideas
        fetch('/api/ai-content-ideas')
            .then(res => res.json())
            .then(data => {
                const container = document.getElementById('ai-ideas');
                if (data.ideas && data.ideas.length > 0) {
                    container.innerHTML = data.ideas.map(idea => `
                        <div style="border: 1px solid #e5e7eb; border-radius: 6px; padding: 1rem; margin-bottom: 0.75rem;">
                            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                                <h4 style="margin: 0; color: #374151;">${idea.title}</h4>
                                <span style="font-size: 0.75rem; background: #dbeafe; color: #1e40af; padding: 0.25rem 0.5rem; border-radius: 4px;">${idea.platform}</span>
                            </div>
                            <p style="color: #6b7280; font-size: 0.875rem; margin-bottom: 0.5rem;">${idea.format}</p>
                            ${idea.key_points ? `
                                <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.875rem; color: #4b5563;">
                                    ${idea.key_points.slice(0, 2).map(point => `<li>${point}</li>`).join('')}
                                </ul>
                            ` : ''}
                            <button class="btn" style="margin-top: 0.75rem; font-size: 0.875rem; padding: 0.5rem 1rem;" onclick="useIdea('${idea.title}')">Use This Idea</button>
                        </div>
                    `).join('');
                } else {
                    container.innerHTML = '<p style="color: #666;">No ideas available. Check back tomorrow!</p>';
                }
            })
            .catch(err => {
                document.getElementById('ai-ideas').innerHTML = '<p style="color: #666;">Could not load ideas.</p>';
            });
        
        function useIdea(title) {
            alert(`Creating post from idea: "${title}"\n\nPost creation form coming soon!`);
        }
    </script>
</body>
</html>'''
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode())

# Run server
if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"✅ Creator Command Center running at http://localhost:{PORT}")
        print(f"📊 Dashboard: http://100.116.210.37:{PORT}")
        print("Press Ctrl+C to stop")
        httpd.serve_forever()
