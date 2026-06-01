# 儲存路徑: 路由開發/app/routes/main.py
from flask import render_template, redirect, url_for, session
from app.routes import main_bp
from app.models.leave import Leave
from app.models.shift import Shift

@main_bp.route('/', methods=['GET'])
def index():
    """
    系統首頁分流控制器
    :return: 根據 Session 角色重導向至店長或員工儀表板；未登入重導向至 /auth/login
    """
    pass

@main_bp.route('/dashboard/manager', methods=['GET'])
def manager_dashboard():
    """
    顯示店長後台管理儀表板
    包含：今日缺工警示、今日出勤人數統計、待審核請假數量、今日班表名單
    :return: 渲染 templates/main/dashboard.html (管理員版面)
    """
    pass

@main_bp.route('/dashboard/staff', methods=['GET'])
def staff_dashboard():
    """
    顯示員工個人前台儀表板
    包含：個人當週排班表、請假審核狀態與歷史記錄
    :return: 渲染 templates/main/dashboard.html (一般員工版面)
    """
    pass
