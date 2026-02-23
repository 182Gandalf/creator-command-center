# SSL/TLS Fixes for FlowCast - Priority Actions

## Issues Found (From SSL Scan Image)

1. **TLS 1.0 and 1.1 Enabled** - Security vulnerability
2. **Certificate Chain Incomplete** - Missing intermediate certificates
3. **Grade B** instead of A+ (should be A+)

---

## Fix 1: Disable TLS 1.0/1.1 in Cloudflare

1. Go to https://dash.cloudflare.com → flowcast.space
2. **SSL/TLS** → **Edge Certificates**
3. Find **"Minimum TLS Version"**
4. Change from "TLS 1.0" to **"TLS 1.2"**
5. Save

---

## Fix 2: Enable OCSP Stapling

In same Cloudflare page:
1. Scroll to **"Always Use HTTPS"** - Ensure it's **ON**
2. **"Automatic HTTPS Rewrites"** - Turn **ON**
3. **"Opportunistic Encryption"** - Turn **ON**

---

## Fix 3: Certificate Chain (If Using Custom Cert)

If you're using your own certificate (not Cloudflare's):

**Option A: Use Cloudflare's Universal SSL (Recommended)**
1. SSL/TLS → Overview
2. Set encryption mode to **"Full (Strict)"**
3. Enable **"Universal SSL"**

**Option B: Fix Your Certificate Chain**
Your certificate needs the full chain including intermediate certificates.

---

## Fix 4: HSTS Header

Enable HTTP Strict Transport Security:

1. SSL/TLS → Edge Certificates
2. Find **"HTTP Strict Transport Security (HSTS)"**
3. Click **"Enable HSTS"**
4. Set:
   - Max Age: 6 months (15768000 seconds)
   - Include subdomains: ✅ ON
   - Preload: ✅ ON
5. Save

---

## Fix 5: Verify on SSL Labs

After making changes, test at:
https://www.ssllabs.com/ssltest/analyze.html?d=flowcast.space

**Target Grade: A+**

---

## Quick Cloudflare SSL Checklist

| Setting | Value | Status |
|---------|-------|--------|
| SSL/TLS Mode | Full (Strict) | Verify |
| Minimum TLS | 1.2 | ✅ Fix this |
| Always Use HTTPS | ON | Verify |
| HSTS | Enabled | ✅ Fix this |
| Automatic HTTPS Rewrites | ON | Verify |

---

## Railway-Specific (If Applicable)

If Railway is handling SSL:

1. Check Railway dashboard → Settings → Domains
2. Ensure SSL certificate is valid
3. Verify domain points to Railway correctly
4. **Important:** If using Cloudflare + Railway, set Cloudflare SSL to "Full (Strict)" not "Flexible"

---

## Test Commands

```bash
# Check TLS versions supported
nmap --script ssl-enum-ciphers -p 443 flowcast.space

# Check certificate chain
openssl s_client -connect flowcast.space:443 -servername flowcast.space 2>&1 | grep -E "(Verify|depth)"

# Check HSTS header
curl -sI https://flowcast.space | grep strict-transport
```

---

## Expected Results After Fixes

✅ TLS 1.2 and 1.3 only (1.0/1.1 disabled)  
✅ Complete certificate chain  
✅ HSTS header present  
✅ Grade A+ on SSL Labs  
✅ No "Not Secure" warning in browsers  

---

**Priority Order:**
1. Disable TLS 1.0/1.1 (immediate security fix)
2. Enable HSTS (prevents downgrade attacks)
3. Fix certificate chain (if needed)
4. Test and verify A+ grade