#!/bin/bash
# Setup script for Creator Command Center

echo "Setting up Creator Command Center..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set environment variables
export FLASK_APP=app.py
export FLASK_ENV=development
export YOUTUBE_API_KEY="[REDACTED_YOUTUBE_KEY]"
export INSTAGRAM_APP_ID="[REDACTED_INSTAGRAM_ID]"
export INSTAGRAM_APP_SECRET="[REDACTED_INSTAGRAM_SECRET]"

# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

echo "Setup complete!"
echo "Run: flask run"
