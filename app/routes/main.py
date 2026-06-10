from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.work_record import WorkRecord
from app.models.job_setting import JobSetting
from app.utils import get_current_date_str, get_current_time_str, calculate_hours_and_salary

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """顯示首頁面板與今日狀態"""
    today_str = get_current_date_str()
    record = WorkRecord.get_by_date(today_str)
    
    status = "尚未打卡"
    if record:
        if record['clock_out']:
            status = "已下班"
        elif record['clock_in']:
            status = "上班中"
            
    return render_template('index.html', record=record, status=status, today=today_str)

@main_bp.route('/clock-in', methods=['POST'])
def clock_in():
    """處理上班打卡邏輯"""
    today_str = get_current_date_str()
    record = WorkRecord.get_by_date(today_str)
    
    if record and record['clock_in']:
        flash("今日已經打過上班卡了！", "warning")
        return redirect(url_for('main.index'))
        
    # 取得預設工作
    job = JobSetting.get_default()
    job_id = job['id'] if job else 1
    
    now_str = get_current_time_str()
    
    if record:
        WorkRecord.update(record['id'], clock_in=now_str, note=record.get('note', ''))
    else:
        WorkRecord.create(job_id=job_id, work_date=today_str, clock_in=now_str)
        
    flash("上班打卡成功！", "success")
    return redirect(url_for('main.index'))

@main_bp.route('/clock-out', methods=['POST'])
def clock_out():
    """處理下班打卡與薪資計算邏輯"""
    today_str = get_current_date_str()
    record = WorkRecord.get_by_date(today_str)
    
    if not record or not record['clock_in']:
        flash("尚未打上班卡，無法下班！", "danger")
        return redirect(url_for('main.index'))
        
    if record['clock_out']:
        flash("今日已經打過下班卡了！", "warning")
        return redirect(url_for('main.index'))
        
    now_str = get_current_time_str()
    job = JobSetting.get_default()
    hourly_rate = job['hourly_rate'] if job else 183.0
    
    # 計算時數與薪水
    total_hours, ot_hours, salary = calculate_hours_and_salary(
        record['clock_in'], now_str, hourly_rate
    )
    
    WorkRecord.update(
        record['id'], 
        clock_in=record['clock_in'],
        clock_out=now_str,
        total_hours=total_hours,
        overtime_hours=ot_hours,
        estimated_salary=salary,
        note=record.get('note', '')
    )
    
    flash(f"下班打卡成功！今日工時 {total_hours} 小時，預估薪水 ${int(salary)}", "success")
    return redirect(url_for('main.index'))
