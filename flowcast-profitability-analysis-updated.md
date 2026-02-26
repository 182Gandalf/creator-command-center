# FlowCast Profitability Analysis - Updated Pricing

**Date:** February 24, 2026  
**Pricing Update:** Starter €6/month, Pro €29/month  
**Analysis Period:** 24 months projection

---

## 📊 NEW Pricing Structure

| Plan | Monthly Price | Annual Price (20% off) | Features |
|------|--------------|----------------------|----------|
| **Free Trial** | €0 (7 days) | - | 20 posts, 2 platforms, 5 AI ideas/day |
| **Starter** | €6/month | €58/year | 50 posts/month, 2 platforms, 10 AI ideas/day |
| **Creator** | €15/month | €144/year | Unlimited posts, 5 platforms, unlimited AI ideas |
| **Pro** | €29/month | €278/year | Unlimited everything, team features, API access |

**Previous Pricing:** Starter €5 → **€6** (+20%), Pro €39 → **€29** (-26%)

**Target Customer Mix (Month 12+):**
- Starter: 55% of paid users
- Creator: 35% of paid users  
- Pro: 10% of paid users (increased from 5% due to lower price)

**Average Revenue Per User (ARPU):**
- Month 1-3: €9.00 (mixed trial conversions)
- Month 4-6: €10.80 (maturing mix)
- Month 7-12: €12.20 (higher-tier adoption)
- Month 12+: €12.85 (optimal mix with better Pro adoption)

---

## 💰 Revenue Projections - Conservative Growth

| Month | Free Users | Paid Users | Starter | Creator | Pro | MRR (€) | ARR (€) |
|-------|-----------|-----------|---------|---------|-----|---------|---------|
| 1 | 100 | 5 | 3 | 2 | 0 | €48 | €576 |
| 3 | 350 | 25 | 14 | 9 | 2 | €247 | €2,964 |
| 6 | 900 | 80 | 44 | 28 | 8 | €850 | €10,200 |
| 9 | 1,800 | 200 | 110 | 70 | 20 | €2,440 | €29,280 |
| 12 | 3,000 | 450 | 248 | 158 | 45 | €5,783 | €69,396 |
| 18 | 5,500 | 1,000 | 550 | 350 | 100 | €12,850 | €154,200 |
| 24 | 8,000 | 1,800 | 990 | 630 | 180 | €23,130 | €277,560 |

**Key Assumptions:**
- Free-to-paid conversion: 5% → 15% (improving over time)
- Monthly churn: 8% (industry average for SaaS)
- Organic growth: 10-15% MoM (word of mouth + content marketing)
- Trial-to-paid: 12% conversion rate
- Pro adoption: Higher due to reduced €29 price point

---

## 💸 Cost Structure

### Fixed Costs (Monthly)

| Category | Service | Monthly Cost | Notes |
|----------|---------|--------------|-------|
| **Hosting** | Railway/Railway Pro | €19-49 | Scales with usage |
| **Database** | PostgreSQL (Railway) | €0-15 | Included in hosting initially |
| **Domain** | Porkbun (.space) | €1 | Annual: €12 |
| **Email** | Gmail/Google Workspace | €6 | For support/customer comms |
| **Payment Processing** | Paddle | Variable | 5% + €0.50 per transaction |
| **Analytics** | Plausible/PostHog | €9-20 | Privacy-focused analytics |
| **Monitoring** | UptimeRobot/Sentry | €0-15 | Free tiers initially |
| **SSL/CDN** | Cloudflare Free | €0 | Free tier sufficient |
| | **Total Fixed** | **€35-105** | Starting lean |

### Variable Costs (Per User/Usage)

| Category | Service | Cost | Unit |
|----------|---------|------|------|
| **AI/LLM** | Gemini API | €0.0006 | Per 1K tokens (input) |
| **AI/LLM** | Gemini API | €0.0024 | Per 1K tokens (output) |
| **Email Sending** | SendGrid/Postmark | €0.001 | Per email |
| **Storage** | AWS S3/Cloudflare R2 | €0.023 | Per GB stored |

### AI Cost Per Active User/Month

| Plan | AI Requests/Day | Monthly Tokens | Gemini Cost |
|------|-----------------|----------------|-------------|
| Free Trial | 5 | ~45K | €0.08 |
| Starter | 10 | ~90K | €0.16 |
| Creator | 25 | ~225K | €0.40 |
| Pro | 50 | ~450K | €0.80 |

**Safety Margin:** Assume €0.50-1.50 per user/month for AI costs

### Total Cost of Goods Sold (COGS)

| Users | Fixed Costs | Variable Costs | Total COGS | COGS/User |
|-------|-------------|----------------|------------|-----------|
| 50 | €50 | €25 | €75 | €1.50 |
| 100 | €65 | €50 | €115 | €1.15 |
| 250 | €85 | €125 | €210 | €0.84 |
| 500 | €105 | €250 | €355 | €0.71 |
| 1,000 | €150 | €500 | €650 | €0.65 |
| 2,500 | €250 | €1,250 | €1,500 | €0.60 |
| 5,000 | €400 | €2,500 | €2,900 | €0.58 |

