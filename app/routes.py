from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import os
import random

main_bp = Blueprint('main', __name__)

# 讀取資料庫
base_dir = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(base_dir, '..', 'data.csv')
df = pd.read_csv(csv_path)
df["cp"] = df["rating"] / df["price"]

@main_bp.route('/')
def index():
    """首頁"""
    return render_template('index.html', title='首頁')

@main_bp.route('/about')
def about():
    """關於我們頁面"""
    return render_template('about.html', title='關於我們')

@main_bp.route('/api/hello', methods=['GET'])
def api_hello():
    """測試 API"""
    return jsonify({
        'message': '你好，世界！',
        'status': 'success'
    })

@main_bp.route('/analysis')
def analysis():
    """數據分析頁面"""
    avg_price_brand = df.groupby("brand")["price"].mean().to_dict()
    avg_price_type = df.groupby("type")["price"].mean().to_dict()
    return render_template("analysis.html",
                           avg_price_brand=avg_price_brand,
                           avg_price_type=avg_price_type)

@main_bp.route('/recommend', methods=['POST'])
def recommend():
    """推薦系統 API"""
    data = request.get_json()
    budget = int(data.get("budget", 0))
    cloth_type = data.get("type", "")

    filtered = df[(df["price"] <= budget) & (df["type"] == cloth_type)]
    if filtered.empty:
        return jsonify({"success": False, "message": "找不到符合條件的商品"})
    best = filtered.sort_values(by="cp", ascending=False).iloc[0]
    return jsonify({
        "success": True,
        "brand": best["brand"],
        "type": best["type"],
        "price": int(best["price"]),
        "rating": float(best["rating"]),
        "cp": float(best["cp"]),
        "title": best["title"],
        "image_url": best["image_url"]
    })
