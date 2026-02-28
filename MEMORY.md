# Critical Context & Lessons Learned - February 24, 2026

## User Context - DO NOT FORGET

### Google Account Ban (CRITICAL)
- **gandalftheclaw@gmail.com BANNED** for "bot activity"
- Date: February 2026
- Impact: Lost GitHub, Railway, Cloudflare access simultaneously
- **Lesson:** Never suggest Gmail solutions again
- **Lesson:** Never suggest Gmail IMAP again

### New Accounts Created
- **GitHub:** 182gandalf@gmail.com (NEW, active, SSH key added)
- **Google Cloud:** 182gandalf@gmail.com (NEW project: flowcast-prod)
- **ProtonMail:** 182gandalf@proton.me (free plan, forwarding from Gmail)

### Active Credentials (All in .env file, NOT in git)
- Google OAuth 2.0 (flowcast-prod)
- TikTok API (needs rotation - exposed in old git history)
- No hardcoded secrets in code anymore

## Important Lessons

### ALWAYS Warn About Payment Requirements
Before suggesting any solution, check if it requires payment:
- ProtonMail Bridge: Requires €3.99+/month paid plan
- Railway Pro: $5+/month
- Cloudflare Pro: $20+/month
- **Rule:** Always ask before suggesting paid solutions

### Never Forget Context
- Gmail is banned - don't suggest Gmail IMAP
- Google account lost - don't suggest Google solutions
- User is non-technical - keep explanations simple
- Security audits are on HOLD - don't spawn them

### ALWAYS Commit and Push Code Changes
**Rule:** After ANY code change, immediately:
1. `git add <file>`
2. `git commit -m "descriptive message"`
3. `git push origin main`

**Never** tell user "I've updated the file" without committing and pushing. The change doesn't exist until it's in GitHub.

### Self-Improvement & Subagent Results — COMPLETE SILENCE
- **NEVER share self-improvement summaries in Telegram/chat**
- **NEVER mention self-improvement work, subagents, or reviews in chat**
- **NEVER acknowledge self-improvement in responses — complete radio silence**
- Do the work in background, but keep it 100% silent
- User does not want to hear about it at all

### Security Priorities (Pending)
1. **Rotate TikTok client secret** (exposed in git history)
2. Clean old exposed credentials from git history before new repo push
3. Move all credentials from TOOLS.md to password manager

## Infrastructure Blockers
- Railway account recovery (support ticket active)
- Cloudflare domain transfer needed (flowcast.space)
- Porkbun domain locked (support ticket filed)

## Today's Work Completed
✅ Pricing updated (Starter €6, Pro €29) with annual billing
✅ Competitor comparison table added
✅ Terms updated with AI Services section
✅ Secure credential management implemented (.env files)
✅ Hardcoded secrets removed from app.py
✅ Google OAuth credentials configured

## User Preferences
- Bullet points over walls of text
- Simple explanations with analogies
- Proactive but not pushy
- Honest about mistakes
