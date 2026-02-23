# SSL/HTTPS Troubleshooting Guide for FlowCast.space

## Current Status

### ✅ What's Working
- SSL certificate is valid (Let's Encrypt, expires May 23, 2026)
- HTTPS is active and serving content
- HTTP → HTTPS redirect is working (301 redirect)
- All resources loaded over HTTPS (fonts, images, links)
- Canonical URL is HTTPS
- Certificate covers both flowcast.space and *.flowcast.space

### ❌ What's Missing
- **HSTS Header** - Not enabled (see fix below)
- **TLS Version Enforcement** - Need to verify minimum TLS version

---

## Potential Causes of "Not Secure" Warning

### 1. Missing HSTS Header (Most Likely)

**The Issue:**
Without HTTP Strict Transport Security (HSTS), browsers don't automatically enforce HTTPS. Users can still access the site via HTTP bookmarks or by typing the URL without https://.

**Fix in Cloudflare:**
1. Go to https://dash.cloudflare.com
2. Select flowcast.space
3. Go to **SSL/TLS** → **Edge Certificates**
4. Scroll to **"HTTP Strict Transport Security (HSTS)"**
5. Click **"Enable HSTS"**
6. Set these values:
   - **Max Age:** 6 months (15768000 seconds)
   - **Include subdomains:** ✅ ON
   - **Preload:** ✅ ON
   - **No-Sniff:** ✅ ON
7. Save

**What HSTS does:**
- Tells browsers: "Always use HTTPS for this domain"
- Prevents downgrade attacks
- Gets your site on browser preload lists

---

### 2. TLS Version Issues

**Check Current TLS Support:**
```bash
# Check if TLS 1.0/1.1 are still enabled (they shouldn't be)
echo | openssl s_client -connect flowcast.space:443 -tls1 2>&1 | grep Protocol
# Should fail

echo | openssl s_client -connect flowcast.space:443 -tls1_2 2>&1 | grep Protocol  
# Should work (TLSv1.2)
```

**Fix in Cloudflare:**
1. Go to **SSL/TLS** → **Edge Certificates**
2. Find **"Minimum TLS Version"**
3. Set to **"TLS 1.2"** (or TLS 1.3)
4. Save

---

### 3. Mixed Content (Already Verified Good)

All resources on flowcast.space are loading over HTTPS:
- ✅ Fonts (Google Fonts via HTTPS)
- ✅ Images (relative URLs)
- ✅ Links (relative URLs)
- ✅ Canonical URL (HTTPS)
- ✅ Open Graph URLs (HTTPS)

---

### 4. Certificate Chain Issues

**Verify Certificate Chain:**
```bash
openssl s_client -connect flowcast.space:443 -servername flowcast.space 2>&1 | grep -E "(Verify|depth|subject)"
```

**Should show:**
```
Verify return code: 0 (ok)
```

If you see certificate chain errors, the Let's Encrypt intermediate certificate might not be properly configured.

---

### 5. Browser-Specific Issues

**Common Causes:**
- Outdated browser cache
- Old bookmarks using http://
- Browser extensions interfering
- Corporate network MITM proxies

**User Actions to Try:**
1. **Hard refresh:** Ctrl+Shift+R (or Cmd+Shift+R on Mac)
2. **Clear browser cache** for flowcast.space
3. **Test in incognito/private mode**
4. **Try different browser** (Chrome, Firefox, Safari)
5. **Check URL bar** - make sure it shows https:// not http://

---

## Immediate Fixes to Implement

### Fix 1: Enable HSTS (Critical)

In Cloudflare:
```
SSL/TLS → Edge Certificates → HSTS → Enable
Max Age: 6 months
Include subdomains: ON
Preload: ON
```

### Fix 2: Set Minimum TLS to 1.2

In Cloudflare:
```
SSL/TLS → Edge Certificates → Minimum TLS Version
Select: TLS 1.2
```

### Fix 3: Verify Always Use HTTPS

In Cloudflare:
```
SSL/TLS → Edge Certificates → Always Use HTTPS
Toggle: ON
```

This creates automatic 301 redirects from HTTP to HTTPS.

---

## Testing After Fixes

### 1. Check SSL Labs Grade
Visit: https://www.ssllabs.com/ssltest/analyze.html?d=flowcast.space

**Target:** A+ grade

### 2. Check Why No Padlock
Visit: https://whynopadlock.com/

Enter: https://flowcast.space

This tool identifies specific issues causing the warning.

### 3. Browser Console Check
1. Open site in Chrome
2. Press F12 → Console tab
3. Look for red errors about "Mixed Content" or "Insecure"

### 4. Command Line Test
```bash
# Check all headers
curl -sI https://flowcast.space

# Look for:
# - strict-transport-security (HSTS)
# - x-content-type-options
# - x-frame-options
# - referrer-policy
```

---

## Cloudflare SSL Settings Summary

| Setting | Recommended Value | Current Status |
|---------|-------------------|----------------|
| SSL/TLS Mode | Full (Strict) | Verify |
| Always Use HTTPS | ON | Verify |
| Minimum TLS | TLS 1.2 | Verify |
| HSTS | Enabled (6 months) | ❌ Missing |
| Automatic HTTPS Rewrites | ON | Verify |

---

## If Problems Persist

If you've made all Cloudflare changes and still see warnings:

1. **Wait 5 minutes** - Cloudflare changes take time to propagate
2. **Clear browser cache completely**
3. **Test on mobile** (different network)
4. **Check from different location** (use VPN or mobile hotspot)
5. **Verify Railway SSL** - Check if Railway has its own SSL settings

---

## Railway-Specific Checks

Since you're hosting on Railway behind Cloudflare:

1. **Railway Domain Settings:**
   - Check if Railway provides its own SSL certificate
   - Ensure Cloudflare is set to "Full (Strict)" not "Flexible"

2. **Domain Configuration:**
   - Verify custom domain in Railway dashboard
   - Check CNAME records point to Railway

3. **No Railway SSL Override:**
   - Railway shouldn't force HTTP
   - Let Cloudflare handle SSL termination

---

## Quick Fix Checklist

- [ ] Cloudflare: Always Use HTTPS = ON
- [ ] Cloudflare: Minimum TLS = 1.2
- [ ] Cloudflare: Enable HSTS (6 months, subdomains, preload)
- [ ] Cloudflare: SSL/TLS Mode = Full (Strict)
- [ ] Clear browser cache
- [ ] Test in incognito mode
- [ ] Test on ssllabs.com (target A+)
- [ ] Test on whynopadlock.com

---

## Expected Result After Fixes

✅ Browser shows padlock icon  
✅ URL bar shows "https://" in green/secure color  
✅ No "Not Secure" warning  
✅ SSL Labs grade: A+  
✅ Why No Padlock: All green checks  

---

*Last updated: 2026-02-23*
