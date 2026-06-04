from flask import Flask, render_template, request, jsonify
from app.routes import register_routes
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 註冊所有路由
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
