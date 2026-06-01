# 儲存路徑: 路由開發/app/routes/leave.py
from flask import render_template, redirect, url_for, request, flash, session
from app.routes import leave_bp
from app.models.leave import Leave

@leave_bp.route('/leave/apply', methods=['GET'])
def leave_apply_page():
    """
    顯示員工請假申請表單頁面
    :return: 渲染 templates/leave/apply.html
    """
    pass

@leave_bp.route('/leave/apply', methods=['POST'])
def leave_apply():
    """
    處理員工請假表單提交
    :return: 申請成功重導向至 /dashboard/staff 並顯示成功提示；失敗則顯示衝突警告
    """
    pass

@leave_bp.route('/leave/review', methods=['GET'])
def leave_review_page():
    """
    店長待審核請假申請名單頁面
    :return: 渲染 templates/leave/review.html
    """
    pass

@leave_bp.route('/leave/review/<int:leave_id>/approve', methods=['POST'])
def leave_approve(leave_id):
    """
    店長核准請假申請
    核准後將調用 Model 自動將該員工在請假期間內已排定的班次清空 (staff_id = NULL)
    :param leave_id: 假單唯一識別碼
    :return: 重導向回 /leave/review
    """
    pass

@leave_bp.route('/leave/review/<int:leave_id>/reject', methods=['POST'])
def leave_reject(leave_id):
    """
    店長拒絕請假申請，可選填寫退回原因
    :param leave_id: 假單唯一識別碼
    :return: 重導向回 /leave/review
    """
    pass

@leave_bp.route('/shift/swap/post', methods=['POST'])
def shift_swap_post():
    """
    員工針對自己已排定的特定班次，發起線上代班換班募集
    :return: 募集成功重導向回 /dashboard/staff 顯示代班募集狀態
    """
    pass
