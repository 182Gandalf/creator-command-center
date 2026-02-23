# SSL/TLS Fixes for FlowCast

## Issue 1: Force HTTPS Redirect

**In Cloudflare Dashboard:**
1. Go to https://dash.cloudflare.com
2. Select your domain (flowcast.space)
3. Go to **SSL/TLS** → **Edge Certificates**
4. Find **"Always Use HTTPS"** toggle
5. **Enable it** ✅

This will automatically redirect all HTTP traffic to HTTPS.

**Alternative: Using Page Rules (if toggle doesn't work)**
1. Go to **Rules** → **Page Rules**
2. Create new rule:
   - URL: `http://*flowcast.space/*`
   - Setting: **Always Use HTTPS**
3. Save

---

## Issue 2: Disable TLS 1.0/1.1

**In Cloudflare Dashboard:**
1. Go to **SSL/TLS** → **Edge Certificates**
2. Scroll to **"Minimum TLS Version"**
3. Change from "TLS 1.0" to **"TLS 1.2"** ✅

This will disable TLS 1.0 and 1.1, leaving only TLS 1.2 and 1.3 enabled.

---

## Issue 3: Enable HSTS (Recommended)

**In Cloudflare Dashboard:**
1. Go to **SSL/TLS** → **Edge Certificates**
2. Find **"HTTP Strict Transport Security (HSTS)"**
3. Click **"Enable HSTS"**
4. Set:
   - Max Age: **6 months** (or 1 year)
   - Include subdomains: ✅
   - Preload: ✅
5. Save

This tells browsers to always use HTTPS for your domain.

---

## Summary of Cloudflare Settings

| Setting | Current | Recommended |
|---------|---------|-------------|
| SSL/TLS Mode | Flexible/Full | **Full (Strict)** |
| Always Use HTTPS | Off | **On** |
| Minimum TLS | TLS 1.0 | **TLS 1.2** |
| HSTS | Off | **On** |

---

## Verify After Changes

Test these commands after making changes:

```bash
# Test HTTP redirects to HTTPS
curl -I http://flowcast.space
# Should show: HTTP/1.1 301 Moved Permanently
#              Location: https://flowcast.space

# Test TLS version
echo | openssl s_client -connect flowcast.space:443 -tls1 2>&1 | grep Protocol
# Should fail (TLS 1.0 rejected)

echo | openssl s_client -connect flowcast.space:443 -tls1_2 2>&1 | grep Protocol
# Should work: Protocol : TLSv1.2
```

---

## Railway-Side Configuration (Optional)

If you want to enforce HTTPS at the application level, add this to your Flask app (`app.py`):

```python
@app.before_request
def enforce_https():
    """Redirect HTTP to HTTPS in production"""
    if not request.is_secure and not request.headers.get('X-Forwarded-Proto') == 'https':
        if request.headers.get('X-Forwarded-For'):  # Behind proxy (Cloudflare)
            url = request.url.replace('http://', 'https://', 1)
            return redirect(url, code=301)
```

However, Cloudflare's "Always Use HTTPS" is the cleaner solution.

---

## Check SSL Rating

After making changes, test at:
- https://www.ssllabs.com/ssltest/analyze.html?d=flowcast.space
- https://whynopadlock.com

Target: **A+ rating**
