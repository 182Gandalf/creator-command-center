# Cloudflare Domain Transfer - Settings Backup

**Domain:** flowcast.space  
**Date:** 2026-02-24  
**Purpose:** Document all DNS and SSL settings for replication on new Cloudflare account

---

## 📋 DNS Records

### Required DNS Records (From Current Setup)

| Type | Name | Value | TTL | Notes |
|------|------|-------|-----|-------|
| A | @ | (Railway IP) | Auto | Points to Railway hosting |
| A | www | (Railway IP) | Auto | WWW redirect |
| TXT | @ | v=spf1 include:_spf.google.com ~all | Auto | SPF record for email |
| TXT | _dmarc | v=DMARC1; p=quarantine; rua=mailto:dmarc@flowcast.space; ruf=mailto:dmarc@flowcast.space; fo=1 | Auto | DMARC policy |
| TXT | @ | google-site-verification=... | Auto | Google Search Console verification (if applicable) |
| CNAME | _acme-challenge | (Let's Encrypt challenge) | Auto | SSL certificate validation |
| MX | @ | route1.mx.cloudflare.net (priority: 1) | Auto | Cloudflare Email Routing |
| MX | @ | route2.mx.cloudflare.net (priority: 2) | Auto | Cloudflare Email Routing |
| TXT | _github-challenge-... | (GitHub verification) | Auto | If GitHub domain verification exists |

### To Check on Current Cloudflare:
1. Go to **DNS** → **Records**
2. Export or screenshot all records
3. Note any custom records for:
   - Railway domain verification
   - GitHub Pages (if any)
   - Third-party integrations (TikTok, Meta, etc.)

---

## 🔒 SSL/TLS Settings

### SSL/TLS Mode
| Setting | Current Value | Recommended |
|---------|---------------|-------------|
| **Encryption Mode** | Full (Strict) | Full (Strict) |

### Edge Certificates
| Setting | Current Value | Action |
|---------|---------------|--------|
| **Always Use HTTPS** | ON | ✅ Keep ON |
| **Automatic HTTPS Rewrites** | ON | ✅ Keep ON |
| **Opportunistic Encryption** | ON | ✅ Keep ON |
| **Minimum TLS Version** | TLS 1.2 | ✅ Keep TLS 1.2 |
| **HTTP Strict Transport Security (HSTS)** | Enabled | ✅ Keep Enabled |
| - Max Age | 6 months (15768000) | ✅ Keep 6 months |
| - Include Subdomains | ON | ✅ Keep ON |
| - Preload | ON | ✅ Keep ON |

### Certificate Details
- **Type:** Universal SSL (Cloudflare-managed) or Custom
- **Authority:** Let's Encrypt or Cloudflare Origin CA
- **Coverage:** *.flowcast.space, flowcast.space

---

## 🌐 Page Rules (If Any)

Check **Rules** → **Page Rules** for:
- HTTP to HTTPS redirects
- WWW to non-WWW redirects (or vice versa)
- Caching rules
- Forwarding URLs

**Common Rule:**
```
URL: http://*flowcast.space/*
Setting: Always Use HTTPS
```

---

## 📧 Email Settings

### Cloudflare Email Routing (If Enabled)
- **Status:** (Check if enabled)
- **Catch-all:** (Check destination address)
- **Custom addresses:**
  - support@flowcast.space → (destination)
  - customersupport@flowcast.space → (destination)

### DNS Records for Email
```
Type: TXT
Name: @
Value: v=spf1 include:_spf.google.com ~all

Type: TXT
Name: _dmarc
Value: v=DMARC1; p=quarantine; rua=mailto:dmarc@flowcast.space; ruf=mailto:dmarc@flowcast.space; fo=1
```

**Note:** DMARC record was missing and needs to be added.

---

## 🔧 Speed & Optimization Settings

### Auto Minify
| Asset | Status |
|-------|--------|
| JavaScript | (Check) |
| CSS | (Check) |
| HTML | (Check) |

### Brotli Compression: (Check status)

### Caching Level: (Check current setting)
- Standard (recommended)
- Aggressive

### Browser Cache TTL: (Check current)

---

## 🛡️ Security Settings

### Security Level
| Setting | Value |
|---------|-------|
| Security Level | Medium/High |
| Challenge Passage | 30 minutes |

### Bots
| Setting | Value |
|---------|-------|
| Bot Fight Mode | (Check) |
| Super Bot Fight Mode | (Check - if on paid plan) |

---

## 📝 Transfer Checklist

### Step 1: Export Current Settings
- [ ] Screenshot all DNS records
- [ ] Note SSL/TLS settings
- [ ] Document Page Rules
- [ ] Check Email Routing settings

### Step 2: Prepare New Cloudflare Account
- [ ] Create new Cloudflare account (use non-Google email)
- [ ] Add domain: flowcast.space
- [ ] Note new nameservers provided

### Step 3: Configure New Cloudflare
- [ ] Add all DNS records from backup
- [ ] Set SSL/TLS to "Full (Strict)"
- [ ] Enable "Always Use HTTPS"
- [ ] Set Minimum TLS to 1.2
- [ ] Enable HSTS (Max Age: 6 months, Include Subdomains, Preload)
- [ ] Add DMARC TXT record
- [ ] Replicate Page Rules
- [ ] Configure Email Routing (if used)

### Step 4: Domain Registrar (Porkbun) Update
- [ ] Log into Porkbun
- [ ] Update nameservers to new Cloudflare nameservers
- [ ] Wait for propagation (24-48 hours)

### Step 5: Verify
- [ ] Check DNS propagation: `dig flowcast.space`
- [ ] Test HTTPS: `curl -I https://flowcast.space`
- [ ] Verify SSL grade: https://www.ssllabs.com/ssltest/
- [ ] Test email deliverability

---

## 🚨 Critical Settings to Verify Post-Transfer

1. **DNS A Record** - Must point to Railway IP
2. **SSL Mode** - Must be "Full (Strict)" not "Flexible"
3. **DMARC Record** - Must be added (was missing before)
4. **HSTS** - Must be enabled for A+ SSL grade
5. **Min TLS** - Must be 1.2 (not 1.0)

---

## 📞 Support References

- **Cloudflare Support:** https://support.cloudflare.com
- **Porkbun Support:** support@porkbun.com
- **Railway Support:** support@railway.app

---

*Document created for Cloudflare account transfer due to Google account ban.*
*Update this document after successful transfer with actual values.*
