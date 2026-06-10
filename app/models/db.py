import sqlite3
import os

DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'instance', 'database.db')

def get_db_connection():
    """取得 SQLite 資料庫連線，並設定 row_factory"""
    # 確保 instance 資料夾存在
    os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # 讓回傳結果可以像字典一樣透過 key 存取
    return conn

def init_db():
    """初始化資料庫表結構"""
    schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'schema.sql')
    if os.path.exists(schema_path):
        conn = get_db_connection()
        with open(schema_path, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()
