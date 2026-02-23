#!/bin/bash
# Google Drive Upload Script for Level Up with AI
# Uses Service Account authentication

KEY_FILE="/home/daz/gdrive-service-account.json"
FOLDER_NAME="Level-Up-AI-Drafts"

# Extract service account details
CLIENT_EMAIL=$(cat "$KEY_FILE" | grep -o '"client_email": "[^"]*"' | cut -d'"' -f4)
PRIVATE_KEY=$(cat "$KEY_FILE" | grep -o '"private_key": "[^"]*"' | sed 's/"private_key": "//' | sed 's/"$//' | sed 's/\\n/\n/g')
TOKEN_URI=$(cat "$KEY_FILE" | grep -o '"token_uri": "[^"]*"' | cut -d'"' -f4)

# Create JWT header
HEADER='{"alg":"RS256","typ":"JWT"}'
HEADER_B64=$(echo -n "$HEADER" | base64 | tr -d '=' | tr '/+' '_-')

# Create JWT claim set
NOW=$(date +%s)
EXPIRE=$(($NOW + 3600))
CLAIMS="{\"iss\":\"$CLIENT_EMAIL\",\"scope\":\"https://www.googleapis.com/auth/drive\",\"aud\":\"$TOKEN_URI\",\"exp\":$EXPIRE,\"iat\":$NOW}"
CLAIMS_B64=$(echo -n "$CLAIMS" | base64 | tr -d '=' | tr '/+' '_-')

# Sign the JWT (this requires openssl)
JWT_UNSIGNED="$HEADER_B64.$CLAIMS_B64"

# For now, use a simpler approach with gcloud or direct API calls
# This is a placeholder - the full implementation requires openssl for JWT signing

echo "Service Account: $CLIENT_EMAIL"
echo "Token URI: $TOKEN_URI"
echo ""
echo "To complete setup, you need to:"
echo "1. Ensure the service account has access to the Drive folder"
echo "2. Use the Google Drive API with the service account key"
echo ""
echo "Key file location: $KEY_FILE"
