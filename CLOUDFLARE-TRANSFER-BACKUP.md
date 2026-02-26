# Cloudflare Transfer Backup & DNS Configuration

**Date:** 2026-02-26
**Domain:** flowcast.space
**Registrar:** Porkbun
**Hosting:** Railway (creator-command-center-production.up.railway.app)

---

## Step 1: Porkbun (Registrar) Settings

Once Porkbun unlocks your domain and you can access it, update the nameservers:

### Nameservers to Use (Cloudflare)

After adding the domain to your NEW Cloudflare account, they will provide 2 nameservers. Typically they look like:

```
[unique-string].ns.cloudflare.com
[unique-string].ns.cloudflare.com
```

**Action:** Replace Porkbun's default nameservers with Cloudflare's nameservers.

---

## Step 2: Cloudflare DNS Records

Add these DNS records in your new Cloudflare account:

### Required Records

| Type | Name | Target/Value | Proxy Status | TTL |
|------|------|--------------|--------------|-----|
| CNAME | @ | creator-command-center-production.up.railway.app | Proxied (Orange Cloud) | Auto |
| CNAME | www | creator-command-center-production.up.railway.app | Proxied (Orange Cloud) | Auto |

### Optional: Email (MX) Records

If you want to use ProtonMail for support@flowcast.space:

| Type | Name | Priority | Target | TTL |
|------|------|----------|--------|-----|
| MX | @ | 10 | mail.protonmail.ch | Auto |
| MX | @ | 20 | mailsec.protonmail.ch | Auto |
| TXT | @ | - | "v=spf1 include:_spf.protonmail.ch ~all" | Auto |
| TXT | _dmarc | - | "v=DMARC1; p=quarantine; rua=mailto:182gandalf@proton.me" | Auto |

### Optional: Security/Verification Records

| Type | Name | Value | Purpose |
|------|------|-------|---------|
| TXT | @ | "v=spf1 include:_spf.protonmail.ch ~all" | Email SPF |

---

## Step 3: Railway Custom Domain Setup

In Railway dashboard:

1. Go to your project → Settings → Domains
2. Click "Add Domain"
3. Enter: `flowcast.space`
4. Railway will provide a target (should match: `creator-command-center-production.up.railway.app`)
5. Verify the CNAME record matches what we configured in Cloudflare

Repeat for `www.flowcast.space` if needed.

---

## Step 4: HTTPS/SSL

Cloudflare will automatically provide SSL when proxying is enabled (orange cloud).

Railway also provides SSL certificates for custom domains.

**Recommended:** Use Cloudflare's "Full (Strict)" SSL mode for best security.

---

## Step 5: Verify Setup

After DNS propagates (5 minutes to 24 hours):

```bash
# Check DNS resolution
nslookup flowcast.space

# Should return Cloudflare IPs (if proxied) or Railway CNAME
```

Visit: https://flowcast.space

---

## Important URLs to Remember

| Service | URL |
|---------|-----|
| Live Site | https://flowcast.space |
| Railway Direct | https://creator-command-center-production.up.railway.app |
| GitHub Repo | https://github.com/182gandalf/creator-command-center |
| Cloudflare Dashboard | https://dash.cloudflare.com |
| Porkbun Dashboard | https://porkbun.com |

---

## OAuth Redirect URIs (for reference)

These need to be configured in respective developer consoles:

**Google OAuth:**
- https://flowcast.space/auth/callback
- https://flowcast.space/oauth2callback
- https://flowcast.space/login/callback
- https://flowcast.space/api/google/callback

**YouTube API:**
- https://flowcast.space/api/youtube/auth

---

## Recovery Checklist

- [ ] Porkbun domain unlocked (support ticket resolved)
- [ ] Nameservers changed to Cloudflare
- [ ] DNS records added in Cloudflare
- [ ] Custom domain added in Railway
- [ ] SSL/HTTPS working
- [ ] Site loads at https://flowcast.space

---

*Created: 2026-02-26*
*Last Updated: 2026-02-26*
