# RENDER DEPLOYMENT GUIDE - STEP BY STEP

## Your Project Status: READY FOR DEPLOYMENT

All files are committed to Git and ready to deploy to Render.

---

## REQUIREMENTS BEFORE STARTING

✓ Git repository initialized (done)
✓ Project committed to Git (ready)
✓ GitHub account (needed)
✓ Render account (free to create)

---

## STEP 1: PUSH TO GITHUB

If your project is not yet on GitHub, do this first:

### Option A: New GitHub Repository
```bash
# Navigate to project
cd C:\Users\abhis\TT_Project

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - E-commerce analysis app ready for deployment"

# Create new repo on GitHub.com
# Then follow GitHub instructions to push
git remote add origin https://github.com/YOUR_USERNAME/TT_Project.git
git branch -M main
git push -u origin main
```

### Option B: Already on GitHub
```bash
cd C:\Users\abhis\TT_Project
git push origin main
```

**Verify:** Go to GitHub.com and check that your repository shows all project files.

---

## STEP 2: CREATE RENDER ACCOUNT

1. Go to **https://render.com**
2. Click **Sign Up**
3. Choose **Sign up with GitHub** (recommended)
   - This allows Render to access your repositories
4. Authorize Render to access your GitHub account
5. Complete setup

**Why GitHub?** Render auto-deploys when you push code updates.

---

## STEP 3: CREATE NEW WEB SERVICE

