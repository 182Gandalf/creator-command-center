#!/bin/bash
# Setup auto-start for Creator Command Center

echo "Setting up Creator Command Center auto-start..."

# Create user systemd directory if not exists
mkdir -p ~/.config/systemd/user/

# Copy service file
cp /home/daz/.openclaw/workspace/levelup-ai/creator-app/creator-command-center.service ~/.config/systemd/user/

# Reload systemd
systemctl --user daemon-reload

# Enable service (start on boot)
systemctl --user enable creator-command-center.service

# Start service now
systemctl --user start creator-command-center.service

# Check status
systemctl --user status creator-command-center.service

echo ""
echo "✅ Auto-start configured!"
echo "The app will now start automatically on boot."
echo ""
echo "Commands to manage:"
echo "  Start:   systemctl --user start creator-command-center"
echo "  Stop:    systemctl --user stop creator-command-center"
echo "  Restart: systemctl --user restart creator-command-center"
echo "  Status:  systemctl --user status creator-command-center"
