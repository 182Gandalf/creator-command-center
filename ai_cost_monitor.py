# AI Token Usage Monitor
# Track and optimize AI API costs

import os
import json
from datetime import datetime, timedelta
from collections import defaultdict

class AICostMonitor:
    """Monitor and optimize AI API costs"""
    
    def __init__(self, log_file='instance/ai_usage.json'):
        self.log_file = log_file
        self.daily_budget = 5.0  # $5 USD daily budget
        self.usage = self._load_usage()
    
    def _load_usage(self):
        """Load usage history"""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return {
            'daily': {},
            'total_requests': 0,
            'total_cost_usd': 0,
            'by_tier': defaultdict(float),
            'by_model': defaultdict(float)
        }
    
    def log_request(self, model, tier, tokens_in, tokens_out, cost_usd):
        """Log an AI request"""
        today = datetime.now().strftime('%Y-%m-%d')
        
        if today not in self.usage['daily']:
            self.usage['daily'][today] = {
                'requests': 0,
                'cost_usd': 0,
                'tokens_in': 0,
                'tokens_out': 0
            }
        
        self.usage['daily'][today]['requests'] += 1
        self.usage['daily'][today]['cost_usd'] += cost_usd
        self.usage['daily'][today]['tokens_in'] += tokens_in
        self.usage['daily'][today]['tokens_out'] += tokens_out
        
        self.usage['total_requests'] += 1
        self.usage['total_cost_usd'] += cost_usd
        self.usage['by_tier'][tier] += cost_usd
        self.usage['by_model'][model] += cost_usd
        
        self._save_usage()
    
    def _save_usage(self):
        """Save usage to file"""
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)
        with open(self.log_file, 'w') as f:
            json.dump(self.usage, f, indent=2, default=str)
    
    def get_today_stats(self):
        """Get today's usage stats"""
        today = datetime.now().strftime('%Y-%m-%d')
        today_data = self.usage['daily'].get(today, {
            'requests': 0,
            'cost_usd': 0,
            'tokens_in': 0,
            'tokens_out': 0
        })
        
        budget_remaining = self.daily_budget - today_data['cost_usd']
        
        return {
            'date': today,
            'requests': today_data['requests'],
            'cost_usd': round(today_data['cost_usd'], 4),
            'tokens_in': today_data['tokens_in'],
            'tokens_out': today_data['tokens_out'],
            'budget_remaining': round(budget_remaining, 2),
            'budget_percent_used': round((today_data['cost_usd'] / self.daily_budget) * 100, 1)
        }
    
    def should_throttle(self, tier='free'):
        """Check if we should throttle requests to save costs"""
        stats = self.get_today_stats()
        
        # Throttle if over 80% of daily budget
        if stats['budget_percent_used'] > 80:
            return True
        
        # Throttle free tier more aggressively
        if tier == 'free' and stats['requests'] > 100:
            return True
        
        return False
    
    def get_optimization_suggestions(self):
        """Get cost optimization suggestions"""
        suggestions = []
        stats = self.get_today_stats()
        
        if stats['cost_usd'] > 3.0:
            suggestions.append("High daily spend - consider implementing stricter caching")
        
        if stats['requests'] > 500:
            suggestions.append("High request volume - increase cache TTL to reduce API calls")
        
        if self.usage['by_model'].get('gpt4', 0) > 1.0:
            suggestions.append("GPT-4 usage detected - route more traffic to cheaper Gemini/DeepSeek")
        
        if stats['budget_percent_used'] > 50:
            suggestions.append("Over 50% of daily budget used - monitor closely")
        
        return suggestions

# Global instance
monitor = AICostMonitor()

def track_ai_usage(func):
    """Decorator to track AI usage"""
    def wrapper(*args, **kwargs):
        # Get tier from kwargs
        tier = kwargs.get('user_tier', 'free')
        
        # Call function
        result = func(*args, **kwargs)
        
        # Track if successful
        if result and result.get('success'):
            model = result.get('model_used', 'unknown')
            cost = result.get('cost_usd', 0)
            tokens = result.get('tokens', 500)
            
            monitor.log_request(
                model=model,
                tier=tier,
                tokens_in=int(tokens * 0.6),  # Estimate
                tokens_out=int(tokens * 0.4),
                cost_usd=cost
            )
        
        return result
    return wrapper

if __name__ == "__main__":
    # Test
    print("AI Cost Monitor")
    print("=" * 50)
    print(f"Daily Budget: ${monitor.daily_budget}")
    print(f"Today's Usage:")
    stats = monitor.get_today_stats()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    suggestions = monitor.get_optimization_suggestions()
    if suggestions:
        print("\nOptimization Suggestions:")
        for s in suggestions:
            print(f"  - {s}")
