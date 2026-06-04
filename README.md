# 基本網站架構

這是一個最基本的網站架構模式示例，使用Flask框架。

## 專案結構

```
project/
├── main.py                 # 主應用入口
├── requirements.txt        # 依賴項
├── README.md              # 說明文件
├── app/                   # 應用程序代碼
│   ├── __init__.py
│   ├── config.py          # 配置文件
│   └── routes.py          # 路由定義
├── templates/             # HTML 模板
│   ├── base.html          # 基礎模板
│   ├── index.html         # 首頁
│   └── about.html         # 關於頁面
└── static/                # 靜態文件
    ├── css/
    │   └── style.css      # 樣式表
    └── js/
        └── main.js        # JavaScript
```

## 快速開始

### 1. 安裝依賴
```bash
pip install -r requirements.txt
```

### 2. 運行應用
```bash
python main.py
```

### 3. 訪問網站
打開瀏覽器，訪問 `http://localhost:5000`

## 主要組件

### 1. **後端** (main.py, app/)
- Flask應用配置
- 路由定義
- 配置管理

### 2. **前端** (templates/, static/)
- HTML模板（Jinja2）
- CSS樣式
- JavaScript交互

### 3. **結構優勢**
- 清晰的文件組織
- 易於擴展
- 分離關注點
- 易於維護

## 下一步擴展

1. 添加數據庫（SQLAlchemy）
2. 添加用戶認證
3. 添加API端點
4. 添加表單驗證
5. 添加日誌系統
