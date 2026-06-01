# 儲存路徑: 路由開發/app/routes/auth.py
from flask import render_template, redirect, url_for, request, flash, session
from app.routes import auth_bp
from app.models.user import User

@auth_bp.route('/register', methods=['GET'])
def register_page():
    """
    顯示員工/管理員註冊頁面
    :return: 渲染 templates/auth/register.html
    """
    pass

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    處理使用者註冊表單提交
    :return: 註冊成功重導向至登入頁 /auth/login；失敗則重新渲染註冊頁並帶入錯誤訊息
    """
    pass

@auth_bp.route('/login', methods=['GET'])
def login_page():
    """
    顯示使用者登入頁面
    :return: 渲染 templates/auth/login.html
    """
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    處理使用者登入驗證表單
    :return: 登入成功寫入 Session 並重導向至 /；失敗則重新渲染登入頁並顯示錯誤訊息
    """
    pass

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """
    使用者登出，清除 Session 資訊
    :return: 重導向至登入頁面 /auth/login
    """
    pass
