# FlowCast Referral Program

**Program Name:** "Creator Circle"  
**Launch Status:** Ready to implement  
**Goal:** 15% organic growth through word-of-mouth

---

## Program Overview

### The Offer
**"Give $15, Get $15"**

- **Referrer (Existing User):** Gets $15 credit per successful referral
- **Referee (New User):** Gets $15 off their first month

### Mechanics
- No limits on referrals
- Credits apply to subscription (not cash out)
- Referee must subscribe to paid plan for referrer to receive credit
- Credits stack indefinitely

### Economics
- CAC via referral: $15 (credit given)
- LTV of referred user: ~$144 (annual plan)
- Payback period: 1 month
- ROI: 860% over 12 months

---

## Email Templates

### 1. Referral Invite (User to Friend)

**Subject:** I found the cure for creative block

```
Hey [Friend Name],

You know that feeling when you sit down to create content and... nothing?

I've been using FlowCast for [time period] and it's completely changed my workflow. Instead of staring at a blank screen, I get personalized content ideas in seconds.

Here's what I love:
• Unlimited AI ideas calibrated to my niche
• Platform-native scripts for TikTok, Reels, and Shorts
• 10 hook variations for every idea
• I can plan a month of content in 10 minutes

Thought you'd find it useful too. Here's $15 off to try it:

[Referral Link]

Let me know what you think!

Cheers,
[Your Name]

P.S. If you sign up, I get a small credit too. Win-win! 🙌
```

### 2. Referral Success Notification (To Referrer)

**Subject:** 🎉 You earned $15 credit!

```
Hey [Name],

Great news! [Friend Name] just signed up for FlowCast using your referral link.

You've earned $15 credit!

**Your referral stats:**
• Friends joined: [X]
• Total credit earned: $[X]
• Months free: [X]

Keep sharing—there's no limit to how much you can earn!

[View Your Referrals]

Thanks for spreading the word!

— The FlowCast Team
```

### 3. Referral Welcome (To Referee)

**Subject:** Welcome! Here's your $15 discount

```
Hey [Name],

[Referrer Name] thought you'd love FlowCast—and they were right to tell you about it!

Welcome to the community of creators who never run out of ideas.

**Your $15 discount has been applied!**

Your first month is just $[discounted amount].

**What's next:**
1. Complete your creator profile (2 minutes)
2. Generate your first AI content ideas
3. Never stare at a blank screen again

[Get Started]

Questions? Reply to this email—we read every one.

Excited to see what you create!

— The FlowCast Team

P.S. Want to earn free months too? Share your own referral link once you're in!
```

---

## Social Share Templates

### Twitter/X

```
I used to spend 3 hours planning content every week.

Now I spend 3 minutes.

Game changer: @flowcastapp

[Referral Link]
```

### LinkedIn

```
I've been using FlowCast for content ideation and it's completely changed my workflow.

Instead of creative block, I get personalized AI ideas in seconds.

If you're a creator, worth checking out:

[Referral Link]

#ContentCreation #CreatorTools
```

### Instagram Story

```
[Image: Screenshot of FlowCast dashboard]

Text: "This app generates my content ideas 👀"

Sticker: "Link in bio"

Caption: "Swipe up to try it (and get $15 off!)"
```

---

## In-App Referral Prompts

### Prompt 1: Post-First-Idea

**Timing:** After user generates their first AI idea  
**Placement:** Modal or toast notification

```
🎉 Love that idea?

Share FlowCast with a creator friend and you both get $15!

[Share Now] [Maybe Later]
```

### Prompt 2: Subscription Confirmation

**Timing:** After user upgrades to paid plan  
**Placement:** Success page

```
Welcome to FlowCast Creator! 🚀

Want to earn free months?

Refer friends and earn $15 credit for each one that subscribes.

[Get My Referral Link]
```

### Prompt 3: Monthly Summary Email

**Timing:** Monthly usage report  
**Placement:** Bottom of email

