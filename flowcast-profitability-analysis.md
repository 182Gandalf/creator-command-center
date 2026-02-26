# FlowCast Profitability & Cost Analysis

**Date:** February 24, 2026  
**Analysis Period:** 24 months projection

---

## 📊 Pricing Structure

| Plan | Monthly Price | Annual Price | Features |
|------|--------------|--------------|----------|
| **Free Trial** | €0 (7 days) | - | 20 posts, 2 platforms, 5 AI ideas/day |
| **Starter** | €5/month | €48/year (20% savings) | 50 posts/month, 2 platforms, 10 AI ideas/day |
| **Creator** | €15/month | €144/year (20% savings) | Unlimited posts, 5 platforms, unlimited AI ideas |
| **Pro** | €39/month | €374/year (20% savings) | Unlimited everything, team features, API access |

**Target Customer Mix (Month 12+):**
- Starter: 60% of paid users
- Creator: 35% of paid users  
- Pro: 5% of paid users

**Average Revenue Per User (ARPU):**
- Month 1-3: €8.50 (mixed trial conversions)
- Month 4-6: €10.20 (maturing mix)
- Month 7-12: €11.80 (higher-tier adoption)
- Month 12+: €12.40 (optimal mix)

---

## 💰 Revenue Projections

### Conservative Growth Scenario

| Month | Free Users | Paid Users | MRR (€) | ARR (€) |
|-------|-----------|-----------|---------|---------|
| 1 | 100 | 5 | €42.50 | €510 |
| 3 | 350 | 25 | €255 | €3,060 |
| 6 | 900 | 80 | €816 | €9,792 |
| 9 | 1,800 | 200 | €2,360 | €28,320 |
| 12 | 3,000 | 450 | €5,310 | €63,720 |
| 18 | 5,500 | 1,000 | €12,400 | €148,800 |
| 24 | 8,000 | 1,800 | €22,320 | €267,840 |

**Key Assumptions:**
- Free-to-paid conversion: 5% → 15% (improving over time)
- Monthly churn: 8% (industry average for SaaS)
- Organic growth: 10-15% MoM (word of mouth + content marketing)
- Trial-to-paid: 12% conversion rate

### Optimistic Growth Scenario (Viral/Product-Market Fit)

| Month | Free Users | Paid Users | MRR (€) | ARR (€) |
|-------|-----------|-----------|---------|---------|
| 1 | 200 | 15 | €153 | €1,836 |
| 3 | 800 | 80 | €816 | €9,792 |
| 6 | 2,500 | 350 | €4,130 | €49,560 |
| 9 | 5,000 | 900 | €10,620 | €127,440 |
| 12 | 8,000 | 2,000 | €24,800 | €297,600 |
| 18 | 15,000 | 5,000 | €62,000 | €744,000 |
| 24 | 25,000 | 10,000 | €124,000 | €1,488,000 |

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
| **Legal** | Terms/Privacy Generator | €0 | One-time cost |
| **SSL/CDN** | Cloudflare Free | €0 | Free tier sufficient |
| | **Total Fixed** | **€35-105** | Starting lean |

### Variable Costs (Per User/Usage)

| Category | Service | Cost | Unit |
|----------|---------|------|------|
| **AI/LLM** | Gemini API | €0.0006 | Per 1K tokens (input) |
| **AI/LLM** | Gemini API | €0.0024 | Per 1K tokens (output) |
| **AI/LLM** | OpenAI (fallback) | €0.001-0.03 | Per 1K tokens (varies by model) |
| **Email Sending** | SendGrid/Postmark | €0.001 | Per email |
| **Storage** | AWS S3/Cloudflare R2 | €0.023 | Per GB stored |
| **Bandwidth** | Cloudflare/CDN | €0 | Free tier (10TB) |

### AI Cost Calculations

**Per User Daily AI Usage:**
- Content ideas: ~500 tokens input, ~150 tokens output
- Caption generation: ~300 tokens input, ~100 tokens output
- Scheduling optimization: ~200 tokens input, ~50 tokens output

**Average AI Cost Per Active User/Month:**
| Plan | AI Requests/Day | Monthly Tokens | Gemini Cost | OpenAI Cost |
|------|-----------------|----------------|-------------|-------------|
| Free Trial | 5 | ~45K | €0.08 | €0.15 |
| Starter | 10 | ~90K | €0.16 | €0.30 |
| Creator | 25 | ~225K | €0.40 | €0.75 |
| Pro | 50 | ~450K | €0.80 | €1.50 |

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

## 📈 Profitability Analysis

### Conservative Scenario

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|--------|---------|----------|----------|----------|
| **MRR** | €816 | €5,310 | €12,400 | €22,320 |
| **ARR** | €9,792 | €63,720 | €148,800 | €267,840 |
| **COGS** | €355 | €650 | €1,500 | €2,900 |
| **Gross Profit** | €461 | €4,660 | €10,900 | €19,420 |
| **Gross Margin** | 56% | 88% | 88% | 87% |
| **Operating Costs** | €500 | €800 | €1,200 | €2,000 |
| **Net Profit** | -€39 | €3,860 | €9,700 | €17,420 |
| **Net Margin** | -5% | 73% | 78% | 78% |

**Break-Even Point:** Month 8 (80 paid users at €10.20 ARPU)

### Optimistic Scenario

