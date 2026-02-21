# Creator Command Center

A social media management tool for content creators. Schedule posts, track analytics, and get AI-powered content ideas.

## Features

- **Multi-Platform Posting:** YouTube, Instagram (TikTok coming soon)
- **Content Calendar:** Visual schedule of all your posts
- **AI Content Ideas:** Get suggestions for your next posts
- **Analytics Dashboard:** Track performance across platforms
- **Cross-Platform Posting:** Write once, post everywhere

## Tech Stack

- **Backend:** Flask (Python)
- **Database:** SQLite (upgrade to PostgreSQL for production)
- **Frontend:** HTML/CSS/JS (minimal, dashboard-focused)
- **APIs:** YouTube Data API v3, Instagram Basic Display API

## Project Structure

```
creator-app/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── setup.sh              # Setup script
├── static/               # CSS, JS, images
├── templates/            # HTML templates
│   └── dashboard.html   # Main dashboard
└── migrations/          # Database migrations
```

## Setup Instructions

### 1. Install Dependencies

```bash
cd creator-app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```bash
export YOUTUBE_API_KEY="your-youtube-api-key"
export INSTAGRAM_APP_ID="your-instagram-app-id"
export INSTAGRAM_APP_SECRET="your-instagram-app-secret"
export SECRET_KEY="your-secret-key-for-sessions"
```

### 3. Initialize Database

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Run the App

```bash
flask run
```

Visit: http://localhost:5000

## API Status

| Platform | Status | Notes |
|----------|--------|-------|
| YouTube | ✅ Active | API key configured |
| Instagram | ⚠️ In Progress | OAuth flow needed |
| TikTok | ⏸️ Pending | Apply for Research API |
| Reddit | ⏸️ Skipped | Policy restrictions |

## Development Roadmap

### Phase 1: MVP (Week 1-2)
- [x] Flask app structure
- [x] Database models
- [x] Basic dashboard UI
- [ ] YouTube API integration
- [ ] Post scheduling system
- [ ] Content calendar

### Phase 2: Features (Week 3-4)
- [ ] Instagram integration
- [ ] AI content ideas
- [ ] Analytics tracking
- [ ] User authentication
- [ ] Media upload

### Phase 3: Polish (Week 5-6)
- [ ] TikTok integration
- [ ] Cross-platform posting
- [ ] Advanced analytics
- [ ] Mobile responsiveness
- [ ] Production deployment

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `YOUTUBE_API_KEY` | YouTube Data API key | Yes |
| `INSTAGRAM_APP_ID` | Instagram App ID | Yes |
| `INSTAGRAM_APP_SECRET` | Instagram App Secret | Yes |
| `SECRET_KEY` | Flask session secret | Yes |
| `DATABASE_URL` | Database URL (optional) | No |

## Contributing

This is a personal project. For questions, contact via Telegram.

## License

Private - Not for public distribution.
