#!/usr/bin/env python3
"""
Favicon Set Generator
Creates full favicon package from logo
"""

from PIL import Image
import os

# Configuration
INPUT_LOGO = "generated_logos/main_logo_dalle.png"  # Default input
OUTPUT_DIR = "favicon_package"

# Standard favicon sizes
FAVICON_SIZES = {
    "favicon-16x16.png": (16, 16),
    "favicon-32x32.png": (32, 32),
    "favicon-48x48.png": (48, 48),
    "apple-touch-icon.png": (180, 180),
    "android-chrome-192x192.png": (192, 192),
    "android-chrome-512x512.png": (512, 512),
    "mstile-150x150.png": (150, 150),
}

def find_input_logo():
    """Find a suitable logo file"""
    possible_paths = [
        "generated_logos/main_logo_dalle.png",
        "generated_logos/main_logo_stability.png",
        "static/logo.png",
        "static/logo.svg",
        "logo.png",
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None

def generate_favicons(input_path=None):
    """Generate all favicon sizes from logo"""
    
    # Find input file
    if input_path is None:
        input_path = find_input_logo()
    
    if not input_path or not os.path.exists(input_path):
        print("❌ Logo file not found!")
        print("Please provide a logo file (PNG, 512x512 or larger recommended)")
        print("\nSearched locations:")
        print("  - generated_logos/main_logo_dalle.png")
        print("  - generated_logos/main_logo_stability.png")
        print("  - static/logo.png")
        print("  - logo.png")
        return False
    
    print(f"✅ Using logo: {input_path}")
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    try:
        # Open logo
        with Image.open(input_path) as img:
            print(f"📐 Original size: {img.size}")
            
            # Convert to RGBA if needed
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Generate each favicon size
            for filename, size in FAVICON_SIZES.items():
                # Resize with high quality
                resized = img.resize(size, Image.Resampling.LANCZOS)
                
                # Save
                filepath = os.path.join(OUTPUT_DIR, filename)
                resized.save(filepath, "PNG", optimize=True)
                print(f"✅ {filename} ({size[0]}x{size[1]})")
            
            # Generate ICO file (multi-size for Windows)
            ico_sizes = [(16, 16), (32, 32), (48, 48)]
            ico_images = []
            
            for size in ico_sizes:
                ico_img = img.resize(size, Image.Resampling.LANCZOS)
                # Convert to RGB for ICO (no transparency issues)
                if ico_img.mode == 'RGBA':
                    # Create white background
                    background = Image.new('RGB', size, (255, 255, 255))
                    background.paste(ico_img, mask=ico_img.split()[-1])
                    ico_img = background
                ico_images.append(ico_img)
            
            ico_path = os.path.join(OUTPUT_DIR, "favicon.ico")
            ico_images[0].save(
                ico_path, 
                format='ICO', 
                sizes=ico_sizes,
                optimize=True
            )
            print(f"✅ favicon.ico (16x16, 32x32, 48x48)")
            
            # Generate site.webmanifest for PWA
            manifest = '''{
  "name": "FlowCast",
  "short_name": "FlowCast",
  "icons": [
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#6366F1",
  "background_color": "#0F172A",
  "display": "standalone"
}'''
            
            manifest_path = os.path.join(OUTPUT_DIR, "site.webmanifest")
            with open(manifest_path, 'w') as f:
                f.write(manifest)
            print(f"✅ site.webmanifest")
            
            # Generate HTML snippet
            html_snippet = '''<!-- Favicons -->
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#6366F1">'''
            
            html_path = os.path.join(OUTPUT_DIR, "favicon_html_snippet.txt")
            with open(html_path, 'w') as f:
                f.write(html_snippet)
            print(f"✅ favicon_html_snippet.txt")
        
        print("\n" + "="*50)
        print("✅ Favicon generation complete!")
        print(f"📁 All files saved to: {OUTPUT_DIR}/")
        print("="*50)
        
        # List all generated files
        files = sorted(os.listdir(OUTPUT_DIR))
        print("\nGenerated files:")
        for filename in files:
            filepath = os.path.join(OUTPUT_DIR, filename)
            size = os.path.getsize(filepath)
            print(f"  - {filename} ({size/1024:.1f} KB)")
        
        print(f"\n💡 Copy these files to your static/ folder")
        print(f"💡 Add the HTML snippet to your <head> section")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    # Allow custom input file
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    
    generate_favicons(input_file)
