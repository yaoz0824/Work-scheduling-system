from flask import Flask
from app.routes import register_blueprints
from app.models.db import init_db
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev_secret_key')
    
    # 註冊路由
    register_blueprints(app)
    
    # 初始化資料庫表
    init_db()
    
    return app
