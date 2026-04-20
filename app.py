"""
E-Commerce Product Analysis Dashboard
Flask web application to host and visualize analysis results
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import json
from pathlib import Path
import base64
from io import BytesIO

app = Flask(__name__)
PROJECT_DIR = Path(__file__).parent

# Load data
try:
    df = pd.read_csv(PROJECT_DIR / 'products_clean.csv')
    with open(PROJECT_DIR / 'analysis_summary.txt', 'r', encoding='utf-8') as f:
        analysis_text = f.read()
except Exception as e:
    df = None
    analysis_text = str(e)

def encode_image(image_path):
    """Encode image to base64 for embedding in HTML"""
    try:
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

@app.route('/')
def index():
    """Homepage with dashboard overview"""
    stats = {
        'total_products': len(df),
        'avg_price': f"${df['Price'].mean():.2f}",
        'avg_rating': f"{df['Rating'].mean():.2f}/5.0",
        'avg_reviews': f"{df['Number of Reviews'].mean():.0f}",
        'price_min': f"${df['Price'].min():.2f}",
        'price_max': f"${df['Price'].max():.2f}",
        'rating_min': f"{df['Rating'].min():.1f}",
        'rating_max': f"{df['Rating'].max():.1f}",
    }
    
    # Get top products
    top_products = df.nlargest(5, 'Rating')[['Product Name', 'Price', 'Rating', 'Number of Reviews']].to_dict('records')
    
    return render_template('index.html', stats=stats, top_products=top_products)

@app.route('/data')
def data_page():
    """Data exploration page"""
    data_json = df.to_json(orient='records')
    return render_template('data.html', data=data_json, columns=list(df.columns))

@app.route('/analysis')
def analysis_page():
    """Analysis report page"""
    return render_template('analysis.html', analysis_text=analysis_text)

@app.route('/visualizations')
def visualizations():
    """Visualizations page with all charts"""
    viz_dir = PROJECT_DIR / 'outputs'
    
    images = {}
    for filename in ['top_products.png', 'price_distribution.png', 'price_vs_rating.png', 'category_distribution.png']:
        img_path = viz_dir / filename
        encoded = encode_image(img_path)
        if encoded:
            images[filename] = f"data:image/png;base64,{encoded}"
    
    return render_template('visualizations.html', images=images)

@app.route('/api/stats')
def get_stats():
    """API endpoint for statistics"""
    return jsonify({
        'total_products': int(len(df)),
        'avg_price': float(df['Price'].mean()),
        'avg_rating': float(df['Rating'].mean()),
        'price_range': {
            'min': float(df['Price'].min()),
            'max': float(df['Price'].max())
        },
        'rating_range': {
            'min': float(df['Rating'].min()),
            'max': float(df['Rating'].max())
        }
    })

@app.route('/api/products')
def get_products():
    """API endpoint for all products"""
    return jsonify(df.to_dict('records'))

@app.route('/api/top-products')
def get_top_products():
    """API endpoint for top rated products"""
    top = df.nlargest(10, 'Rating')[['Product Name', 'Price', 'Rating', 'Number of Reviews']]
    return jsonify(top.to_dict('records'))

@app.route('/api/best-value')
def get_best_value():
    """API endpoint for best value products"""
    df_temp = df.copy()
    df_temp['price_pct'] = df_temp['Price'].rank(pct=True)
    df_temp['rating_pct'] = df_temp['Rating'].rank(pct=True)
    df_temp['value'] = (df_temp['rating_pct'] + (1 - df_temp['price_pct'])) / 2
    best = df_temp.nlargest(10, 'value')[['Product Name', 'Price', 'Rating', 'Category']]
    return jsonify(best.to_dict('records'))

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return render_template('500.html', error=str(error)), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
