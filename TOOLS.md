# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## SSH Tunnels

**OpenClaw Gateway (remote → local):**
```bash
ssh -N -L 18789:127.0.0.1:18789 daz@100.116.210.37
```
Forwards gateway from remote machine to localhost:18789.

---

## Credentials (Sensitive - Local Only)

**GitHub (NEW ACCOUNT):**
- Email: 182gandalf@gmail.com
- Password: [Stored in password manager]
- Created: 2026-02-23
- Status: Active (not Google-linked)

**ProtonMail (Bot Operations):**
- Email: 182gandalf@proton.me
- Password: [Stored in password manager]
- Created: 2026-02-24
- Status: Active
- Forwarding: 182gandalf@gmail.com → 182gandalf@proton.me
- Purpose: Safe email for bot operations

**Google OAuth 2.0 (FlowCast Production):**
- Project ID: flowcast-prod
- Credentials: Stored in `.env` file (secure)
- Created: 2026-02-24
- Status: Active
- Redirect URIs:
  - https://flowcast.space/auth/callback
  - https://flowcast.space/oauth2callback
  - https://flowcast.space/login/callback
  - http://localhost:5000/auth/callback (dev)
- JavaScript Origins:
  - https://flowcast.space
  - https://www.flowcast.space
  - http://localhost:5000 (dev)
- Purpose: Google OAuth login, YouTube API access

⚠️ **Security Note:** Credentials stored in `.env` file. TOOLS.md contains references only.

---

Add whatever helps you do your job. This is your cheat sheet.
