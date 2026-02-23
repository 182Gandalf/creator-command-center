# DNS & Email Configuration Fixes for FlowCast

## Issues Found & Solutions

### 1. DMARC Record Not Found

**Problem:** No DMARC policy for email authentication

**Fix:** Add DMARC TXT record in Cloudflare DNS

**Record:**
```
Type: TXT
Name: _dmarc
Value: v=DMARC1; p=quarantine; rua=mailto:dmarc@flowcast.space; ruf=mailto:dmarc@flowcast.space; fo=1
TTL: Auto
```

**What this does:**
- `p=quarantine` - Suspicious emails go to spam (use `p=reject` after testing)
- `rua` - Aggregate reports sent to this email
- `ruf` - Forensic reports sent to this email

---

### 2. SMTP Open Relay (Cloudflare route2.mx)

**Problem:** Email server configuration allows open relay

**Fix:** This is a **Cloudflare Email Routing** issue, not your application

**In Cloudflare:**
1. Go to https://dash.cloudflare.com → flowcast.space
2. **Email** → **Email Routing**
3. Check "Destination addresses" settings
4. Ensure only authorized addresses can receive email
5. Review "Catch-all address" - disable if not needed

**Alternative:** If you're not using email, disable Email Routing entirely

---

### 3. Reverse DNS Does Not Match SMTP Banner

**Problem:** Your server's reverse DNS (PTR) doesn't match the SMTP banner

**Fix:** This is typically a hosting provider (Railway) issue

**Options:**
1. Contact Railway support to set PTR record for your IP
2. Or use a dedicated email service (SendGrid, Mailgun) instead of direct SMTP

**Recommended:** Use a transactional email service for better deliverability:
- SendGrid
- Mailgun
- Amazon SES

---

### 4. SOA Expire Value Out of Range

**Problem:** DNS SOA record has incorrect expire value

**Fix:** Update SOA record in Cloudflare

**Current:** Likely too high or too low
**Recommended:** 2419200 (28 days)

**In Cloudflare:**
1. Go to **DNS** → **Records**
2. Look for SOA record (usually auto-managed)
3. If manual, set:
   - **Expire:** 2419200
   - **Retry:** 7200
   - **Refresh:** 3600
   - **Minimum TTL:** 3600

**Note:** Cloudflare usually manages this automatically. If you see this error, it may be a false positive.

---

### 5. SOA Serial Number Format Invalid

**Problem:** Serial number doesn't follow YYYYMMDDNN format

**Fix:** Cloudflare should auto-manage this

**If manually managing:**
- Format: `2026022301` (YYYYMMDD + 2-digit revision)
- Increment revision number (01, 02, etc.) with each change

**In Cloudflare:**
- This is usually auto-generated
- If custom SOA, update serial to today's date format

---

## Quick Fix Checklist

### Email (DMARC + SMTP)
- [ ] Add DMARC TXT record (see above)
- [ ] Check Cloudflare Email Routing settings
- [ ] Consider using SendGrid/Mailgun instead of direct SMTP

### DNS (SOA Records)
- [ ] Verify SOA record in Cloudflare DNS
- [ ] Ensure serial uses YYYYMMDDNN format
- [ ] Set expire to 2419200 (28 days)

### Reverse DNS
- [ ] Contact Railway support for PTR record
- [ ] Or switch to dedicated email service

---

## Priority: What to Fix First

1. **DMARC Record** - Most important for email deliverability
2. **Email Service** - Switch to SendGrid/Mailgun (recommended)
3. **SOA Record** - Minor, Cloudflare usually handles this

---

## Recommended Email Setup (Best Practice)

Instead of fixing SMTP issues, use a transactional email service:

**SendGrid Setup:**
1. Sign up at sendgrid.com
2. Verify sender domain (flowcast.space)
3. Add SendGrid DNS records in Cloudflare
4. Use SendGrid API in your app

**Benefits:**
- Better deliverability
- No reverse DNS issues
- No open relay concerns
- Built-in analytics

---

## Testing After Fixes

Check email configuration:
```bash
# Check DMARC
dig TXT _dmarc.flowcast.space

# Check MX records
dig MX flowcast.space

# Check SOA
dig SOA flowcast.space

# Test email deliverability
https://mxtoolbox.com/dmarc.aspx
```

---

## Impact of These Issues

| Issue | Impact | Priority |
|-------|--------|----------|
| Missing DMARC | Emails may go to spam | HIGH |
| SMTP Open Relay | Security risk | HIGH |
| Reverse DNS | Email deliverability | MEDIUM |
| SOA Expire | DNS caching issues | LOW |
| SOA Serial | Zone transfer issues | LOW |

---

**Recommendation:** For a SaaS app, use SendGrid or Mailgun for transactional emails. It's easier than managing your own SMTP server and avoids most of these issues.