---

## 📈 Profitability Analysis - Conservative Scenario

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|--------|---------|----------|----------|----------|
| **MRR** | €850 | €5,783 | €12,850 | €23,130 |
| **ARR** | €10,200 | €69,396 | €154,200 | €277,560 |
| **COGS** | €355 | €650 | €1,500 | €2,900 |
| **Gross Profit** | €495 | €5,133 | €11,350 | €20,230 |
| **Gross Margin** | 58% | 89% | 88% | 87% |
| **Operating Costs** | €500 | €800 | €1,200 | €2,000 |
| **Net Profit** | -€5 | €4,333 | €10,150 | €18,230 |
| **Net Margin** | -1% | 75% | 79% | 79% |

**Break-Even Point:** Month 7 (75 paid users)

---

## 📊 Pricing Comparison Impact

### OLD vs NEW Pricing (Month 12 Projection)

| Metric | OLD Pricing | NEW Pricing | Change |
|--------|-------------|-------------|--------|
| **Starter Price** | €5 | €6 | +20% |
| **Pro Price** | €39 | €29 | -26% |
| **ARPU** | €12.40 | €12.85 | +3.6% |
| **Month 12 MRR** | €5,310 | €5,783 | +8.9% |
| **Pro Adoption** | 5% | 10% | +5pp |
| **Break-Even** | Month 8 | Month 7 | -1 month |

**Analysis:**
- Starter price increase (+20%) offsets Pro price decrease (-26%)
- Lower Pro price drives higher adoption (5% → 10%)
- Overall ARPU increases slightly due to better mix
- Break-even achieved 1 month earlier

---

## 🎯 Key Metrics & Benchmarks

### FlowCast Projections (Month 12 - New Pricing)

| Metric | Value | Industry Benchmark |
|--------|-------|-------------------|
| **Gross Margin** | 89% | 75-80% (Good) |
| **Net Margin** | 75% | 40%+ (Great) |
| **ARPU** | €12.85 | - |
| **CAC** | €15-25 | - |
| **LTV** | €193 | - |
| **LTV/CAC** | 7.7x | >3x (Good), >5x (Great) |
| **Payback Period** | 2-3 months | <12 months |

---

## 🔮 Sensitivity Analysis

### Scenario 1: Higher Pro Adoption (15% vs 10%)
| Metric | Base (10% Pro) | Optimistic (15% Pro) |
|--------|---------------|---------------------|
| **Month 12 MRR** | €5,783 | €6,450 |
| **ARPU** | €12.85 | €14.33 |
| **Net Profit** | €4,333 | €4,850 |

### Scenario 2: Lower Conversion (8% vs 12%)
| Metric | Base (12%) | Conservative (8%) |
|--------|-----------|-------------------|
| **Month 12 Paid Users** | 450 | 300 |
| **Month 12 MRR** | €5,783 | €3,855 |
| **Break-Even** | Month 7 | Month 10 |

### Scenario 3: Higher Churn (12% vs 8%)
| Metric | Base (8%) | High Churn (12%) |
|--------|----------|------------------|
| **Month 12 Paid Users** | 450 | 380 |
| **Month 12 MRR** | €5,783 | €4,883 |
| **Impact** | - | -15% revenue |

---

## 💡 Strategic Recommendations

### Pricing Strategy
1. **€6 Starter** - Still highly competitive (Buffer starts at $20)
2. **€29 Pro** - Sweet spot for teams (vs Hootsuite $99+, Sprout $199+)
3. **Annual Discount (20%)** - Improves cash flow significantly

### Revenue Optimization
1. **Push Annual Billing** - 20% discount = better cash flow + retention
2. **Pro Tier Focus** - At €29, it's 50-70% cheaper than competitors
3. **Creator Tier Anchor** - €15 makes Pro look like great value

### Key Advantages vs Competitors
- **Buffer:** 70% cheaper (€6 vs $20)
- **Later:** 76% cheaper (€6 vs $25)
- **Hootsuite:** 94% cheaper (€29 vs $99)
- **Sprout Social:** 95% cheaper (€29 vs $199)

---

## 📋 Summary Dashboard

### Conservative Scenario (Month 12)
```
Revenue:        €69,396 ARR
COGS:           €7,800/year
Gross Profit:   €61,596 (89% margin)
OpEx:           €9,600/year
Net Profit:     €51,996 (75% margin)
Break-even:     Month 7
ARPU:           €12.85
```

### Risk Assessment
| Risk Level | Item | Mitigation |
|------------|------|------------|
| 🟢 Low | AI costs | Gemini is cheap, cache responses |
| 🟡 Medium | Churn | Focus on onboarding, engagement |
| 🟡 Medium | Conversion | A/B test trial flow |
| 🟢 Low | Competition | Pricing is 50-95% cheaper |

---

*Analysis based on updated FlowCast pricing: Starter (€6), Creator (€15), Pro (€29). Assumes Gemini API for AI features, Railway for hosting, and Paddle for payments.*
