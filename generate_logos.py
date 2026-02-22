#!/usr/bin/env python3
"""
FlowCast Logo Generator
Generates logos using multiple AI providers
"""

import os
import requests
from pathlib import Path

# Configuration
OUTPUT_DIR = "generated_logos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Optimized prompts for FlowCast
LOGO_PROMPTS = {
    "main_logo": """
Minimalist modern logo for "FlowCast", a social media content scheduler app. 
Abstract flowing waves or signal lines emanating from a central point, suggesting 
broadcasting and content flow. Color palette: deep purple (#6366F1) to pink (#EC4899) 
gradient on dark navy background. Clean geometric shapes, flat design, vector style. 
Professional, trustworthy, innovative. Transparent background, centered composition.
""",
    
    "app_icon": """
Simple app icon for "FlowCast". Circular badge with wave/signal symbol inside. 
Purple to pink gradient. Minimalist, flat design, iOS app icon style. No text, 
purely symbolic. Clean lines, geometric shapes. Dark background.
""",
    
    "monogram": """
Modern lettermark "F" logo for tech startup "FlowCast". The letter F formed by 
flowing curved lines that become broadcast signal waves. Purple (#6366F1) to 
pink (#EC4899) gradient. Tech aesthetic, clean, bold. Dark background, vector style.
""",
    
    "favicon": """
Tiny 32x32 pixel favicon for "FlowCast". Simplified wave or signal icon. 
Purple gradient. Extremely minimal, readable at small size. Dark background. 
Single color icon style.
"""
}

def generate_with_dalle(prompt, size="1024x1024", filename="logo.png"):
    """Generate logo using DALL-E 3"""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not set")
        return None
    
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "size": size,
        "quality": "standard",
        "n": 1
    }
    
    try:
        print(f"🎨 Generating with DALL-E: {filename}")
        response = requests.post(url, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        
        # Download image
        image_url = result['data'][0]['url']
        img_response = requests.get(image_url, timeout=30)
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(img_response.content)
        
        print(f"✅ Generated: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error with DALL-E: {e}")
        return None

def generate_with_stability(prompt, filename="logo.png"):
    """Generate logo using Stability AI (cheaper alternative)"""
    api_key = os.environ.get('STABILITY_API_KEY')
    if not api_key:
        print("❌ STABILITY_API_KEY not set")
        return None
    
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "authorization": api_key,
        "accept": "image/*"
    }
    
    files = {
        "prompt": (None, prompt),
        "aspect_ratio": (None, "1:1"),
        "model": (None, "sd3-large"),
        "output_format": (None, "png")
    }
    
    try:
        print(f"🎨 Generating with Stability AI: {filename}")
        response = requests.post(url, headers=headers, files=files, timeout=60)
        response.raise_for_status()
        
        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"✅ Generated: {filepath}")
        return filepath
    except Exception as e:
        print(f"❌ Error with Stability: {e}")
        return None

def generate_all_logos():
    """Generate complete logo set"""
    print("🎨 FlowCast Logo Generation Pipeline")
    print("=" * 50)
    
    providers = []
    if os.environ.get('OPENAI_API_KEY'):
        providers.append('dalle')
    if os.environ.get('STABILITY_API_KEY'):
        providers.append('stability')
    
    if not providers:
        print("\n❌ No AI providers configured!")
        print("Set one of these environment variables:")
        print("  - OPENAI_API_KEY (for DALL-E 3)")
        print("  - STABILITY_API_KEY (for Stable Diffusion)")
        print("\nOr use the manual prompts in LOGO-GENERATION-GUIDE.md")
        return
    
    print(f"\n✓ Available providers: {', '.join(providers)}")
    
    for name, prompt in LOGO_PROMPTS.items():
        print(f"\n{'='*50}")
        print(f"Generating: {name}")
        print('='*50)
        
        # Try DALL-E first (better quality)
        if 'dalle' in providers:
            generate_with_dalle(prompt, filename=f"{name}_dalle.png")
        
        # Try Stability as backup/cheaper alternative
        if 'stability' in providers:
            generate_with_stability(prompt, filename=f"{name}_stability.png")
    
    print("\n" + "="*50)
    print("✅ Generation complete!")
    print(f"📁 Check: {OUTPUT_DIR}/")
    print("="*50)
    
    # List generated files
    files = os.listdir(OUTPUT_DIR)
    if files:
        print("\nGenerated files:")
        for f in sorted(files):
            size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
            print(f"  - {f} ({size/1024:.1f} KB)")

if __name__ == "__main__":
    generate_all_logos()
