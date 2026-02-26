# ProtonMail Bridge + Himalaya Setup Guide

## Step 1: Install ProtonMail Bridge

### Option A: Using .deb package (Recommended for Debian/Ubuntu)

```bash
# Download the latest release
cd /tmp
wget https://github.com/ProtonMail/proton-bridge/releases/download/v3.22.0/protonmail-bridge_3.22.0-1_amd64.deb

# Install (requires sudo)
sudo dpkg -i protonmail-bridge_3.22.0-1_amd64.deb

# Fix any dependency issues
sudo apt-get install -f -y
```

### Option B: Using AppImage

```bash
# Download AppImage
cd ~/Applications
wget https://github.com/ProtonMail/proton-bridge/releases/download/v3.22.0/protonmail-bridge_3.22.0-1_amd64.AppImage
chmod +x protonmail-bridge_3.22.0-1_amd64.AppImage

# Create symlink for easy access
sudo ln -s ~/Applications/protonmail-bridge_3.22.0-1_amd64.AppImage /usr/local/bin/protonmail-bridge
```

### Option C: Build from Source

```bash
# If you prefer building from source
git clone https://github.com/ProtonMail/proton-bridge.git
cd proton-bridge
make build
```

---

## Step 2: Start ProtonMail Bridge

### GUI Mode (Interactive setup)

```bash
# If installed via .deb
protonmail-bridge

# Or if using AppImage
~/Applications/protonmail-bridge_3.22.0-1_amd64.AppImage
```

### CLI Mode (Headless setup)

```bash
# Start bridge in CLI mode
protonmail-bridge --cli
```

---

## Step 3: Configure ProtonMail Bridge

### Initial Setup (One-time)

When you first start the bridge, you'll need to log in:

```bash
# In the Bridge CLI, run:
>>> login
Enter username: 182gandalf@proton.me
Enter password: Freya@06082021
# Optional: Enter 2FA code if prompted
```

After successful login, the bridge will show you the IMAP/SMTP credentials:

```
IMAP Server: 127.0.0.1:1143
SMTP Server: 127.0.0.1:1025
Username: 182gandalf@proton.me
Password: [Bridge-generated app password - COPY THIS]
```

**IMPORTANT:** Copy the bridge-generated password - this is different from your ProtonMail password!

---

## Step 4: Create Himalaya Configuration

Create the config file at `~/.config/himalaya/config.toml`:

```toml
[accounts.proton]
email = "182gandalf@proton.me"
display-name = "FlowCast Bot"
default = true

# IMAP backend (connects to ProtonMail Bridge)
backend.type = "imap"
backend.host = "127.0.0.1"
backend.port = 1143
backend.encryption.type = "none"  # Bridge runs locally, no TLS needed
backend.login = "182gandalf@proton.me"
backend.auth.type = "password"
# Use the bridge-generated password here, NOT your ProtonMail password
backend.auth.raw = "[BRIDGE-GENERATED-PASSWORD]"

# SMTP backend (for sending)
message.send.backend.type = "smtp"
message.send.backend.host = "127.0.0.1"
message.send.backend.port = 1025
message.send.backend.encryption.type = "none"  # Bridge runs locally
message.send.backend.login = "182gandalf@proton.me"
message.send.backend.auth.type = "password"
# Use the bridge-generated password here
message.send.backend.auth.raw = "[BRIDGE-GENERATED-PASSWORD]"

# Folder aliases
[accounts.proton.folder.alias]
inbox = "INBOX"
sent = "Sent"
drafts = "Drafts"
trash = "Trash"
spam = "Spam"

# Signature for bot emails
signature = "---\nBest regards,\nFlowCast Support Team\nsupport@flowcast.space"
```

---

## Step 5: Secure the Password (Recommended)

Instead of storing the password in plain text, use a password manager:

### Option A: Using `pass` (password store)

```bash
# Install pass
sudo apt-get install pass

# Initialize pass
gpg --full-generate-key  # Create a GPG key if you don't have one
pass init "your-gpg-key-id"

# Store the bridge password
pass insert email/protonmail-bridge
# Enter the bridge-generated password when prompted

# Update config.toml to use:
backend.auth.cmd = "pass show email/protonmail-bridge"
message.send.backend.auth.cmd = "pass show email/protonmail-bridge"
```

### Option B: Using environment variable

```bash
# Add to ~/.bashrc or ~/.zshrc
export PROTON_BRIDGE_PASSWORD="your-bridge-generated-password"

# Update config.toml:
backend.auth.cmd = "echo $PROTON_BRIDGE_PASSWORD"
message.send.backend.auth.cmd = "echo $PROTON_BRIDGE_PASSWORD"
```

---

## Step 6: Start Bridge and Test

### Terminal 1: Start ProtonMail Bridge

```bash
# Keep this running in the background
protonmail-bridge --cli
```

Or run as a systemd service:

