# FinLearnX Deployment Guide

## 🚀 Deploy to Streamlit Cloud (FREE & Easiest)

### Prerequisites
- GitHub account (you already have this!)
- Streamlit Cloud account (sign up at [share.streamlit.io](https://share.streamlit.io))

### Step-by-Step Deployment

#### 1. Sign up for Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign up" and use your GitHub account
3. Authorize Streamlit to access your repositories

#### 2. Deploy Your App
1. Click "New app" button
2. Select:
   - **Repository**: `sagarmandavkar-UX/FinLearnX`
   - **Branch**: `main`
   - **Main file path**: `app/main.py`
3. Click "Deploy!"

#### 3. Wait for Deployment (2-3 minutes)
- Streamlit will install all dependencies from `requirements.txt`
- Your app will be live at: `https://finlearnx-[random].streamlit.app`

#### 4. Customize Your URL (Optional)
1. Go to App settings
2. Under "General" → "App URL"
3. Change to: `https://finlearnx.streamlit.app` (if available)

### ✅ Your Live Demo Link
Once deployed, update your README with:
```markdown
## 🚀 Live Demo
👉 [Try FinLearnX Live](https://your-app-url.streamlit.app)
```

---

## 🐳 Alternative: Deploy to Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed

### Files Needed (Already Included)
1. `requirements.txt` ✅
2. Create `Procfile`:
```
web: streamlit run app/main.py --server.port=$PORT
```

3. Create `runtime.txt`:
```
python-3.10.12
```

### Deployment Steps
```bash
# Login to Heroku
heroku login

# Create new app
heroku create finlearnx-app

# Deploy
git push heroku main

# Open app
heroku open
```

---

## 🌐 Alternative: Deploy to Render

### Steps
1. Go to [render.com](https://render.com)
2. Connect your GitHub repository
3. Select "Web Service"
4. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app/main.py --server.port=$PORT --server.address=0.0.0.0`
5. Deploy!

---

## 🧪 Local Development

### Run Locally
```bash
# Clone repository
git clone https://github.com/sagarmandavkar-UX/FinLearnX.git
cd FinLearnX

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit
streamlit run app/main.py
```

### Run Tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=. --cov-report=html

# Open coverage report
open htmlcov/index.html
```

---

## 📸 Taking Screenshots for README

### Best Practices
1. **Full-screen browser** for clean screenshots
2. **Hide sensitive info** (if any)
3. **Use different features**:
   - Dashboard with metrics
   - Stock simulator with chart
   - Portfolio allocation
   - Trade history
   - AI tutor chat (coming soon)

### Recommended Screenshots
1. `dashboard.png` - Main dashboard view
2. `simulator.png` - Stock simulator with candlestick chart
3. `portfolio.png` - Portfolio allocation pie chart
4. `performance.png` - Performance metrics
5. `mobile.png` - Mobile responsive view

### Where to Save
Save screenshots in: `docs/images/`

---

## 🎥 Creating Demo Video

### Tools
- **Loom** (Free): [loom.com](https://loom.com)
- **OBS Studio** (Free): [obsproject.com](https://obsproject.com)
- **QuickTime** (Mac): Built-in screen recording

### Video Script (30-60 seconds)
1. **0-10s**: Show homepage/dashboard
2. **10-25s**: Execute a trade (buy stock)
3. **25-40s**: Show portfolio with chart
4. **40-50s**: Display performance metrics
5. **50-60s**: Show trade history

### Upload Location
- YouTube (Unlisted)
- Loom (Public link)
- Add link to README

---

## 🔒 Environment Variables (If Needed)

If you add API integrations later:

### Streamlit Cloud
1. Go to App settings → Secrets
2. Add in TOML format:
```toml
ALPACA_API_KEY = "your_key_here"
FINNHUB_API_KEY = "your_key_here"
```

### Heroku
```bash
heroku config:set ALPACA_API_KEY=your_key_here
heroku config:set FINNHUB_API_KEY=your_key_here
```

---

## 🎯 Post-Deployment Checklist

- [ ] App is live and accessible
- [ ] All features work (buy/sell, charts, portfolio)
- [ ] Mobile responsive
- [ ] Take 5+ screenshots
- [ ] Record 30-60s demo video
- [ ] Update README with live demo link
- [ ] Update README with screenshots
- [ ] Add deployment badge
- [ ] Test on different devices
- [ ] Share on LinkedIn!

---

## 📊 Adding Badges to README

Add these badges after deployment:

```markdown
![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-FF4B4B?logo=streamlit)
![Tests](https://github.com/sagarmandavkar-UX/FinLearnX/workflows/Run%20Tests/badge.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
```

---

## 🚨 Troubleshooting

### App Won't Start
**Issue**: Missing dependencies
**Fix**: Ensure all packages in `requirements.txt` are compatible

### Charts Not Loading
**Issue**: yfinance rate limiting
**Fix**: Add caching with `@st.cache_data`

### Tests Failing
**Issue**: Module import errors
**Fix**: Ensure proper `sys.path` configuration

---

## 📞 Need Help?

- Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- Documentation: [docs.streamlit.io](https://docs.streamlit.io)
- GitHub Issues: Open an issue in this repo

---

**You're all set! Your project is production-ready! 🎉**
