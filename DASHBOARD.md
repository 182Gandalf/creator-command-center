# Gandalf Operations Dashboard

**Single source of truth for all active blockers and action items.**

**Last Updated:** April 25, 2026 UTC (2:58 PM)  
**Next Review:** Weekly (Sundays)

---

## 🚨 Active Blockers (Max 3 P0)

No active P0 blockers.

---

## ⏳ User Action Required

None.

---

## ✅ Recently Completed (Major)

| ID | Issue | Completed Date | Impact |
|----|-------|----------------|--------|
| **PERF-002** | **Dashboard Slowness Fix** | **Apr 25, 2026** | **🚀 Committed a6ab756** |
| | - Increased DB pool: 5→10, max_overflow: 10→20 | | |
| | - Removed Clerk API call from hot path | | |
| | - Only fetch email on user creation (not every request) | | |
| **PERF-001** | **Trend Query Optimization** | **Apr 25, 2026** | **🚀 Committed 6e71385** |
| | - Fixed slow trend queries (ilike → exact match) | | |
| | - Services: trends.py, reddit_trends.py | | |
| | - Enables PostgreSQL index usage | | |
| **BETA-001** | **Formal Beta Request Modal** | **Mar 23, 2026** | **🚀 Committed f18da47** |
| | - New /api/beta-request endpoint | | |
| | - Modal popup on landing + pricing pages | | |
| | - Email sent to hello@flowcast.space on submit | | |
| **PDF-001** | **White-label PDF exports (Studio)** | **Mar 13, 2026** | **🚀 Committed e562cb3** |
| | - Brand Settings modal (name/color/logo) | | |
| | - /api/export/pdf/hooks, /scripts, /content-pack | | |
| | - reportlab, DB migration, Studio-tier gate | | |
| **PIVOT-001** | **Brand Repivot — AI Co-Creator** | **Mar 1, 2026** | **🚀 LIVE ON PRODUCTION** |
| | - Landing page complete rewrite | | |
| | - New positioning: "Know what to film" | | |
| | - Three-tier pricing: Splash/Creator/Studio | | |
| | - OpusClip differentiation strategy | | |
| SEC-002 | Password hashing migration to pbkdf2 | Mar 1, 2026 | ✅ Security improved |
| SEC-003 | Remove credentials from TOOLS.md | Feb 26, 2026 | ✅ Security |
| SEC-004 | Move API keys to .env | Feb 26, 2026 | ✅ Security |

---

## 📊 Brand Pivot Summary — LIVE

**Commit:** 97a787b (Production)  
**Strategic Shift:** Content Scheduler → AI Co-Creator

| Before | After |
|--------|-------|
| Content scheduler | AI co-creator |
| Post-production | Pre-production |
| Compete with Buffer | Complement OpusClip |
| "Schedule smarter" | "Know what to film" |

**New Positioning:**
- **Hero:** "Know what to film. Before you film it."
- **Problem:** "You don't have an editing problem. You have an ideas problem"
- **Differentiation:** "OpusClip clips what you've already made. FlowCast helps you make what's worth clipping."

**Pricing Tiers:**
- ✦ **Splash:** Free (20 ideas/mo, TikTok only) — taste conversion
- ✦✦ **Creator:** $15/mo ($12 annual) — unlimited, all platforms
- ✦✦✦ **Studio:** $39/mo ($31 annual) — 5 workspaces, team seats, white-label

---

## 📝 On Hold

| ID | Issue | Priority | Notes |
|----|-------|----------|-------|
| DOM-001 | Domain transfer to Cloudflare | P2 | Can wait until post-launch |
| TRENDS-001 | Migrate Google Trends to SerpAPI | P2 | Execute when first paying users come in |

---

## 🗺️ TRENDS-001 — SerpAPI Migration Plan

**Trigger:** First paying users / revenue covers $25/mo  
**Cost:** $25/mo (Starter — 1,000 searches/mo, 200/hr throughput)  
**Why:** pytrends is archived (Apr 2025), rate-limited, unreliable long-term  
**Current workaround:** 60s+jitter delay, 3 AM UTC fetch — acceptable for early stage

### What to do

**1. Sign up**
- https://serpapi.com → Starter plan ($25/mo)
- Get API key → add to Railway env vars as `SERPAPI_KEY`

**2. Replace `services/trends.py` fetch logic**

Current pytrends call:
```python
pt = TrendReq(hl="en-US", tz=0, ...)
pt.build_payload([niche], timeframe="now 7-d", geo="")
related = pt.related_queries()
top_df = related.get(niche, {}).get("top")
```

Replace with SerpAPI call:
```python
import httpx

async def _fetch_sync():
    resp = httpx.get("https://serpapi.com/search", params={
        "engine": "google_trends",
        "q": niche,
        "date": "now 7-d",
        "api_key": os.environ["SERPAPI_KEY"],
    }, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("related_queries", {}).get("top", []):
        results.append({"topic": item["query"], "score": int(item["value"])})
    return results
```

**3. Remove from requirements.txt**
- Remove `pytrends`
- Remove `urllib3<2` (no longer needed)
- Add `httpx` (already in requirements)

**4. Test locally → push → verify Railway deploy**

### Expected outcome
- Zero 429 errors
- Reliable daily fetch for all 17 niches
- ~510 requests/month used out of 1,000 quota (~490 headroom)

---

## 🗺️ TRENDS-002 — Extended Trend Data (implement AFTER TRENDS-001)

**Trigger:** SerpAPI or Official Google Trends API is live (TRENDS-001 complete)  
**Why blocked:** Adding more pytrends endpoints now = 4x more rate-limit exposure on an archived library. Wrong moment.

### New endpoints to add

| Priority | Endpoint | Feature | Est. daily calls |
|----------|----------|---------|-----------------|
| P1 | `realtime_trending_searches` | "Hot right now" feed on Trends tab (past 24h breaking topics) | +17 |
| P1 | `interest_over_time` | Niche health score — is your niche growing or shrinking this month? | +17 |
| P2 | `trending_searches` | Daily digest card — yesterday's top searches in user's region | +17 |
| P3 | `interest_by_region` | Geo-targeting for Studio tier — where is your niche hottest? | +17 |

**Total after TRENDS-002:** ~68 calls/day (up from 17) — well within SerpAPI Starter 1,000/mo quota

### Feature ideas per endpoint
- **realtime_trending_searches** → "🔥 Hot right now" section on Trends tab, refreshed daily
- **interest_over_time** → Niche health badge (📈 +28% this month / 📉 cooling) shown on Ideas tab
- **trending_searches** → "Yesterday's top searches" digest card on dashboard
- **interest_by_region** → Studio-tier geo map — top countries for your niche

---

## 📋 Quick Status

### Health Check
- P0 Issues: 0
- User Blockers: 0
- Security Items: 0 open, 4 closed
- Major Milestone: ✅ Brand pivot LIVE

### This Week's Goal
Ship beta users. Everything else is secondary.

---

## 🔗 Related Files

- **Security:** `memory/security-findings.md`
- **Daily Logs:** `memory/YYYY-MM-DD.md`
- **Long-term Memory:** `MEMORY.md`
- **Product Positioning:** This dashboard

---

*Updated after every significant action.*
