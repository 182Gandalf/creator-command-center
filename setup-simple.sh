#!/bin/bash
# Simple setup for Creator Command Center (no venv)

echo "Setting up Creator Command Center..."

# Install dependencies to user directory
python3 -m pip install --user flask flask-sqlalchemy flask-migrate requests python-dotenv

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export YOUTUBE_API_KEY="[REDACTED_YOUTUBE_KEY]"
export SECRET_KEY="dev-secret-key-$(date +%s)"

echo "Dependencies installed."
echo ""
echo "To run the app:"
echo "export FLASK_APP=app.py"
echo "python3 -m flask run --host=0.0.0.0 --port=5000"
echo ""
echo "Then visit: http://100.116.210.37:5000"
