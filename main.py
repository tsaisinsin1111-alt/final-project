from flask import Flask
from app.routes import main_bp
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 註冊 Blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

