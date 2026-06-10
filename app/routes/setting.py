from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.job_setting import JobSetting

setting_bp = Blueprint('setting', __name__, url_prefix='/settings')

@setting_bp.route('/')
def index():
    """顯示目前的工作設定表單"""
    job = JobSetting.get_default()
    if not job:
        job = {'id': 1, 'job_name': '預設工作', 'hourly_rate': 183.0}
    return render_template('settings.html', job=job)

@setting_bp.route('/update', methods=['POST'])
def update():
    """更新工作設定（如：時薪）"""
    job_id = request.form.get('id')
    hourly_rate_str = request.form.get('hourly_rate')
    
    if not job_id or not hourly_rate_str:
        flash("參數錯誤", "danger")
        return redirect(url_for('setting.index'))
        
    try:
        hourly_rate = float(hourly_rate_str)
        JobSetting.update_rate(int(job_id), hourly_rate)
        flash("設定更新成功！", "success")
    except ValueError:
        flash("時薪格式錯誤，請輸入數字。", "danger")
        
    return redirect(url_for('setting.index'))
