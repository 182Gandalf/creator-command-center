#!/bin/bash
# Quick deployment check
echo "Checking deployment files..."
echo ""
echo "Requirements:"
cat requirements.txt
echo ""
echo "Procfile:"
cat Procfile
echo ""
echo "Railway config:"
cat railway.json
echo ""
echo "App entry point check:"
python3 -c "import app; print('✓ app.py imports successfully')" 2>/dev/null || echo "✗ app.py has import errors"
