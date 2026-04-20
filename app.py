"""Flask Dashboard for E-Commerce Product Analysis"""
import os, base64, pandas as pd
from flask import Flask, render_template, jsonify
from pathlib import Path

app = Flask(__name__)
df = None

def load_data():
    global df
    try:
        csv_file = Path(__file__).parent / 'products_clean.csv'
        if csv_file.exists():
            df = pd.read_csv(csv_file)
    except: pass

load_data()

def img_b64(path):
    try:
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode()
    except: return None

@app.route('/')
def index():
    if df is None or len(df) == 0:
        return render_template('500.html', error='No data'), 500
    return render_template('index.html', stats={
        'total_products': len(df),
        'categories': df['Category'].nunique(),
        'avg_price': f"{df['Price'].mean():.2f}",
        'avg_rating': f"{df['Rating'].mean():.2f}",
        'top_products': df.nlargest(5, 'Rating')[['Product Name','Price','Rating','Category']].to_dict('records')
    })

@app.route('/data')
def data():
    if df is None: return render_template('500.html', error='No data'), 500
    return render_template('data.html', total_products=len(df), products=df.to_dict('records'))

@app.route('/analysis')
def analysis():
    if df is None: return render_template('500.html', error='No data'), 500
    summary_file = Path(__file__).parent / 'analysis_summary.txt'
    report = summary_file.read_text() if summary_file.exists() else "Report not found"
    return render_template('analysis.html', report=report)

@app.route('/visualizations')
def visualizations():
    if df is None: return render_template('500.html', error='No data'), 500
    images = {}
    output_dir = Path(__file__).parent / 'outputs'
    for key, fname in {'top_products': 'top_products.png', 'price_distribution': 'price_distribution.png', 
                       'price_vs_rating': 'price_vs_rating.png', 'category_distribution': 'category_distribution.png'}.items():
        img_path = output_dir / fname
        if img_path.exists():
            images[key] = img_b64(str(img_path))
    return render_template('visualizations.html', images=images)

@app.route('/api/stats')
def stats():
    if df is None: return jsonify({'error': 'No data'}), 500
    return jsonify({'total': len(df), 'categories': int(df['Category'].nunique()),
                    'avg_price': float(df['Price'].mean()), 'avg_rating': float(df['Rating'].mean())})

@app.route('/api/products')
def products():
    if df is None: return jsonify({'error': 'No data'}), 500
    return jsonify(df.to_dict('records'))

@app.route('/api/top-products')
def top_products():
    if df is None: return jsonify({'error': 'No data'}), 500
    return jsonify(df.nlargest(10, 'Rating')[['Product Name','Price','Rating','Number of Reviews']].to_dict('records'))

@app.route('/api/best-value')
def best_value():
    if df is None: return jsonify({'error': 'No data'}), 500
    p25 = df['Price'].quantile(0.25)
    return jsonify(df[(df['Price'] <= p25) & (df['Rating'] >= 4.0)].nlargest(10, 'Rating')[['Product Name','Price','Rating','Category']].to_dict('records'))

@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'data_loaded': df is not None}), 200

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error(e):
    return render_template('500.html', error=str(e)), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
