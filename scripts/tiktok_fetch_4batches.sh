#!/bin/bash
# TikTok Fetch - 4 Batches with 15min delays
# Run this on your VPS or local machine

ADMIN_KEY="fc_admin_2024_xyz789"
API_URL="https://flowcast.space/api/admin/trends/fetch-tiktok-niches"

# Split 23 niches into 4 batches
# Batch 1: 6 niches
BATCH1="fitness,finance,food,cooking,travel,beauty"

# Batch 2: 6 niches  
BATCH2="gaming,movies,tv,music,self_improvement,education"

# Batch 3: 6 niches
BATCH3="lifestyle,business,technology,fashion,health,parenting"

# Batch 4: 5 niches
BATCH4="home%20decor,pets,sports,politics,diy"

echo "=========================================="
echo "TikTok Fetch - 4 Batches"
echo "Admin Key: ${ADMIN_KEY:0:10}..."
echo "=========================================="
echo ""

# Function to run a batch
run_batch() {
    local num=$1
    local niches=$2
    
    echo ""
    echo "🚀 BATCH $num/4 - $(date '+%H:%M:%S')"
    echo "Niches: $(echo $niches | tr ',' ' ')"
    echo "------------------------------------------"
    
    curl -X POST "${API_URL}?niches=${niches}&force=true" \
        -H "X-Admin-Key: ${ADMIN_KEY}" \
        -s -w "\nHTTP: %{http_code}\nTime: %{time_total}s\n" \
        | tee /tmp/tiktok_batch_${num}.log
    
    echo ""
    echo "✅ Batch $num complete"
}

# Kill any existing heavy operations first
echo "⚠️  Note: If site is still unresponsive, wait for it to recover first"
echo "   or restart the Railway service from dashboard"
echo ""
read -p "Press Enter when ready to start Batch 1..."

# Batch 1
run_batch 1 "$BATCH1"

# Wait 15 minutes
echo ""
echo "⏱️  Waiting 15 minutes before Batch 2..."
echo "   Next batch at: $(date -d '+15 minutes' '+%H:%M:%S')"
sleep 900

# Batch 2
run_batch 2 "$BATCH2"

# Wait 15 minutes
echo ""
echo "⏱️  Waiting 15 minutes before Batch 3..."
echo "   Next batch at: $(date -d '+15 minutes' '+%H:%M:%S')"
sleep 900

# Batch 3
run_batch 3 "$BATCH3"

# Wait 15 minutes
echo ""
echo "⏱️  Waiting 15 minutes before Batch 4..."
echo "   Next batch at: $(date -d '+15 minutes' '+%H:%M:%S')"
sleep 900

# Batch 4
run_batch 4 "$BATCH4"

echo ""
echo "=========================================="
echo "🎉 ALL BATCHES COMPLETE!"
echo "=========================================="
echo "Logs saved to: /tmp/tiktok_batch_*.log"
