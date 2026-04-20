# E-Commerce Product Analysis Dashboard - Hosting Guide

## Quick Start - Run Locally

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Web Server
```bash
python app.py
```

### 3. Access the Dashboard
Open your browser and navigate to:
```
http://localhost:5000
```

## Dashboard Pages

- **Dashboard** (/) - Overview with key metrics
- **Data Explorer** (/data) - Browse and search all products
- **Visualizations** (/visualizations) - View all charts
- **Analysis Report** (/analysis) - Read comprehensive insights

## API Endpoints

All endpoints return JSON data:

- `GET /api/stats` - Summary statistics
- `GET /api/products` - All products
- `GET /api/top-products` - Top 10 rated products
- `GET /api/best-value` - Best value products

Example:
```bash
curl http://localhost:5000/api/stats
```

---

## Deploy to Heroku

### Prerequisites
- Heroku account (free tier available)
- Git installed
- Heroku CLI installed

### Deployment Steps

1. **Login to Heroku**
```bash
heroku login
```

2. **Create Heroku App**
```bash
heroku create your-app-name
```

3. **Deploy Code**
```bash
git push heroku main
```

4. **View Live App**
```bash
heroku open
```

5. **View Logs**
```bash
heroku logs --tail
```

---

## Deploy to Render

### Prerequisites
- Render account (free tier available)
- GitHub repository with your code

### Deployment Steps

1. **Create New Web Service on Render**
   - Go to https://dashboard.render.com
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repository

2. **Configure Service**
   - Name: ecommerce-analysis
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`

3. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy

4. **Access Your App**
   - Render provides a public URL
   - Available at `https://your-app-name.onrender.com`

---

## Deploy to Vercel (with Backend API)

### Note
Vercel is optimized for frontend hosting. Use Render or Heroku for Flask apps.

---

## Environment Variables

If needed, add environment variables on your hosting platform:

```
FLASK_ENV=production
DEBUG=False
```

---

## Troubleshooting

### Port Issues
The app runs on port 5000 locally. Hosting platforms automatically assign a port via `$PORT` environment variable.

### Missing Dependencies
Ensure all packages in `requirements.txt` are installed:
```bash
pip install -r requirements.txt
```

### Module Not Found
If templates aren't loading:
1. Ensure `templates/` directory exists
2. Check file paths are correct
3. Restart the server

### Image Display Issues
- Charts must be in `outputs/` directory
- Images are base64-encoded in HTML
- High-res PNG files (300 DPI) supported

---

## File Structure

```
C:\Users\abhis\TT_Project\
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Procfile                  # Heroku configuration
├── render.yaml              # Render configuration
├── products_clean.csv       # Data
├── products_raw.csv         # Raw data
├── analysis_summary.txt     # Report
├── outputs/                 # Visualizations
│   ├── top_products.png
│   ├── price_distribution.png
│   ├── price_vs_rating.png
│   └── category_distribution.png
└── templates/               # HTML templates
    ├── index.html
    ├── data.html
    ├── visualizations.html
    └── analysis.html
```

---

## Performance Notes

- Dashboard loads instantly (<100ms)
- Data tables support search and filtering
- Images are optimized (300 DPI PNG)
- API endpoints return JSON efficiently
- Responsive design for mobile/tablet

---

## Security Notes

- No authentication required (public dashboard)
- Read-only data access
- No external API dependencies
- No database required
- Static visualizations

---

## Future Enhancements

- Add authentication
- Create admin panel
- Add real-time data updates
- Implement caching
- Add export functionality
- Create API keys for programmatic access

---

## Support

For issues or questions:
1. Check logs: `heroku logs --tail` or Render dashboard
2. Review Flask error messages
3. Verify all files are present
4. Ensure Python 3.7+ is used

---

**Happy Hosting!**