| Metric | Month 6 | Month 12 | Month 18 | Month 24 |
|--------|---------|----------|----------|----------|
| **MRR** | €4,130 | €24,800 | €62,000 | €124,000 |
| **ARR** | €49,560 | €297,600 | €744,000 | €1,488,000 |
| **COGS** | €650 | €1,500 | €2,900 | €5,500 |
| **Gross Profit** | €3,480 | €23,300 | €59,100 | €118,500 |
| **Gross Margin** | 84% | 94% | 95% | 96% |
| **Operating Costs** | €800 | €2,000 | €4,000 | €8,000 |
| **Net Profit** | €2,680 | €21,300 | €55,100 | €110,500 |
| **Net Margin** | 65% | 86% | 89% | 89% |

**Break-Even Point:** Month 4 (45 paid users)

---

## 🎯 Key Metrics & Benchmarks

### SaaS Benchmarks (B2C/B2SMB)

| Metric | FlowCast Target | Industry Good | Industry Great |
|--------|-----------------|---------------|----------------|
| **Gross Margin** | 85%+ | 75% | 80%+ |
| **Net Margin** | 70%+ | 20% | 40%+ |
| **Churn Rate** | <8% | <5% | <2% |
| **LTV/CAC Ratio** | >3x | >3x | >5x |
| **Payback Period** | <12 months | <12 months | <6 months |
| **ARR Growth** | 15% MoM | 10% MoM | 20%+ MoM |

### FlowCast Projections (Month 12)

| Metric | Conservative | Optimistic |
|--------|--------------|------------|
| **Gross Margin** | 88% | 94% |
| **Net Margin** | 73% | 86% |
| **CAC** | €15-25 | €10-15 |
| **LTV** | €178 | €372 |
| **LTV/CAC** | 7.1x | 24.8x |
| **Months to Payback** | 2-3 | 1-2 |

---

## 🔮 Sensitivity Analysis

### What If Scenarios

**1. Lower Conversion Rate (8% vs 12%)**
- Month 12 paid users: 300 (vs 450)
- Month 12 MRR: €3,540 (vs €5,310)
- Break-even: Month 10 (vs Month 8)

**2. Higher Churn (12% vs 8%)**
- Month 12 paid users: 380 (vs 450)
- Month 12 MRR: €4,484 (vs €5,310)
- Impact: 15% lower revenue

**3. Higher AI Costs (2x expected)**
- COGS increases by €0.50-1.00 per user
- Month 12 profit: €3,110 (vs €3,860)
- Impact: 19% lower profit, still healthy

**4. Lower ARPU (€10 vs €12.40)**
- Month 12 MRR: €4,500 (vs €5,310)
- Break-even: Month 9 (vs Month 8)
- Impact: Manageable

**5. Viral Growth (2x users)****
- Month 12 paid users: 900 (vs 450)
- Month 12 MRR: €10,620 (vs €5,310)
- Need: Scale infrastructure (cost: +€200/month)
- Profit: €8,620 (vs €3,860)

---

## 💡 Recommendations

### Immediate (Pre-Launch)

1. **Start with conservative pricing** — €5/€15/€39 is competitive
2. **Monitor AI costs closely** — Set up cost alerts at €50, €100, €250/month
3. **Implement usage limits** — Hard caps prevent runaway costs
4. **Use Gemini as primary** — 50% cheaper than OpenAI GPT-4

### Short-Term (Months 1-6)

1. **Track cohort retention** — Identify at-risk users early
2. **A/B test pricing** — Test €4/€12/€35 vs current pricing
3. **Add annual discounts** — Improve cash flow with 20% yearly discount
4. **Implement referral program** — Reduce CAC, drive organic growth

### Medium-Term (Months 6-12)

1. **Add higher-tier plan** — €79/month for agencies (10+ users)
2. **Introduce usage-based pricing** — For power users exceeding limits
3. **White-label offering** — €200+/month for resellers
4. **API monetization** — Charge for API access on Pro+ plans

### Cost Optimization

1. **Cache AI responses** — Reduce redundant API calls by 30-40%
2. **Batch operations** — Process posts in batches, not individually
3. **Smart model selection** — Use cheaper models for simple tasks
4. **Monitor abandoned trials** — Clean up inactive data to reduce storage

---

## 📊 Summary Dashboard

### Conservative Scenario (Month 12)
```
Revenue:        €63,720 ARR
COGS:           €7,800/year
Gross Profit:   €55,920 (88% margin)
OpEx:           €9,600/year
Net Profit:     €46,320 (73% margin)
Break-even:     Month 8
```

### Optimistic Scenario (Month 12)
```
Revenue:        €297,600 ARR
COGS:           €18,000/year
Gross Profit:   €279,600 (94% margin)
OpEx:           €24,000/year
Net Profit:     €255,600 (86% margin)
Break-even:     Month 4
```

---

## 🎯 Success Metrics to Track

### Weekly
- New signups
- Trial-to-paid conversion
- Churn rate (rolling 7-day)
- AI API costs

### Monthly
- MRR growth
- ARPU trends
- Customer acquisition cost (CAC)
- Lifetime value (LTV)
- Net revenue retention

### Quarterly
- Gross margin
- Net margin
- Payback period
- LTV/CAC ratio
- Feature adoption rates

---

*Analysis based on FlowCast pricing: Free Trial (€0), Starter (€5), Creator (€15), Pro (€39). Assumes Gemini API for AI features, Railway for hosting, and Paddle for payments.*