```bash
# Create systemd service file
sudo tee /etc/systemd/system/protonmail-bridge.service > /dev/null << 'EOF'
[Unit]
Description=ProtonMail Bridge
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/protonmail-bridge --cli
Restart=on-failure
User=daz

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable protonmail-bridge
sudo systemctl start protonmail-bridge

# Check status
sudo systemctl status protonmail-bridge
```

### Terminal 2: Test Himalaya

```bash
# List folders
himalaya folder list

# List recent emails
himalaya envelope list

# Read first email
himalaya message read 1

# Send test email
cat << 'EOF' | himalaya message write
To: 182gandalf@gmail.com
Subject: Test from Himalaya

This is a test email sent via Himalaya + ProtonMail Bridge.
EOF
```

---

## Step 7: Create Helper Scripts

### Start Bridge Script (`~/scripts/start-bridge.sh`)

```bash
#!/bin/bash
# Start ProtonMail Bridge in background

if pgrep -x "protonmail-bridge" > /dev/null; then
    echo "Bridge is already running"
else
    echo "Starting ProtonMail Bridge..."
    nohup protonmail-bridge --cli > ~/.local/share/protonmail-bridge.log 2>&1 &
    sleep 3
    echo "Bridge started. Check logs: tail -f ~/.local/share/protonmail-bridge.log"
fi
```

### Check Email Script (`~/scripts/check-email.sh`)

```bash
#!/bin/bash
# Quick email check

echo "📧 Checking ProtonMail..."
himalaya --account proton envelope list --page-size 10
```

### Send Support Response Script (`~/scripts/send-support.sh`)

```bash
#!/bin/bash
# Send support email response

if [ $# -lt 2 ]; then
    echo "Usage: $0 <recipient@email.com> <subject>"
    exit 1
fi

RECIPIENT=$1
SUBJECT=$2

himalaya message write -H "To:$RECIPIENT" -H "Subject:$SUBJECT"
```

Make scripts executable:
```bash
chmod +x ~/scripts/*.sh
```

---

## Step 8: Email Templates for FlowCast

### Support Response Template

Save as `~/.config/himalaya/templates/support-response.mml`:

```mml
From: FlowCast Support <182gandalf@proton.me>
To: {{to}}
Subject: Re: {{subject}}

Dear FlowCast User,

Thank you for contacting FlowCast Support.

{{response}}

If you have any further questions, please don't hesitate to reach out.

Best regards,
FlowCast Support Team
support@flowcast.space

---
FlowCast - AI Content Scheduler for Creators
https://flowcast.space
```

### Welcome Email Template

```mml
From: FlowCast <182gandalf@proton.me>
To: {{to}}
Subject: Welcome to FlowCast! 🚀

Welcome to FlowCast!

Your account has been successfully created. Here's how to get started:

1. Connect your social media accounts
2. Explore AI content ideas
3. Schedule your first post

Need help? Reply to this email or contact support@flowcast.space

Best regards,
The FlowCast Team
```

---

## Common Issues & Solutions

### Issue 1: "Connection refused"
**Cause:** Bridge is not running
**Fix:** Start the bridge first: `protonmail-bridge --cli`

### Issue 2: "Authentication failed"
**Cause:** Wrong password (using ProtonMail password instead of bridge password)
**Fix:** Use the bridge-generated password, not your ProtonMail login password

### Issue 3: "TLS/SSL errors"
**Cause:** Trying to use TLS with local bridge
**Fix:** Set `backend.encryption.type = "none"` for local bridge connection

### Issue 4: Bridge asks for password every time
**Cause:** Bridge not properly logged in
**Fix:** Run `login` command in bridge CLI and save credentials

---

## Security Best Practices

1. **Never commit `config.toml` to Git**
   ```bash
   echo "config.toml" >> ~/.gitignore
   ```

2. **Use bridge-generated password, not ProtonMail password**
   - The bridge creates a unique app password
   - This is more secure than using your main password

3. **Run bridge on localhost only**
   - Bridge binds to 127.0.0.1 by default
   - Never expose bridge ports to the internet

4. **Use password manager for bridge password**
   - `pass`, `keyring`, or environment variables
   - Never store in plain text in config files

---

## Quick Reference Commands

```bash
# Start bridge
protonmail-bridge --cli

# List emails
himalaya envelope list

# Read email
himalaya message read <id>

# Reply
himalaya message reply <id>

# Send new email
himalaya message write

# Check specific folder
himalaya envelope list --folder "Sent"

# Search
himalaya envelope list from:support@example.com
```

---

## Next Steps After Setup

1. ✅ Test sending and receiving emails
2. ✅ Set up email templates for common responses
3. ✅ Create scripts for automated notifications (signup alerts, etc.)
4. ✅ Configure logging for support requests
5. ✅ Set up email forwarding rules if needed

---

**Ready to proceed?** Run Step 1 to install the bridge, then follow the configuration steps.