```
---

💰 Earn Free Months

You've created [X] posts this month with FlowCast.

Know a creator who could use this?

Share your link, earn $15 per referral: [Link]

---
```

---

## Referral Tracking

### Database Schema

```sql
CREATE TABLE referrals (
    id SERIAL PRIMARY KEY,
    referrer_id INTEGER REFERENCES users(id),
    referee_id INTEGER REFERENCES users(id),
    referral_code VARCHAR(20) UNIQUE,
    status VARCHAR(20), -- 'pending', 'signed_up', 'converted', 'cancelled'
    credit_issued BOOLEAN DEFAULT FALSE,
    credit_amount INTEGER DEFAULT 1500, -- cents
    created_at TIMESTAMP DEFAULT NOW(),
    converted_at TIMESTAMP
);

CREATE INDEX idx_referrals_referrer ON referrals(referrer_id);
CREATE INDEX idx_referrals_code ON referrals(referral_code);
```

### Key Metrics

| Metric | Target | Tracking Method |
|--------|--------|-----------------|
| Referral Rate | 20% of users | Referrals / Total Users |
| Conversion Rate | 15% | Converted Referrals / Total Referrals |
| Viral Coefficient | 0.3 | Average referrals per user |
| CAC via Referral | $15 | Credit issued |
| Referral Revenue | 15% of MRR | Revenue from referred users |

---

## Gamification Elements

### Milestone Rewards

| Referrals | Reward | Notification |
|-----------|--------|--------------|
| 1 | $15 credit + Badge | "🎉 First referral!" |
| 3 | $20 bonus credit | "⭐ 3 referrals! Extra $20!" |
| 5 | Free month + Swag box | "🏆 5 referrals! You're a champion!" |
| 10 | Lifetime 50% off | "👑 10 referrals! Legend status!" |
| 25 | Free lifetime access | "🚀 25 referrals! You're part of the team!" |

### Badges

- **Seed:** First referral
- **Sprout:** 3 referrals  
- **Growth:** 5 referrals
- **Bloom:** 10 referrals
- **Influencer:** 25 referrals

Display badges on:
- User profile
- Referral page
- Community leaderboard (if implemented)

---

## Launch Strategy

### Phase 1: Soft Launch (Week 1)
- Enable for 10% of users
- Monitor conversion rates
- Gather feedback

### Phase 2: Full Launch (Week 2)
- Roll out to all users
- Email announcement
- In-app promotion

### Phase 3: Optimization (Ongoing)
- A/B test messaging
- Adjust reward amounts
- Add gamification

---

## Launch Email

**Subject:** Earn free months with Creator Circle 🎉

```
Hey [Name],

Big news: We're launching Creator Circle—our referral program!

**Here's how it works:**

1. Share your unique referral link with creator friends
2. They get $15 off their first month
3. You get $15 credit when they subscribe
4. No limits. Refer 10 friends, get 10 months free.

**Your referral stats:**
• Your link: [Referral Link]
• Friends joined: 0
• Credit earned: $0

[Start Sharing]

**Why share FlowCast?**

Because you know the pain of the blank screen. And you know FlowCast fixes it.

Help a fellow creator. Earn free months. Everyone wins.

Questions? Reply to this email.

Happy creating!

— The FlowCast Team

P.S. Top referrers this month get exclusive FlowCast swag. Just sayin' 😉
```

---

## Implementation Notes

### Technical Requirements

1. **Referral Code Generation**
   - Unique 8-character codes
   - URL format: `flowcast.space/r/XXXXXXX`

2. **Tracking**
   - Cookie-based attribution (30-day window)
   - UTM parameters for analytics

3. **Credit System**
   - Credits applied to next invoice automatically
   - Credit balance visible in billing page

4. **Notifications**
   - Email on successful referral
   - In-app notification on credit received

### Fraud Prevention

- Self-referral detection (same IP, email pattern)
- Minimum subscription period before credit issued
- Manual review for high-volume referrers

---

**Last Updated:** 2026-03-04  
**Status:** Ready for implementation
