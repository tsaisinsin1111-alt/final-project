from flask import render_template, jsonify

def register_routes(app):
    """註冊所有路由"""
    
    @app.route('/')
    def index():
        """首頁"""
        return render_template('index.html', title='首頁')
    
    @app.route('/api/hello', methods=['GET'])
    def api_hello():
        """API端點示例"""
        return jsonify({
            'message': '你好，世界！',
            'status': 'success'
        })
    
    @app.route('/about')
    def about():
        """關於頁面"""
        return render_template('about.html', title='關於我們')
