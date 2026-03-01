# PostgreSQL Migration Guide for Railway

## ✅ What's Ready

The app has been updated to support both SQLite (local dev) and PostgreSQL (production).

### Changes Made:
1. ✅ `psycopg2-binary` added to requirements.txt
2. ✅ app.py updated to use `DATABASE_URL` environment variable
3. ✅ Migration scripts created (export_sqlite.py, migrate_to_postgres.py)
4. ✅ Data exported to migration_data.json (1 user, minimal data)

---

## 🚀 Railway Deployment Steps

### Step 1: Add PostgreSQL Database in Railway

1. Go to your Railway dashboard: https://railway.app/dashboard
2. Select your FlowCast project
3. Click **"New"** → **"Database"** → **"Add PostgreSQL"**
4. Railway will create the database and generate a connection string

### Step 2: Get the DATABASE_URL

1. Click on the PostgreSQL database in your project
2. Go to **"Connect"** tab
3. Copy the **"Database URL"** (looks like:
   ```
   postgresql://postgres:password@containers.railway.app:5432/railway
   ```

### Step 3: Add DATABASE_URL to Environment Variables

1. Go to your **FlowCast service** (not the database)
2. Click **"Variables"** tab
3. Click **"New Variable"**
4. Add:
   - **Key:** `DATABASE_URL`
   - **Value:** (paste the connection string from Step 2)
5. Click **"Add"**

### Step 4: Deploy

1. The code is already pushed to GitHub
2. Railway should auto-deploy when it detects the new commit
3. If not, go to your service → **"Deploy"** tab → Click **"Deploy"**

### Step 5: Verify Database Connection

After deployment, check the Railway logs:
1. Go to your service → **"Logs"** tab
2. You should see: `"Using PostgreSQL database"`
3. If you see: `"Using SQLite database (development)"` → DATABASE_URL is not set correctly

---

## 📊 Database Migration Status

### Current SQLite Data:
- **Users:** 1 (test@example.com)
- **Posts:** 0
- **Content Ideas:** 0
- **AI Usage Trackers:** 0

### Decision: Skip Data Import

Since there's only 1 test user and no real data, **you can skip importing data**.

The test user can simply create a new account after deployment.

If you DO want to import the data later:
```bash
# Run this after PostgreSQL is connected
python migrate_to_postgres.py --import --db-url "YOUR_DATABASE_URL"
```

---

## 🔧 Environment Variables Summary

### Required Variables (Already Set):
```
SECRET_KEY=your-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
YOUTUBE_CLIENT_ID=your-youtube-client-id
YOUTUBE_CLIENT_SECRET=your-youtube-client-secret
TIKTOK_CLIENT_KEY=your-tiktok-key
TIKTOK_CLIENT_SECRET=your-tiktok-secret
```

### New Variable to Add:
```
DATABASE_URL=postgresql://postgres:password@containers.railway.app:5432/railway
```

---

## ✅ Post-Deployment Checklist

- [ ] PostgreSQL database created in Railway
- [ ] DATABASE_URL added to environment variables
- [ ] App deployed successfully
- [ ] Logs show "Using PostgreSQL database"
- [ ] Test user registration works
- [ ] Test login works
- [ ] Database persists after restart (create a user, restart, check if user still exists)

---

## 🆘 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'psycopg2'"
**Fix:** The requirements.txt has been updated. Make sure Railway deploys the latest commit.

### Issue: "Using SQLite database (development)" in logs
**Fix:** DATABASE_URL is not set. Check:
1. Variable name is exactly `DATABASE_URL` (case sensitive)
2. Value is the full connection string from Railway PostgreSQL
3. Redeploy after adding the variable

### Issue: Database connection fails
**Fix:** 
1. Check that PostgreSQL database is in the SAME project as your app
2. Railway automatically adds the database to the same network
3. If using external database, check firewall rules

---

## 📞 Next Steps

1. **Add DATABASE_URL to Railway** (instructions above)
2. **Test the deployment**
3. **Once working, I can help with:**
   - Meta/Instagram API setup
   - AI API keys configuration
   - TikTok secret rotation (security fix)

Ready to proceed?
