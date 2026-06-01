# 儲存路徑: 路由開發/app/routes/schedule.py
from flask import render_template, redirect, url_for, request, flash, session
from app.routes import schedule_bp
from app.models.shift import Shift

@schedule_bp.route('/view', methods=['GET'])
def view_schedule():
    """
    一般員工唯讀班表檢視頁面
    內嵌唯讀之 FullCalendar.js 行事曆，不開放拖拉修改
    :return: 渲染 templates/schedule/view.html
    """
    pass

@schedule_bp.route('/manage', methods=['GET'])
def manage_schedule():
    """
    店長專用排班管理控制台
    內嵌可拖拉、點擊編輯的 FullCalendar.js 控制介面，並提供一鍵自動排班按鈕
    :return: 渲染 templates/schedule/manage.html
    """
    pass

@schedule_bp.route('/auto', methods=['POST'])
def auto_schedule():
    """
    觸發後端智慧自動排班引擎
    讀取傳入的排班日期範圍（start_date 與 end_date），呼叫演算法產出排班草稿
    :return: 執行成功重導向至 /schedule/manage 預覽草稿
    """
    pass

@schedule_bp.route('/publish', methods=['POST'])
def publish_schedule():
    """
    正式發佈特定時間範圍內的排班草稿
    將該時間範圍內所有班表的 is_draft 標記設為 False，使一般員工可看見
    :return: 發佈成功重導向至 /schedule/manage
    """
    pass
