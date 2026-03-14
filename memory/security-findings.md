# Security Findings Tracker

**Purpose:** Track security issues from discovery through remediation  
**Status Values:** OPEN | IN-PROGRESS | PARTIAL | CLOSED  
**Last Updated:** 2026-03-14

---

## Active Findings

### SEC-002: Weak Password Hashing (SHA256 without salt)
| Field | Value |
|-------|-------|
| **ID** | SEC-002 |
| **Severity** | 🟡 MEDIUM |
| **Discovered** | 2026-02-24 |
| **Status** | CLOSED |
| **Closed Date** | 2026-03-01 |

**Description:**
Password hashing implementation uses SHA256 without salt, vulnerable to rainbow table attacks.

**Remediation Steps:**
- [x] Implement bcrypt or Argon2 for password hashing → Used werkzeug's pbkdf2:sha256
- [x] Migrate existing password hashes → Backward compatibility maintained
- [x] Update authentication middleware → Updated signup and login endpoints

**Resolution:**
Migrated to `werkzeug.security.generate_password_hash()` with pbkdf2:sha256 method.
- New passwords use secure salted hashing
- Existing SHA256 hashes still work (backward compatible)
- Commit: `cd7f952`

---

## Closed Findings

### SEC-003: Hardcoded Credentials in TOOLS.md
| Field | Value |
|-------|-------|
| **ID** | SEC-003 |
| **Severity** | 🔴 CRITICAL |
| **Discovered** | 2026-02-24 |
| **Status** | CLOSED |
| **Closed Date** | 2026-02-26 |

**Description:**
GitHub password, Railway token, and Gmail App Password stored in plaintext in TOOLS.md.

**Remediation:**
- [x] Redacted all credentials from TOOLS.md
- [x] Added placeholder references ("[Stored in .env]")
- [x] Verified .env is in .gitignore
- [x] Verified credentials now in .env only

---

### SEC-004: API Keys in api-keys.md
| Field | Value |
|-------|-------|
| **ID** | SEC-004 |
| **Severity** | 🔴 CRITICAL |
| **Discovered** | 2026-02-24 |
| **Status** | CLOSED |
| **Closed Date** | 2026-02-26 |

**Description:**
YouTube, Instagram, and other API keys stored in markdown file.

**Remediation:**
- [x] Moved all API keys to .env file
- [x] Updated api-keys.md to reference .env
- [x] Removed file from git tracking

---

## Security Checklist (For Future Development)

Before committing code that handles credentials:

- [ ] Are credentials loaded from environment variables only?
- [ ] Is `.env` in `.gitignore`?
- [ ] Is there a `.env.example` with dummy values?
- [ ] Have I run `git diff --cached` to check for secrets?
- [ ] Are there NO hardcoded secrets, even as fallbacks?
- [ ] Does the code fail safely if env vars are missing?

### Patterns to Watch For
```bash
# Check for secrets in staged files
git diff --cached | grep -i -E "(password|secret|token|key)"

# Check for high-entropy strings (potential API keys)
git diff --cached | grep -E "[a-zA-Z0-9]{32,}"
```

---

*This file is reviewed and updated as part of every security-related session.*