1. Go to **Render Dashboard** (https://dashboard.render.com)
2. Click **New +** button (top right)
3. Select **Web Service**

---

## STEP 4: CONNECT YOUR REPOSITORY

1. Under "Build and deploy from a Git repository"
2. Click **Connect GitHub**
3. Search for your repository: **TT_Project**
4. Click **Connect**

Render will now access your repository.

---

## STEP 5: CONFIGURE THE WEB SERVICE

Fill in the following fields:

| Field | Value | Notes |
|-------|-------|-------|
| **Name** | `ecommerce-analysis` | Your app name (will be in URL) |
| **Region** | `Oregon (US)` | Closest to you |
| **Branch** | `main` | Default deployment branch |
| **Root Directory** | *(leave blank)* | App is in root |
| **Build Command** | `pip install -r requirements.txt` | Install dependencies |
| **Start Command** | `gunicorn app:app` | Run the Flask app |
| **Plan** | `Free` | Use free tier |

### Environment Variables (Optional)
Leave empty for now. Can be added later if needed.

---

## STEP 6: DEPLOY

1. Review all settings
2. Click **Create Web Service**
3. Watch the deployment logs scroll in real-time

**What's happening:**
- Render clones your GitHub repository
- Installs dependencies from requirements.txt
- Starts your Flask app with gunicorn
- Assigns a public URL

**Deployment time:** 2-3 minutes

---

## STEP 7: VERIFY DEPLOYMENT

Once you see "Deploy successful" in the logs:

1. **Get your URL** from the Render dashboard
   - Looks like: `https://ecommerce-analysis-xxxx.onrender.com`

2. **Test your app** by visiting the URL:
   - Dashboard loads? ✓
   - Data explorer works? ✓
   - Charts display? ✓
   - API endpoints work? ✓

3. **Test an API endpoint:**
   ```
   https://ecommerce-analysis-xxxx.onrender.com/api/stats
   ```
   Should return JSON data.

---

## STEP 8: (OPTIONAL) ADD CUSTOM DOMAIN

If you want a custom domain (e.g., `myapp.com`):

1. In Render dashboard, go to your service
2. Click **Settings** → **Custom Domains**
3. Add your domain
4. Follow DNS instructions from your domain provider

---

## TROUBLESHOOTING

### Build Failed
**Check logs:** Render shows detailed error messages in the logs section.
**Common fixes:**
- Ensure requirements.txt exists and has all dependencies
- Check that render.yaml is properly formatted
- Verify all Python code has correct syntax

### App Crashes After Deploy
**Check logs:** View real-time logs in Render dashboard.
**Common issues:**
- Missing files (templates, CSV, etc.)
- Port configuration (should use auto-assigned port)
- Environment variables missing

### Can't Connect to GitHub
**Solution:** Re-authorize GitHub access in Render settings.

### Slow First Load
**Normal:** Free tier on Render may spin down after inactivity.
First request after inactivity takes 30+ seconds. Subsequent requests are fast.

### Port Binding Error
**Solution:** Don't specify port in app.py - let gunicorn handle it.
Flask should use environment variable: `os.environ.get('PORT', 5000)`

---

## AFTER DEPLOYMENT

### Monitor Your App
- **Render Dashboard:** See logs, metrics, deployments
- **Health Status:** Check if app is running
- **Logs:** View real-time output and errors

### Auto-Deployment
Whenever you:
```bash
git push origin main
```
Render automatically rebuilds and redeploys your app!

### Update Your App
1. Make changes locally
2. Commit and push to GitHub
3. Render auto-deploys within 2-3 minutes
4. No manual deployment needed

---

## YOUR DEPLOYMENT URLS

Once deployed, you'll have:

**Main App:**
```
https://ecommerce-analysis-xxxx.onrender.com
```

**Dashboard:**
```
https://ecommerce-analysis-xxxx.onrender.com/
```

**Data Explorer:**
```
https://ecommerce-analysis-xxxx.onrender.com/data
```

**Visualizations:**
```
https://ecommerce-analysis-xxxx.onrender.com/visualizations
```

**Analysis Report:**
```
https://ecommerce-analysis-xxxx.onrender.com/analysis
```

**API Endpoints:**
```
https://ecommerce-analysis-xxxx.onrender.com/api/stats
https://ecommerce-analysis-xxxx.onrender.com/api/products
https://ecommerce-analysis-xxxx.onrender.com/api/top-products
https://ecommerce-analysis-xxxx.onrender.com/api/best-value
```

---

## WHAT'S INCLUDED IN YOUR DEPLOYMENT

✓ Flask web application with 4 pages
✓ 4 responsive HTML templates
✓ 20 products data (products_clean.csv)
✓ Analysis report with insights
✓ 4 professional PNG visualizations
✓ 4 working API endpoints
✓ Mobile-friendly design
✓ Interactive search functionality
✓ Modern gradient UI

---

## PROJECT FILES DEPLOYED

```
Your GitHub repository includes:
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render configuration
├── Procfile                    # Alternative config (ignored on Render)
├── templates/
│   ├── index.html             # Dashboard
│   ├── data.html              # Data explorer
│   ├── visualizations.html    # Charts
│   └── analysis.html          # Report
├── products_clean.csv         # Product data
├── analysis_summary.txt       # Insights
├── outputs/
│   ├── top_products.png
│   ├── price_distribution.png
│   ├── price_vs_rating.png
│   └── category_distribution.png
└── [documentation files]
```

All files are automatically deployed with your app.

---

## DEPLOYMENT SUMMARY

| Step | Action | Time |
|------|--------|------|
| 1 | Push to GitHub | <5 min |
| 2 | Create Render account | <5 min |
| 3 | Connect GitHub | <1 min |
| 4 | Configure service | <5 min |
| 5 | Deploy | 2-3 min |
| **Total** | **Complete deployment** | **~15 minutes** |

---

## NEXT STEPS AFTER DEPLOYMENT

1. ✓ Share your app URL with team/stakeholders
2. ✓ Test all pages and features
3. ✓ Monitor logs for any errors
4. ✓ Make updates and push to auto-deploy
5. ✓ Add custom domain if needed

---

## SUPPORT

**Render Documentation:** https://render.com/docs

**Flask Documentation:** https://flask.palletsprojects.com

**If you have issues:**
1. Check Render logs for error messages
2. Verify all files are in GitHub repository
3. Check that requirements.txt has all dependencies
4. Ensure app.py uses correct port configuration

---

## SUCCESS INDICATORS

Your deployment is successful when:

- [ ] Render shows "Deploy successful"
- [ ] App URL is accessible
- [ ] Dashboard loads without errors
- [ ] All 4 pages work correctly
- [ ] Search functionality works
- [ ] Charts display properly
- [ ] API endpoints return JSON data

---

**Ready to deploy? Follow the steps above and your app will be live in ~15 minutes!**

For quick reference, see: HOSTING_READY.txt
